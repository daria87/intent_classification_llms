import pandas as pd
import re
from read_file import read_tsv
from sklearn.metrics import classification_report

def rename_manual_label(df):
    df['label_manual'] = df['label_manual'].replace({'Abstain': 'Informational', 'Factual': 'Informational','Instrumental': 'Informational'})
    return df


def extract_query_intent(label):
    # Define a pattern to match any of the target words (case-insensitive)
    pattern = r"\b(informational|navigational|transactional)\b"

    # Search for the first occurrence
    match = re.search(pattern, label, re.IGNORECASE)

    if match:
        # Capitalize the first letter of the matched word
        return match.group(0).capitalize()
    else:
        # Default value if no match is found
        return "Informational"

def print_classification_report(df):
    print("Results definition and keywords:")
    # Generate a classification report
    target_names = ['Informational', 'Navigational', 'Transactional']
    report = classification_report(df['label_manual'], df['llama70B_level1'], target_names=target_names, digits=3)
    print(report)

df_intent_l1 = read_tsv("input/llama70B_def_kw_fsh.tsv")
df_intent_l1 = rename_manual_label(df_intent_l1)
df_intent_l1['llama70B_level1'] = df_intent_l1['llama70B_level1'].astype(str)
df_intent_l1['llama70B_level1'] = df_intent_l1['llama70B_level1'].apply(extract_query_intent)
print_classification_report(df_intent_l1)