#!/usr/bin/env python3
#from flask import Flask
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

def workers(args1=""):
   return args1

@app.route('/')
def root():
   args1="""<h1>This is the main page</h1>
   <h2>Please select an option </h2>
   <ul>
   <li><a href='/form1'>Search for item</a>
   <li><a href='/form2'>Add item item</a>
   <li><a href='/list1'>List items</a>
   </ul>
   """
   return workers(args1)

@app.route('/list1')
def list1():
   args1="""<h1>listing of items</h1>
   You are listing the items<br>
   <a href='/'>To go back to main page</a>
   """
   return workers(args1)
@app.route('/form1')
def form1():
   args1="""<h1>Searching for item</h1>
    <FORM action="/processform1" method="post">
    What do you want to find ? <input type="text" name="name"><br>
    <INPUT type="submit" value="Find"> <INPUT type="reset">
    </form>
    <br>
   <a href='/'>To go back to main page</a>
   """
   return workers(args1)

@app.route('/form2')
def form2():
   args1="""<h1>Add an item</h1>
    <FORM action="/processform2" method="post">
    What do you want to add ? <input type="text" name="name"><br>
    <INPUT type="submit" value="Find"> <INPUT type="reset">
    </form>
    <br>
   <a href='/'>To go back to main page</a>
   """
   return workers(args1)

@app.route('/processform1',methods = ['POST', 'GET'])
def processform1():
   if request.method == "POST":
      item1 = request.form['name']
      if item1 == "":
        args1="""<h1>This is to Search item </h1>
        Item can't be empty<br>
        <a href='/form1'>Search item </a><br>
        <a href='/'>To go back to main page</a>
        """.format(item1)
      else:
        args1="""<h1>This is to Search item </h1>
        You are looking for {} <br>
        <a href='/'>To go back to main page</a>
        """.format(item1)
   return workers(args1)

@app.route('/processform2',methods = ['POST', 'GET'])
def processform2():
   if request.method == "POST":
      item1 = request.form['name']
      if item1 == "":
        args1="""<h1>This is to Add item </h1>
        Item can't be empty<br>
        <a href='/form1'>Add an item </a><br>
        <a href='/'>To go back to main page</a>
        """.format(item1)
      else:
        args1="""<h1>This is to Add item </h1>
        You are adding {} <br>
        <a href='/'>To go back to main page</a>
        """.format(item1)
   return workers(args1)

if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0')
