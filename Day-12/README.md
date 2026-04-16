# 🕒 Day 12: LLM-Based PDF Data Extraction

🏁 **Goal**: Build a web application that extracts structured data from PDFs using LLMs via OpenRouter.

---

## 📚 Overview

Learn how to create a Streamlit web app that uses OpenRouter's LLM to intelligently extract data from PDF documents and return it as structured JSON.

---

## ✅ Learning Objectives

### **1. LLM-Based PDF Extraction (30 mins)**
* **Topics:**
    * Streamlit web interface setup
    * OpenRouter API integration via OpenAI client
    * PDF text extraction with PyPDF2
    * LLM prompt engineering for data extraction
    * JSON output formatting
* **Summary**: Build a complete web app for PDF data extraction using OpenRouter LLMs.
* **Example**: [See `01_pdf_extraction_introduction.py`](./01_pdf_extraction_introduction.py)

---

### **2. Advanced LLM Extraction Techniques (20 mins)**
* **Topics:**
    * Custom prompts for different document types
    * Error handling and validation
    * Batch processing capabilities
    * Cost optimization strategies
* **Summary**: Enhance the extraction system with advanced features.
* **Example**: [See `02_pdf_processing_basics.py`](./02_pdf_processing_basics.py)

---

### **3. Production Deployment (10 mins)**
* **Topics:**
    * Streamlit deployment options
    * API key management
    * Performance monitoring
    * User feedback systems
* **Summary**: Deploy your PDF extraction app for production use.
* **Example**: [See `03_production_deployment.py`](./03_production_deployment.py)

---

### **4. Image-based Extraction (optional)**
* **Topics:**
    * Render PDF pages to images (PyMuPDF)
    * Send base64 image to OpenRouter via OpenAI Responses API
    * Extract structured JSON from images
* **Summary**: Handle scanned PDFs and image-only documents.
* **Example**: [See `04_image_extraction.py`](./04_image_extraction.py)

---

## 🚀 **Complete Setup & Run Instructions**

### **Step 1: Install Dependencies**
First, make sure you're in the project root directory and activate the virtual environment:
```bash
# Navigate to project root (if not already there)
cd C:\YalixTech_workspace\GenAI-Developer-Beginner

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install all required packages
pip install -r Day-12/requirements.txt
```

### **Step 2: Configure Environment**
Create or update your `.env` file in the project root with OpenRouter credentials:
```bash
OPENROUTER_API_KEY=your_openrouter_api_key
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_MODEL_NAME=openrouter/moonshotai/kimi-k2:free
```

### **Step 3: Run the Application**
Navigate to the Day-12 directory and run the Streamlit app:
```bash
# Navigate to Day-12 directory
cd Day-12

# Run the main PDF extraction app
streamlit run .\01_pdf_extraction_introduction.py
```

### **Step 4: Access the Web Interface**
- The app will automatically open in your default browser
- If not, manually navigate to: `http://localhost:8501`
- Upload PDF files and start extracting data!

---

## 🛠️ **Alternative Apps to Run**

You can also run the other demonstration apps:

```bash
# Advanced extraction techniques
streamlit run .\02_pdf_processing_basics.py

# Production deployment demo
streamlit run .\03_production_deployment.py

# Image-based extraction
streamlit run .\04_image_extraction.py
```

---

## 🧪 **Testing Your Setup**

Before running the app, test your OpenRouter configuration:
```bash
# From project root with venv activated
python Day-12/test_sample_pdfs.py
```

You should see: ✅ OpenRouter configuration is complete

---

## 🛠️ Tools & Resources

- **Streamlit**: Web interface framework
- **OpenRouter API**: LLM for intelligent extraction (via OpenAI client)
- **PyPDF2**: PDF text extraction
- **PyMuPDF**: PDF image rendering
- **python-dotenv**: Environment management

---

## 📄 Sample PDFs for Testing

The `assets/` folder contains 5 sample PDFs for testing:
- **sample_invoice.pdf** - Web development invoice
- **sample_contract.pdf** - Service agreement contract  
- **sample_receipt.pdf** - Payment receipt
- **sample_resume.pdf** - Software developer resume
- **sample_medical_report.pdf** - Medical examination report

---

## 🔧 **Troubleshooting**

### **Common Issues:**
1. **Module not found errors**: Make sure virtual environment is activated
2. **API key errors**: Verify `.env` file is in project root
3. **Port conflicts**: Streamlit will automatically find an available port

### **Quick Fixes:**
```bash
# Reinstall requirements if needed
pip install -r Day-12/requirements.txt --force-reinstall

# Check environment variables
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('OPENROUTER_API_KEY:', os.getenv('OPENROUTER_API_KEY')[:10] + '...')"
```

---

*Build intelligent PDF extraction systems with OpenRouter! 📄🤖*
