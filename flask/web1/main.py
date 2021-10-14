#!/usr/bin/env python3
#from flask import Flask
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

def workers(args1=""):
   return args1

@app.route('/')
def root():
   return render_template('main.html')

@app.route('/list1')
def list1():
   return render_template('list1.html')

@app.route('/form1')
def form1():
   return render_template('form1.html')

@app.route('/form2')
def form2():
   return render_template('form2.html')

@app.route('/processform1',methods = ['POST', 'GET'])
def processform1():
   if request.method == "POST":
      item1 = request.form['name']
      if item1 == "":
        args1=render_template('form1_empty.html')
      else:
         args1 = render_template('form1_search.html',item1=item1)
   return args1

@app.route('/processform2',methods = ['POST', 'GET'])
def processform2():
   if request.method == "POST":
      item1 = request.form['name']
      if item1 == "":
        args1=render_template('form2_empty.html')
      else:
        args1=render_template('form2_add.html',item1=item1)
   return args1

if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0')
