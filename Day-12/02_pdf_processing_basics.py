"""
Day 12 - Advanced LLM Extraction Techniques
Advanced prompts, validation, and batch processing for PDF extraction using OpenAI.
"""

import os
import json
import streamlit as st
import PyPDF2
from typing import Dict, List, Any, Optional
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

class AdvancedLLMExtractor:
    """Advanced LLM-based PDF extraction with enhanced features."""
    
    def __init__(self, client, model_name):
        self.client = client
        self.model_name = model_name
        self.extraction_history = []
        self.custom_prompts = {}
        self.setup_default_prompts()
    
    def setup_default_prompts(self):
        """Setup default extraction prompts for different document types."""
        self.custom_prompts = {
            "invoice": """
            Extract invoice data and return as JSON with these fields:
            - invoice_number (string)
            - date (string, format: YYYY-MM-DD)
            - due_date (string, format: YYYY-MM-DD)
            - customer_name (string)
            - customer_address (string)
            - line_items (array of objects with: description, quantity, unit_price, total)
            - subtotal (number)
            - tax_amount (number)
            - total_amount (number)
            - payment_terms (string)
            - currency (string, default: USD)
            
            If any field is not found, use null. Return only valid JSON.
            """,
            
            "contract": """
            Extract contract data and return as JSON with these fields:
            - parties (object with: company_name, client_name, company_address, client_address)
            - effective_date (string, format: YYYY-MM-DD)
            - contract_term (string)
            - services (array of service descriptions)
            - payment_amount (number)
            - payment_frequency (string)
            - termination_terms (string)
            - contract_value (number)
            - key_obligations (array of strings)
            
            If any field is not found, use null. Return only valid JSON.
            """,
            
            "receipt": """
            Extract receipt data and return as JSON with these fields:
            - merchant_name (string)
            - date (string, format: YYYY-MM-DD)
            - time (string, format: HH:MM)
            - items (array of objects with: description, quantity, unit_price, total)
            - subtotal (number)
            - tax_amount (number)
            - total_amount (number)
            - payment_method (string)
            - receipt_number (string)
            - store_location (string)
            
            If any field is not found, use null. Return only valid JSON.
            """,
            
            "resume": """
            Extract resume data and return as JSON with these fields:
            - personal_info (object with: name, email, phone, address, linkedin)
            - summary (string)
            - education (array of objects with: degree, institution, graduation_year, gpa)
            - experience (array of objects with: title, company, duration, description)
            - skills (array of strings)
            - certifications (array of strings)
            - languages (array of strings)
            - projects (array of objects with: name, description, technologies)
            
            If any field is not found, use null. Return only valid JSON.
            """
        }
    
    def add_custom_prompt(self, doc_type: str, prompt: str):
        """Add a custom extraction prompt for a document type."""
        self.custom_prompts[doc_type] = prompt
        st.success(f"Custom prompt added for {doc_type}")
    
    def extract_with_custom_prompt(self, pdf_text: str, doc_type: str, custom_prompt: str = None) -> Dict[str, Any]:
        """Extract data using a custom prompt."""
        prompt = custom_prompt or self.custom_prompts.get(doc_type, self.custom_prompts["general"])
        
        try:
            full_prompt = prompt + "\n\nDocument text:\n" + pdf_text[:4000]
            
            response = self.client.responses.create(
                model=self.model_name,
                input=full_prompt,
                temperature=0.1,
            )

            response_text = (getattr(response, "output_text", None) or "").strip()
            if not response_text:
                try:
                    response_text = response.output[0].content[0].text
                except Exception:
                    raise ValueError("Empty response from model")
            
            # Clean JSON response
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            
            extracted_data = json.loads(response_text)

            usage = getattr(response, "usage", None)
            total_tokens = None
            if usage is not None:
                total_tokens = getattr(usage, "total_tokens", None)
                if total_tokens is None:
                    total_tokens = getattr(usage, "input_tokens", 0) + getattr(usage, "output_tokens", 0)

            extracted_data["extraction_metadata"] = {
                "document_type": doc_type,
                "prompt_type": "custom" if custom_prompt else "default",
                "tokens_used": total_tokens or 0,
                "model_used": self.model_name,
                "confidence": self._calculate_confidence(extracted_data),
            }
            
            # Store in history
            self.extraction_history.append({
                "timestamp": st.session_state.get("timestamp", "now"),
                "doc_type": doc_type,
                "tokens_used": response.usage.total_tokens,
                "success": True
            })
            
            return extracted_data
            
        except Exception as e:
            self.extraction_history.append({
                "timestamp": st.session_state.get("timestamp", "now"),
                "doc_type": doc_type,
                "error": str(e),
                "success": False
            })
            return {"error": str(e)}
    
    def batch_extract(self, pdf_files: List, doc_type: str) -> List[Dict[str, Any]]:
        """Extract data from multiple PDF files."""
        results = []
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, pdf_file in enumerate(pdf_files):
            status_text.text(f"Processing {i+1}/{len(pdf_files)}: {pdf_file.name}")
            
            try:
                # Extract text from PDF
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
                
                # Extract data using LLM
                result = self.extract_with_custom_prompt(text.strip(), doc_type)
                result["filename"] = pdf_file.name
                results.append(result)
                
            except Exception as e:
                results.append({
                    "filename": pdf_file.name,
                    "error": str(e)
                })
            
            progress_bar.progress((i + 1) / len(pdf_files))
        
        status_text.text("✅ Batch processing complete!")
        return results
    
    def validate_extraction(self, extracted_data: Dict[str, Any], doc_type: str) -> Dict[str, Any]:
        """Validate extracted data for completeness and accuracy."""
        validation_result = {
            "is_valid": True,
            "missing_fields": [],
            "data_quality_score": 0,
            "suggestions": []
        }
        
        required_fields = self._get_required_fields(doc_type)
        found_fields = 0
        
        for field in required_fields:
            if field not in extracted_data or extracted_data[field] is None:
                validation_result["missing_fields"].append(field)
            else:
                found_fields += 1
        
        validation_result["data_quality_score"] = found_fields / len(required_fields) * 100
        
        if validation_result["data_quality_score"] < 70:
            validation_result["is_valid"] = False
            validation_result["suggestions"].append("Consider re-extracting with a more specific prompt")
        
        return validation_result
    
    def _get_required_fields(self, doc_type: str) -> List[str]:
        """Get required fields for a document type."""
        field_mapping = {
            "invoice": ["invoice_number", "date", "total_amount"],
            "contract": ["parties", "effective_date", "contract_term"],
            "receipt": ["merchant_name", "date", "total_amount"],
            "resume": ["personal_info", "experience", "skills"]
        }
        return field_mapping.get(doc_type, [])
    
    def _calculate_confidence(self, extracted_data: Dict[str, Any]) -> str:
        """Calculate confidence level based on extracted data."""
        non_null_fields = sum(1 for v in extracted_data.values() if v is not None and v != "")
        total_fields = len(extracted_data)
        
        if total_fields == 0:
            return "unknown"
        
        confidence_ratio = non_null_fields / total_fields
        
        if confidence_ratio >= 0.8:
            return "high"
        elif confidence_ratio >= 0.6:
            return "medium"
        else:
            return "low"
    
    def get_extraction_history(self) -> List[Dict[str, Any]]:
        """Get extraction history."""
        return self.extraction_history.copy()
    
    def get_available_prompts(self) -> List[str]:
        """Get list of available document types."""
        return list(self.custom_prompts.keys())

def main():
    """Streamlit app for advanced LLM extraction."""
    st.set_page_config(page_title="Advanced LLM Extractor", layout="wide")
    st.title("Advanced LLM-Based PDF Extraction")
    st.markdown("Enhanced extraction with custom prompts and validation.")
    
    # Initialize extractor
    extractor = AdvancedLLMExtractor(client, model_name)
    
    # Sidebar for advanced features
    with st.sidebar:
        st.header("🔧 Advanced Features")
        
        # Custom prompt creation
        st.subheader("Create Custom Prompt")
        new_doc_type = st.text_input("Document Type", placeholder="e.g., medical_report")
        custom_prompt = st.text_area("Custom Prompt", placeholder="Enter your extraction prompt...")
        
        if st.button("Add Custom Prompt") and new_doc_type and custom_prompt:
            extractor.add_custom_prompt(new_doc_type, custom_prompt)
        
        # Available prompts
        st.subheader("Available Document Types")
        for doc_type in extractor.get_available_prompts():
            st.write(f"• {doc_type}")
        
        # Extraction history
        st.subheader("Extraction History")
        history = extractor.get_extraction_history()
        for entry in history[-5:]:  # Show last 5 entries
            status = "✅" if entry.get("success", False) else "❌"
            st.write(f"{status} {entry.get('doc_type', 'Unknown')}")
    
    # Main content
    tab1, tab2, tab3 = st.tabs(["📄 Single File", "📁 Batch Processing", "📊 Analytics"])
    
    with tab1:
        st.subheader("Single PDF Extraction")
        
        uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'])
        
        if uploaded_file:
            # Extract text
            with st.spinner("Extracting text..."):
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            
            st.success(f"✅ Extracted {len(text)} characters")
            
            # Document type selection
            doc_type = st.selectbox("Select document type:", extractor.get_available_prompts())
            
            # Custom prompt option
            use_custom = st.checkbox("Use custom prompt")
            custom_prompt_text = ""
            if use_custom:
                custom_prompt_text = st.text_area("Enter custom prompt:", height=150)
            
            if st.button("🚀 Extract Data", type="primary"):
                with st.spinner("Processing with LLM..."):
                    result = extractor.extract_with_custom_prompt(
                        text.strip(), 
                        doc_type, 
                        custom_prompt_text if use_custom else None
                    )
                
                # Display results
                if "error" not in result:
                    st.json(result)
                    
                    # Validation
                    validation = extractor.validate_extraction(result, doc_type)
                    st.subheader("📊 Validation Results")
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Valid", "✅" if validation["is_valid"] else "❌")
                    with col2:
                        st.metric("Quality Score", f"{validation['data_quality_score']:.1f}%")
                    with col3:
                        st.metric("Missing Fields", len(validation["missing_fields"]))
                    
                    if validation["missing_fields"]:
                        st.warning(f"Missing fields: {', '.join(validation['missing_fields'])}")
                    
                    if validation["suggestions"]:
                        st.info(f"Suggestions: {'; '.join(validation['suggestions'])}")
                else:
                    st.error(f"Extraction failed: {result['error']}")
    
    with tab2:
        st.subheader("Batch PDF Processing")
        
        uploaded_files = st.file_uploader("Choose multiple PDF files", type=['pdf'], accept_multiple_files=True)
        
        if uploaded_files:
            doc_type = st.selectbox("Select document type for batch:", extractor.get_available_prompts())
            
            if st.button("🚀 Process All Files", type="primary"):
                results = extractor.batch_extract(uploaded_files, doc_type)
                
                # Display batch results
                st.subheader("📊 Batch Results")
                
                successful = [r for r in results if "error" not in r]
                failed = [r for r in results if "error" in r]
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Successful", len(successful))
                with col2:
                    st.metric("Failed", len(failed))
                
                # Show results
                for result in results:
                    with st.expander(f"📄 {result.get('filename', 'Unknown')}"):
                        if "error" in result:
                            st.error(result["error"])
                        else:
                            st.json(result)
    
    with tab3:
        st.subheader("Extraction Analytics")
        
        history = extractor.get_extraction_history()
        
        if history:
            # Statistics
            total_extractions = len(history)
            successful_extractions = sum(1 for h in history if h.get("success", False))
            total_tokens = sum(h.get("tokens_used", 0) for h in history)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Extractions", total_extractions)
            with col2:
                st.metric("Success Rate", f"{successful_extractions/total_extractions*100:.1f}%")
            with col3:
                st.metric("Total Tokens", total_tokens)
            
            # Document type breakdown
            doc_types = {}
            for entry in history:
                doc_type = entry.get("doc_type", "Unknown")
                doc_types[doc_type] = doc_types.get(doc_type, 0) + 1
            
            st.subheader("Document Types Processed")
            for doc_type, count in doc_types.items():
                st.write(f"• {doc_type}: {count} files")
        else:
            st.info("No extraction history available yet.")

if __name__ == "__main__":
    main()
