DEF_ONLY = """
  Classify the following query as either navigational, transactional, or informational. Only use one of these three categories as your answer.
  A navigational query is used to find a specific website or page. A transactional query indicates an intent to complete a transaction such as to buy something or to download something.
  An informational query seeks knowledge or answers without the intent to act.

  Choose the appropriate category for the following query: {query} \nClassification:"""


DEF_KW = """
    Classify the following query as either navigational, transactional, or informational. Only use one of these three categories as your answer.
    A navigational query is used to find a specific website or page. Navigational queries often contain words such as "log in", "login", "sign in", "signin", "account","site", "www", ".com","sign","link".
    A transactional query indicates an intent to complete a transaction such as to buy something or to download something.
    Transactional queries often contain words such as "download", "buy", "free", "online", "calculator", "converter","pdf".
    An informational query seeks knowledge or answers without the intent to act. Informational queries often contain words such as "do","does","when","where","how","definition".

    Choose the appropriate category for the following query: {query} \nClassification:"""



DEF_KW_FEW_SHOT = """
Classify the following query as either navigational, transactional, or informational. Only use one of these three categories as your answer.
A navigational query is used to find a specific website or page. Navigational queries often contain words such as "log in", "login", "sign in", "signin", "account","site", "www", ".com","sign","link".
A transactional query indicates an intent to complete a transaction such as to buy something or to download something. Transactional queries often contain words such as "download", "buy", "free", "online", "calculator", "converter","pdf".
An informational query seeks knowledge or answers without the intent to act. Informational queries often contain words such as "do","does","when","where","how","definition".

    Examples:

    Query: "google.com"
    Classification: Navigational
    Query: "netflix login"
    Classification: Navigational
    Query: "facebook sign in"
    Classification: Navigational
    Query: "red cross site"
    Classification: Navigational
    Query: "austrian airlines link"
    Classification: Navigational
    Query: "online bank"
    Classification: Transactional
    Query: "dropbox free download"
    Classification: Transactional
    Query: "buy new iPhone"
    Classification: Transactional
    Query: "download Microsoft Office"
    Classification: Transactional
    Query: "weight calculator"
    Classification: Transactional
    Query: "do ants eat grass"
    Classification: Informational
    Query: "dollar vs euro"
    Classification: Informational
    Query: "cities in Austrialia"
    Classification: Informational
    Query: "how to bake a cake"
    Classification: Informational
    Query: "when was John Lennon born"
    Classification: Informational
    Query: "machine learning"
    Classification: Informational
    Query: "ngo activities"
    Classification: Informational

Choose the appropriate category for the following query: {query} \nClassification:"""