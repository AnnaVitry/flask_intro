from flask import Flask, render_template, request, jsonify
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
@app.route('/base')
def base():
    return render_template('index.html')

# Exercice 5
@app.route('/age', methods=['POST', 'GET'])
def age():
    if request.method == 'POST':
        age = request.form['age']
        return f'<p>tu as {escape(age)} ans</p>'
    
    return '''
        <form method="post">
            <input type="text" name="age">
            <input type="submit" value="Envoyer">
        </form>
        '''
# Exercic 6
articles = [
    {"title": "Introduction à Flask", "author": "Alice"},
    {"title": "Découvrir Jinja2", "author": "Bob"},
    {"title": "API REST avec Flask", "author": "Charlie"}
]

@app.route("/articles")
def index():
    return render_template("articles.html", articles=articles)

# Exercice 7
# Voir static/style.css

# 8. Route JSON /api/ping
@app.route("/api/ping")
def api_ping():
    return jsonify({"ping": "pong"})

if __name__ == "__main__":
    app.run(debug=True)