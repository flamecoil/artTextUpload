"""
ATT Calculator
v0.1
@flamecoil
"""
#initially one file--
# separate class from main

from tkinter import *
from application import Application


def main():
    root = Tk()
    root.title("Art Gallery Text")
    root.geometry("600x900")

    app = Application(root)
    root.mainloop()
main()
