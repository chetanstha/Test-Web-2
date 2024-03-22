from flask import Flask,render_template,request, jsonify
import json
import os
import pandas as pd
from chat import chatbot
import nltk
from nltk.metrics import edit_distance
from datetime import datetime
import os

app = Flask(__name__)

# dataset = {
#     "hello" : "greeting",
#     "hi": "greeting",
#     "tell me about you":"about",
#     "about you":"about",
#     "bye":"farewell",
#     "see you":"farewell",
# }

# def find_intent(user_input):
#     min_distance = float('inf')
#     intent = None
#     for example,label in dataset.items():
#         distance = nltk.edit_distance(user_input,example)
#         if distance < min_distance:
#             min_distance = distance
#             intent = label
#     return intent

@app.route("/")
def hello():
    return render_template('chatbot.html')

@app.route("/ask", methods = ["POST"])
def ask():
    user_input = request.json['userInput']
    print(user_input)
    backend_response = chatbot(user_input)
    
    return jsonify({'status':"ok",'backendResponse':backend_response})

# @app.route('/process', methods=['POST'])
# def process():
#     user_input = request.json['userInput']
#     print(user_input)
    
#     intent = find_intent(user_input)
#     backend_response = ""
#     if intent == "greeting":
#         backend_response="Hello! How can I assist you?"
#     elif intent == "about":
#         backend_response ="I am Chatbot. I'll be helping you."
#     elif intent == "farewell":
#         backend_response = "Thank you for your time."
#     else:
#         backend_response ="Sorry, I am not able to help you. Can you rephrase it?"
#     print(backend_response)
#     return jsonify({'backendResponse': backend_response})

if __name__ == "__main__":
    app.run(debug=True)
    