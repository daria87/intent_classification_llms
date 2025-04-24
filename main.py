from read_file import read_tsv
from config import api_key
from intent_classification import QueryIntentClassifier
from prompts_level1_cat import DEF_ONLY_L1, DEF_KW_L1, DEF_KW_FEW_SHOT_L1, CLUE_AND_REAS_L1
from prompts_all_cat import DEF_ONLY_ALL, DEF_KW_ALL, DEF_KW_FEW_SHOT_ALL, CHAIN_OF_THOUGHT_ALL

if __name__ == "__main__":
    orcas_gold = read_tsv("input/ORCAS-I-gold_1.tsv")
    api_url = "https://api.deepinfra.com/v1/inference/meta-llama/Meta-Llama-3-70B-Instruct"
    classifier = QueryIntentClassifier(api_key, api_url)
    orcas_gold = classifier.apply_to_df(orcas_gold,'llama70B_level1',DEF_KW_FEW_SHOT_L1)
    print(orcas_gold)
