# -*- coding: utf-8 -*-
"""Agrichat-bot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x6nj6FVHwQDucH0LD-skTOqRwKkDuwCZ
"""

#pip install -q -U google-generativeai

#pip install gradio

import gradio as gr
import os
import google.generativeai as genai

#import google.generativeai as genai
#from google.colab import userdata

#GOOGLE_API_KEY=userdata.get('G-API_key2')
#genai.configure(api_key=GOOGLE_API_KEY)

def gemini_chat(message, history):
  GOOGLE_API_KEY = 'AIzaSyBJeLAdQIoMkF8cHrNpCFrtb0iU_QAgk84'
  genai.configure(api_key=GOOGLE_API_KEY)
  model = genai.GenerativeModel('gemini-pro')
  chat = model.start_chat()
  prompt = 'Question :' + message + '- ' + 'If this Question is related to agriculture, farming, pests, agricultute practices, farmers, crops, crop management, soil, irrigation, various aspects of agriculture, pest control, weather forecasting, market prices, general farming queries, relevant stuff then consider the question as valid and generate answer(only the answer, not the description of what the instruction I have provided in about 30-40 words), otherwise reply that, I am sorry, but I cannot provide an answer to that question as it is inappropriate or not related to agriculture. One more point to remember is to make sure to be interactive, such as greeting the users if they say hi & introduce yourself & how can you help them with(related to farming & agriculture) but dont say that it is not related to agriculture only if the user is greeting or introducing, or say welcome if user says thank you etc. but make sure you never reveal that you are made using Gemini, if needed respond saying that contact author for more information)'
  response = chat.send_message(prompt)
  return response.text

iface = gr.ChatInterface(
  fn=gemini_chat,
  title='AGRI-CHAT : Your Personal AI powered Chatbot, built for Agriculture/Farming related queries',
  chatbot=gr.Chatbot(height=200),
  textbox=gr.Textbox(
    placeholder="What's your question? Please type here!!",
    scale=7
  ),
  retry_btn=None,
  undo_btn=None,
  clear_btn=None
)

if __name__ == '__main__':
  iface.launch(debug=False)

#!git config --global credential.helper store

#!gradio deploy

