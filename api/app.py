from flask import Flask, redirect, url_for,render_template,request
import matplotlib.pyplot as plt
import os
import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query_image(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()



app = Flask(__name__)

@app.route('/')
def welcome_user():
    return render_template('home.html')


@app.route('/submit', methods = ['POST','GET'])
def submit():
    back = request.referrer
    if request.method == 'POST':
        img  = request.files['img'] 
        img = plt.imread(img)
        path = os.path.join('static/images/img_new.jpg')        
        plt.imsave(path,img)        
        output = query_image(path)
        caption = output[0]['generated_text']      
        print(caption)  
        return render_template('home.html',img_path = path,result = caption)
    
    return redirect(back)


