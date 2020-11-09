import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askyesno, showinfo
import webbrowser
import sys

global filename
filename = ""

fang_mapping = {
    ".": "[.]",
    "http": "hxxp",
    "https":"hxxps",
    "@": "[AT]"
}

def set_initial_size():
    '''windows, linux, and mac default to different geometries in tkinter
    check os type and set geometry appropriately
    It seems the initial size and minimum size are set differently
    so I'll pass both text and min_x and min_y in a tuple'''
    os_type = sys.platform

    if os_type == 'win32':
        return ('408x160', 408, 160)
    elif os_type == 'darwin':
        return ('595x170', 595, 170)
    elif os_type == 'linux':
        return ('528x180', 528, 180)

def defang(url, clip=True):
    str1 = url
    for k, v in fang_mapping.items():
        str1 = str1.replace(k, v)

    if clip:
        master.clipboard_clear()
        master.clipboard_append(str1)
    return str1

def fang(url, clip=True):
    str1 = url
    for k, v in fang_mapping.items():
        str1 = str1.replace(v, k)
    
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

def open_url(url):
    '''check if any of the defanged values appear in the url field
    if they do, refang it and open the page with webbrowser.
    If they don't, just open it with webbrowser. If the url has an @
    in it, add mailto: and open it in webbrowser.
    Message (askyesno) pops up and verifies if you really want to open
    the scary internet.'''
    
    #if no url at all is entered, go ahead and give us Rick
    if url == '':
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    
    defang_vals = ('hxxp', '[.]', '[AT]')
    if any(val in url for val in defang_vals):
        url = fang(url)

    if '@' in url:
        url = f'mailto:{url}'
    
    if askyesno('Verify', 'Do you really want to open this URL?'):
        webbrowser.open(url)
    else:
        showinfo('No', 'URL opening has been cancelled.')
    
#set up main ui and sizing
master = tk.Tk()
master.title("FangOff by @TheCyberViking version: 1.5")
initial_size, min_x, min_y = set_initial_size()
master.geometry(initial_size)
master.minsize(min_x, min_y)

#this labelframe contains only the Entry line (member of url_frame)
url_frame = tk.LabelFrame(master, text='Enter URL')
url_frame.grid(row=0, column=0, columnspan=5, sticky='NW',
                padx=5, pady=5, ipadx=8, ipady=5)

url = tk.Entry(url_frame, width=60)
url.grid(row=0, column=1, padx=5)

#this labelframe contains the fanging buttons (members of fang_frame)
fang_frame = tk.LabelFrame(master, text='Fang')
fang_frame.grid(row=1, columnspan=3, rowspan=2, sticky='SW',
                padx=5, pady=5, ipady=4)

tk.Button(fang_frame,text='De-Fang ',command=lambda: defang(url.get())).grid(row=0, column=0, padx=5, pady=2)
tk.Button(fang_frame,text='Re-Fang  ', command=lambda: fang(url.get())).grid(row=1, column=0, padx=5, pady=2)
tk.Button(fang_frame,text='De-Fang File', command=lambda: fromfileDe()).grid(row=0, column=1, padx=5, pady=2)
tk.Button(fang_frame,text='Re-Fang File ', command=lambda: fromfileRe()).grid(row=1, column=1, padx=5, pady=2)
tk.Button(fang_frame,text='Open File ', command=lambda: open_file()).grid(row=0, column=3, padx=10)

#this labelframe has the open button in it (member of open_frame)
open_frame = tk.LabelFrame(master, text='Open')
open_frame.grid(row=1, column=3, columnspan=2, sticky='SE',
                padx=5, pady=5, ipady=17)

tk.Button(open_frame,text='Open URL', command=lambda: open_url(url.get())).grid(row=0, column=2, padx=10, pady=5)

tk.mainloop()
