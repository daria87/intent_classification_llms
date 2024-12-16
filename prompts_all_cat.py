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

CHAIN_OF_THOUGHT_ALL = """Classify the following query as either navigational, transactional, factual, instructional, or informational. Only 
use one of these three categories as your answer. A navigational query is used to find a specific website or page. 
Navigational queries often contain words such as "log in", "login", "sign in", "signin", "account","site", "www", 
".com","sign","link". A factual query is used to find specific facts, answers to specific questions. Factual queries 
often contain words such as "what","when", "where", "do", "does", "facts", "code", "amount", "number", "definition",
"meaning", "how much", "how many", and numbers. An instructional query is used to find instructions or tutorials. 
Instructional queries often contain words such as "how to", "how do", "how can", "how does". A transactional query 
indicates an intent to complete a transaction such as to buy something or to download something. Transactional 
queries often contain words such as "download", "buy", "free", "online", "calculator", "converter","pdf". An 
informational query seeks general knowledge or general answers. 

    Examples:
  
    Query: "google.com" 
    Reasoning: The user expresses the intent to navigate to google search engine website. The "com" preceded by a dot clearly indicates that the query is navigational.
    Classification: Navigational 
  
    Query: "netflix login" Reasoning: The user wants to navigate to netflix platform. The word "login" signals that the user wants to log in and the query is navigational. 
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

    Query: "when was John Lennon born"
    Reasoning: The user wants to know a specific fact: the date when a public figure was born. The question word "what" clearly indicates that the query is factual.
    Classification: Factual

    Query: "do ants eat grass"
    Reasoning: The user wants to know about specific food habits of insects. The question requires a specific yes or no answer. The question word "do" indicates that the query is factual.
    Classification: Factual

    Query: "california zip codes"
    Reasoning: The user wants to know about specific zip codes in a state. Therefore, the query is factual.
    Classification: Factual

    Query: "arachnophobia meaning"
    Reasoning: The user asks for a definition of a word. The word "meaning" clearly indicates that the query is factual.
    Classification: Factual

    Query: "what is standard deviation"
    Reasoning: The user asks a specific question that requires definition as an answer. The question word "what" confirms that the query is factual.
    Classification: Factual

    Query: "who is British prime minister now"
    Reasoning: The user wants to know a specific fact about a political figure. The question word "who" clearly indicates that the query is factual.
    Classification: Factual

    Query: "FIFA winner 2022"
    Reasoning: The user wants to know who is the winner of a football cup. The year of the event in a query clearly indicates that the query is factual.
    Classification: Factual

    Query: "how to bake a cake"
    Reasoning: The user wants instructions for cooking. The words "how to" indicate that the query is instructional.
    Classification: Instructional

    Query: "how do you repair a fridge"
    Reasoning: The user seeks instructions for reparation. The words "how to" indicate that the query is instructional.
    Classification: Instructional

    Query: "apply for German citizenship"
    Reasoning: The user wants instructions on how to apply for German citizenship. The verb "apply" indicates that the query is instructional
    Classification: Instructional

    Query: "delete Facebook account"
    Reasoning: The user wants to delete an account in a social network. The verb "delete" indicates that the query is instructional.
    Classification: Instructional

    Query: "how can one stay more focused"
    Reasoning: The user wants instructions on how to stay more focused. The words "how to" indicate that the query is instructional.
    Classification: Instructional

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

    Query: "dollar vs euro"
    Reasoning: The user wants to do a general comparison between dollar and euro. The word "vs" (versus) indicates that. Therefore, the query is informational.
    Classification: Informational

    Query: "cities in Austria"
    Reasoning: The user seeks general knowledge about cities in a country. Therefore, it is and informational query.
    Classification: Informational

    Query: "machine learning"
    Reasoning: The user wants general information about machine learning. Therefore, it is an informational query.
    Classification: Informational

    Query: "african elephants"
    Reasoning: The user is searching for general information about animals. Therefore, the query is informational.
    Classification: Informational

    Query: "yellow fever vaccine"
    Reasoning: The user wants general information about vaccines. Therefore, the query is informational.
    Classification: Informational

  Choose the appropriate category for the following query: {query} \nClassification:"""
