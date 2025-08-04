from langchain_openai import ChatOpenAI
from langchain_core.globals import set_llm_cache
from langchain_core.caches import InMemoryCache
# from langchain_community.cache import SQLiteCache


model = ChatOpenAI(
    model="gpt-4.1-nano",
    temperature=0,
)

set_llm_cache(InMemoryCache())
# set_llm_cache(SQLiteCache(database_path=".langchain.db"))

response = model.invoke("Tell me a joke")
print(response.content)

response_1 = model.invoke("Tell me a joke")
print(response_1.content)
