"""
Day 12 - Image-based Extraction from PDF (OpenAI Responses API)
Render a PDF page to an image, send it as base64 to OpenAI, and extract JSON.
"""

import os
import io
import json
import base64
from typing import Dict, Any

import streamlit as st
import fitz  # PyMuPDF
from dotenv import load_dotenv


load_dotenv()

# Check for OpenRouter configuration
try:
    from openrouter_provider import create_openrouter_provider
    provider = create_openrouter_provider()
    client = provider.get_client()
    model_name = provider.get_model_name()
    st.success(f"✅ Using OpenRouter model: {model_name}")
except ValueError as e:
    st.error(f"Configuration error: {e}")
    st.stop()
except ImportError:
    st.error("Please install openai: pip install openai")
    st.stop()


def render_pdf_page_to_png_bytes(pdf_bytes: bytes, page_index: int, zoom: float = 2.0) -> bytes:
    """Render a single PDF page to PNG bytes using PyMuPDF."""
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    page = doc.load_page(page_index)
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    png_bytes = pix.tobytes("png")
    doc.close()
    return png_bytes


def encode_png_base64(png_bytes: bytes) -> str:
    return base64.b64encode(png_bytes).decode("utf-8")


def call_openai_with_image(prompt: str, image_b64: str) -> Dict[str, Any]:
    print(prompt)
    print(image_b64)
    # Use the global client and model_name from OpenRouter provider
    try:
        # Chat Completions API with multimodal input
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{image_b64}",
                            },
                        },
                    ],
                }
            ],
            temperature=0.0,
        )

        # Extract text from response
        text = response.choices[0].message.content.strip()
        if not text:
            raise RuntimeError("Empty response from model")

        # Handle markdown-wrapped JSON responses
        if text.startswith("```json"):
            # Remove markdown code block formatting
            text = text.replace("```json", "").replace("```", "").strip()
        elif text.startswith("```"):
            # Handle generic code blocks
            text = text.replace("```", "").strip()

        return json.loads(text)
    except Exception as e:
        raise RuntimeError(f"OpenAI API error: {str(e)}")


def build_prompt(doc_type: str) -> str:
    if doc_type == "Invoice":
        return (
            "Extract these fields as JSON: invoice_number, date, due_date, customer_name, "
            "line_items (array of {description, quantity, unit_price, total}), subtotal, tax_amount, total_amount. "
            "Use null where missing."
        )
    if doc_type == "Receipt":
        return (
            "Extract these fields as JSON: merchant_name, date, time, items (array of {description, quantity, total}), "
            "subtotal, tax_amount, total_amount, payment_method. Use null where missing."
        )
    return (
        "Extract key information as JSON with fields: document_type, key_entities, main_topics, amounts, dates, "
        "contact_info. Use null where missing."
    )


def main() -> None:
    st.set_page_config(page_title="PDF Image Extraction (LLM)", layout="wide")
    st.title("PDF Image Extraction using OpenAI Responses API")
    st.markdown("Upload a PDF, render a page as an image, and extract structured data.")

    uploaded = st.file_uploader("Choose a PDF", type=["pdf"])
    if not uploaded:
        return

    pdf_bytes = uploaded.read()
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    except Exception as e:
        st.error(f"Failed to open PDF: {e}")
        return

    num_pages = doc.page_count
    doc.close()

    col_left, col_right = st.columns([1, 1])
    with col_left:
        page_index = st.number_input("Page (0-based)", min_value=0, max_value=max(num_pages - 1, 0), value=0, step=1)
        zoom = st.slider("Render zoom", min_value=1.0, max_value=3.0, value=2.0, step=0.1)
        doc_type = st.selectbox("Document type", ["Auto", "Invoice", "Receipt", "General"])

    with col_right:
        with st.spinner("Rendering page..."):
            png_bytes = render_pdf_page_to_png_bytes(pdf_bytes, int(page_index), zoom=zoom)
        st.image(png_bytes, caption=f"Page {page_index}")

    if st.button("Extract from Image", type="primary"):
        with st.spinner("Calling OpenAI..."):
            prompt = build_prompt(doc_type if doc_type != "Auto" else "General")
            try:
                data = call_openai_with_image(prompt, encode_png_base64(png_bytes))
                st.subheader("Extracted JSON")
                st.json(data)
                st.download_button(
                    label="Download JSON",
                    data=json.dumps(data, indent=2),
                    file_name="image_extraction.json",
                    mime="application/json",
                )
            except Exception as e:
                st.error(f"Extraction failed: {e}")


if __name__ == "__main__":
    main()


