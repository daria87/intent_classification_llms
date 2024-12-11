import dspy
from dspy import Signature, Predict
import litellm
import pandas as pd

lm = dspy.LM('deepinfra/meta-llama/Meta-Llama-3-70B-Instruct', api_key='KECaTH6rxvMMAURNAzS3syzmL6hvxtNy',temperature= 0.2,max_tokens=5)
dspy.configure(lm=lm)
print(lm)
result = lm("Say this is a test!")  # => ['This is a test!']
print(result)  # Explicitly print the result

chat_result = lm(messages=[{"role": "user", "content": "Say this is a test!"}])
print(chat_result)  # Explicitly print the result

#Define a simple signature for basic question answering
class BasicQA(dspy.Signature):
    """Answer questions with short factoid answers."""
    question = dspy.InputField()
    answer = dspy.OutputField(desc="often between 1 and 5 words")

generate_answer = dspy.ChainOfThought(BasicQA)

# Call the predictor on a particular input alongside a hint.
question='What is the color of the sky?'
pred = generate_answer(question=question)


