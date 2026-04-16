# 🕒 Day 16: Azure AI Services (Theory)

🏁 Goal: Understand Microsoft Azure AI Services (including Azure OpenAI), core concepts, security/governance, and how to integrate them into GenAI apps. This day is theory-focused (no coding) with curated links for self-study.

---

## 📚 Overview

Azure AI Services provide managed access to foundation models (Azure OpenAI) and classic cognitive services (Vision, Speech, Language, Search). Azure offers enterprise-grade security, compliance, networking, and monitoring options across regions.

---

## ✅ Learning Objectives

1) Know the main building blocks: Azure OpenAI, Azure AI Studio, Cognitive Services
2) Understand deployments, model versions, and quota/regions
3) Learn security, governance, and responsible AI features
4) Know SDK/API integration paths and monitoring options

---

## 🧩 Core Concepts

- **Azure OpenAI**: Managed access to OpenAI models (chat, embeddings, image). You deploy a model (e.g., GPT-4o family) and call it via your endpoint + key or AAD.
- **Azure AI Studio**: Portal for prompt flow, grounding (RAG), safety filters, evaluation, and model orchestration.
- **Cognitive Services**: Vision, Speech, Language, Translator, Search (Bing/AI Search) with classic APIs.
- **Deployments**: Create a deployment name for a specific model + version; your apps call that deployment.
- **Networking**: Private endpoints/VNET, IP firewalling; data-residency controls.
- **Security/Identity**: Keys or Azure AD (Managed Identity, OAuth2), RBAC, Key Vault for secret storage.
- **Responsible AI**: Content filters, safety policies, abuse monitoring; policy configuration in Studio.
- **Observability**: Azure Monitor, App Insights, Log Analytics; Request metrics and tracing.

---

## 🏗️ Reference Architectures

- **Basic Chat**: Client → App Service/Function → Azure OpenAI (deployed model)
- **RAG**: Client → API → Azure AI Search (vector index) → Azure OpenAI
- **Multimodal**: Client uploads media → Storage → Cognitive Services (Vision/Speech) → Azure OpenAI
- **Enterprise**: Private networking + Key Vault + Managed Identity + Azure Monitor

---

## 💡 Best Practices

- Choose a region that supports your target model and features
- Use **deployments** to pin model versions and manage rollouts
- Prefer **Azure AD**/Managed Identity over static keys where possible
- Store secrets in **Key Vault**; enforce RBAC and network restrictions
- Enable content filters and document acceptable use
- Log requests/metrics and set alerts in Azure Monitor
- Plan quotas/costs; test token usage and throughput

---

## 🔎 What You Should Be Able To Explain

- Difference between Azure OpenAI vs OpenAI public API
- How a model deployment works and why it’s required
- Identity options (keys vs AAD), network isolation, and data governance
- Where to configure safety/content filters and observe usage

---

## 🔗 Official Documentation & Resources

- **Azure OpenAI**
  - Service overview: https://learn.microsoft.com/azure/ai-services/openai/overview
  - Quickstarts & SDKs: https://learn.microsoft.com/azure/ai-services/openai/quickstart
  - Model catalog & versions: https://learn.microsoft.com/azure/ai-services/openai/how-to/working-with-models
  - Deployments & quotas: https://learn.microsoft.com/azure/ai-services/openai/how-to/quota
- **Azure AI Studio**
  - Studio overview: https://learn.microsoft.com/azure/ai-studio/overview
  - Prompt flow & evaluation: https://learn.microsoft.com/azure/ai-studio/concepts/prompt-flow
  - Safety: https://learn.microsoft.com/azure/ai-studio/concepts/responsible-use-of-ai-overview
- **Cognitive Services**
  - Vision/Speech/Language: https://learn.microsoft.com/azure/ai-services/
  - Azure AI Search (vector/RAG): https://learn.microsoft.com/azure/search/
- **Security & Networking**
  - Authentication & AAD: https://learn.microsoft.com/azure/ai-services/openai/how-to/managed-identity
  - Private networking: https://learn.microsoft.com/azure/ai-services/openai/how-to/private-networking
  - Key Vault: https://learn.microsoft.com/azure/key-vault/general/overview
- **Monitoring**
  - Azure Monitor: https://learn.microsoft.com/azure/azure-monitor/overview
  - Application Insights: https://learn.microsoft.com/azure/azure-monitor/app/app-insights-overview

---

## 🧭 Optional Next Steps (Hands-on later)

- Create an Azure OpenAI resource and deploy a model in your region
- Call the deployed model via SDK (Python) using AAD/Managed Identity
- Add content filters and observe blocked categories
- Build a small RAG using Azure AI Search + Azure OpenAI

---

## 📋 Quick Checklist

- [ ] Region supports target models/features
- [ ] Deployment created for each model/version
- [ ] Identity chosen (AAD/Managed Identity ≥ keys)
- [ ] Secrets stored in Key Vault; RBAC enforced
- [ ] Monitoring enabled; alerts configured
- [ ] Safety/content policies documented

---

This day is theory-only. Use the links above to explore and prepare for hands-on Azure AI integrations later.
