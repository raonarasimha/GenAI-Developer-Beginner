# 🕒 Day 19: No‑Code AI Agents & Automation (Theory)

🏁 Goal: Learn how to build simple AI agent workflows using no‑code/low‑code tools for automation, data routing, and integrations. This day is theory-focused with curated links to explore.

---

## 📚 Overview

No‑code platforms let you orchestrate AI tasks and connect services without writing much code. Typical use cases:
- Intake (forms, webhooks) → AI enrichment (summarize, extract) → route to CRM/DB
- AI agent chains that call tools (search, email, sheets) and make decisions
- Human‑in‑the‑loop approvals and notifications

---

## ✅ Learning Objectives

1) Understand core building blocks: triggers, nodes/tools, variables, branches
2) Know common AI steps: prompt templates, structured output, retries/guards
3) Learn human‑in‑the‑loop and approval patterns
4) Map real processes to workflows (support triage, lead scoring, content ops)

---

## 🧩 Core Concepts

- **Triggers**: Start flows via schedule, webhook, form, or app events
- **Tools/Nodes**: Connectors for email, sheets, docs, DBs, Slack, HTTP, webhooks
- **AI Steps**: Prompt with context; parse JSON; route based on model output
- **Data Stores**: Built‑in tables, Google Sheets, Airtable, or external DBs
- **Approvals**: Pause flows for review, escalate, or collect more info
- **Observability**: Run history, input/output logs, error handling, retries
- **Security**: Vaulted creds, environment separation, audit logs

---

## 🧭 Example Use Cases (Design‑first)

- Support triage: classify, summarize, assign to team, notify Slack
- Lead qualification: enrich company data, score, create CRM record
- Content pipeline: draft → review → publish → archive
- Back‑office: invoice parsing → approval → export to accounting

---

## 💡 Best Practices

- Use clear prompt templates with explicit JSON schema
- Add guardrails: max tokens, temperature, retries, fallbacks
- Validate model output before routing (schema/regex checks)
- Keep secrets in platform vaults; separate dev/staging/prod
- Start small; monitor run history and iterate

---

## 🔗 Platforms & Resources

- n8n (open‑source): https://n8n.io/
  - Docs: https://docs.n8n.io/
  - AI features: https://docs.n8n.io/ai/
- Make (Integromat): https://www.make.com/
  - Docs: https://www.make.com/en/help
- Zapier: https://zapier.com/
  - AI actions & interfaces: https://zapier.com/ai
  - Webhooks & Code steps: https://zapier.com/apps/webhook/integrations
- Miro (for agent design & collaboration): https://miro.com/
  - Templates (flows/workshops): https://miro.com/templates/
- Airtable: https://airtable.com/
  - Automations & scripts: https://support.airtable.com/docs
- Google Apps Script (light‑code glue): https://developers.google.com/apps-script
- Prompt patterns (general): https://www.promptingguide.ai/

---

## 📝 Suggested Exercises (Optional, design‑only)

- Sketch a support triage flow in Miro (triggers, AI step, routing)
- List tools/data you need and the fields to standardize
- Define a JSON schema for model output to drive routing decisions

---

Use these resources to plan and prototype no‑code agent automations before implementing.
