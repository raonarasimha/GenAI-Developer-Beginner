"""
Use OpenAI to propose JSON fixes for conflicting rows between two CSVs.
"""

import os
import json
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI


def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path, dtype=str)


def find_conflicts(source: pd.DataFrame, target: pd.DataFrame) -> list[dict]:
    source = source.set_index("id")
    target = target.set_index("id")
    conflicts = []
    ids = set(source.index) & set(target.index)
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
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set OPENAI_API_KEY in your .env file")
        return
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    base = os.path.dirname(__file__)
    src_path = os.path.join(base, "assets", ".gitkeep")
    tgt_path = os.path.join(base, "assets", "target.csv")
    source = load_csv(src_path)
    target = load_csv(tgt_path)

    conflicts = find_conflicts(source, target)
    print("Found conflicts:", json.dumps(conflicts, indent=2))

    fixes = propose_fixes(client, conflicts)
    print("Proposed fixes:\n", json.dumps(fixes, indent=2))


if __name__ == "__main__":
    main()


