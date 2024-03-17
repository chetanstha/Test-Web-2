from flask import Flask,render_template,request, jsonify
import json
import os
import pandas as pd
from chat import chatbot
# import nltk
# from nltk.metrics import edit_distance

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chatbot.html')

@app.route("/ask", methods = ["POST"])
def ask():
    user_input = request.json['userInput']
    print(user_input)
    backend_response = chatbot(user_input)
    
    return jsonify({'status':"ok",'backendResponse':backend_response})

if __name__ == "__main__":
    app.run(debug=True)
    