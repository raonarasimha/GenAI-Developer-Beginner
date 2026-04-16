# 🕒 Day 25: Project Showcase, Interview Prep & Learning Path (Theory)

🏁 Goal: Prepare to present your work professionally, practice core interview topics, and map a realistic learning path beyond this course.

---

## 📚 Overview

Today is reflection and preparation:
- Curate and present your mini project(s)
- Review typical interview themes for junior GenAI/dev roles
- Plan what to learn next (framework depth, cloud, security, teamwork)

---

## ✅ Objectives

1) Build a concise project showcase (repo + README + demo)
2) Practice foundational interview questions (prompts, APIs, data, security)
3) Outline a 30–60–90 day learning plan

---

## 🧩 Project Showcase Guide

- Repository basics
  - Clear README: problem, features, stack, how to run, screenshots/GIF
  - One‑click/run instructions; sample `.env.example`
  - Short demo video (2–5 min) hosted on unlisted YouTube/Drive
- Storytelling
  - Problem → approach → trade‑offs → results → next steps
  - What you measured (latency, tokens, cost) and how you improved it
- Quality
  - Lint/format, minimal tests (smoke), basic error handling
  - No secrets in code; `.gitignore` and sample env

---

## 🎤 Interview Prep Topics (Starter)

- Prompting & LLMs
  - Few‑shot vs zero‑shot; controlling output (JSON), temperature, tokens
  - Hallucinations and mitigation (RAG, validation, “I don’t know”)
- APIs & Data
  - Calling OpenAI (Responses/Images/Embeddings); rate limits, retries
  - File formats: JSON, CSV, PDF basics; chunking strategies
- RAG & Indexing
  - Chunk size/overlap; top‑k; embeddings; vector stores (FAISS/Chroma)
- Agents & Tools
  - When to use agents; tool schemas; guardrails; human‑in‑the‑loop
- Security & Ethics
  - Secrets management, PII handling, prompt injection defenses
- Web & Deployment (high‑level)
  - Frontend/backend split, serverless vs containers, env vars, logs

Sample behavioral prompts
- “Describe a time you debugged a tricky issue.”
- “How do you handle ambiguous requirements?”
- “What trade‑offs did you make in your project?”

---

## 🧭 Learning Path (30–60–90)

- 0–30 days
  - Solidify Python & FastAPI/Streamlit
  - Deeper prompt engineering; structured outputs; evaluations
  - Ship 1–2 small features to your project (e.g., better prompts, caching)
- 31–60 days
  - RAG depth: chunkers, hybrid search, evals, observability
  - One agentic workflow with safe tool use and approvals
  - Add tests, CI, preview deploys; basic dashboards
- 61–90 days
  - Cloud specialization (AWS/Azure/GCP) and one managed vector store
  - Security pass: secrets, PII policy, logging/redaction, threat model
  - Portfolio: 2–3 polished demos with short videos

---

## ✅ Personal Checklist

- [ ] Project README, demo video, and clean repo
- [ ] Practice answers for 10–15 common questions
- [ ] One‑page learning plan with milestones
- [ ] Updated resume + LinkedIn + GitHub profile

---

## 🔗 Curated Resources

- Prompting & Eval
  - Prompt Engineering Guide: https://www.promptingguide.ai/
  - OpenAI Evals ideas: https://platform.openai.com/docs/guides/evals
- Frameworks & Agents
  - OpenAI Agents SDK: https://openai.github.io/openai-agents-python/
  - LangChain Docs: https://python.langchain.com/
  - CrewAI Docs: https://docs.crewai.com/
- RAG & Vector DBs
  - FAISS: https://faiss.ai/
  - Chroma: https://docs.trychroma.com/
- Web & Deploy
  - FastAPI: https://fastapi.tiangolo.com/
  - Streamlit: https://docs.streamlit.io/
  - Vercel: https://vercel.com/docs
  - Netlify: https://docs.netlify.com/
- Cloud & Security
  - AWS Bedrock: https://docs.aws.amazon.com/bedrock/
  - Azure OpenAI: https://learn.microsoft.com/azure/ai-services/openai/overview
  - OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications/

---

Use this day to polish your story, rehearse, and set a realistic next‑steps plan.
