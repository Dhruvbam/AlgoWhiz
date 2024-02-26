from flask import Flask, render_template, request
import openai


app = Flask(__name__)

openai.api_key = "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"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    message = request.json.get("message")
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run()

