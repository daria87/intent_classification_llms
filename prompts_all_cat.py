DEF_ONLY_ALL = """Classify the following query as either navigational, transactional, factual, instructional, 
or informational. Only use one of these three categories as your answer. A navigational query is used to find a 
specific website or page. A factual query is used to find specific facts, answers to specific questions. An 
instructional query is used to find instructions or tutorials. A transactional query indicates an intent to complete 
a transaction such as to buy something or to download something. An informational query seeks general knowledge or 
general answers. 

Choose the appropriate category for the following query: {query} \nClassification:"""

DEF_KW_ALL = """Classify the following query as either navigational, transactional, factual, instructional, 
or informational. Only use one of these three categories as your answer. A navigational query is used to find a 
specific website or page. Navigational queries often contain words such as "log in", "login", "sign in", "signin", 
"account","site", "www", ".com","sign","link". A factual query is used to find specific facts, answers to specific 
questions. Factual queries often contain words such as "what","when", "where", "do", "does", "facts", "code", 
"amount", "number", "definition","meaning", "how much", "how many", and numbers. An instructional query is used to 
find instructions or tutorials. Instructional queries often contain words such as "how to", "how do", "how can", 
"how does". A transactional query indicates an intent to complete a transaction such as to buy something or to 
download something. Transactional queries often contain words such as "download", "buy", "free", "online", 
"calculator", "converter","pdf". An informational query seeks general knowledge or general answers. 
  
Choose the appropriate category for the following query: {query} \nClassification:"""

DEF_KW_FEW_SHOT_ALL = """Classify the following query as either navigational, transactional, factual, instructional, 
or informational. Only use one of these three categories as your answer. A navigational query is used to find a 
specific website or page. Navigational queries often contain words such as "log in", "login", "sign in", "signin", 
"account","site", "www", ".com","sign","link". A factual query is used to find specific facts, answers to specific 
questions. Factual queries often contain words such as "what","when", "where", "do", "does", "facts", "code", 
"amount", "number", "definition","meaning", "how much", "how many", and numbers. An instructional query is used to 
find instructions or tutorials. Instructional queries often contain words such as "how to", "how do", "how can", 
"how does". A transactional query indicates an intent to complete a transaction such as to buy something or to 
download something. Transactional queries often contain words such as "download", "buy", "free", "online", 
"calculator", "converter","pdf". An informational query seeks general knowledge or general answers. 

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
    Query: "when was John Lennon born"
    Classification: Factual
    Query: "do ants eat grass"
    Classification: Factual
    Query: "california zip codes"
    Classification: Factual
    Query: "arachnophobia meaning"
    Classification: Factual
    Query: "what is standard deviation"
    Classification: Factual
    Query: "who is British prime minister now"
    Classification: Factual
    Query: "FIFA winner 2022"
    Classification: Factual
    Query: "how to bake a cake"
    Classification: Instructional
    Query: "how do you repair a fridge"
    Classification: Instructional
    Query: "apply for German citizenship"
    Classification: Instructional
    Query: "delete Facebook account"
    Classification: Instructional
    Query: "how can one stay more focused"
    Classification: Instructional
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
    Query: "dollar vs euro"
    Classification: Informational
    Query: "cities in Austria"
    Classification: Informational
    Query: "machine learning"
    Classification: Informational
    Query: "african elephants"
    Classification: Informational
    Query: "yellow fever vaccine"
    Classification: Informational

Choose the appropriate category for the following query: {query} \nClassification:"""
