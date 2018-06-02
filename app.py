from flask import Flask, render_template,session, redirect, url_for, escape, request,make_response
app = Flask(__name__)


app.secret_key = 'fullstackDQWERTYU'
username = ''

@app.route('/')
def index():
   return  render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST' :
      session['username'] = request.form['username']
      username = request.form['username']
      password = request.form['password']
      if(username == 'sharan' and password=='dinesh'):
         username = username.capitalize()
         return render_template('home.html',username=username)
      elif (request.cookies.get('username') != ''):
         name = request.cookies.get('username')
         passwordC = request.cookies.get('password')
         if(username == name and password== passwordC):
            username = name.capitalize()
            return render_template('home.html',username=username)
      else:
         return "INVALID LOGIN CREDENTIALS"


      


@app.route('/newsignup',methods=['GET','POST'])
def newsignup():
   # print("hello")
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['psw']
      passwordRepeat = request.form['psw-repeat']
      resp = make_response(render_template('index.html'))
      resp.set_cookie('username' , username)
      resp.set_cookie('password' , password)
      return resp
      
@app.route('/signup')
def register():
   return render_template("signup.html")


@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/page2')
def page2():
   if (request.cookies.get('username') != ''):
      username = request.cookies.get('username')
      return render_template('page2.html',username=username)
   else:
      return render_template('page2.html')

@app.route('/page3')
def page3():
   if (request.cookies.get('username') != ''):
      username = request.cookies.get('username')
      return render_template('page3.html',username=username)
   else:
      return render_template('page3.html')

@app.route('/page4')
def page4():
   if (request.cookies.get('username') != ''):
      username = request.cookies.get('username')
      return render_template('page4.html',username=username)
   else:
      return render_template('page4.html')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   resp = make_response(render_template('index.html'))
   resp.delete_cookie('username')
   print("resp deleted" , resp)
   resp.delete_cookie('password')
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(debug=True, port=9000)