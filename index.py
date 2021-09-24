#coding:utf-8

"""
Pour que les scripts Python aient la capacité de recevoir les données
 (en provenance de requêtes GET ou POST), il faut utiliser la bibliothèque Python cgi
"""
import cgi

# Puis déclarer le type de donnée qui sera envoyé => type encodage
print("Content-Type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Une page web avec Python CGI !</title>
</head>
<body>
    <h1>Formulaire de ma page web en utilisant CGI et HTML</h1>
    
    <form action="result.py" method="post">
        <p>
            <input type="text" name="username" value="" />
            <input type="submit" name="envoyer" value="Envoyer">
        </p>
    </form>

</body>
</html>
"""
print(html)


"""
les arguments de la requête peuvent être 
récupérés dans une variable de type FieldStorage, grâce à cette commande
"""

#data = cgi.FieldStorage()

