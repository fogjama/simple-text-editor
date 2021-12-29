from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font

# Create class File

class File():
    def __init__(self, text, root):
        self.filename = None
        self.text = text
        self.root = root

    def newFile(self, *args):
        self.filename = "Untitled"
        self.text.delete(0.0,END)
    
    def saveFile(self, *args):
        try:
            t = self.text.dump(0.0, END)
            f = open(self.filename, 'w')
            f.write(str(t))
            f.close()
        except:
            self.saveAs()
    
    def saveAs(self):
        f = asksaveasfile(mode='w', defaultextension='.txt')
        t = self.text.dump(0.0, END)
        try:
            f.write(str(t))
        except:
            showerror(title,"Oops!", message="Uable to seave file...")
    
    def openFile(self, *args):
        f = askopenfile(mode='r')
        self.filename = f.name
        t = f.read()
        self.text.delete(0.0, END)

        tag_dump = []
        mark_dump = []
        other_dump = []

        content = [j.split(', ') for j in [i.strip() for i in t[1:-1].replace('\'','').replace('(','').split('),')]]


        for [key, value, index] in content:
            if key == "text":
                if '\\n' in value:
                    self.text.insert(END, value.replace('\\n','') + '\n')
                else:
                    self.text.insert(END, value)
            elif key in ("tagon", "tagoff"):
                tag_dump.append((key, value, index))
            elif key == "mark":
                mark_dump.append((key, value, index))
            else:
                other_dump.append((key, value, index))

        # @TODO: Implement reading tags on file open and applying relevant formatting

        """
        used_tags = []

        for key, value, index in tag_dump:
            print(key, value, index)
            if key == "tagon" and (key, value, index) not in used_tags:
                for key2, value2, index2 in tag_dump:
                    print(key2, value2, index2)
                    if key2 == "tagoff" and value2 == value and (key2, value2, index2 not in used_tags):
                        self.text.tag_add(value, index, index2)
                        # tag_dump.remove((key, value, index))
                        # tag_dump.remove((key2, value2, index2))
                        used_tags.append((key, value, index))
                        used_tags.append((key2, value2, index2))
                        break
                    # else:
                        # print("Tag at index " + index + " did not match tag at index " + index2)
                # tag_dump.remove((key, value, index))
        
        # self.initial_formatting()

        """

    
    def initial_formatting(self):

        italic_font = Font(self.text, self.text.cget("font"))
        italic_font.configure(slant="italic")
        self.text.tag_configure("italic", font=italic_font)

        bold_font = Font(self.text, self.text.cget("font"))
        bold_font.configure(weight="bold")
        self.text.tag_configure("bold", font=bold_font)

        underline_font = Font(self.text, self.text.cget("font"))
        underline_font.configure(underline=1)
        self.text.tag_configure("underline", font=underline_font)

        overstrike_font = Font(self.text, self.text.cget("font"))
        overstrike_font.configure(overstrike=1)
        self.text.tag_configure("overstrike", font=overstrike_font)
    
    def quit(self):
        entry = askyesno(title="Quit", message="Are you sure you want to quit?")
        if entry == True:
            self.root.destroy()

def main(root, text, menubar):
    filemenu = Menu(menubar, tearoff=0)
    objFile = File(text, root)
    filemenu.add_command(label = "New", command=objFile.newFile, accelerator="Ctrl+N")
    filemenu.add_command(label="Open", command=objFile.openFile, accelerator="Ctrl+O")
    filemenu.add_command(label="Save", command=objFile.saveFile, accelerator="Ctrl+S")
    filemenu.add_command(label="Save as...", command=objFile.saveAs)
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command=objFile.quit)

    menubar.add_cascade(label="File", menu=filemenu)

    root.bind_all("<Control-s>", objFile.saveFile)
    root.bind_all("<Control-o>", objFile.openFile)
    root.bind_all("<Control-n>", objFile.newFile)

    root.config(menu=menubar)

if __name__ == "__main__":
    print("Please run 'main.py'")
