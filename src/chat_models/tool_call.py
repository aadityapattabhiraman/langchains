from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI


class add(BaseModel):
    """Add two integers."""

    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")


class multiply(BaseModel):
    """Multiply two integers."""

    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")


tools = [add, multiply]

llm = ChatOpenAI(
    model="gpt-4.1-nano",
    temperature=0,
)
llm_with_tools = llm.bind_tools(tools)

query = "what is 3 * 12?"
result = llm_with_tools.invoke(query)

print(result)
