import google.generativeai as genai
import os
import webbrowser
import random
#from dotenv import load_dotenv
gemkey='enter your api key'
def create_html_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
genai.configure(api_key=gemkey)
model = genai.GenerativeModel("gemini-2.0-flash-exp")
descr=input("Enter description for your site \n :")
filename=input("enter a file name to save the site as \n :")
prompt=f"Generate an HTML code based on the descsription given below use CSS and Java script if required and put them under the <style> and <script> section of the html file respectively description=```{descr}``` don't put it in a code block or give any explanation just return the html code in plain text format, if the user provides any links for css styles use that instead, start with <html>"
print("Generating Site")
response = model.generate_content(prompt)
print(response)
create_html_file((f"{filename}.html"),response.text)
webbrowser.open_new_tab(f'{filename}.html') 
input("Press Enter to exit...")
