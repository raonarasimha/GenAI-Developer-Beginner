# 🕒 Day 22: Data Reconciliation with AI Agents

🏁 Goal: Detect mismatches between two datasets and use an AI assistant to propose reconciliations, with both CLI and Streamlit workflows.

---

## 📚 Overview

You will:
- Compare two tabular datasets (CSV) by a key column
- Report missing, conflicting, and matching records
- Ask an AI assistant to propose fixes (standardization, best-value suggestions)
- Review results in a simple Streamlit app

---

## ✅ Learning Objectives

1) Load and compare datasets with pandas
2) Produce reconciliation reports (missing/conflicts)
3) Use OpenAI Responses API to propose field-level fixes in JSON
4) Build a minimal Streamlit UI to visualize and export results

---

## ⚙️ Quick Setup (Day-22 only)

- Install dependencies:
```bash
pip install -r Day-22/requirements.txt
```

- Create `.env` (repo root or `Day-22/`) with:
```bash
OPENAI_API_KEY=your_openai_api_key
```

- Sample data is in `Day-22/assets/` (two CSV files).

---

## ▶️ How to Run

1) Reconciliation (CLI):
```bash
python Day-22/01_reconciliation_basics.py
```

2) AI-Assisted Reconciliation (CLI):
```bash
python Day-22/02_agent_reconciler.py
```

3) Streamlit Reconciliation App:
```bash
streamlit run Day-22/03_streamlit_reconciliation_app.py
```

---

## 📁 Files

- `01_reconciliation_basics.py`: Load two CSVs, compare by key, print a summary report
- `02_agent_reconciler.py`: Use OpenAI to propose JSON fixes for conflicting rows
- `03_streamlit_reconciliation_app.py`: Upload two CSVs, view diffs, request AI proposals, export CSV/JSON
- `assets/`: Sample `source.csv` and `target.csv`

---

## 🧪 Tips

- Keep a small set of key columns (e.g., `id`, `name`, `email`)
- Normalize text before comparing (strip/lower) when appropriate
- Limit AI prompts to only the fields you want corrected

---

Build trustworthy reconciliation flows with human review in the loop!
