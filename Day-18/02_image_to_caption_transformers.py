"""
Caption a local image using Hugging Face transformers library (local inference).
"""

import os
from dotenv import load_dotenv
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image


def main() -> None:
    load_dotenv()
    
    # Check if we have the required libraries
    try:
        from transformers import BlipProcessor, BlipForConditionalGeneration
    except ImportError:
        print("❌ transformers library not found. Install with: pip install transformers")
        return
    
    assets_dir = os.path.join(os.path.dirname(__file__), "assets")
    sample_path = os.path.join(assets_dir, "sample.jpg")

    if not os.path.isfile(sample_path):
        print(f"Place an image at: {sample_path}")
        return

    try:
        print("Loading BLIP model (this may take a moment on first run)...")
        
        # Load the processor and model
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        
        print("Loading image...")
        # Load the image
        image = Image.open(sample_path).convert('RGB')
        
        print("Generating caption...")
        # Process the image and generate a caption
        inputs = processor(images=image, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=50, num_beams=4)
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        
        print(f"✅ Caption: {caption}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure you have transformers installed: pip install transformers")


if __name__ == "__main__":
    main()
