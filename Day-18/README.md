# 🕒 Day 18: Simple Image Generation & Processing (Hugging Face)

🏁 Goal: Generate images from text with Hugging Face, caption existing images, and do basic processing locally.

---

## 📚 Overview

You will:
- Generate images from prompts using Hugging Face text-to-image models
- Caption images using Hugging Face image-to-text models
- Perform simple processing (resize/thumbnail) with Pillow

---

## ✅ Learning Objectives

1) Use Hugging Face Inference API for text-to-image generation
2) Use Hugging Face models to describe/caption images
3) Apply basic image processing locally (resize/crop)

---

## ⚙️ Quick Setup (Day-18 only)

- Install dependencies:
```bash
pip install -r Day-18/requirements.txt
```

- Create `.env` (repo root or `Day-18/`) with:
```bash
HF_TOKEN=your_huggingface_token
```

- Get your Hugging Face token:
  1. Go to [huggingface.co](https://huggingface.co)
  2. Sign up/Login and go to Settings → Access Tokens
  3. Create a new token with "Read" permissions

- Folders:
  - `Day-18/assets/` for input images
  - `Day-18/outputs/` will be created for generated files

---

## ▶️ How to Run

1) Text → Image (CLI):
```bash
python Day-18/01_text_to_image.py
```

2) Image → Caption (CLI):
```bash
python Day-18/02_image_to_caption_transformers.py
```

3) Streamlit Playground:
```bash
streamlit run Day-18/03_streamlit_image_playground.py
```

---

## 📁 Files

- `01_text_to_image.py`: Generate images from prompts using Stable Diffusion XL
- `02_image_to_caption.py`: Caption an image using API (may not work)
- `02_image_to_caption_transformers.py`: ✅ **Working!** Caption using local BLIP model
- `03_streamlit_image_playground.py`: Interactive UI with both generation and captioning
- `test_api_connection.py`: Test which models work via API
- `test_caption_models.py`: Test captioning models
- `assets/`: Place test images here (e.g., `.png`, `.jpg`)
- `outputs/`: Generated images and processed results

---

## 🤖 Available Models (All Free!)

**Text-to-Image:**
- `stabilityai/stable-diffusion-xl-base-1.0` (default) - ✅ **Working!** Latest, highest quality
- `prompthero/openjourney` - Midjourney-style outputs
- `dreamlike-art/dreamlike-diffusion-1.0` - Artistic style
- `runwayml/stable-diffusion-v1-5` - High quality, versatile
- `stabilityai/stable-diffusion-2-1` - Improved version
- `CompVis/stable-diffusion-v1-4` - Original Stable Diffusion

**Image Captioning:**
- `Salesforce/blip-image-captioning-base` ✅ **Working!** - Local inference with transformers
- `Salesforce/blip-image-captioning-large` - More detailed captions (local)
- Alternative: Image classification models via API (labels only)

---

## 🧪 Tips

- **All models are completely free** - no payment required!
- Hugging Face models may take longer to load on first use
- Use clear, specific prompts for better results
- Free accounts have ~1000 requests/month limit
- Keep uploads under a few MB for smooth processing
- Try different models to find your preferred style

---

Have fun creating and processing images with Hugging Face!
