from langchain_openai import ChatOpenAI
from typing import Optional
from pydantic import BaseModel, Field


model = ChatOpenAI(
    model="gpt-4.1-nano",
    temperature=0,
)


class Joke(BaseModel):

    """
    Joke to tell the user
    """

    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline of the joke")
    rating: Optional[int] = Field(
        default=None, description="How funny the joke is, from 1 to 10"
    )


structured_model = model.with_structured_output(Joke)
response = structured_model.invoke("Tell me a joke about life")

print(response)
