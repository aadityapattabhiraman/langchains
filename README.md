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

#### Streaming

Appears to user as if something is happening, cost is more than a normal one. I honestly dont care.  

Reference: `https://python.langchain.com/docs/how_to/chat_streaming/`  

#### Track Token usage

Tracks the amount of token being used. `response.usage_metadata` works, but for detailed there are 2 methods:  
* through configuration  
* through context manager  

Reference: `https://python.langchain.com/docs/how_to/chat_token_usage_tracking/`

#### Response Metadata

Metadata from llm, also list token usage

Reference: `https://python.langchain.com/docs/how_to/response_metadata/`  

#### Multimodel data

* Images base64, url
* Pdf base64, url
* Audio base64

Reference: `https://python.langchain.com/docs/how_to/multimodal_inputs/`  

### Messages

#### Trimming
All models have finite context windows, meaning there's a limit to how many tokens they can take as input. If you have very long messages or a chain/agent that accumulates a long message history, you'll need to manage the length of the messages you're passing in to the model.  
```python
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
    trim_messages,
)
from langchain_core.messages.utils import count_tokens_approximately

messages = [
    SystemMessage("you're a good assistant, you always respond with a joke."),
    HumanMessage("i wonder why it's called langchain"),
    AIMessage(
        'Well, I guess they thought "WordRope" and "SentenceString" just didn\'t have the same ring to it!'
    ),
    HumanMessage("and who is harrison chasing anyways"),
    AIMessage(
        "Hmmm let me think.\n\nWhy, he's probably chasing after the last cup of coffee in the office!"
    ),
    HumanMessage("what do you call a speechless parrot"),
]
```

* based on token count
```python

trim_messages(
    messages,
    strategy="last",
    token_counter=count_tokens_approximately,
    max_tokens=45,
    start_on="human",
    end_on=("human", "tool"),
    include_system=True,
    allow_partial=False,
)
```

* based on message count
```python
trim_messages(
    messages,
    strategy="last",
    token_counter=len,
    max_tokens=5,
    start_on="human",
    end_on=("human", "tool"),
    include_system=True,
)
```
