import requests
from constantes import *

from pytube import YouTube
import youtube_dl
class Downloader:

    def playlist(self, url, extension="", parent_dir=""):
        """
        Cette procédure télécharge une playlist sous le format demandé.

        param url: str, lien vers la playlist.
        param extension: str, le format du fichier.
        """
        links = self.extraire(url)
        for l in links:
            self.installer(l, extension, parent_dir)

    def extraire(self, url):
        """
        Cette fonction renvoie les liens des videos de la playlist.

        param url: str, mot clé permettant de retrouvé la vidéo
        return: list, liens des videos
        """
        html = requests.get(url)
        liste = html.text.split(" ")
        return self.link(liste)

    def link(self, html):
        """
        Cette fonction renvoie les liens de vidéos du code html

        param html: list str, le code html d'une page youtube
        return: list str, lien des videos
        """
        res = []

        for lien in html:
            if not lien == str() and lien_watch in lien:
                res.append(watch)

                # Kirby
                for j in range(len(lien_watch), len(lien) - 1):
                    res[-1] += lien[j]

                # Cette condition sert à effacer un lien si il est placé 2 fois dans la liste
                if len(res) >= 2 and res[-1] == res[-2]:
                    res.pop(-1)

        # Pour éviter un bug, j'efface le premier lien
        res.pop(0)

        return res

    def installer(self, url, extension, parent_dir):
        """
        Cette procédure télécharge la video sous le format mp3.

        param url: str, lien vers la video
        """

        # Cette Boucle evite d'avoir le titre par d
        while True:
            yt = YouTube(url)
            if not yt.title == "Youtube":
                break

        if parent_dir == "":
            parent_dir = "C:/Users/pdass/Downloads"

        if extension == mp4:
            videos = yt.streams.filter(only_video=True).all()
            videos[0].download(parent_dir)

        elif extension == mp3:
            videos = yt.streams.filter(only_audio=True).all()
            videos[0].download(parent_dir)
