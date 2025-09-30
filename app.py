from flask import Flask, render_template, request, jsonify, g
from markupsafe import escape
import sqlite3

app = Flask(__name__)
DATABASE = "database.db"

# # pour lancer depuis `python3 app.py` en terminal
# if __name__=="__main__":
#     app*.run(debug = True)
@app.route('/')
def accueil():
    return '''
    <h1>Links</h1>
    <ul>
        <li><a href="/hello">Hello World</a></li>
        <li><a href="/contact">Contact</a></li>
        <li><a href="/user/John">Saluer un utilisateur</a></li>
        <li><a href="/base">Template Index</a></li>
        <li><a href="/age">Formulaire âge</a></li>
        <li><a href="/articles">Articles</a></li>
        <li><a href="/api/ping">API Ping</a></li>
        <li><a href="/add_user/TestUser">Ajouter utilisateur</a></li>
        <li><a href="/users">Liste des utilisateurs</a></li>
        <li><a href="/search?q=Flask">Recherche</a></li>
        <li><a href="/404">404</a></li>
    </ul>
    '''
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

# Exercice 8
@app.route("/api/ping")
def api_ping():
    return jsonify({"ping": "pong"})

# Exercice 9
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

# Créer la table si elle n’existe pas 
with sqlite3.connect(DATABASE) as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS users (name TEXT)")

# Route pour insérer un utilisateur 
@app.route("/add_user/<name>")
def add_user(name):
    db = get_db()
    db.execute("INSERT INTO users (name) VALUES (?)", (name,))
    db.commit()
    return f"Utilisateur {escape(name)} ajouté avec succès !"

# Exercice 10
@app.route("/users")
def users():
    db = get_db()
    users = db.execute("SELECT name FROM users").fetchall()
    return render_template("users.html", users=users)

# Exercice 11
# --- Gestionnaire d'erreur 404 ---
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Exercice 12
@app.route("/search")
def search():
    # Lire le paramètre 'q' de la query string
    query = request.args.get("q", "")  # "" par défaut si absent
    return render_template("search.html", query=query)

if __name__ == "__main__":
    app.run(debug=True)

