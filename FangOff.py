import tkinter as tk
from tkinter.filedialog import askopenfile, askopenfilename

global filename
filename = ""

def defang(url, clip=True):
    str1 = url.replace(".", "[.]").replace("http", "hxxp").replace("https", "hxxps").replace("@", "[AT]")
    if clip:
        master.clipboard_clear()
        master.clipboard_append(str1)
    return str1

def fang(url, clip=True):
    str1 = url.replace("[.]", ".").replace("hxxps", "https").replace("hxxp", "http").replace("[AT]", "@")
    if clip:
        master.clipboard_clear()
        master.clipboard_append(str1)
    return str1

def fromfileDe():
    global filename
    openfile = filename
    textfile = open(openfile, 'r')
    openfile = openfile.replace(".txt", "File De-fanged.txt")
    file = open(openfile, "w")
    for line in textfile.readlines():
        str = defang(line, clip=False)
        file.write(str)
    file.close()
    textfile.close()

def fromfileRe():
    global filename
    openfile = filename
    textfile = open(openfile, 'r')
    openfile = openfile.replace(".txt", "File Re-fanged.txt")
    file = open(openfile, "w")
    for line in textfile.readlines():
        str = fang(line, clip=False)
        file.write(str)
    file.close()
    textfile.close()

def open_file():
    global filename
    filename = askopenfilename(filetypes =[('txt Files', '*.txt')])
    return filename

master = tk.Tk()
master.title("FangOff by @TheCyberViking version: 1.5")
master.geometry("552x88")
tk.Label(master, text="Enter URL: ").grid(row=0)
url = tk.Entry(master, width=54)
url.grid(row=0, column=1)
tk.Button(master,text='De-Fang ',command=lambda: defang(url.get())).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Button(master,text='Re-Fang ', command=lambda: fang(url.get())).grid(row=3,column=1,sticky=tk.W,pady=4)
tk.Button(master,text='De-Fang File ', command=lambda: fromfileDe()).grid(row=3,column=2,sticky=tk.W,pady=4)
tk.Button(master,text='Re-Fang File ', command=lambda: fromfileRe()).grid(row=3,column=3,sticky=tk.W,pady=4)
open_button = tk.Button(master,text='Open File ', command=lambda: open_file()).grid(row=2,column=3,sticky=tk.W,pady=4)

tk.mainloop()
