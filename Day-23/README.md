# 🕒 Day 23: Full‑Stack Web Development with AI Tools (Theory)

🏁 Goal: Understand how to build and ship simple full‑stack apps using AI‑powered tools (Lovable.dev, Replit) and modern hosts (Vercel/Netlify/Cloudflare/Render/Railway). This day is theory‑focused with curated links.

---

## 📚 Overview

AI‑augmented platforms accelerate the full‑stack workflow:
- Scaffold frontends/backends
- Generate components/pages, APIs, and tests
- Seamlessly deploy with CI/CD and environment management

Today you’ll review common architectures, deployment paths, and best practices for secrets, data, logging, and iteration speed.

---

## ✅ Learning Objectives

1) Know typical full‑stack architecture patterns for small AI apps
2) Understand where AI tools (Lovable.dev, Replit) add value in the dev loop
3) Learn modern deployment options and secrets management
4) Understand minimal CI/CD and observability for hobby/entry‑level projects

---

## 🧩 Core Concepts

- **Frontend**: React/Next.js, SSG/SSR; UI components; state & forms
- **Backend**: REST/GraphQL endpoints (FastAPI/Express), auth, rate‑limits
- **Data Layer**: Hosted Postgres (Neon/Supabase/Railway), KV/Edge storage
- **AI Layer**: Server‑side calls to model APIs; prompt templates; guards
- **Secrets & Config**: `.env` files locally; encrypted env vars in hosts
- **Build & Deploy**: One‑click deploys (Vercel/Netlify/Cloudflare); Docker for portability
- **Observability**: Basic logs/metrics; error tracking; simple dashboards

---

## 🏗️ Reference Architectures

- **Static Frontend + Serverless API**
  - Next.js/React on Vercel → API routes call OpenAI → results rendered client‑side
- **SPA + Dedicated Backend**
  - React/Vite (Netlify/Cloudflare Pages) → FastAPI on Render/Railway → DB (Neon/Supabase)
- **All‑in‑one Sandbox**
  - Replit project: frontend + backend + secrets → deploy from the IDE
- **AI‑Assisted Scaffolding**
  - Lovable.dev generates base app (pages/components/api) → push to repo → deploy

---

## 💡 Best Practices

- Keep backend model calls server‑side; never expose raw API keys to the browser
- Use environment‑specific configs: `.env.local` vs hosted env vars
- Add simple auth (passwordless/OTP, OAuth) if storing user data
- Log inputs/outputs (with redaction) for debugging; keep PII minimal
- Start with free hosted Postgres or KV; back up and migrate early
- Add basic CI (format, lint, typecheck) and a smoke test
- Prefer incremental deploys; use preview deployments for reviews

---

## 🔎 What You Should Be Able To Explain

- The difference between static hosting, serverless functions, and full containers
- When to choose Vercel/Netlify/Cloudflare vs Render/Railway
- Where and how to store secrets; how to set `.env` locally
- How AI tools (Lovable.dev, Replit) accelerate iteration and onboarding

---

## 🔗 Platforms & Resources

- **Lovable.dev**
  - Site: https://lovable.dev/
  - Docs/Guides: (product help pages)
- **Replit**
  - Site: https://replit.com/
  - Deployments: https://docs.replit.com/hosting
  - Secrets: https://docs.replit.com/programming-ide/storing-sensitive-information-environment-variables
- **Vercel**
  - Site: https://vercel.com/
  - Env & Deploy: https://vercel.com/docs
- **Netlify**
  - Site: https://www.netlify.com/
  - Functions & Env: https://docs.netlify.com/
- **Cloudflare** (Pages/Workers/D1/KV)
  - Site: https://developers.cloudflare.com/
- **Render**
  - Site: https://render.com/docs
- **Railway**
  - Site: https://railway.app/docs
- **Databases**
  - Neon (Postgres): https://neon.tech/docs
  - Supabase (Postgres + Auth/Storage): https://supabase.com/docs
- **Frameworks**
  - Next.js: https://nextjs.org/docs
  - FastAPI: https://fastapi.tiangolo.com/
- **CI/CD**
  - GitHub Actions: https://docs.github.com/actions
  - Docker Basics: https://docs.docker.com/get-started/

---

## 🧭 Optional Planning Exercises (Design‑only)

- Sketch a small full‑stack app: pages, API endpoints, data tables, and an AI call
- List required environment variables and where they’ll be set in the host
- Define rollout steps: dev → preview → prod; and a rollback plan

---

## ✅ Quick Checklist

- [ ] Secrets configured in host; no keys committed
- [ ] Server‑side model calls; basic input validation
- [ ] Minimal DB schema and backup plan
- [ ] Logs and error alerts enabled
- [ ] Preview deploys working; CI checks pass

---

Use these references to plan and launch simple full‑stack AI apps quickly and safely.
