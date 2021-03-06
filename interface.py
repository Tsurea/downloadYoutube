"""This file content the graphical interface"""
from tkinter import *
from tkinter.ttk import Treeview
from threading import Thread


class Interface(Thread):
    def __init__(self):
        Thread.__init__(self)

        # How many video you will download
        self.number = 0

        #
        self.video = []

    def run(self):
        """
        This procedure run the interface graphical.
        """
        # Initialize the page
        self.window = Tk()

        # Config of the page
        self.window.title("Download Music")
        self.window.geometry("800x480")
        self.window.resizable(0, 0)
        self.window.config(bg="#666b69")

        # Creation of frames for the window
        self.details = Frame(self.window, bg="#3e403f")
        self.downloading = Frame(self.window, bg="#666b69")

        self.create_widgets()

        # Place frames
        self.details.place(relx=0, rely=0, relwidth=0.25, relheight=1)
        self.downloading.place(relx=0.25, rely=0, relwidth=0.75, relheight=1)

        self.window.mainloop()

    def create_widgets(self):
        """
        This procedure create all the widgets.
        """
        self.create_label()
        self.create_entry()
        self.create_checkbutton()
        self.create_button()
        self.create_treeview()

    def create_menu(self):
        """
        This procedure create the unique menu.
        """
        pass

    def create_treeview(self):
        self.scrollbar = Scrollbar(self.downloading)
        self.scrollbar.place(relx=0.97, rely=0, relwidth=0.03, relheight=1)

        self.tree = Treeview(self.downloading, yscrollcommand=self.scrollbar.set)

        # Define our columns
        self.tree['columns'] = ("Index", "Nom", "Extension")

        # Formate our columns
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("Index", anchor=W, width=1)
        self.tree.column("Nom", anchor=CENTER, width=360)
        self.tree.column("Extension", anchor=W, width=20)

        # Create heading
        self.tree.heading("#0")
        self.tree.heading("Index", text="ID", anchor=W)
        self.tree.heading("Nom", text="Nom", anchor=CENTER)
        self.tree.heading("Extension", text="Extension", anchor=W)

        self.tree.place(relx=0, rely=0, relwidth=0.97, relheight=1)

        #
        self.scrollbar.config(command=self.tree.yview)

    def create_label(self):
        """
        This procedure create the best labels.
        """
        self.nom = Label(self.details, text="Nom :", font=("Courrier", 15), bg="#3e403f", fg="white")
        self.nom.place(relx=0.03, rely=0.05, relwidth=0.3, relheight=0.05)

        self.fichier = Label(self.details, text="Chemin :", font=("Courrier", 15), bg="#3e403f", fg="white")
        self.fichier.place(relx=0.03, rely=0.55, relwidth=0.4, relheight=0.05)

    def create_checkbutton(self):
        """
        This procedure create awesome checkbutton.
        """
        self.checkVar1 = BooleanVar()
        self.checkVar1.set(True)

        self.mp3 = Checkbutton(self.details, text="mp3", variable=self.checkVar1, bg="#3e403f", fg="#c7c7c7")
        self.mp3.place(relx=0.15, rely=0.22, relwidth=0.3, relheight=0.07)

        self.checkVar2 = BooleanVar()
        self.checkVar2.set(False)

        self.mp4 = Checkbutton(self.details, text="mp4", variable=self.checkVar2, bg="#3e403f", fg="#c7c7c7")
        self.mp4.place(relx=0.5, rely=0.22, relwidth=0.3, relheight=0.07)

    def create_entry(self):
        """
        This procedure create entries.
        """
        self.entryVideo = Entry(self.details, font=("Courrier", 11))
        self.entryVideo.place(relx=0.03, rely=0.12, relwidth=0.94, relheight=0.07)

        self.entryFile = Entry(self.details, font=("Courrier", 11))
        self.entryFile.place(relx=0.03, rely=0.62, relwidth=0.94, relheight=0.07)

    def create_button(self):
        """
        This procedure create buttons.
        """
        self.add = Button(self.details, text="Ajouter", font=("Courrier", 10), command=self.add_video)
        self.add.place(relx=0.23, rely=0.3, relwidth=0.5, relheight=0.07)

        self.download = Button(self.details, text="Télécharger", font=("Courrier", 10))
        self.download.place(relx=0.25, rely=0.72, relwidth=0.5, relheight=0.07)

    def add_video(self):
        """
        This procedure add a name video to the listbox.
        """

        extension = ""

        if self.checkVar1.get() is True:
            extension += "mp3 "
        if self.checkVar2.get() is True:
            extension += "mp4"

        if extension == "mp3 mp4":
            extension = "mp3 / mp4"
        elif extension == "":
            extension = "mp3"

        self.number += 1
        self.video.append(self.entryVideo.get())

        self.tree.insert(parent='', index='end', iid=self.number, values=(self.number, self.entryVideo.get(), extension))

        self.entryVideo.delete(0, END)

    def modify(self):
        pass

    def initialize(self):
        pass


bof = Interface()

bof.start()
bof.join()
