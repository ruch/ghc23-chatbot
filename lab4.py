import openai

#Set API Key
openai.api_key = "Your API key here"

#Create prompt
prompt = "A women in technology conference showing a person presenting in front of a large audience"

#Call the API
response = openai.Image.create(prompt=prompt, n=1, size="512x512")

#Get image
image = response["data"][0]["url"]

#Output url
print(image)
