#coding:utf-8

"""
Objectif
    + mettre en place un serveur HTTP (c'est comme le serveur appach)
    + Démaré le serveur http python avec la commande python .\httpServer.py dans une fenêtre cmd ou powershell 
"""

# 0/ 
import http.server
import socketserver  # c'est une moyen pour comminiquer deux applications

port = 80
adrerr = ("", port) # "" <=> localhost adresse de coonexion 

# Créer un gestionnaire de requette HTTP et les traités 
handler = http.server.SimpleHTTPRequestHandler

# Etablir une connexion 
httpd = socketserver.TCPServer(adrerr, handler) 

print(f"Serveur démarré sur le port {port} adresse {adrerr} ")

# laisser le serveur démaré 
httpd.serve_forever()


