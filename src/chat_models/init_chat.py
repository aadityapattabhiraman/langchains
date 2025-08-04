from langchain.chat_models import init_chat_model


model = init_chat_model(
    "gpt-4.1-nano",
    model_provider="openai",
    temperature=0.5
)

result = model.invoke("Whats your name?")
print(result.content)
