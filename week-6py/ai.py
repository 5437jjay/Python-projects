from openai import OpenAI

client = OpenAI(api_key=os.getenv("Open_AI_Key"))

messages = []

while True:
    user = input("You: ")

    if user.lower() == "quit":
        break

    messages.append({"role": "user", "content": user})

    response = client.responses.create(
        model="gpt-5",
        input=messages
    )

    answer = response.output_text

    messages.append({"role": "assistant", "content": answer})

    print("Bot:", answer)