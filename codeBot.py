pip install nltk
pip install newspaper3k

from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)
True

article = Article('https://www.mayoclinic.org/diseases-conditions/breast-cancer/symptoms-causes/syc-20352470')
article.download()
article.parse()
article.nlp()
corpus = article.text
print(corpus)

text = corpus
sentence_list = nltk.sent_tokenize (text)
print(sentence_list)

def greeting_response(text):

  text = text.lower()

  bot_greetings = ['howdy', 'hi', 'hey']
  user_greetings = ['hi', 'hello']

  for word in text.split():
   if word in user_greetings:
    return random.choice(bot_greetings)


def index_sort(list_var):
 length = len(list_var)
 list_index = list(range(0,length))

 x = list_var
 for i in range(length):
   for j in range(length):
     if x[list_index[i]] > x[list_index[j]]:

      temp = list_index[i]
      list_index[i] = list_index[j]
      list_index[j] = temp

 return list_index

def bot_response(user_input):
  user_input = user_input.lower()
  sentence_list.append(user_input)
  bot_response =''
  cm = CountVectorizer().fit_transform(sentence_list)
  similarity_scores = cosine_similarity(cm[-1],cm)
  similarity_scores_list = similarity_scores.flatten()
  index = index_sort (similarity_scores_list)
  index = index[1:]
  response_flag = 0

  j =0

  for i in range(len(index)):
    if similarity_scores_list[index[i]] > 0.0:
      bot_response = bot_response+' '+sentence_list[index[i]]
      response_flag = 1
      j = j+1

    if j> 2:
      break

    if response_flag == 0:
      bot_response = bot_response+ ' '+"I appologize, don't understand"
    sentence_list.remove(user_input)

    return bot_response
   

import tkinter
from tkinter import *

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    exit_list =['exit','bye','break']
    #if msg
    if msg in exit_list:
        res= 'Chat with You later'
        ChatLog.insert(END, "Bot: " + res + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        
    if greeting_response(msg) !=None:
         
        res = greeting_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    
    if msg != '': 
        
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

        #res = chatbot_response(msg)
        res = bot_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

base = Tk()
base.title("Hello Dear")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()