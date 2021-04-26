import webbrowser
import subprocess
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as msg

base = tk.Tk()
base.title("Pyinstaller GUI 0.1 (GitHub Version)")
base.geometry("400x500")

base.resizable(0,0)
label = tk.Label(base, text = "Pyinstaller").grid(row=0,column=0)
label2 = tk.Label(base, text = "Please enter filename:*").grid(row=1,column=0)
var = tk.StringVar()
entry = tk.Entry(base, textvariable=var).grid(row=2, column = 0, ipadx=100)
def choosefile():
    filepath = fd.askopenfilename(title = "Select File", filetypes = (("Python file", ".py"), ("All files", "*.*")))
    var.set(filepath)
button = tk.Button(base, text = "Select file...", bg = "green", fg = "white",command=choosefile).grid(row=2, column=1)
label3 = tk.Label(base, text = "Please enter icon:*").grid(row=3, column = 0)
var2 = tk.StringVar()
entry1 = tk.Entry(base, textvariable=var2).grid(row=4, column = 0, ipadx=100)


def choosefile():
    filepath = fd.askopenfilename(title = "Select File", filetypes = (("ICO FIle", "*.ico"), ("All files", "*.*")))
    var2.set(filepath)
button2 = tk.Button(base, text = "Select file...", bg = "green", fg = "white",command=choosefile).grid(row=4, column=1)
label4 = tk.Label(base, text = "Please enter filename:*").grid(row=5, column=0)
var3 = tk.StringVar()
entry2 = tk.Entry(base, textvariable=var3).grid(row=6, column = 0, ipadx=100)
label5 = tk.Label(base, text = "Onefile:*").grid(row=7, column=0)


var4 = tk.StringVar()
chk1 = tk.Checkbutton(base, text = "--onefile", variable = var4, onvalue = "--onefile", offvalue = "").grid(row=8, column = 0)
text = tk.Text(base, bg = "black", fg = "white", font = ("Consolas", 11), height = "12", width = "48")
label6 = tk.Label(base, text = "Noconsole:").grid(row=9, column = 0)
var5 = tk.StringVar()
chk2 = tk.Checkbutton(base, text = "Noconsole", variable = var5, onvalue = "noconsole", offvalue = "").grid(row=10, column = 0)
def convert():
    if var4.get() == "--onefile" and var5.get() == "":

        output = subprocess.Popen(["pyinstaller", var.get(), "--icon", var2.get(), "--name", var3.get(), "--onefile"], stdout = subprocess.PIPE).communicate()[0]
        print(output)
    elif var4.get() == "--onefile" and var5.get() == "noconsole":

        output = subprocess.Popen(["pyinstaller", var.get(), "--icon", var2.get(), "--name", var3.get(), "--onefile", "--noconsole"],
                                  stdout=subprocess.PIPE).communicate()[0]
        print(output)
    elif var.get() == "":
        msg.showerror("Pyinstaller Error", "Please enter a filename!")
    elif var2.get() == "":
        msg.showerror("Pyinstaller Error", "Please enter a icon!")
    elif var3.get() == "":
        msg.showerror("Pyinstaller Error", "Please enter a name!")
    elif var4.get() == "" and var5.get() == "noconsole":

        output = subprocess.Popen(
            ["pyinstaller", var.get(), "--icon", var2.get(), "--name", var3.get(), "--noconsole"],
            stdout=subprocess.PIPE).communicate()[0]
        print(output)
    elif var4.get() == "--onefile" and var5.get() == "":

        output = subprocess.Popen(
            ["pyinstaller", var.get(), "--icon", var2.get(), "--name", var3.get(), "--onefile"],
            stdout=subprocess.PIPE).communicate()[0]
        print(output)



button3 = tk.Button(base, text = "Install your package!", bg = "green", fg = "white", command = convert).grid(row=11, column = 0)



def about():
    window = tk.Tk()
    window.title("About the Program...")
    window.geometry("400x300")
    window.resizable(0,0)
    label = tk.Label(window, text = "About The App", font = ("Roboto Bold", 20)).grid(row=0, column=0)
    label2 = tk.Label(window, text="", font=("Roboto", 20)).grid(row=1, column=0)
    label3 = tk.Label(window, text = "Pyinstaller GUI", font = ("Roboto Bold Italic", 15)).grid(row=2, column=0)
    label4 = tk.Label(window, text="Version 0.1 (0511)", font=("Roboto", 10)).grid(row=3, column=0)
    label5 = tk.Label(window, text="2020-2021 HowToTech TV Team/ Authors. All rights reserved.", font=("Roboto", 10)).grid(row=4, column=0)
    def visit(link):
        webbrowser.open(link)

    button3 = tk.Button(window, text="View in Github.com", bg = "green", fg = "white", command=lambda: visit("https://github.com/HowToTech-TV/Pyinstaller-GUI-For-Windows")).grid(row=5, column=0)
    button4 = tk.Button(window, text="Visit My Youtube Channel", bg = "green", fg = "white",
                        command=lambda: visit("https://www.youtube.com/channel/UCQDOdxPg3BXJjY0EWNMJgpQ")).grid(
        row=6, column=0)


    window.mainloop()
def exitapp():
    base.destroy()
def ins():
    import os
    os.system("pip install pyinstaller")
menu = tk.Menu(base)
menubar = tk.Menu(menu)
aboutmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = "About", menu = aboutmenu)
aboutmenu.add_command(label = "About the Program...", command=about)
aboutmenu.add_command(label = "Install Pyinstaller Extension (If no)", command=ins)

aboutmenu.add_command(label = "Exit App", command=exitapp)
base.config(menu=menubar)



base.mainloop()
