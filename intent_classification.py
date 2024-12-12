import requests
import json

class QueryIntentClassifier:

    def __init__(self, api_key, api_url, max_tokens=5, temperature=0.2):
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.api_url = api_url
        self.max_tokens = max_tokens
        self.temperature = temperature



    def classify_intent(self, query,prompt):
        """
        Classifies a query into navigational, transactional, or informational intent (1rst level)
        """

        # Construct the generator
        generator = {
            "input": prompt.format(query=query),
            "parameters": {
                "max_new_tokens": self.max_tokens,
                "temperature": self.temperature
            }
        }

        # Send the request
        response = requests.post(self.api_url, headers=self.headers, data=json.dumps(generator))

        # Handle the response
        if response.status_code == 200:
            print(query)
            print(response.json()['results'][0]['generated_text'])
            return response.json()['results'][0]['generated_text']
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

    def apply_to_df(self, df, level, prompt_template):
        """
        Apply the classify_intent function to a DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame containing the queries.
            level (str): The column name to store the classification results.
            prompt_template (str): The prompt template to use for classification.

        Returns:
            pd.DataFrame: DataFrame with a new column containing classification results.
        """

    def apply_to_df(self, df, level, prompt_template):
        # Define a wrapper for the classify_intent function
        def classify_row(query):
            try:
                return self.classify_intent(query, prompt_template)
            except Exception as e:
                return f"Error: {e}"

        # Apply the classification function to each row
        df[level] = df['query'].apply(classify_row)
        return df
