import tkinter as tk
import webbrowser

def defang(url):
    '''Check and see if any of the defanged values appear and if
    they do, just return, doing nothing. If they do not, fang it.'''
    
    defang_vals = ('hxxp', '[.]', '[AT]')
    if any(val in url for val in defang_vals):
        return
    else:
        str1 = url.replace(".", "[.]").replace("http", "hxxp").replace("https", "hxxps").replace("@", "[AT]")
        update_url(str1)

def fang(url):
    '''remove the particular things we are looking for, make url dangerous again'''
    str1 = url.replace("[.]", ".").replace("hxxps", "https").replace("hxxp", "http").replace("[AT]", "@")
    update_url(str1)

def update_url(text):
        '''just take the new value and update the url field
        This will be run during both defang and fang'''
        
        url.delete(0, len(url.get()))
        url.insert(0, text)

def open_page():
    '''check if any of the defanged values appear in the url field
    if they do, refang it and open the page with webbrowser.
    If they don't, just open it with webbrowser. If the url has an @
    in it, add mailto: and open it in webbrowser.'''

    defang_vals = ('hxxp', '[.]', '[AT]')
    if any(val in url.get() for val in defang_vals):
        fang(url.get())
    
    if '@' in url.get():
        webbrowser.open(f'mailto:{url.get()}')
    else:
        webbrowser.open(url.get())

#set up the master window
master = tk.Tk()
master.title("FangOff by @TheCyberViking")
master.geometry("630x70")
master.resizable(0, 0)

#set up the Entry line with default value
tk.Label(master, text="Enter URL: ").grid(row=0)
url = tk.Entry(master, width=54)
url.grid(row=0, column=1)
url.bind('<Return>', (lambda event: open_page())) #hit enter in the Entry and open the page
url.insert(0, 'hxxps://github[.]com/TheCyberViking') #default value

#set up buttons... two at the bottom, one after the Entry line
tk.Button(master,text='De-Fang ',command=lambda: defang(url.get())).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Button(master,text='Re-Fang ', command=lambda: fang (url.get())).grid(row=3,column=1,sticky=tk.W,pady=4)
tk.Button(master,text='Open URL', command=lambda: open_page()).grid(row=0,column=2, sticky=tk.W,padx=4)

tk.mainloop()
