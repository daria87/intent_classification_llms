from read_file import read_tsv
from config import api_key
from intent_classification import QueryIntentClassifier
from prompts import DEF_ONLY, DEF_KW, DEF_KW_FEW_SHOT, CHAIN_OF_THOUGHT

if __name__ == "__main__":
    orcas_gold = read_tsv("input/ORCAS-I-gold_1.tsv")
    api_url = "https://api.deepinfra.com/v1/inference/meta-llama/Meta-Llama-3-70B-Instruct"
    classifier = QueryIntentClassifier(api_key, api_url)
    orcas_gold = classifier.apply_to_df(orcas_gold,'llama70B_level1',DEF_KW_FEW_SHOT)
    print(orcas_gold)
