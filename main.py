from cryptography.fernet import Fernet
from tkinter import *
from tkinter import filedialog
from functools import partial
from tkinter import messagebox

def browseFiles():
    browseFiles.filename = filedialog.askopenfilename(initialdir="/", title="Select a File",)
    label_file_explorer.configure(text="File Opened: " + browseFiles.filename)

    pass_label.pack()
    passwd.pack()
    temp_label.pack()
    enterbutton.pack()
    temp_label2.pack()

def checkpass():
    if (password.get() == ""):
        messagebox.showinfo("Encrypt or Decrypt", "Please enter your password")
    elif(password.get() == "12345"):
        button_encrypt.pack()
        temp_label4.pack()
        button_decrypt.pack()
        temp_label3.pack()
    else:
        messagebox.showinfo("Encrypt or Decrypt", "Wrong password")

def encrypt_file(p_word):
    temp_key = p_word.get()
    temp_key = ''.join(e for e in temp_key if e.isalnum())
    key = temp_key + ("s" * (43 - len(temp_key)) + "=")

    fernet = Fernet(key)

    with open(browseFiles.filename, 'rb') as file:  original = file.read()
    encrypted = fernet.encrypt(original)

    with open(browseFiles.filename, 'wb') as encrypted_file: encrypted_file.write(encrypted)

    status_label.configure(text="Encryption Done! Now check your file",font=("chiller",40))
    status_label.pack()

def decrypt_file(p_word):
    temp_key = p_word.get()
    temp_key = ''.join(e for e in temp_key if e.isalnum())
    key = temp_key + ("s" * (43 - len(temp_key)) + "=")

    fernet = Fernet(key)

    with open(browseFiles.filename, 'rb') as enc_file:  encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)

    with open(browseFiles.filename, 'wb') as dec_file:  dec_file.write(decrypted)

    status_label.configure(text="Decryption Done! Now check your file",font=("chiller",40))
    status_label.pack()

window = Tk()

window.title('Encryption & Decryption')
window.geometry('1270x600+0+0')
window.config(background="#17A589")

main_title = Label(window, text="Encryption & Decryption System", width=100, height=2, fg="black", bg="#999999",font =("",30))
password = StringVar()

submit_para_en = partial(encrypt_file, password)
submit_para_de = partial(decrypt_file, password)

label_file_explorer = Label(window, text="File location : ", width=100, height=2, fg="white", bg="#17A589",font =("",20))
pass_label = Label(window, text="Password for encryption/decryption : ", width=100, height=2, fg="white", bg="#17A589",font =("",20))
temp_label = Label(window, text="", bg="#17A589")
temp_label2 = Label(window, text="", bg="#17A589")
temp_label3 = Label(window, text="", bg="#17A589")
temp_label4 = Label(window, text="", bg="#17A589")
button_explore = Button(window, text="Browse File", command=browseFiles, width=25, height=2, font =("",15))

passwd = Entry(window, textvariable=password,show="*",width=30,borderwidth=2)

enterbutton=Button(window, text="Enter", command=checkpass, width=25, height=2,font =("",15))
button_encrypt = Button(window, text="Encrypt", command=submit_para_en, width=25, height=2,
                        font=("", 15))

button_decrypt = Button(window, text="Decrypt", command=submit_para_de, width=25, height=2,
                        font=("", 15))

status_label = Label(window, text="", width=50, fg="#ffffff", bg="#17A589",font =("",17))

main_title.pack()
label_file_explorer.pack()
button_explore.pack()
window.mainloop()