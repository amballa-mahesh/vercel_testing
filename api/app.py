from flask import Flask, redirect, url_for,render_template,request
import matplotlib.pyplot as plt
import os
import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query_image(filename):
    
    response = requests.post(API_URL, headers=headers, data=filename)
    return response.json()



app = Flask(__name__)

@app.route('/')
def welcome_user():
    return render_template('home.html')


@app.route('/submit', methods = ['POST','GET'])
def submit():
    
    if request.method == 'POST':
        img  = request.files['img']       
        output = query_image(img)
        caption = output[0]['generated_text']      

        print(caption)  
    return render_template('home.html', result = caption)
    
    


