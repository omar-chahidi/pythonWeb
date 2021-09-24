#coding:utf-8

"""
https://info.blaisepascal.fr/nsi-serveur-http-python-cgi

http://localhost/result.py?username=toto ==> c'est equivalent de get 
"""
import cgi
import cgitb

cgitb.enable() # activer le mode débugue 

# creation un formulaire 


# Ainsi, les arguments de la requête peuvent être récupérés dans une variable de type FieldStorage, grâce à cette commande
data = cgi.FieldStorage()

print("Content-Type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Une page web avec Python CGI !</title>
</head>
<body>
    <h1>Page résultat</h1>
"""
print(html)

try:
    if data.getvalue("username"):
        #Ainsi, les arguments de la requête peuvent être récupérés dans une variable de type FieldStorage, grâce à cette commande
        nom = data.getvalue("username")
        print(f"<p>Bonjour {nom}</p>")
    else:
        raise Exception("Pseudo non transmis")
except:
    print("<p>Pseudo non transmis</p>")


html = """
</body>
</html>
"""
print(html)
