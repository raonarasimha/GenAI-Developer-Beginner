"""
Streamlit reconciliation app: upload two CSVs, compare by `id`, view differences,
and request AI-proposed fixes via OpenAI Responses API.
"""

import os
import json
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


def find_conflicts_df(source: pd.DataFrame, target: pd.DataFrame) -> list[dict]:
    source = source.set_index("id")
    target = target.set_index("id")
    ids = set(source.index) & set(target.index)
    conflicts = []
    for rid in sorted(ids):
        row_s = source.loc[rid]
        row_t = target.loc[rid]
        diffs = {}
        for col in source.columns:
            if col in target.columns and row_s[col] != row_t[col]:
                diffs[col] = {"source": row_s[col], "target": row_t[col]}
        if diffs:
            conflicts.append({"id": rid, "diffs": diffs})
    return conflicts


def propose_fixes(client: OpenAI, conflicts: list[dict]) -> dict:
    prompt = (
        "You are a data reconciliation assistant. For each conflicting field, propose a fix as JSON. "
        "Prefer values that look valid (e.g., emails). If unknown, set null.\n\n"
        f"Conflicts:\n{json.dumps(conflicts, indent=2)}\n\nReturn JSON with: fixes: [{{id, fields: {{col: value_or_null}}}}]"
    )
    resp = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        temperature=0.2,
        response_format={"type": "json_object"},
    )
    text = (getattr(resp, "output_text", None) or "").strip()
    if not text:
        try:
            text = resp.output[0].content[0].text
        except Exception:
            text = "{}"
    try:
        return json.loads(text)
    except Exception:
        return {"fixes": []}


def main() -> None:
    load_dotenv()
    st.set_page_config(page_title="Day-22 Reconciliation", layout="wide")
    st.title("Day-22: Data Reconciliation with AI Agents")

    if not os.getenv("OPENAI_API_KEY"):
        st.error("Please set OPENAI_API_KEY in your .env file")
        st.stop()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    st.subheader("Upload CSVs")
    col1, col2 = st.columns(2)
    with col1:
        src_file = st.file_uploader("Source CSV", type=["csv"])
    with col2:
        tgt_file = st.file_uploader("Target CSV", type=["csv"])

    if src_file and tgt_file:
        src_df = pd.read_csv(src_file, dtype=str).fillna("")
        tgt_df = pd.read_csv(tgt_file, dtype=str).fillna("")

        st.subheader("Basic Stats")
        st.write("Source rows:", len(src_df))
        st.write("Target rows:", len(tgt_df))

        st.subheader("Conflicts")
        conflicts = find_conflicts_df(src_df, tgt_df)
        st.json(conflicts)

        if conflicts:
            if st.button("Propose AI Fixes", type="primary"):
                with st.spinner("Calling OpenAI..."):
                    fixes = propose_fixes(client, conflicts)
                st.subheader("AI-Proposed Fixes")
                st.json(fixes)
                st.download_button(
                    label="Download Fixes (JSON)",
                    data=json.dumps(fixes, indent=2),
                    file_name="reconciliation_fixes.json",
                    mime="application/json",
                )


if __name__ == "__main__":
    main()


