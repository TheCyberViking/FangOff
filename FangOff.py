import tkinter as tk

def defang(url):
    str1 = url.replace(".", "[.]").replace("http", "hxxp").replace("https", "hxxps").replace("@", "[AT]")
    master.clipboard_clear()
    master.clipboard_append(str1)

def fang(url):
    str1 = url.replace("[.]", ".").replace("hxxps", "https").replace("hxxp", "http").replace("[AT]", "@")
    master.clipboard_clear()
    master.clipboard_append(str1)

master = tk.Tk()
master.title("FangOff by @TheCyberViking")
master.geometry("400x55")
tk.Label(master, text="Enter URL: ").grid(row=0)
url = tk.Entry(master, width=54)
url.grid(row=0, column=1)
tk.Button(master,text='De-Fang ',command=lambda: defang(url.get()) ).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Button(master,text='Re-Fang ', command=lambda: fang(url.get())).grid(row=3,column=1,sticky=tk.W,pady=4)
tk.mainloop()