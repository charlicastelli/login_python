from tkinter import *
import tkinter.messagebox as tkMessageBox
import re 



COLOR_BUTTON = "#7984EE"
COLOR_TEXT_BUTTON = "#FFFFFF"
COLOR_BLACK = "#000000"
FONT_TEXT = 'arial'
FONT_SIZE_BTN = 14
FONT_SIZE_TXT = 18

user_text = 'E-mail ID: '
password_text = 'Password: '

#validar email
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

#Criar tela
screen = Tk()
screen.title("Sistema de Login")
screen.geometry("700x300")
screen.resizable(False, False) 
screen['bg'] = COLOR_BLACK
screen.iconphoto(True, PhotoImage(file='./images/icon.png'))


def buscar_usuario(login, senha):
    usuarios = []
    try:
        with open('users.txt', 'r+', encoding='Utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(",")
                usuarios.append(linha.split())
                for usuario in usuarios:
                    nome = usuario[0]
                    password = usuario[1]
                    if login == nome and senha == password:
                        return True
    except FileNotFoundError:
        return False

def sign_up():
    user = txt_input.get().strip()
    passw = password_input.get().strip()
    #validar senha
    flag = 0
    while True:   
        if (len(passw)<8): 
            flag = -1
            break
        elif not re.search("[a-z]", passw): 
            flag = -1
            break
        elif not re.search("[A-Z]", passw): 
            flag = -1
            break
        elif not re.search("[0-9]", passw): 
            flag = -1
            break
        else: 
            flag = 0
            print("Valid Password") 
            break

    if(re.search(regex,user) and flag == 0):  
        new_user = buscar_usuario(user, passw)
        if new_user == True:
            tkMessageBox.showinfo(
                "ATENÇÃO", 
                message= "Este usuário já possui cadastro"),
            txt_input.delete(0,"end")
            password_input.delete(0,"end")
        else:
            with open('users.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                arquivo.writelines(f' {user} {passw}\n')
                tkMessageBox.showinfo("ATENÇÃO", message= "Novo usuário cadastrado com sucesso"),
    else:  
        tkMessageBox.showinfo("ATENÇÃO", message= "E-mail ou senha inválidos\n\n"
        "- A senha de possuir pelo menos;\n"
        "- 8 caracteres\n" 
        "- Uma letra minúscula [az]\n" 
        "- Uma letra maiúscula [AZ]\n"
        "- 1 número ou dígito entre [0-9]") 

    

    txt_input.delete(0,"end")
    password_input.delete(0,"end")

def sign_in():
    user = txt_input.get()
    passw = password_input.get()
    login_user = buscar_usuario(user, passw)
    if login_user == True:
        tkMessageBox.showinfo("BEM VINDO", message= "Você está logado!"),
        txt_input.delete(0,"end")
        password_input.delete(0,"end")
    else:
        tkMessageBox.showinfo("ATENÇÃO", message= "Usuário ou senha incorretos. Por favor verifique"),
        txt_input.delete(0,"end")
        password_input.delete(0,"end")
    
text_login = Label(
    screen, 
    foreground=COLOR_TEXT_BUTTON, 
    bg= COLOR_BLACK,
    text = user_text,
    font=(FONT_TEXT, FONT_SIZE_TXT, 'bold'))
text_login.place(relx = 0.1, rely = 0.28)

txt_input = Entry(
    screen, 
    width=40,
    justify='left',
    fg=COLOR_BLACK, 
    font=(FONT_TEXT,14))
txt_input.place(relx=0.3, rely=0.3)


text_login = Label(
    screen, 
    foreground=COLOR_TEXT_BUTTON, 
    bg= COLOR_BLACK,
    text = password_text,
    font=(FONT_TEXT, FONT_SIZE_TXT, 'bold'))
text_login.place(relx = 0.1, rely = 0.41)

password_input = Entry(
    screen, 
    width=40,
    justify='left',
    show='*',
    fg=COLOR_BLACK, 
    font=(FONT_TEXT,14))
password_input.place(relx=0.3, rely=0.43)


bt_login = Button(
    screen, 
    width=18, 
    text = "SIGN IN", 
    foreground=COLOR_TEXT_BUTTON, 
    bg=COLOR_BUTTON, 
    font=(FONT_TEXT,FONT_SIZE_BTN,'bold'),
    command= sign_in)
bt_login.place(relx = 0.18, rely = 0.8)

bt_create = Button(
    screen, 
    width=18, 
    text = "SIGN UP", 
    foreground=COLOR_TEXT_BUTTON, 
    bg=COLOR_BUTTON, 
    font=(FONT_TEXT,FONT_SIZE_BTN,'bold'),
    command= sign_up)
bt_create.place(relx = 0.53, rely = 0.8)

screen.mainloop()
