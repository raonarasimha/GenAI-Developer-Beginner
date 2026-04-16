"""
Generate images from text prompts using Hugging Face Inference API and save PNGs to outputs/.
"""

import os
import requests
from io import BytesIO
from base64 import b64decode
from dotenv import load_dotenv
from PIL import Image


def ensure_dirs(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def generate_image_hf(prompt: str, api_key: str, model: str = "runwayml/stable-diffusion-v1-5") -> bytes:
    """
    Generate image using Hugging Face Inference API.
    
    Args:
        prompt: Text prompt for image generation
        api_key: Hugging Face API key
        model: Model to use for generation (default: runwayml/stable-diffusion-v1-5)
    
    Returns:
        Image bytes
    """
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
    
    if response.status_code == 503:
        # Model is loading, wait and retry
        print("Model is loading, please wait...")
        import time
        time.sleep(10)
        response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 404:
        raise Exception(f"Model '{model}' not found. Try a different model like 'stabilityai/stable-diffusion-2-1'")
    
    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}: {response.text}")
    
    return response.content


def main() -> None:
    load_dotenv()
    api_key = os.getenv("HF_TOKEN")
    if not api_key:
        print("Please set HF_TOKEN in your .env file")
        return

    outputs_dir = os.path.join(os.path.dirname(__file__), "outputs")
    ensure_dirs(outputs_dir)

    prompt = "A minimalist, isometric illustration of a cozy reading nook, soft lighting"
    
    # Try different models in order of preference
    models_to_try = [
        "stabilityai/stable-diffusion-xl-base-1.0",  # This one works!
        "prompthero/openjourney",
        "dreamlike-art/dreamlike-diffusion-1.0",
        "runwayml/stable-diffusion-v1-5",
        "stabilityai/stable-diffusion-2-1"
    ]
    
    for model in models_to_try:
        try:
            print(f"Trying model: {model}")
            img_bytes = generate_image_hf(prompt, api_key, model)
            
            out_path = os.path.join(outputs_dir, "generated_1.png")
            with open(out_path, "wb") as f:
                f.write(img_bytes)
            print(f"✅ Success! Saved: {out_path}")
            
            # Display image info
            img = Image.open(BytesIO(img_bytes))
            print(f"Image size: {img.size}")
            break
            
        except Exception as e:
            print(f"❌ Failed with {model}: {e}")
            if model == models_to_try[-1]:  # Last model
                print("All models failed. Please check your API key and internet connection.")


if __name__ == "__main__":
    main()


