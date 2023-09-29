import openai
import streamlit as st


def generate_response(myprompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=myprompt,
        temperature=.3,  # 0 to 2
        max_tokens=1024  # 50 words
    )
    # print(response.choices)
    return response.choices[0].text.strip()


def main():
    myprompt = st.text_input("How can I help you? \n")
    if st.button("Submit"):
        st.write(generate_response(myprompt))


if __name__ == "__main__":
    main()
