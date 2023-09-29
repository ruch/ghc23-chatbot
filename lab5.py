import openai

#NOTE: Run this command prior to running the code below: pip install openai

openai.api_key = "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"

#Set up the model and prompt
engine = "text-davinci-003"
prompt = "Make a detailed DALL-E prompt with several adjectives for a "

#Get input from the user
room = input("Enter a room of the house you'd like to decorate: ")
desc = input("Enter what type of decoration you'd like to do: ")

#Append input from user with our prompt
prompt = prompt + room + " that has " + desc

#Call OpenAI using the ChatGPT model
response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.7)

#Get image generation prompt from response
image_generation_prompt = response["choices"][0]["text"]

#Display prompt
print("Open AI Response: " + image_generation_prompt)

#Call OpenAI DALL-E model
response = openai.Image.create(prompt=image_generation_prompt, n=1, size="512x512")

#Get image from response
image = response.data[0].url

print("\r\rHere is the location to your image: " + image)