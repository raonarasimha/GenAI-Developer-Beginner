"""
Load two CSVs (source/target), compare by `id`, and print a basic reconciliation report.
"""

import os
import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path, dtype=str)


def normalize_df(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in out.columns:
        out[col] = out[col].astype(str).str.strip()
    return out


def main() -> None:
    base = os.path.dirname(__file__)
    src_path = os.path.join(base, "assets", ".gitkeep")  # used as source.csv
    tgt_path = os.path.join(base, "assets", "target.csv")

    source = normalize_df(load_csv(src_path)).set_index("id")
    target = normalize_df(load_csv(tgt_path)).set_index("id")

    src_ids = set(source.index)
    tgt_ids = set(target.index)

    missing_in_target = sorted(src_ids - tgt_ids)
    missing_in_source = sorted(tgt_ids - src_ids)
    common_ids = sorted(src_ids & tgt_ids)

    print("Missing in target:", missing_in_target)
    print("Missing in source:", missing_in_source)

    conflicts = []
    for rid in common_ids:
        row_s = source.loc[rid]
        row_t = target.loc[rid]
        diffs = {}
        for col in source.columns:
            if col in target.columns and row_s[col] != row_t[col]:
                diffs[col] = {"source": row_s[col], "target": row_t[col]}
        if diffs:
            conflicts.append({"id": rid, "diffs": diffs})

    print("Conflicts:")
    for c in conflicts:
        print(c)


if __name__ == "__main__":
    main()


