# GHC 2023 - From Idea to Chatbot: A Step-by-Step Guide with ChatGPT and Python

Welcome to the  "From Idea to Chatbot: A Step-by-Step Guide with ChatGPT and Python" Level Up Lab. We have put together what you need to do prior to attending the lab and some pointers in case you miss anything. Please let us know if you have any issues!

## Tasks Prior to Attending GHC 2023

As this is a lab, please ensure you come prepared to participate by doing the following steps (*this should be done **prior** to coming to the conference*):

### Setup your development environment:

|Task|URL  |
|--|--|
| Watch a quick video on dev environment setup | https://youtu.be/Zwgj9JdgM0U |
| Install Visual Studio Code (or you're favorite editor) | https://code.visualstudio.com/download |
| Install Python | https://www.python.org/downloads/ |

### Setup an OpenAI account and obtain an API Key

|Task|URL  |
|--|--|
| Watch a quick video on registering with OpenAI/Obtaining API Key | https://youtu.be/kALp2yN6fic |
| Create an OpenAI account | https://platform.openai.com/signup?launch |
| Create an OpenAI API Key | https://platform.openai.com/account/api-keys. |

<span style="background-color: #FFFF00">CRITICAL!!! Copy the key generated in these steps and store it somewhere safe - we will need this for activities during the lab!!!</span>

### Put it all together and verify it works

This last step is to ensure everything you have done so far is working as expected. In addition to a quick video, there we have pasted the code snippet as well as the pip command to install openai.

| Task | URL |
|--|--|
| Watch a quick video on testing out your dev environment and API Key | https://youtu.be/TjJS7C161II |

From the video: Installing OpenAI for use with Python:

```
pip install openai
```

From the video: ```demo.py``` in this repo (NOTE: replace \<YOUR API KEY GOES HERE> with your API Key)

From the video: TEST!!! by running the application
```
python demo.py
```

## COMMON ISSUES
Here's a list of some common issues that you may come across. If you have any issues, please let us know and we'll add them to the list to help others out.

**Issue 1:**

 If you attempt to run the python demo.py and you get the following error:
 ```
 can't open file 'demo.py': [Errno 2] No such file or directory
 ```

Ensure you are in the same directory as the demo.py file - python can not find the file you are attempting to compile and run.

**Issue 2:**

If you get the following error:

```
Exception has occurred: ModuleNotFoundError
No module named 'openai'
```
You need to ensure that you ran the following command prior to attempting to compile and run:

```
pip install openai
```
**Issue 3:**

If you get the following error:

```
openai.error.AuthenticationError: Incorrect API key provided: <YOUR AP************ERE>. You can find your API key at https://platform.openai.com/account/api-keys.
```

You have either a bad API Key or you have not updated the code with your current API Key. To fix this, either overwrite the \<YOUR API KEY GOES HERE> section with your API Key, or go through the same process as getting a new API Key 
(https://platform.openai.com/account/api-keys)  and replace it.

**Issue 4:**

If you get the following error:

```
Command 'python' not found, did you mean:
```
* You need to check if python is installed --> ```python3 --version```
* If it installed, check if your symbolick link is setup as python3, try ```python3 demo.py```

