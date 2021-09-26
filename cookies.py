#coding:utf-8

"""
    Objectif : c'est fichier texte que le navigateur va enregistrer pour stocker des informations
    + fichier cookies contient
        - un nom 
        - une valeur
        - date expiration
    + Création de cookies
        - set-Cookie: pref_lang=fr; 
        - argument de cookies
            * expires=
            * path
            * ...
        - comment
    + /!\ Géneration de la cookie avec la génération du code HTML
    + Récupération de cookies

"""

"""
Pour que les scripts Python aient la capacité de recevoir les données
 (en provenance de requêtes GET ou POST), il faut utiliser la bibliothèque Python cgi
"""
import cgi
import http.cookies
import datetime
import os

# import pour ecrire des caractères spéciaux pour un bon codage
import sys
import codecs 
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# création date limite de l'utilisation du cookies => cookies valable un ans
expiration = datetime.datetime.now() + datetime.timedelta(days=365)
# formatage de la date d'expiration avec format de date
expiration = expiration.strftime("%a, %d-%b-%Y %H:%M:%S")

# Création cookies avec un dictionaire
my_cookie = http.cookies.SimpleCookie()
my_cookie["pref_lang"] = "fr"
my_cookie["pref_lang"]["expires"] = expiration
my_cookie["pref_lang"] ["httponly"]= True
#my_cookie["pref_lang"] =

print(my_cookie.output())

# Puis déclarer le type de donnée qui sera envoyé => type encodage
print("Content-Type: text/html; charset=utf-8\n")

# pour afficher les valeurs de la cookie il faut mettre le print de my_cooki après le print de la géneration du code html
#print(my_cookie.output())
#print(my_cookie)


html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Une page web avec Python!</title>
</head>
<body>
    <h1>Cookies avec Python</h1>
"""
print(html)

print(f"<p>Recupération de cookie !!!!</p>")

"""
if "HTTP_COOKIE" in os.environ:
    print(os.environ["HTTP_COOKIE"])
else:
    print("HTTP_COOKIE n'existe pas") 
"""
try:
    user_lang = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    print("La lange choisi par l'utilisateur est :", user_lang["pref_lang"].value)
except:
    print("Non trouvé")


html = """
</body>
</html>
"""
print(html)