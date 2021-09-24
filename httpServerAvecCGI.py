#coding:utf-8
"""
    https://info.blaisepascal.fr/nsi-serveur-http-python-cgi
"""

"""
# On a d’abord besoin d’un serveur HTTP
import http.server
server = http.server.HTTPServer    # classe du serveur HTTP

#  il faut utiliser un gestionnaire de requêtes, prenant en charge le CGI,  auquel il faut indiquer le chemin (relatif !) des scripts CGI
handler = http.server.CGIHTTPRequestHandler    # classe du gestionnaire
handler.cgi_directories = ["/"]

# On choisit quelle(s) interface(s) réseau utiliser (rappel : «  »  = toutes les interfaces) et sur quel port écouter :
PORT = 8080
server_address = ("", PORT)

# enfin on instancie le serveur, en lui indiquant son adresse et le gestionnaire de requêtes à utiliser :
httpd = server(server_address, handler)   # objet "serveur"

print(f"serveur port {PORT}")

#on le démarre
httpd.serve_forever()
"""
import http.server

port = 80
adress = ("", port) 

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(adress, handler)

print(f"serveur port {port}")

httpd.serve_forever()

