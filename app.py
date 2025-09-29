from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)


# # pour lancer depuis `python3 app.py` en terminal
# if __name__=="__main__":
#     app*.run(debug = True)

# Exercice 1
@app.route('/hello')
def hello_world():
    return '<p>Hello World!</p>'

# Exercice 2
@app.route('/contact')
def contact():
    return '<h1>Contact</h1><p>Cest la page contact</p>'

# Exercice 3
@app.route('/user/<name>')
def salut(name):
    return f'<p>Hello {escape(name)}!</p>'

# Exercice 4
@app.route('/index')
def index():
    return render_template('index.html')

# Exercice 5
@app.route('/age', methods=['POST', 'GET'])
def age():
    if request.method == 'POST':
        name = request.form['username']
        age = request.form['age']
        return f'<p>tu as {escape(age)} ans</p>'

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)