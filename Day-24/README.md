# 🕒 Day 24: Mini Project – Simple AI Application (Theory)

🏁 Goal: Plan a small end‑to‑end AI app you could implement in a day or two. Today is planning/theory only: define scope, UX, data, prompts, evaluation, and deployment. No coding required.

---

## 📚 Overview

You will draft a lightweight plan for a simple AI application (web or CLI). Examples:
- PDF assistant: upload PDF → ask questions → answers grounded in doc (basic RAG)
- Content helper: generate post/title/summary → approve → export to CMS/Sheet
- Support triage: classify ticket, summarize, suggest next actions

Focus on a small slice you can realistically build with tools learned so far.

---

## ✅ Planning Objectives

1) Define a clear user problem and success criteria
2) Outline UX (screens/flows) and data requirements
3) Design prompts and guardrails; decide on evaluation
4) Prepare a minimal deployment plan and checklist

---

## 🧭 Project Scoping Template

- Problem statement: who is the user; what is painful today?
- Goal/Outcome: what will success look like (1–2 KPIs)?
- Primary user tasks: list 2–3 tasks (e.g., upload, ask, export)
- Constraints: model cost, latency, privacy, uptime
- Risks: hallucinations, prompt injection, PII, rate limits

---

## 🎨 UX & Data

- Entry points: upload, paste text, type prompt
- Screens: input → result → history/log → export
- Data: what is stored (inputs/outputs/metadata); retention policy
- State: session history length; what’s shown to user; how errors appear

---

## 🧠 Prompts & Guards

- System prompt: role, style, constraints
- User prompts: structure, few‑shot examples, JSON schema (if needed)
- Guardrails: max tokens, temperature, content policies, output validation
- RAG (optional): chunk size, top‑k, context window, “I don’t know” policy

---

## 📏 Evaluation (Lightweight)

- Functional checks: required fields present; output passes schema
- Quality spot‑checks: 5–10 examples with rubric (1–5)
- Cost/latency tracking: tokens/time per request
- Safety checks: red‑team prompts for injection/abuse

---

## 🚀 Deployment (Minimal)

- Hosting: Vercel/Netlify (frontend) + Render/Railway (API) or Streamlit Cloud
- Secrets: `.env` locally; encrypted env vars in host
- Monitoring: logs, error alerts, simple dashboards
- Rollback: keep previous version; easy revert path

---

## ✅ Launch Checklist

- [ ] Clear scope and success criteria
- [ ] Prompts documented; outputs validated (schema if applicable)
- [ ] Secrets configured; no keys in client code
- [ ] Basic logs/metrics enabled; error handling tested
- [ ] Privacy notes and data retention stated
- [ ] Small user test (3–5 people) and feedback collected

---

## 🔗 Useful References

- Prompt engineering guide: https://www.promptingguide.ai/
- OpenAI evals & testing ideas: https://platform.openai.com/docs/guides/evals
- Streamlit docs (rapid UI): https://docs.streamlit.io/
- FastAPI docs (APIs): https://fastapi.tiangolo.com/
- Vercel deploy docs: https://vercel.com/docs
- Netlify docs: https://docs.netlify.com/
- Render docs: https://render.com/docs
- Railway docs: https://railway.app/docs
- Supabase docs (DB/Auth/Storage): https://supabase.com/docs
- Security checklists (OWASP LLM): https://owasp.org/www-project-top-10-for-large-language-model-applications/

---

Use this day to create a concise plan you can implement on Day 25 or afterwards.
