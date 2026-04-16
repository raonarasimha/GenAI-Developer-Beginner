"""
Test Sample PDFs
===============

Test the sample PDFs with the LLM extraction system.
"""

import os
import PyPDF2
from dotenv import load_dotenv

load_dotenv()

def test_pdf_extraction():
    """Test extracting text from sample PDFs."""
    assets_dir = "assets"
    
    sample_pdfs = [
        "sample_invoice.pdf",
        "sample_contract.pdf", 
        "sample_receipt.pdf",
        "sample_resume.pdf",
        "sample_medical_report.pdf"
    ]
    
    print("🧪 Testing Sample PDF Text Extraction")
    print("=" * 50)
    
    for pdf_file in sample_pdfs:
        filepath = os.path.join(assets_dir, pdf_file)
        
        if not os.path.exists(filepath):
            print(f"❌ File not found: {pdf_file}")
            continue
        
        try:
            # Extract text from PDF
            with open(filepath, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
                
                # Basic analysis
                char_count = len(text)
                word_count = len(text.split())
                line_count = len(text.split('\n'))
                
                print(f"✅ {pdf_file}")
                print(f"   Characters: {char_count:,}")
                print(f"   Words: {word_count:,}")
                print(f"   Lines: {line_count:,}")
                print(f"   Preview: {text[:100]}...")
                print()
                
        except Exception as e:
            print(f"❌ Error processing {pdf_file}: {e}")
            print()

def check_api_key():
    """Check if OpenAI API key is set."""
    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key:
        print("✅ OpenAI API key is configured")
        print(f"   Key preview: {api_key[:10]}...")
    else:
        print("❌ OpenAI API key not found")
        print("   Please set OPENAI_API_KEY in your .env file")
    
    print()

def main():
    """Run all tests."""
    print("🚀 Day 12 - Sample PDF Testing")
    print("=" * 50)
    print()
    
    # Check API key
    check_api_key()
    
    # Test PDF extraction
    test_pdf_extraction()
    
    print("=" * 50)
    print("✅ Testing complete!")
    print()
    print("Next steps:")
    print("1. Set up your OpenAI API key in .env file")
    print("2. Run: streamlit run 01_pdf_extraction_introduction.py")
    print("3. Upload the sample PDFs to test extraction")

if __name__ == "__main__":
    main()
