DEF_ONLY_L1 = """Classify the following query as either navigational, transactional, or informational. Only use one 
of these three categories as your answer. A navigational query is used to find a specific website or page. A 
transactional query indicates an intent to complete a transaction such as to buy something or to download something. 
An informational query seeks knowledge or answers without the intent to act. 

Choose the appropriate category for the following query: {query} \nClassification:"""

DEF_KW_L1 = """Classify the following query as either navigational, transactional, or informational. Only use one of 
these three categories as your answer. A navigational query is used to find a specific website or page. Navigational 
queries often contain words such as "log in", "login", "sign in", "signin", "account","site", "www", ".com","sign",
"link". A transactional query indicates an intent to complete a transaction such as to buy something or to download 
something. Transactional queries often contain words such as "download", "buy", "free", "online", "calculator", 
"converter","pdf". An informational query seeks knowledge or answers without the intent to act. Informational queries 
often contain words such as "do","does","when","where","how","definition". 

Choose the appropriate category for the following query: {query} \nClassification:"""

DEF_KW_FEW_SHOT_L1 = """Classify the following query as either navigational, transactional, or informational. Only 
use one of these three categories as your answer. A navigational query is used to find a specific website or page. 
Navigational queries often contain words such as "log in", "login", "sign in", "signin", "account","site", "www", 
".com","sign","link". A transactional query indicates an intent to complete a transaction such as to buy something or 
to download something. Transactional queries often contain words such as "download", "buy", "free", "online", 
"calculator", "converter","pdf". An informational query seeks knowledge or answers without the intent to act. 
Informational queries often contain words such as "do","does","when","where","how","definition". 

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

CLUE_AND_REAS_L1 = """Classify the following query as either navigational, transactional, or informational. Only use one of these three categories as your answer.
A navigational query is used to find a specific website or page. Navigational queries often contain words such as "log in", "login", "sign in", "signin", "account","site", "www", ".com","sign","link".
A transactional query indicates an intent to complete a transaction such as to buy something or to download something.
Transactional queries often contain words such as "download", "buy", "free", "online", "calculator", "converter", "pdf".
An informational query seeks knowledge or answers without the intent to act. Informational queries often contain words such as "do", "does", "when", "where", "how", "definition".

Examples:

    Query: "google.com"
    Reasoning: 1. The query contains the word ".com". 2. It shows that the user wants to navigate to a specific site. 3. Therefore, it is a navigational query.
    Classification: Navigational

    Query: "netflix login"
    Reasoning: 1.The query contains the word "login". 2. It indicates that the user wants to navigate to a specific site. 3. Consequently, it is a navigational query.
    Classification: Navigational

    Query: "facebook sign in"
    Reasoning: 1. The query contains the words "sign in". 2. It indicates that the user wants to navigate to a site. 3. Therefore, it is a navigational query.
    Classification: Navigational

    Query: "red cross site"
    Reasoning: 1. The query contains the word "site". 2. It shows that the user wants to navigate to a site. 3. Therefore, it is a navigational query.

    Query: "austrian airlines link"
    Reasoning: 1. The query contains the word "link. 2. It indicates that the user wants to navigate to a site. 3. Consequently, it is a navigational query.

    Query: "online bank"
    Reasoning: 1. The query contains the words "online" and "bank". 2. It indicates that the user wants to perform a transaction. 3. Therefore, it is a transactional query.
    Classification: Transactional

    Query: "dropbox free download"
    Reasoning: 1. The query contains the words "dropbox" and "free". 2. It indicates that the user wants to perform a transaction. 3. Consequently, it is a transactional query.
    Classification: Transactional

    Query: "buy iPhone 15"
    Reasoning: 1. The query contains the word "buy". 2. It indicates that the user wants to perform a transaction. 3. Therefore, it is a transactional query.
    Classification: Transactional

    Query: "download Microsoft Office"
    Reasoning: 1. The query contains the word "download" and the name of the software. 2. It indicates that the user wants to perform a transaction. 3. Therefore, it is a transactional query.
    Classification: Transactional

    Query: "weight calculator"
    Reasoning: 1. The query contains the word "calculator". 2. It indicates that the user wants to perform a transaction. 3. Therefore, it is a transactional query.
    Classification: Transactional

    Query: "do ants eat grass"
    Reasoning: 1. The query contains the question word "do". 2. It indicates that the user is searching for an answer about specific facts. 3. Consequtively, it is an informational query.
    Classification: Informational

    Query: "dollar vs euro"
    Reasoning: 1. The query contains the word "vs", which means "versus". 2. It shows that the user wants to do a comparison. 3. Consequtively, it is an informational query.
    Classification: Informational

    Query: "cities in Austria"
    Reasoning: 1. The query contains the words that are linked to a country. 2. It shows that the user is searching for general information. 3. Consequtively, it is an informational query.
    Classification: Informational

    Query: "how to bake a cake"
    Reasoning: 1. The query contains the words "how to" and seeks information about baking food. 2. It indicates that the user is searching for an advice about performing a task. 3. Consequtively, it is an informational query.
    Classification: Informational

    Query: "when was John Lennon born"
    Reasoning: 1. The query contains the question word "when" and seeks information about a person's birth date. 2. It indicates that the user's goal is to find facts. 3. Consequtively, it is an informational query.
    Classification: Informational

    Query: "machine learning"
    Reasoning: 1. The query contains the words of a concept 2. It shows that the user is searching for general information 3. Consequtively, it is an informational query.
    Classification: Informational

    Query: "ngo activities"
    Reasoning: 1. The query contains an abbreviation "ngo". 2. Informational queries typically contain abbreviations 3. Consequtively, it is an informational query.
    Classification: Informational

    Choose the appropriate category for the following query: {query} \nClassification:"""
