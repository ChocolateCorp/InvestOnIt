from flask import Flask, render_template,session, redirect, url_for, escape, request
app = Flask(__name__)


app.secret_key = 'fullstackDQWERTYU'
username = ''

@app.route('/')
def index():
   return  render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      username = request.form['username']
      password = request.form['password']
      if(username == 'sharan' and password=='dinesh'):
      	username = username.capitalize()
      	return render_template('home.html',username=username)

      else:
      	return "INVALID LOGIN CREDENTIALS"



@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/page2')
def page2():
   return render_template('page2.html')

@app.route('/page3')
def page3():
   return render_template('page3.html')

@app.route('/page4')
def page4():
   return render_template('page4.html')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(debug=True, port=9000)