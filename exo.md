### Énoncés (15 exercices)

1. Crée une route `/hello` qui retourne **"Hello World"**.
2. Crée une page `/contact` qui retourne du **HTML simple** (titre + paragraphe).
3. Crée une route avec paramètre `/user/<name>` qui salue l’utilisateur.
4. Mets en place un `base.html` et un `index.html` qui l’étend (**héritage Jinja**).
5. Ajoute un formulaire `/age` (GET/POST) qui affiche **"Tu as X ans"**.
6. Défini une liste Python `articles = [{"title":..., "author":...}, ...]` et affiche-la dans un template avec une **boucle Jinja**.
7. Ajoute un fichier `static/style.css` et utilise-le via `url_for('static', ...)`.
8. Crée une route `/api/ping` qui retourne du JSON :  
   ```json
   { "ping": "pong" }
