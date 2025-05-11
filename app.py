from flask import Flask, render_template, request
# import google.generativeai as palm
from google import genai

from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=GEMINI_API_KEY)

# palm.configure(api_key="")

# defaults = { 'model': "models/text-bison-001" }

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        t = request.form.get("txt")
        # r = palm.generate_test(**defaults,messages=t)
        # return(render_template("index.html",result=r.last))
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', contents=t
        )
        return render_template("index.html", result=response.text)
    else:
        return(render_template("index.html", result="waiting"))

if __name__ == "__main__":
    app.run(debug=True)


