# 🕒 Day 21: AI Application Security & Ethics (Theory)

🏁 Goal: Learn essential security, privacy, and ethics practices for GenAI apps. This day is theory-focused (no coding) with curated links to read and reference.

---

## 📚 Overview

Building GenAI systems safely requires more than good prompts. You must protect secrets and data, defend against prompt‑level threats, respect user consent, and design for responsible use. Today you’ll review core risks and controls used in production AI applications.

---

## ✅ Learning Objectives

1) Understand common GenAI security risks (secrets, injections, data leakage, misuse)
2) Learn practical controls: key management, least privilege, input/output validation, logging/redaction
3) Recognize responsible AI principles: transparency, consent, safety, fairness, and oversight
4) Know where to find official guidance and checklists

---

## 🧩 Core Topics

- **Secrets & Access**
  - Store API keys in env/secret vaults; never commit secrets
  - Rotate keys; scope with least‑privilege policies
  - Use role‑based access, audit trails, rate limits

- **Data Protection**
  - Minimize and mask PII before sending to models
  - Encrypt at rest/in transit; define retention/TTL
  - Redact logs; separate production/test data

- **Prompt Injection & Abuse**
  - Treat user input as untrusted
  - System prompt hardening; instruction hierarchies
  - Content filters/guardrails; tool‑use allowlists
  - Validate structured outputs (JSON schema) before acting

- **Output Validation & Safety**
  - Check for policy violations, hallucinations, and unsafe actions
  - Human‑in‑the‑loop for critical operations
  - Stabilize prompts; test with red‑team inputs

- **Observability & Governance**
  - Log model metadata (model, version, tokens) and decisions
  - Track incidents; define rollback/kill‑switches
  - Document data sources and limitations (model/capability cards)

- **Ethics & Responsible AI**
  - Transparency and consent for data usage
  - Fairness: assess bias; avoid discriminatory outcomes
  - Safety: do no harm; guard against abuse
  - Accountability: clear ownership and escalation paths

---

## 💡 Best Practices

- Use secret managers (Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager)
- Enforce least privilege and network isolation where possible
- Sanitize/normalize inputs; constrain outputs with schemas
- Apply safety filters and monitoring; add human approval for risky actions
- Run regular red‑team tests; maintain a prompt/library version history
- Provide user opt‑out and data deletion pathways

---

## 🔎 What You Should Be Able To Explain

- Why prompt injection is dangerous and how to mitigate it
- How to handle PII and user consent in GenAI workflows
- When to add human‑in‑the‑loop and why
- What logs/metrics to keep for audits without violating privacy

---

## 🔗 Recommended Resources

- OWASP Top 10 for LLM Applications (2023): https://owasp.org/www-project-top-10-for-large-language-model-applications/
- NIST AI Risk Management Framework (AI RMF): https://www.nist.gov/itl/ai-risk-management-framework
- Microsoft Responsible AI Standard: https://www.microsoft.com/ai/responsible-ai
- Google Responsible AI Practices: https://ai.google/responsibilities/responsible-ai-practices/
- OpenAI Safety & System Cards: https://openai.com/policies
- Anthropic Responsible Scaling Policy (RSP): https://www.anthropic.com/research/responsible-scaling-policy
- UK AISI & US AI Safety guidance (overview): https://www.gov.uk/government/collections/ai-safety-institute and https://www.ai.gov/
- GDPR overview (EU data protection): https://gdpr.eu/

---

## 🧭 Optional Next Steps (Design Exercises)

- Draft a threat model (STRIDE‑lite) for a simple AI feature
- Write a data‑handling policy: what is logged, masked, retained, deleted
- Define a JSON schema and validator for a high‑risk tool output
- Create a red‑team checklist for prompt injection and jailbreaks

---

## ✅ Quick Checklist

- [ ] Secrets in vaults; keys rotated; least‑privilege in place
- [ ] PII minimized/masked; retention defined; user consent documented
- [ ] Input/output validation; schemas; guardrails configured
- [ ] Monitoring/alerts; incident/rollback runbooks
- [ ] Ethics reviewed (fairness, transparency, safety, accountability)

---

Use this as a reference when building and reviewing AI features before production.
