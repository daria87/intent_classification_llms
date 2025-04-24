# Weak supervision vs LLMs for intent classification

This package serves as basis for the paper "n a Few Words: Comparing Weak Supervision and LLMs for
Short Query Intent Classification"

Link to the paper: 

DOI of the paper: https://doi.org/10.1145/3726302.3730213


## In-context learning:


Create conda environment:

```bash
$ conda create --name intent_classification_llms python==3.10
```

Activate the environment:

```bash
$ source activate intent_classification_llms
```

Use pip to install requirements:

```bash
(intent_classification_llms) $ pip install -r requirements.txt
```

## Fine-tuning:

Fine-tuning experiments are in the folder `fine-tuning` (Jupyter notebooks)

Parameters used for fine-tuning up to 15000 examples:
```bash
learning_rate = 2e-5 
lora_rank = 8
batch_size = 8 
gradient_accumulation_steps = 8
weight_decay = 0.05 
max_grad_norm = 1.0
early_stop_patience = 2
```
Parameters used for fine-tuning from 30000 examples:
```bash
learning_rate = 1.5e-5  
lora_rank = 8  
batch_size = 16  
gradient_accumulation_steps = 8  
weight_decay = 0.1
max_grad_norm = 1.0 
early_stop_patience = 3 
```