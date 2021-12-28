from tkinter import *
from tkinter.messagebox import *

class Help():
    def about(root):
        showinfo(title="About", message="""
        This is a text editor made by fogjama using Python

        Original tutorial at https://dev.to/insidiousthedev/make-a-simple-text-editor-using-python-31bd

        Created December 2021
        """)

def main(root, menubar):
    help = Help()

    helpMenu = Menu(menubar, tearoff=0)
    helpMenu.add_command(label="About", command=help.about)
    
    menubar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menubar)

if __name__ == "__main__":
    print("Please run 'main.py'")