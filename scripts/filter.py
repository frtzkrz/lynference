"""
Load CSV data containing lymphatic involvement of head and neck cancer patients
and keep only those with oral cavity tumors (i.e., specific ICD codes).
"""
import argparse
from pathlib import Path

import pandas as pd


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="Input CSV file")
    parser.add_argument("--output", type=Path, help="Output CSV file")
    parser.add_argument("--location", type=str, help="Location (Hypopharynx)")
    args = parser.parse_args()

    patient_data = pd.read_csv(args.input, header=[0, 1, 2])
    hypopharynx_data = patient_data.loc[patient_data['tumor', '1', 'location']==args.location]

    hypopharynx_data.to_csv(args.output, index=False)