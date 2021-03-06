from urllib.request import urlopen
import requests

from constantes import *



class MyApp:
    def __init__(self):
        self.get_code(self.stick("Spider-man"))

    def get_code(self, url):
        print(url)
        html = urlopen(url)
        liste = html.read().decode("utf-8").split(' ')

        for lien in liste:
            if not lien == "" and lien_watch in lien:
                u = lien.split('"')
                for i in u:
                    if '/watch?v=' in i:
                        print(i)

    def stick(self, message):
        return search + "+".join(message.split(" "))

