"""
Day 12 - Production Deployment
=============================

Production-ready deployment for LLM-based PDF extraction.
"""

import os
import json
import streamlit as st
import PyPDF2
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv
import time
import logging

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

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductionPDFExtractor:
    """Production-ready PDF extraction system."""
    
    def __init__(self, client, model_name):
        self.client = client
        self.model_name = model_name
        self.rate_limits = {"requests_per_minute": 60, "last_request": 0}
        self.error_counts = {"total": 0, "rate_limit": 0, "api_error": 0}
        self.performance_metrics = {"avg_response_time": 0, "total_requests": 0}
    
    def extract_with_rate_limiting(self, pdf_text: str, doc_type: str) -> Dict[str, Any]:
        """Extract data with rate limiting and error handling."""
        start_time = time.time()
        
        try:
            # Rate limiting
            current_time = time.time()
            if current_time - self.rate_limits["last_request"] < 1:  # 1 second between requests
                time.sleep(1)
            
            # Prepare prompt
            prompt = self._get_production_prompt(doc_type)
            full_prompt = prompt + "\n\nDocument text:\n" + pdf_text[:4000]
            
            # Make API call
            response = self.client.responses.create(
                model=self.model_name,
                input=full_prompt,
                temperature=0.1,
                timeout=30,
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

            # Update metrics
            response_time = time.time() - start_time
            self._update_metrics(response_time, True)
            self.rate_limits["last_request"] = current_time
            
            # Add production metadata
            extracted_data["production_metadata"] = {
                "extraction_time": response_time,
                "tokens_used": total_tokens or 0,
                "model_version": self.model_name,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "request_id": f"req_{int(time.time())}"
            }
            
            logger.info(f"Successful extraction: {doc_type} in {response_time:.2f}s")
            return extracted_data
            
        except json.JSONDecodeError as e:
            self._update_metrics(time.time() - start_time, False)
            logger.error(f"JSON parsing error: {str(e)}")
            return {"error": "Invalid JSON response", "details": str(e)}
            
        except Exception as e:
            self._update_metrics(time.time() - start_time, False)
            logger.error(f"Extraction error: {str(e)}")
            return {"error": "Extraction failed", "details": str(e)}
    
    def _get_production_prompt(self, doc_type: str) -> str:
        """Get production-optimized prompts."""
        prompts = {
            "invoice": """
            Extract invoice data as JSON with these exact fields:
            - invoice_number (string)
            - date (string, YYYY-MM-DD format)
            - due_date (string, YYYY-MM-DD format)
            - customer_name (string)
            - customer_address (string)
            - line_items (array of objects: description, quantity, unit_price, total)
            - subtotal (number)
            - tax_amount (number)
            - total_amount (number)
            - payment_terms (string)
            
            Use null for missing fields. Return only valid JSON.
            """,
            
            "contract": """
            Extract contract data as JSON with these exact fields:
            - parties (object: company_name, client_name, addresses)
            - effective_date (string, YYYY-MM-DD format)
            - contract_term (string)
            - services (array of strings)
            - payment_amount (number)
            - payment_frequency (string)
            - termination_terms (string)
            
            Use null for missing fields. Return only valid JSON.
            """,
            
            "receipt": """
            Extract receipt data as JSON with these exact fields:
            - merchant_name (string)
            - date (string, YYYY-MM-DD format)
            - time (string, HH:MM format)
            - items (array of objects: description, quantity, unit_price, total)
            - subtotal (number)
            - tax_amount (number)
            - total_amount (number)
            - payment_method (string)
            
            Use null for missing fields. Return only valid JSON.
            """
        }
        return prompts.get(doc_type, prompts["invoice"])
    
    def _update_metrics(self, response_time: float, success: bool):
        """Update performance metrics."""
        self.performance_metrics["total_requests"] += 1
        
        if success:
            # Update average response time
            total_requests = self.performance_metrics["total_requests"]
            current_avg = self.performance_metrics["avg_response_time"]
            self.performance_metrics["avg_response_time"] = (
                (current_avg * (total_requests - 1) + response_time) / total_requests
            )
        else:
            self.error_counts["total"] += 1
    
    def get_health_status(self) -> Dict[str, Any]:
        """Get system health status."""
        return {
            "status": "healthy" if self.error_counts["total"] < 10 else "degraded",
            "error_rate": self.error_counts["total"] / max(self.performance_metrics["total_requests"], 1),
            "avg_response_time": self.performance_metrics["avg_response_time"],
            "total_requests": self.performance_metrics["total_requests"],
            "error_counts": self.error_counts
        }
    
    def reset_metrics(self):
        """Reset performance metrics."""
        self.error_counts = {"total": 0, "rate_limit": 0, "api_error": 0}
        self.performance_metrics = {"avg_response_time": 0, "total_requests": 0}

def main():
    """Production deployment demonstration."""
    st.set_page_config(page_title="Production PDF Extractor", layout="wide")
    st.title("🚀 Production-Ready PDF Extraction")
    st.markdown("Enterprise-grade PDF extraction with monitoring and error handling")
    
    # Initialize extractor
    extractor = ProductionPDFExtractor(client, model_name)
    
    # Sidebar for production features
    with st.sidebar:
        st.header("🏭 Production Features")
        
        # Health monitoring
        st.subheader("System Health")
        health = extractor.get_health_status()
        
        status_color = "green" if health["status"] == "healthy" else "orange"
        st.metric("Status", health["status"], delta=None)
        st.metric("Error Rate", f"{health['error_rate']*100:.1f}%")
        st.metric("Avg Response Time", f"{health['avg_response_time']:.2f}s")
        st.metric("Total Requests", health["total_requests"])
        
        # Reset metrics
        if st.button("Reset Metrics"):
            extractor.reset_metrics()
            st.success("Metrics reset!")
        
        # Deployment info
        st.subheader("Deployment Info")
        st.write("• Environment: Production")
        st.write(f"• Model: {model_name} (OpenRouter)")
        st.write("• Rate Limiting: Enabled")
        st.write("• Error Handling: Active")
        st.write("• Logging: Enabled")
    
    # Main content
    tab1, tab2, tab3 = st.tabs(["📄 Extraction", "📊 Monitoring", "🔧 Configuration"])
    
    with tab1:
        st.subheader("Production PDF Extraction")
        
        uploaded_file = st.file_uploader("Upload PDF for extraction", type=['pdf'])
        
        if uploaded_file:
            # Extract text
            with st.spinner("Extracting text from PDF..."):
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            
            st.success(f"✅ Extracted {len(text)} characters")
            
            # Document type selection
            doc_type = st.selectbox("Select document type:", ["invoice", "contract", "receipt"])
            
            # Production extraction
            if st.button("🚀 Extract (Production)", type="primary"):
                with st.spinner("Processing with production system..."):
                    result = extractor.extract_with_rate_limiting(text.strip(), doc_type)
                
                # Display results
                if "error" not in result:
                    st.success("✅ Extraction successful!")
                    
                    # Show extracted data
                    st.subheader("📊 Extracted Data")
                    st.json(result)
                    
                    # Show production metadata
                    if "production_metadata" in result:
                        metadata = result["production_metadata"]
                        st.subheader("🏭 Production Metadata")
                        
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            st.metric("Extraction Time", f"{metadata['extraction_time']:.2f}s")
                        with col2:
                            st.metric("Tokens Used", metadata["tokens_used"])
                        with col3:
                            st.metric("Model", metadata["model_version"])
                        with col4:
                            st.metric("Request ID", metadata["request_id"])
                    
                    # Download result
                    json_str = json.dumps(result, indent=2)
                    st.download_button(
                        label="📥 Download JSON",
                        data=json_str,
                        file_name=f"production_extraction_{doc_type}.json",
                        mime="application/json"
                    )
                else:
                    st.error(f"❌ Extraction failed: {result['error']}")
                    if "details" in result:
                        st.error(f"Details: {result['details']}")
    
    with tab2:
        st.subheader("System Monitoring")
        
        # Real-time metrics
        health = extractor.get_health_status()
        
        # Performance chart
        st.subheader("📈 Performance Metrics")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("System Status", health["status"].title())
            st.metric("Average Response Time", f"{health['avg_response_time']:.2f}s")
        with col2:
            st.metric("Error Rate", f"{health['error_rate']*100:.1f}%")
            st.metric("Total Requests", health["total_requests"])
        
        # Error breakdown
        st.subheader("🚨 Error Analysis")
        error_counts = health["error_counts"]
        
        if error_counts["total"] > 0:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Errors", error_counts["total"])
            with col2:
                st.metric("Rate Limit Errors", error_counts["rate_limit"])
            with col3:
                st.metric("API Errors", error_counts["api_error"])
        else:
            st.success("✅ No errors recorded")
        
        # System recommendations
        st.subheader("💡 System Recommendations")
        
        if health["error_rate"] > 0.1:
            st.warning("⚠️ High error rate detected. Consider checking API limits.")
        
        if health["avg_response_time"] > 5:
            st.warning("⚠️ Slow response times. Consider optimizing prompts.")
        
        if health["status"] == "healthy":
            st.success("✅ System performing well")
    
    with tab3:
        st.subheader("Production Configuration")
        
        # Environment variables
        st.subheader("🔧 Environment Configuration")
        
        env_vars = {
            "OPENROUTER_API_KEY": "Set" if os.getenv("OPENROUTER_API_KEY") else "Not Set",
            "OPENAI_API_BASE": "Set" if os.getenv("OPENAI_API_BASE") else "Not Set",
            "OPENAI_MODEL_NAME": "Set" if os.getenv("OPENAI_MODEL_NAME") else "Not Set",
            "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
            "RATE_LIMIT": "60 requests/minute",
            "TIMEOUT": "30 seconds",
            "MODEL": model_name
        }
        
        for var, value in env_vars.items():
            st.write(f"**{var}**: {value}")
        
        # Production settings
        st.subheader("⚙️ Production Settings")
        
        st.write("**Rate Limiting**: Enabled (1 second between requests)")
        st.write("**Error Handling**: Comprehensive error catching")
        st.write("**Logging**: Structured logging enabled")
        st.write("**Timeout**: 30 seconds per request")
        st.write(f"**Model**: {model_name} (OpenRouter)")
        
        # Deployment checklist
        st.subheader("✅ Deployment Checklist")
        
        checklist_items = [
            "✅ API key configured",
            "✅ Error handling implemented",
            "✅ Rate limiting enabled",
            "✅ Logging configured",
            "✅ Performance monitoring active",
            "✅ Health checks implemented"
        ]
        
        for item in checklist_items:
            st.write(item)
        
        # Deployment commands
        st.subheader("🚀 Deployment Commands")
        
        st.code("""
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export OPENROUTER_API_KEY=your_key_here
export OPENAI_API_BASE=https://openrouter.ai/api/v1
export OPENAI_MODEL_NAME=openrouter/moonshotai/kimi-k2:free

# Run with Streamlit
streamlit run 03_production_deployment.py

# Deploy to Streamlit Cloud
# 1. Push to GitHub
# 2. Connect to Streamlit Cloud
# 3. Set environment variables in dashboard
        """, language="bash")

if __name__ == "__main__":
    main()
