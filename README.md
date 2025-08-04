# LangChain

### Chat Models

#### init any model

The `init_chat_model()` helper method makes it easy to initialize a number of different model integrations without having to worry about import paths and class names.  

For example:
chatgpt, grok, gemini etc. all have their different models and important statements for each of them. `init_chat_model()` just makes it easy for user to use any model with just a single statement.  

Example: `./src/LangChain/chat_models/init_chat.py`  
Reference: `https://python.langchain.com/docs/how_to/chat_models_universal_init/`  

#### Local LLMs

I am not going through this as I mostly wont be using this, plus it differs for each provider.  
If you need refer it from here: `https://python.langchain.com/docs/how_to/local_llms/`  

#### Tool Calling

Allows a chat model to respond to a given prompt by "calling a tool".  

Example: `./src/LangChain/chat_models/tool_call.py`  
Reference: `https://python.langchain.com/docs/how_to/tool_calling/`  

#### Structured Output

`with_structured_output` is the simplest and reliable way of doing this.  

If for some reason the model has to choose a particular schema, then a parent schema can be created with a union type attribute.  
Say for example: if the user greets, it greets back and if they ask some other question it will answer based on the schema.  

There are many more things mentioned, but this is one that is most useful along with few shot prompting.  

Reference: `https://python.langchain.com/docs/how_to/structured_output/`  
Example: `./src/LangChain/chat_models/structured.py`  

#### Caching

`set_llm_cache(InMemoryCache())`
It can save money by reducing the number of API calls you make to the llm provider, if you are requesting the same content multiple times.  
Really useful.  

Reference: `https://python.langchain.com/docs/how_to/chat_model_caching/`  
Example: `./src/LangChain/chat_models/caching.py`  

#### Log Probablities

Certain chat models can be configured to return token level log probablities representing the likelihood of a given token.  
Cool stuff but IDC.  

#### Custom Chat Model

Cool stuff, but dont see myself using that.  

Reference: `https://python.langchain.com/docs/how_to/custom_chat_model/`  
Example: `./src/LangChain/chat_models/custom_chat_model.py`  


