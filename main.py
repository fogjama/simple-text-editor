from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.font import Font
from tkinter.scrolledtext import *
import file_menu
import edit_menu
import format_menu
import help_menu

# Create a tkinter window
root = Tk()

# Give the window a title and dimensions
root.title("SimpleTextEditor-newfile")
root.geometry("300x250+300+300")
root.minsize(width=400, height=400)

# Create ScrolledText widget

text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
text.pack(fill=Y, expand=1)
text.focus_set()

# Create a menu bar

menubar = Menu(root)

file_menu.main(root, text, menubar)
edit_menu.main(root, text, menubar)
format_menu.main(root, text, menubar)
help_menu.main(root, menubar)

# Run the program

root.mainloop()