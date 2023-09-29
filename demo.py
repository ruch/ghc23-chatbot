import openai
openai.api_key="Your API Key here"

def generate_response(myprompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=myprompt,
        temperature=.1,
        max_tokens=1024
    )
    print (response.choices)
    return response.choices[0].text.strip()

def main ():
    myprompt = input("How can I help you? \n")
    print(generate_response(myprompt))

if __name__ == "__main__":
    main()