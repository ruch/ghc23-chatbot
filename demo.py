import openai
openai.api_key="your API Key"

def generate_response(myprompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=myprompt,
        temperature=0.3,
        max_tokens=1024
    )
    return response.choices[0].text.strip()

def main ():
    myprompt = input("How can I help you? \n")
    print(generate_response(myprompt))

if __name__ == "__main__":
    main()
