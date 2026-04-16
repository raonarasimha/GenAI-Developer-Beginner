# 🕒 Day 15: AWS Bedrock Integration (Theory)

🏁 Goal: Understand Amazon Bedrock, its core concepts, supported models, security/IAM, and how to integrate it into GenAI apps. This day is theory-focused (no coding required) and provides curated links to continue learning.

---

## 📚 Overview

Amazon Bedrock is a fully managed service that provides foundation models (FMs) from leading providers (e.g., Anthropic, Meta, Cohere, Amazon) via a unified API, with enterprise-grade security, governance, and tooling (Guardrails, Knowledge Bases, Agents, Model Evaluation).

---

## ✅ Learning Objectives

1) Understand Bedrock building blocks: Models, Guardrails, Knowledge Bases, Agents
2) Learn how access control works (IAM, model access), quotas and regions
3) Know the typical integration paths: Console, SDK/Runtime APIs, and with other AWS services
4) Learn cost, governance, and observability considerations

---

## 🧩 Core Concepts

- **Foundation Models (FMs)**: Multiple providers under one service (text, chat, embeddings, image)
- **Model Access**: Enable specific models per account/region before use
- **Invocation Paths**:
  - Console playgrounds (try models interactively)
  - **Runtime APIs** (Bedrock Runtime / Converse, embeddings/image endpoints)
  - SDKs via AWS SDK (e.g., `boto3`), or through managed integrations
- **Guardrails**: Safety, content filtering, sensitive topics controls
- **Knowledge Bases (RAG)**: Managed retrieval with vector stores; index your data and ground model responses
- **Agents for Bedrock**: Orchestrate multi-step tasks with tool invocations and function-calling
- **Observability**: CloudWatch metrics/logs, traces, model usage dashboards
- **Security & Compliance**: IAM policies, VPC endpoints, encryption, data residency, private model endpoints

---

## 🏗️ Reference Architectures

- **Basic Chat App**: Client → API (Lambda/FastAPI) → Bedrock Runtime
- **RAG**: Client → API → Knowledge Base (data sources + embeddings) → Bedrock model
- **Tools/Agents**: Client → API → Agents for Bedrock (tool schema, steps) → Downstream AWS services
- **Enterprise**: Add Guardrails, CloudWatch logs/metrics, KMS encryption, VPC endpoints

---

## 💡 Best Practices

- **Access & Regions**: Confirm chosen region supports your target models and features
- **Least-privilege IAM**: Scope to Bedrock runtime actions and specific models
- **Cost Awareness**: Track tokens and image generations; set budgets/alarms
- **Governance**: Use Guardrails for safety and content policies; document allowed use cases
- **RAG First**: Ground responses with approved knowledge sources via Knowledge Bases
- **Observability**: Enable CloudWatch metrics/logs; consider tracing for critical flows
- **Data Privacy**: Review data retention and model data handling policies

---

## 🔎 What Students Should Be Able To Explain

- When to choose Bedrock vs direct model APIs
- How to enable and invoke a specific model
- The role of Guardrails, Knowledge Bases, and Agents
- IAM policies and security boundaries

---

## 🔗 Official Documentation & Resources

- **Service Docs**
  - Amazon Bedrock – Product page & docs: https://docs.aws.amazon.com/bedrock/
  - Regions and quotas: https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html
  - Pricing: https://aws.amazon.com/bedrock/pricing/
- **Runtime & SDK**
  - Bedrock Runtime (API): https://docs.aws.amazon.com/bedrock/latest/userguide/model-invoke.html
  - boto3 Bedrock Runtime (Python): https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html
  - Converse/Converse-stream APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html
- **Guardrails**
  - Guardrails for Amazon Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html
- **Knowledge Bases (RAG)**
  - Knowledge Bases: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html
- **Agents**
  - Agents for Amazon Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html
- **Security & IAM**
  - IAM for Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html
  - VPC & Private Access: https://docs.aws.amazon.com/bedrock/latest/userguide/vpc.html
- **Observability**
  - CloudWatch for Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-cloudwatch.html

---

## 🧭 Optional Next Steps (Hands-on, later days)

- Enable a model in your AWS account and invoke it via the console playground
- Use `boto3` to call the Bedrock Runtime from a simple Python script
- Create a Guardrail policy and test prompt filtering
- Set up a minimal Knowledge Base to perform a RAG query

---

## 📋 Quick Checklist

- [ ] Region supports chosen models/features
- [ ] Model access enabled
- [ ] IAM roles/policies in place (least privilege)
- [ ] Budget/alarms for cost control
- [ ] Logging/metrics enabled
- [ ] Data governance (PII, retention) defined

---

This day is theory-only. Use the links above to explore and prepare for hands-on Bedrock integrations later.
