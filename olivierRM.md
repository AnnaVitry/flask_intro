# Formation Flask Python – Débutants

## 0. Veille & ressources (auto-documentation)

Pour progresser de façon autonome, adopte une routine de veille :

* **Lire la doc officielle** (Quickstart, Patterns, Extensions) :

  * Flask : [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
  * Jinja : [https://jinja.palletsprojects.com/](https://jinja.palletsprojects.com/)
  * Werkzeug : [https://werkzeug.palletsprojects.com/](https://werkzeug.palletsprojects.com/)
* **Bases de données & ORM** :

  * SQLAlchemy (pattern Flask) : [https://flask.palletsprojects.com/en/stable/patterns/sqlalchemy/](https://flask.palletsprojects.com/en/stable/patterns/sqlalchemy/)
  * Flask‑SQLAlchemy : [https://flask-sqlalchemy.readthedocs.io/en/stable/](https://flask-sqlalchemy.readthedocs.io/en/stable/)
  * Alembic / Flask‑Migrate : [https://alembic.sqlalchemy.org/en/latest/tutorial.html](https://alembic.sqlalchemy.org/en/latest/tutorial.html) et [https://flask-migrate.readthedocs.io/](https://flask-migrate.readthedocs.io/)
  * SQLite (tutoriels) : [https://www.sqlitetutorial.net/](https://www.sqlitetutorial.net/)
* **Formulaires** :

  * WTForms / Flask‑WTF : [https://wtforms.readthedocs.io/](https://wtforms.readthedocs.io/) et [https://flask-wtf.readthedocs.io/](https://flask-wtf.readthedocs.io/)
* **Auth & sessions** :

  * Flask‑Login : [https://flask-login.readthedocs.io/](https://flask-login.readthedocs.io/)
* **Bonnes pratiques** :

  * Structure de projet, Blueprints, Config, 12‑factor, gestion des erreurs, tests (pytest).

Astuce : garde un fichier `LEARNING.md` dans ton repo avec les liens utiles, snippets et notes.

---

## 1. Pourquoi utiliser Flask ?

Un site web statique (HTML, CSS, éventuellement un peu de JavaScript) permet de présenter du contenu, mais reste limité :

* Pas d’interaction réelle avec une base de données.
* Pas de logique métier dynamique (calculs, authentification, formulaires complexes…).

Avec **Flask**, un micro-framework Python, on peut :

* Transformer son site statique en site **dynamique**.
* Réutiliser directement ses compétences en **Python** (au lieu d’apprendre un autre langage côté serveur).
* Créer rapidement des **APIs**, des formulaires interactifs, des sites personnalisés.

En résumé : si tu sais coder en Python, tu peux créer des sites web puissants en quelques lignes seulement.

---

## 2. Installation

1. Vérifie que Python est installé :

   ```bash
   python --version
   ```
2. Crée un environnement virtuel (recommandé) :

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```
3. Installe Flask :

   ```bash
   pip install flask
   ```
4. Vérifie l’installation :

   ```bash
   python -m flask --version
   ```

---

## 3. Cours progressif

### 3.1. Premier projet minimal

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bienvenue sur mon premier site Flask !</h1>"

if __name__ == "__main__":
    app.run(debug=True)
```

Exécute :

```bash
python app.py
```

Puis ouvre : [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 3.2. Ajouter une deuxième page

```python
@app.route("/about")
def about():
    return "<p>Ce site est un exemple Flask</p>"
```

### 3.3. Rendre une page HTML avec templates

Crée un dossier `templates/` et ajoute `index.html` :

```html
<!DOCTYPE html>
<html>
<head><title>Accueil</title></head>
<body>
  <h1>Bienvenue avec Flask et HTML !</h1>
</body>
</html>
```

Modifie ton `app.py` :

```python
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")
```

### 3.4. Passer des variables au template

```python
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", username=name)
```

`templates/user.html` :

```html
<h1>Bonjour {{ username }} !</h1>
```

### 3.5. Formulaire et POST

```python
from flask import request

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Bonjour {name} !"
    return '''
        <form method="post">
            <input type="text" name="name">
            <input type="submit" value="Envoyer">
        </form>
    '''
```

### 3.6. Gestion de base de données avec SQLite

```python
import sqlite3

@app.route("/add/<string:task>")
def add(task):
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, task TEXT)")
    cur.execute("INSERT INTO todo (task) VALUES (?)", (task,))
    con.commit()
    con.close()
    return f"Tâche '{task}' ajoutée !"
```

### 3.7. Héritage avec Jinja2

Pour éviter de répéter le même code HTML sur toutes les pages, on utilise un **template parent** et des **templates enfants**.

`templates/base.html` :

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Mon site Flask{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>Mon site avec Flask</h1>
        <nav>
            <a href="/">Accueil</a> |
            <a href="/about">À propos</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    {% block scripts %}{% endblock %}
    <footer>
        <p>&copy; 2025 - Formation Flask</p>
    </footer>
</body>
</html>
```

`templates/index.html` :

```html
{% extends "base.html" %}

{% block title %}Accueil{% endblock %}

{% block content %}
  <h2>Bienvenue sur la page d’accueil</h2>
  <p>Ceci est un exemple de contenu spécifique.</p>
{% endblock %}
```

`templates/about.html` :

```html
{% extends "base.html" %}

{% block title %}À propos{% endblock %}

{% block content %}
  <h2>À propos</h2>
  <p>Ce site montre comment utiliser l’héritage Jinja2.</p>
{% endblock %}
```

Cette structure permet de maintenir un design uniforme (header, footer, CSS) tout en changeant seulement le contenu spécifique à chaque page. On peut ajouter d’autres blocs (`scripts`, `sidebar`, etc.).

exemple d'utilisation de scripts dans un template enfant :

```html
{% block scripts %}
  <script src="{{ url_for('static', filename='script.js') }}"></script>
{% endblock %}
```

### 3.8. Structure d’un projet Flask typique

```
myproject/
│   app.py
│   requirements.txt
└───templates/
│      base.html
│      index.html
│      about.html
└───static/
       style.css
```
