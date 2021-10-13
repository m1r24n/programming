#!/usr/bin/env python3
#from flask import Flask
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

def workers(args1=""):
   return args1

@app.route('/')
def root():
   args1="""<h1>This is the main page</h1>
   <h2>Please select an option </h2>
   <ul>
   <li><a href='/page1'>page 1 </a>
   <li><a href='/page2'>page 2 </a>
   <li><a href='/page3'>page 3 </a>
   <li><a href='/form1'>Form 1</a>
   </ul>
   """
   return workers(args1)

@app.route('/page1')
def page1():
   args1="""<h1>This is page1</h1>
   welcome to page 1 <br>
   thank you<br>
   <a href='/'>To go back to main page</a>
   """
   return workers(args1)

@app.route('/form1')
def form1():
   args1="""<h1>This is Form 1</h1>
    <FORM action="/processform1" method="post">
    What is your name <input type="text" name="name"><br>
    <INPUT type="submit" value="Send"> <INPUT type="reset">
    </form>
    <br>
   <a href='/'>To go back to main page</a>
   """
   return workers(args1)

@app.route('/processform1',methods = ['POST', 'GET'])
def processform1():
   if request.method == "POST":
      name = request.form['name']
      args1="""<h1>This is to process form 1</h1>
      Hello {},<br> good morning <br>
      <a href='/'>To go back to main page</a>
      """.format(name)
   return workers(args1)

@app.route('/page2')
def page2():
   args1="""<h1>This is page2</h1>
   welcome to page 2 <br>
   thank you<br>
   <a href='/'>To go back to main page</a>
   """
   return workers(args1)

@app.route('/page3')
def page3():
   args1="""<h1>This is page3</h1>
   welcome to page 3 <br>
   thank you<br>
   <a href='/'>To go back to main page</a>
   """
   return workers(args1)

@app.route('/page/<int:Page>')
def page(Page):
   args1="""<h1>This is page {} </h1>
   welcome to page {} <br>
   thank you<br>
   <a href='/'>To go back to main page</a>
   """
   return workers(args1.format(Page,Page))

if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0')
