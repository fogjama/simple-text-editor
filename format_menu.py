from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.font import Font, families
from tkinter.scrolledtext import *
import time

# Create Forma class

class Format():

    def __init__(self, text):
        self.text = text
    
    def changeBg(self):
        (triple, hexstr) = askcolor()
        if hexstr:
            self.text.config(bg=hexstr)
    
    def changeFg(self):
        (triple, hexstr) = askcolor()
        if hexstr:
            self.text.config(fg=hexstr)

    # @TODO: Re-write Bold, Italic, Underline, and Overstrike functions to avoid breaking font changes
    """
    def bold(self, *args): 
        try:
            current_tags = self.text.tag_names("sel.first") # Only proceed if some text is selected
            if "bold" in current_tags:
                self.text.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.text.tag_add("bold", "sel.first","sel.last")
                bold_font = Font(self.text, self.text.cget("font"))
                bold_font.configure(weight="bold")
                self.text.tag_configure("bold", font=bold_font)
        except:
            pass
    
    def italics(self, *args): 
        try:
            current_tags = self.text.tag_names("sel.first")
            if "italic" in current_tags:
                self.text.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.text.tag_add("italic", "sel.first", "sel.last")
                italic_font = Font(self.text, self.text.cget("font"))
                italic_font.configure(slant="italic")
                self.text.tag_configure("italic", font=italic_font)
        except:
            pass
    
    def underline(self, *args):
        try:
            current_tags = self.text.tag_names("sel.first")
            if "underline" in current_tags:
                self.text.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.text.tag_add("underline", "sel.first", "sel.last")
                underline_font = Font(self.text, self.text.cget("font"))
                underline_font.configure(underline=1)
                self.text.tag_configure("underline", font=underline_font)
        except:
            pass
    
    def overstrike(self, *args):
        try:
            current_tags = self.text.tag_names("sel.first")
            if "overstrike" in current_tags:
                self.text.tag_remove("overstrike", "sel.first", "sel.last")
            else:
                self.text.tag_add("overstrike", "sel.first", "sel.last")
                overstrike_font = Font(self.text, self.text.cget("font"))
                overstrike_font.configure(overstrike=1)
                self.text.tag_configure("overstrike", font=overstrike_font)
        except:
            pass
    """
    
    # @TODO: Implement change_font and change_size functions
    """"
    def change_font(self, option):
        pass
    """
    
    def addDate(self):
        full_date = time.localtime()
        day = str(full_date.tm_mday)
        month = str(full_date.tm_mon)
        year = str(full_date.tm_year)
        date = day + '.' + month + '.' + year
        self.text.insert(INSERT, date, "a")

def main(root, text, menubar):
    
    objFormat = Format(text)
    
    fontoptions = families(root)
    font = Font(family="Courier", size=10)
    text.configure(font=font)

    formatMenu = Menu(menubar, tearoff=0)

    fsubmenu = Menu(formatMenu, tearoff=0)
    ssubmenu = Menu(formatMenu, tearoff=0)

    allowed_fonts = ["Arial", "Calibri", "Courier", "Helvetica", "Verdana"]
    fontlist = []

    for option in fontoptions:
        if any(allowed in option for allowed in allowed_fonts):
            fontlist.append(option)
        fontlist.sort()
    for option in fontlist:
        fsubmenu.add_command(label=option, command=lambda option=option: font.configure(family=option))
    for value in [8,9,10,11,12,14,16,18,20,24,28,32,36]:
        ssubmenu.add_command(label=str(value), command=lambda value=value: font.configure(size=value))
    
    formatMenu.add_command(label="Change canvas background", command=objFormat.changeBg)
    formatMenu.add_command(label="Change document font colour", command=objFormat.changeFg)
    formatMenu.add_cascade(label="Change document font", underline=0, menu=fsubmenu)
    formatMenu.add_cascade(label="Change document text size", underline=0, menu=ssubmenu)
    formatMenu.add_separator()

    """
    @TODO: Fix formatting functions above

    formatMenu.add_command(label="Bold", command=objFormat.bold, accelerator="Ctrl+B")
    formatMenu.add_command(label="Italic", command=objFormat.italics, accelerator="Ctrl+I")
    formatMenu.add_command(label="Underline", command=objFormat.underline, accelerator="Ctrl+U")
    formatMenu.add_command(label="Overstrike", command=objFormat.overstrike, accelerator="Ctrl+T+T")
    """

    formatMenu.add_command(label="Add Date", command=objFormat.addDate)

    menubar.add_cascade(label="Format", menu=formatMenu)

    """
    @TODO: Fix formatting functions above
    root.bind_all("<Control-b>", objFormat.bold)
    root.bind_all("<Control-i>", objFormat.italics)
    root.bind_all("<Control-u>", objFormat.underline)
    root.bind_all("<Control-t>", objFormat.overstrike)
    """

    root.grid_columnconfigure(0, weight=1)
    root.resizable(True, True)

    root.configure(menu=menubar)

if __name__ == "__main__":
    print("Please run 'main.py'")