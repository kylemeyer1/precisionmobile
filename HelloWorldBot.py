from flask import Flask, request
import requests
import json
import traceback
import random
app = Flask(__name__)

token = "EAAYsDLt13D8BALR3lvD9sYJcRr8EsS2bJHkbaa6FkZBq4ToVMvSFPfKpQbCNLwJFxeU4s7fF0W5Py7y4YOm2f56YpyRwKvOdnU6mPlIjDBDGAn3KcSiZBmZB0t6794kcTt7IuUyKETrPSSwGudi70vf4m51ulJKae1MhzHL7wZDZD"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
  if request.method == 'POST':
    try:
      data = json.loads(request.data)
      text = data['entry'][0]['messaging'][0]['message']['text'] # Incoming Message Text
      sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
      payload = {'recipient': {'id': sender}, 'message': {'text': "Hello World"}} # We're going to send this back
      r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload) # Lets send it
    except Exception as e:
      print traceback.format_exc() # something went wrong
  elif request.method == 'GET': # For the initial verification
    if request.args.get('hub.verify_token') == 'Eureka':
      return request.args.get('hub.challenge')
    return "Wrong Verify Token"
  return "Hello World" #Not Really Necessary

if __name__ == '__main__':
  app.run(debug=True)