
from openai import OpenAI

client = OpenAI(
  api_key=OPEN_API_API_KEY,
)
print(client.models.list())
# assistant = client.beta.assistants.create(
#   instructions="You are a personal math tutor. When asked a math question, write and run code to answer the question.",
#   model="gpt-4-1106-preview",
#   tools=[{"type": "code_interpreter"}]
# )