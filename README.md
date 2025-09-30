# Flask – Mini Framework Web en Python

Pour lancer le app.py: flask run

## Qu’est-ce que Flask ?
[Flask](https://flask.palletsprojects.com/) est un **micro-framework web** écrit en Python.  
Il est conçu pour être **simple, léger et extensible**, parfait pour créer rapidement des applications web, des API REST ou des prototypes.  

Contrairement à des frameworks plus complets (comme Django), Flask vous laisse une grande liberté : vous ajoutez uniquement les composants dont vous avez besoin.  

---

## Installation
Avant tout, assurez-vous d’avoir **Python 3.7+** installé.  
Puis, dans votre environnement virtuel :

```bash
pip install flask
```

---

## Exemple minimal
Voici une app de base sur Flask:

```bash
from flask import Flask

# Crée une instance de l’application Flask
app = Flask(__name__)

# Route racine (http://localhost:5000)
@app.route("/")
def home():
    return "Hello, Flask !"

# Point d’entrée
if __name__ == "__main__":
    app.run(debug=True)
```

---

## Structure recommandé d'un projet

```csharp
mon_projet/
│── app.py            # Point d’entrée
│── requirements.txt  # Dépendances
│── static/           # Fichiers statiques (CSS, JS, images…)
│── templates/        # Fichiers HTML (Jinja2)
└── routes/           # Routes séparées
```

---

## Concepts clés
 - **Routes**: définissnt les URL et leurs fonctions associées(`@app.route`)
 - **Templates**: HTML dynamiqur avec Jinja2.
 - **Request & Response**: gestion des requêtes(`GET`, `POST`, ...).
 - **Extensions**: ajout de fonctionnalités (base de données avec SQLAlchemy, authentication, etc.).

 ---

 ## Example avec template

 ```python
 from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", nom="Alice")

if __name__ == "__main__":
    app.run(debug=True)
 ```

index.html (dans </templates>):
```html
<!DOCTYPE html>
<html>
<head><title>Accueil</title></head>
<body>
    <h1>Bienvenue, {{ nom }} 👋</h1>
</body>
</html>
```

---

## Quand utiliser Flask?

- Créer une API REST légére.
- Dévelpper rapidement un prototype web.
- Comprendre les bases des frameworks web avant de passer à quelque chose de plus complexe (ex: Django).
- Construire un projet flexible, modulable et minimaliste.

---

## Ressources

- Documentation Flask officielle: https://flask.palletsprojects.com/en/stable/quickstart/
- Extensions Flask: https://flask.palletsprojects.com/en/stable/extensions/
- Tutoriels Flask: https://realpython.com/tutorials/flask/
- Step-by-step Tutoriel Flask de digitalocean: https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
