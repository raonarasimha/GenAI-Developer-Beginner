"""
Day 12 - LLM-Based PDF Data Extraction
=====================================

Real PDF extraction using LLMs (OpenAI/DeepSeek) with Streamlit interface.
"""

import os
import json
import streamlit as st
import PyPDF2
import io
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv

# Load environment variables
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

class LLMPDFExtractor:
    """LLM-based PDF extraction using OpenAI API."""
    
    def __init__(self, client, model_name):
        self.client = client
        self.model_name = model_name
        self.extraction_stats = {
            "documents_processed": 0,
            "successful_extractions": 0,
            "failed_extractions": 0,
            "total_tokens_used": 0
        }
    
    def extract_text_from_pdf(self, pdf_file) -> str:
        """Extract text content from uploaded PDF file."""
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            
            return text.strip()
            
        except Exception as e:
            st.error(f"Error extracting text from PDF: {str(e)}")
            return ""
    
    def extract_invoice_data(self, pdf_text: str) -> Dict[str, Any]:
        """Extract invoice data using LLM."""
        prompt = """
        Extract the following information from this invoice and return it as JSON:
        - invoice_number
        - date
        - due_date
        - customer_name
        - customer_address
        - line_items (array of objects with description, quantity, unit_price, total)
        - subtotal
        - tax_amount
        - total_amount
        - payment_terms
        
        If any field is not found, use null. Return only valid JSON.
        
        Invoice text:
        """
        
        return self._extract_with_llm(pdf_text, prompt, "invoice")
    
    def extract_contract_data(self, pdf_text: str) -> Dict[str, Any]:
        """Extract contract data using LLM."""
        prompt = """
        Extract the following information from this contract and return it as JSON:
        - parties (object with company_name, client_name, addresses)
        - effective_date
        - contract_term
        - services (array of service descriptions)
        - payment_amount
        - payment_frequency
        - termination_terms
        
        If any field is not found, use null. Return only valid JSON.
        
        Contract text:
        """
        
        return self._extract_with_llm(pdf_text, prompt, "contract")
    
    def extract_form_data(self, pdf_text: str) -> Dict[str, Any]:
        """Extract form data using LLM."""
        prompt = """
        Extract the following information from this form and return it as JSON:
        - personal_info (object with name, email, phone, address)
        - education (object with degree, university, graduation_year)
        - experience (object with previous_job, years_experience, skills)
        - references_available
        
        If any field is not found, use null. Return only valid JSON.
        
        Form text:
        """
        
        return self._extract_with_llm(pdf_text, prompt, "form")
    
    def extract_general_data(self, pdf_text: str) -> Dict[str, Any]:
        """Extract general document data using LLM."""
        prompt = """
        Analyze this document and extract key information. Return as JSON with:
        - document_type (invoice, contract, form, report, etc.)
        - key_entities (names, companies, dates, amounts)
        - main_topics
        - important_dates
        - financial_data (if any)
        - contact_information (if any)
        
        Return only valid JSON.
        
        Document text:
        """
        
        return self._extract_with_llm(pdf_text, prompt, "general")
    
    def _extract_with_llm(self, pdf_text: str, prompt: str, doc_type: str) -> Dict[str, Any]:
        """Extract data using OpenAI Chat Completions API with JSON output enforced."""
        try:
            # Use chat completions API instead of responses API for better OpenRouter compatibility
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a PDF data extraction expert. You must return ONLY valid JSON without any markdown formatting, explanations, or additional text."},
                    {"role": "user", "content": prompt + "\n\n" + pdf_text[:4000] + "\n\nIMPORTANT: Return ONLY the JSON object, no ```json``` markers, no explanations."}
                ],
                temperature=0.1,
            )

            # Extract response text from chat completions
            response_text = response.choices[0].message.content.strip()

            # Clean JSON response - remove markdown formatting if present
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            
            # Try to parse JSON, with better error handling
            try:
                extracted_data = json.loads(response_text.strip())
            except json.JSONDecodeError as e:
                # Try to extract JSON from the response if it's wrapped in text
                import re
                json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
                if json_match:
                    try:
                        extracted_data = json.loads(json_match.group())
                    except json.JSONDecodeError:
                        raise ValueError(f"Failed to parse JSON response: {str(e)}")
                else:
                    raise ValueError(f"Failed to parse JSON response: {str(e)}")

            usage = getattr(response, "usage", None)
            total_tokens = None
            if usage is not None:
                total_tokens = getattr(usage, "total_tokens", None)
                if total_tokens is None:
                    total_tokens = getattr(usage, "input_tokens", 0) + getattr(usage, "output_tokens", 0)

            extracted_data["extraction_metadata"] = {
                "document_type": doc_type,
                "confidence": "high",
                "tokens_used": total_tokens or 0,
                "model_used": self.model_name,
            }

            self.extraction_stats["successful_extractions"] += 1
            if total_tokens:
                self.extraction_stats["total_tokens_used"] += total_tokens

            return extracted_data

        except json.JSONDecodeError as e:
            self.extraction_stats["failed_extractions"] += 1
            return {"error": f"Failed to parse JSON: {str(e)}"}
        except Exception as e:
            self.extraction_stats["failed_extractions"] += 1
            return {"error": str(e)}
    
    def get_extraction_stats(self) -> Dict[str, Any]:
        """Get extraction statistics."""
        return self.extraction_stats.copy()

def main():
    """Streamlit app for LLM-based PDF extraction."""
    st.set_page_config(page_title="LLM PDF Extractor", layout="wide")
    st.title("LLM-Based PDF Data Extraction")
    st.markdown("Upload a PDF and extract structured data using OpenAI Chat Completions API via OpenRouter.")
    
    # Initialize extractor
    extractor = LLMPDFExtractor(client, model_name)
    
    # File upload
    uploaded_file = st.file_uploader(
        "Choose a PDF file", 
        type=['pdf'],
        help="Upload a PDF document to extract data from"
    )
    
    if uploaded_file is not None:
        # Extract text from PDF
        with st.spinner("Extracting text from PDF..."):
            pdf_text = extractor.extract_text_from_pdf(uploaded_file)
        
        if pdf_text:
            st.success(f"Extracted {len(pdf_text)} characters from PDF")
            
            # Show extracted text
            with st.expander("📄 View Extracted Text"):
                st.text_area("PDF Text Content", pdf_text, height=200)
            
            # Document type selection
            st.subheader("Select Extraction Type")
            extraction_type = st.selectbox(
                "Choose the type of document for extraction:",
                ["Auto-detect", "Invoice", "Contract", "Form", "General Analysis"]
            )
            
            # Extract button
            if st.button("Extract Data", type="primary"):
                with st.spinner("Processing with LLM..."):
                    
                    if extraction_type == "Invoice":
                        result = extractor.extract_invoice_data(pdf_text)
                    elif extraction_type == "Contract":
                        result = extractor.extract_contract_data(pdf_text)
                    elif extraction_type == "Form":
                        result = extractor.extract_form_data(pdf_text)
                    else:
                        result = extractor.extract_general_data(pdf_text)
                    
                    # Display results
                    st.subheader("Extracted Data")
                    
                    if "error" in result:
                        st.error(f"Extraction failed: {result['error']}")
                    else:
                        st.json(result)
                        
                        # Download button
                        json_str = json.dumps(result, indent=2)
                        st.download_button(
                            label="📥 Download JSON",
                            data=json_str,
                            file_name=f"extracted_data_{extraction_type.lower()}.json",
                            mime="application/json"
                        )
                        
                        if "extraction_metadata" in result:
                            metadata = result["extraction_metadata"]
                            col1, col2, col3, col4 = st.columns(4)
                            with col1:
                                st.metric("Document Type", metadata.get("document_type", "Unknown"))
                            with col2:
                                st.metric("Confidence", metadata.get("confidence", "Unknown"))
                            with col3:
                                st.metric("Tokens Used", metadata.get("tokens_used", 0))
                            with col4:
                                st.metric("Model", metadata.get("model_used", "Unknown"))
        else:
            st.error("Failed to extract text from PDF")
    
    # Show overall statistics
    with st.sidebar:
        st.header("Extraction Statistics")
        stats = extractor.get_extraction_stats()
        
        st.metric("Documents Processed", stats["documents_processed"])
        st.metric("Successful Extractions", stats["successful_extractions"])
        st.metric("Failed Extractions", stats["failed_extractions"])
        st.metric("Total Tokens Used", stats["total_tokens_used"])
        
        st.markdown("---")
        st.markdown("### Tips")
        st.markdown("""
        - Prefer clear, text-based PDFs
        - Select the closest document type
        - Large PDFs are truncated for token limits
        - Verify extracted text
        """)
        
        st.markdown("### Setup")
        st.markdown("""
        Ensure you have:
        - OPENROUTER_API_KEY in .env
        - OPENAI_API_BASE in .env
        - OPENAI_MODEL_NAME in .env
        - Packages: `streamlit openai PyPDF2 python-dotenv`
        """)

if __name__ == "__main__":
    main()
