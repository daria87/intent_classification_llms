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

CHAIN_OF_THOUGHT = """
Classify the following query as either navigational, transactional, or informational. Only use one of these three categories as your answer.
A navigational query is used to find a specific website or page. Navigational queries often contain words such as "log in", "login", "sign in", "signin", "account","site", "www", ".com","sign","link".
A transactional query indicates an intent to complete a transaction such as to buy something or to download something.
Transactional queries often contain words such as "download", "buy", "free", "online", "calculator", "converter", "pdf".
An informational query seeks knowledge or answers without the intent to act. Informational queries often contain words such as "do", "does", "when", "where", "how", "definition".

    Examples:

    Query: "google.com"
    Reasoning: The user expresses the intent to navigate to google search engine website. The "com" preceeded by a dot clearly indicates that the query is navigational.
    Classification: Navigational

    Query: "netflix login"
    Reasoning: The user wants to navigate to netflix platform. The word "login" signals that the user wants to log in and the query is navigational.
    Classification: Navigational

    Query: "facebook sign in"
    Reasoning: The user wants to navigate to facebook site, which means that the query is navigational. The words "sign in" confirms it.
    Classification: Navigational

    Query: "red cross site"
    Reasoning: The user expresses the intent to navigate to the site of an organisation, that is why it is a navigational query.
    Classification: Navigational

    Query: "austrian airlines link"
    Reasoning: The user wants to visit a site of a specific company, which is an indicator of the navigational query. The presence of the word "link" further confirms that the query is navigational.
    Classification: Navigational

    Query: "online bank"
    Reasoning: The user expresses the intent to perform a transaction on the web. The word "online" confirms that. That indicates that it is a transactional query.
    Classification: Transactional

    Query: "dropbox free download"
    Reasoning: The user wants to download an app, that is to perform a transaction. The word "free" followed by the word "download" indicate that the query is transactional.
    Classification: Transactional

    Query: "buy iPhone 15"
    Reasoning: The user is aiming to buy a product, that is to perform a transaction. The word "buy" indicates that the query is transactional.
    Classification: Transactional

    Query: "download Microsoft Office"
    Reasoning: The user wants to download a software. The word "download" shows that the query is transactional.
    Classification: Transactional

    Query: "weight calculator"
    Reasoning: The user wants to use a weight calculator which is an application. The word "calculator" further indicates that the query is transactional.
    Classification: Transactional

    Query: "do ants eat grass"
    Reasoning: It is a question that requires an answer about specific facts. The word "do" further confirms it. Therefore, the query is informational.
    Classification: Informational

    Query: "dollar vs euro"
    Reasoning: The user is searching for a comparison between dollar and euro. The word "vs" (versus) indicates that. Therefore, the query is informational.
    Classification: Informational

    Query: "cities in Austria"
    Reasoning: The user is requiring geographical information which is indicated by the words "cities" and "Austria". That indicates that it is an informational query.
    Classification: Informational

    Query: "how to bake a cake"
    Reasoning: The user requires instructions. The words "how to" confirm that. Therefore, the query is informational.
    Classification: Informational

    Query: "when was John Lennon born"
    Reasoning: The user requires an answer about specific facts. The word "when" confirms that. Consequently, it is an informational query.
    Classification: Informational

    Query: "machine learning"
    Reasoning: The user wants to explore a topic, search for general knowledge. That is why the query is informational.
    Classification: Informational

    Query: "ngo activities"
    Reasoning: The abbreviations such as "ngo" are ofen present in informational queries. Therefore, the query is informational.
    Classification: Informational

Choose the appropriate category for the following query: {query} \nClassification:"""
