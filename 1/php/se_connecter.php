<?php

//Gestion erreurs 

ini_set('display_errors', 1);
error_reporting(E_ALL);




session_start();
require "bdd.php";


//Récupération des données du formulaire 

$login=$_POST["login"];
$mdp=$_POST["mdp"];

//requete SQL pour avoir le login et le mdp de l'utilisateur qui essaye de se connecter 

$requete_login = "SELECT user_login, user_password FROM user WHERE user_login = :login";
$stmt = $pdo->prepare($requete_login);
$stmt->execute(['login' => $login]);

//Récupère seulement la ligne que l'on veut 
$user = $stmt->fetch(PDO::FETCH_ASSOC);   

//Verification de l'existence du login et de la justesse du mdp 
if ($user) {
    if ($user["user_password"]=== $mdp){
        echo ("Connexion réussie");
        echo '<form method="post" action="se_connecter.html">
                <button type="submit">Déconnexion</button>
              </form>';
    }
    else {
        echo "Mdp incorrect";
        echo '<form method="post" action="se_connecter.html">
                <button type="submit">Retour</button>
              </form>';
    }


}
else {
    echo "Login inexistant";
     echo '<form method="post" action="se_connecter.html">
                <button type="submit">Retour</button>
              </form>';
}


?>