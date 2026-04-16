"""
Streamlit playground for image generation and basic processing using Hugging Face.
"""

import os
import io
import base64
import requests
from PIL import Image
import streamlit as st
from dotenv import load_dotenv


def ensure_dirs(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def save_bytes_png(data: bytes, path: str) -> None:
    with open(path, "wb") as f:
        f.write(data)


def generate_image_hf(prompt: str, api_key: str, model: str = "runwayml/stable-diffusion-v1-5") -> bytes:
    """Generate image using Hugging Face Inference API."""
    API_URL = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    payload = {
        "inputs": prompt,
        "parameters": {
            "num_inference_steps": 20,
            "guidance_scale": 7.5
        }
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}: {response.text}")
    
    return response.content


def caption_image_local(image: Image.Image) -> str:
    """Generate caption for image using local BLIP model."""
    try:
        from transformers import BlipProcessor, BlipForConditionalGeneration
        
        # Load the processor and model
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        
        # Process the image and generate a caption
        inputs = processor(images=image, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=50, num_beams=4)
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        
        return caption
    except ImportError:
        raise Exception("transformers library not found. Install with: pip install transformers")
    except Exception as e:
        raise Exception(f"Captioning failed: {e}")


def main() -> None:
    load_dotenv()
    st.set_page_config(page_title="Image Playground", layout="wide")
    st.title("Day-18: Image Generation & Processing (Hugging Face)")

    if not os.getenv("HF_TOKEN"):
        st.error("Please set HF_TOKEN in your .env file")
        st.stop()

    api_key = os.getenv("HF_TOKEN")
    outputs_dir = os.path.join(os.path.dirname(__file__), "outputs")
    ensure_dirs(outputs_dir)

    tab1, tab2 = st.tabs(["Text → Image", "Processing & Caption"]) 

    with tab1:
        st.subheader("Generate Images with Hugging Face")
        prompt = st.text_area("Prompt", "A watercolor painting of a lighthouse at sunset")
        
        col1, col2 = st.columns(2)
        with col1:
            model = st.selectbox(
                "Model", 
                [
                    "stabilityai/stable-diffusion-xl-base-1.0",  # Working model
                    "prompthero/openjourney",
                    "dreamlike-art/dreamlike-diffusion-1.0",
                    "runwayml/stable-diffusion-v1-5",
                    "stabilityai/stable-diffusion-2-1", 
                    "CompVis/stable-diffusion-v1-4"
                ],
                index=0
            )
        with col2:
            num_steps = st.slider("Inference Steps", 10, 50, 20)
        
        if st.button("Generate Image", type="primary"):
            with st.spinner("Generating with Hugging Face..."):
                try:
                    img_bytes = generate_image_hf(prompt, api_key, model)
                    st.image(img_bytes)
                    out_path = os.path.join(outputs_dir, "playground_generated.png")
                    save_bytes_png(img_bytes, out_path)
                    st.success(f"Saved: {out_path}")
                except Exception as e:
                    st.error(f"Error generating image: {e}")

    with tab2:
        st.subheader("Image Processing & Captioning")
        upload = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"]) 
        if upload is not None:
            img = Image.open(upload).convert("RGB")
            w = st.slider("Width", 64, 1024, img.width)
            h = st.slider("Height", 64, 1024, img.height)
            resized = img.resize((w, h))
            st.image(resized, caption=f"{w}x{h}")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Save Resized"):
                    out_path = os.path.join(outputs_dir, "resized.png")
                    resized.save(out_path)
                    st.success(f"Saved: {out_path}")

            if st.button("Caption Image"):
                with st.spinner("Generating caption with BLIP model..."):
                    try:
                        caption = caption_image_local(resized)
                        st.write("**Caption:**", caption)
                    except Exception as e:
                        st.error(f"Error generating caption: {e}")
                        st.info("💡 Make sure transformers is installed: pip install transformers")


if __name__ == "__main__":
    main()


