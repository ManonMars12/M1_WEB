from flask import Flask, render_template, request, redirect, url_for
from bdd import get_db, close_db  

#Choix de Flask car débutante et il apparait comme plus léger et flexible / facilité d'apprentissage 

app = Flask(__name__)

#Fermer la connexion proprement 
@app.teardown_appcontext
def teardown_db(exception):
    close_db(exception)


@app.route("/")
def index():
    conn = get_db()
    cur = conn.cursor() #Permet d'exéctuer des requêtes 
    cur.close()
    return render_template("se_connecter.html") #afficher mon front-end 

@app.route("/login", methods=["POST"])
def login():
    conn = get_db()
    cur = conn.cursor()   
    login = request.form.get("login")
    mdp = request.form.get("mdp")
    cur.execute("SELECT user_login FROM user")
    rows = cur.fetchall()
    

    logins=[]
    for row in rows:
        logins.append(row[0])
    
    if login not in logins :
       return f"""
    <html>
        <p> Login inexistant </p>
            <form action="{url_for('logout')}" method="get">
                <button type="submit">Déconnexion</button>
            </form>
        </body>
    </html>
    """
    else : 
        cur.execute(f"SELECT user_password FROM user WHERE user_login = '{login}'")
        mdp_bdd_ligne=cur.fetchone()
        cur.close() 
        if mdp_bdd_ligne is None:
            return "Erreur"
        mdp_bdd=mdp_bdd_ligne[0]
        if mdp_bdd == mdp : 
            return f"""
    <html>
        <p> Connexion réussie </p>
            <form action="{url_for('logout')}" method="get">
                <button type="submit">Déconnexion</button>
            </form>
        </body>
    </html>
    """
        else : 
            return f"""
    <html>
        <p> Mot de passe incorrect </p>
            <form action="{url_for('logout')}" method="get">
                <button type="submit">Déconnexion</button>
            </form>
        </body>
    </html>
    """


  
    
        

@app.route("/logout")
def logout():
    return redirect(url_for("index"))

  

#Lancer l'application 
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8000)
