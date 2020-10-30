import tkinter as tk

fang_mapping = {
    ".": "[.]",
    "http": "hxxp",
    "https":"hxxps",
    "@": "[AT]"
}

def defang(url):
    out_string = [a_url]
    [out_string.append(out_string[-1].replace(value, key)) for key,value in fang_mapping.items()]
    master.clipboard_clear()
    master.clipboard_append(out_string[-1])

def fang(url):
    out_string = [a_url]
    [out_string.append(out_string[-1].replace(key, value)) for key,value in fang_mapping.items()]
    master.clipboard_clear()
    master.clipboard_append(out_string[-1])

master = tk.Tk()
master.title("FangOff by @TheCyberViking")
master.geometry("400x55")
tk.Label(master, text="Enter URL: ").grid(row=0)
url = tk.Entry(master, width=54)
url.grid(row=0, column=1)
tk.Button(master,text='De-Fang ',command=lambda: defang(url.get()) ).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Button(master,text='Re-Fang ', command=lambda: fang(url.get())).grid(row=3,column=1,sticky=tk.W,pady=4)
tk.mainloop()
