# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import random
from Database import *

i = 0
jan_usa = []
iniciador = "Pc"

sit = []

def Reset():
    global i
    i = 0


def Check(lista, jan_usa):
    if iniciador == "Pc":
        Joga_pc(lista, jan_usa)





def Nov_jog(lista_de_entries):
    global iniciador
    global jan_usa
    global sit


    for item in lista_de_entries:
        item.configure(text=' ')



    jan_usa = []
    iniciador = Geraini()
    if iniciador == "Pc":
        pc = "X"
        jogador = "O"
    else:
        pc = "O"
        jogador = "X"


    sit = [pc,jogador]

    if sit[0] == "X":
        Joga_pc(lista_de_entries, jan_usa)


def Geraini():
    esc = random.randint(0, 1)
    if esc == 0:
        iniciador = "Pc"
    else:
        iniciador = "Jogador"
    return iniciador


def Joga_pc(lista, jan_usa):
    # noinspection PyGlobalUndefined
    global iniciador
    global i

    global sit

    if not i == 8:
        base = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for item in jan_usa:
            if item in base:
                base.remove(item)
        esc = random.randint(0, 8)
        while not esc in base:
            esc = random.randint(0, 8)
        lista[esc].configure(text=f"{sit[0]}")
        i += 1
        jan_usa.append(esc)
        Verificar(lista)



def Apga(local):
    for item in local:
        item.delete(0, "end")


def Cpf_val():
    i = 0
    cpf = "14176547405"
    if len(cpf) == 11:
        if cpf.isnumeric():
            dv = cpf[9:]
            res = cpf[:9]
            cal = 0
            h = 1
            for letra in res:
                cal += int(letra) * h
                h += 1
            resto = cal % 11
            if resto == int(dv[0]):

                cal = 0
                h = 0
                con = res + str(resto)
                for letra in con:
                    cal += int(letra) * h
                    h += 1
                novo = cal % 11
                if novo == int(dv[1]):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def Validar(usuario, senha, cpf, nome, email):
    if Cpf_val():
        if "@" and ".com" in email:
            Botar(usuario, senha, cpf, nome, email)
            messagebox.showwarning("Atenção!", "Cadastro Efetuado!")

    else:
        messagebox.showwarning("Atenção!", "Algum dado inválido!")


def Log_banco(usuario, senha, window):
    if Ver_bank(usuario, senha):
        cpf = Get_cpf(usuario, senha)

        Jogo(window, cpf)
    else:
        messagebox.showwarning("Atenção!", "Login inválido")


def Verificar(lista_de_entries):
    def acertou(x_or_o):
        global iniciador

        global whindersson
        global i
        global sit

        if x_or_o == "X" or x_or_o == "O":

                if sit[0] == x_or_o:
                    ganhou = "Pc"
                    ss = Get_geral('partidas', cpf)
                    ss = int(ss) + 1
                    Muda('partidas', ss, cpf)
                    ss = Get_geral('derrotas',cpf)
                    ss = int(ss) + 1
                    Muda('derrotas',ss ,cpf)

                elif sit[1] == x_or_o:
                    ganhou = "jogador"
                    ss = Get_geral('partidas', cpf)
                    ss = int(ss) + 1
                    Muda('partidas', ss, cpf)
                    ss = Get_geral('vitorias', cpf)
                    ss = int(ss) + 1
                    Muda('vitorias', ss, cpf)

                if messagebox.askyesno('Vencedor', f' {ganhou} ganhou! Gostaria de jogar novamente?'):
                    iniciador = Geraini()
                    i = 0
                    Nov_jog(lista_de_entries)
                    #Check(lista_de_entries, jan_usa)
                else:
                    i = 0
                    whindersson.destroy()
                    Init()


    a1 = lista_de_entries[0].cget("text")
    a2 = lista_de_entries[1].cget("text")
    a3 = lista_de_entries[2].cget("text")
    b1 = lista_de_entries[3].cget("text")
    b2 = lista_de_entries[4].cget("text")
    b3 = lista_de_entries[5].cget("text")
    c1 = lista_de_entries[6].cget("text")
    c2 = lista_de_entries[7].cget("text")
    c3 = lista_de_entries[8].cget("text")

    if a1 == a2 == a3 == "X" or a1 == a2 == a3 == "O":
        if a1 == a2 == a3 == "X":
            acertou("X")
        elif a1 == a2 == a3 == "O":
            acertou("O")

    elif b1 == b2 == b3 == "X" or b1 == b2 == b3 == "O":
        if b1 == b2 == b3 == "X":
            acertou("X")
        elif b1 == b2 == b3 == "O":
            acertou("O")

    elif c1 == c2 == c3 == "X" or c1 == c2 == c3 == "O":
        if c1 == c2 == c3 == "X":
            acertou("X")
        elif c1 == c2 == c3 == "O":
            acertou("O")

    elif a1 == b1 == c1 == "X" or a1 == b1 == c1 == "O":
        if a1 == b1 == c1 == "X":
            acertou("X")
        elif a1 == b1 == c1 == "O":
            acertou("O")

    elif a2 == b2 == c2 == "X" or a2 == b2 == c2 == "O":
        if a2 == b2 == c2 == "X":
            acertou("X")
        elif a2 == b2 == c2 == "O":
            acertou("O")

    elif a3 == b3 == c3 == "X" or a3 == b3 == c3 == "O":
        if a3 == b3 == c3 == "X":
            acertou("X")
        elif a3 == b3 == c3 == "O":
            acertou("O")

    elif a1 == b2 == c3 == "X" or a1 == b2 == c3 == "O":
        if a1 == b2 == c3 == "X":
            acertou("X")
        elif a1 == b2 == c3 == "O":
            acertou("O")

    elif a3 == b2 == c1 == "X" or a3 == b2 == c1 == "O":
        if a3 == b2 == c1 == "X":
            acertou("X")
        elif a3 == b2 == c1 == "O":
            acertou("O")

    #testes = [a1, a2, a3, b1, b2, b3, c1, c2, c3]


def Jogo(janela, cpf2):
    # Botoes
    # noinspection PyGlobalUndefined
    global lista_de_entries
    global whindersson
    # noinspection PyGlobalUndefined
    global cpf
    # noinspection PyGlobalUndefined
    global vitorias
    # noinspection PyGlobalUndefined
    global jog
    # noinspection PyGlobalUndefined
    global nome

    cpf = cpf2

    janela.destroy()
    whindersson = tk.Tk()
    # window.geometry('700x500')
    whindersson.resizable(False, False)
    whindersson.title('Tela De Jogo')
    nome = Get_geral("nome", cpf)

    A1 = tk.Button(whindersson, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                   command=lambda: A_click(0, lista_de_entries, whindersson))
    A2 = tk.Button(whindersson, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                   command=lambda: A_click(1, lista_de_entries, whindersson))
    A3 = tk.Button(whindersson, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                   command=lambda: A_click(2, lista_de_entries, whindersson))

    A4 = tk.Button(whindersson, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                   command=lambda: A_click(3, lista_de_entries, whindersson))
    A5 = tk.Button(whindersson, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                   command=lambda: A_click(4, lista_de_entries, whindersson))
    A6 = tk.Button(whindersson, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                   command=lambda: A_click(5, lista_de_entries, whindersson))

    A7 = tk.Button(whindersson, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                   command=lambda: A_click(6, lista_de_entries, whindersson))
    A8 = tk.Button(whindersson, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                   command=lambda: A_click(7, lista_de_entries, whindersson))
    A9 = tk.Button(whindersson, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                   command=lambda: A_click(8, lista_de_entries, whindersson))

    # mapeamento
    A1.grid(row=1, column=1)
    A2.grid(row=2, column=1)
    A3.grid(row=3, column=1)

    A4.grid(row=1, column=2)
    A5.grid(row=2, column=2)
    A6.grid(row=3, column=2)

    A7.grid(row=1, column=3)
    A8.grid(row=2, column=3)
    A9.grid(row=3, column=3)

    lista_de_entries = [A1, A2, A3, A4, A5, A6, A7, A8, A9]

    Nov_jog(lista_de_entries)

    vitorias = Get_geral('vitorias', cpf)

    jog = tk.Label(whindersson, text=f"   {nome} :  Vitórias = {vitorias} (placar atualiza no fim do jogo) ",
                   font=("Helvetica", 12))
    jog.grid(row=1, column=4)
    pc = tk.Label(whindersson, text=f"   Computador: Vitórias = {Get_geral('derrotas', cpf)} ", font=("Helvetica", 12))
    pc.grid(row=2, column=4)

    jojo = tk.Button(whindersson, text="Sair", width=7, height=3,
                     command=lambda: [Reset(), whindersson.destroy(), Init()])
    jojo.grid(row=3, column=4)

    whindersson.mainloop()



def A_click(botao, lista_de_entries, whindersson):
    global iniciador
    global i
    global jan_usa
    global sit

    jan_usa.append(botao)

    if lista_de_entries[botao].cget('text') == ' ':

        lista_de_entries[botao].configure(text=f"{sit[1]}")

        Joga_pc(lista_de_entries, jan_usa)
        i += 1
        Verificar(lista_de_entries)

        if i == 9:
            i = 0
            if messagebox.askyesno('Resultado', 'Deu Um Empate! Gostaria de jogar novamente?'):
                ss = Get_geral('empates', cpf)
                ss = int(ss) + 1
                Muda('empates', ss, cpf)
                ss = Get_geral('partidas', cpf)
                ss = int(ss) + 1
                Muda('partidas', ss, cpf)
                Nov_jog(lista_de_entries)
                iniciador = Geraini()
                Check(lista_de_entries, jan_usa)
            else:
                whindersson.destroy()
                Init()



def Init():
    window = tk.Tk()
    window.title("Login.exe")
    window.geometry('700x500')
    window.resizable(False, False)
    tk.Label(window, text="Usuario").grid(row=0, column=0)
    tk.Label(window, text="Senha").grid(row=1, column=0)
    l = tk.Entry(window)
    s = tk.Entry(window)
    l.grid(row=0, column=1)
    s.grid(row=1, column=1)
    tk.Button(window, text='Login', command=lambda: Log_banco(l.get(), s.get(), window)).grid(row=3, column=0,
                                                                                              sticky=tk.W, pady=9)
    tk.Button(window, text='Cadastrar', command=lambda: Cadastro(window)).grid(row=3, column=1, sticky=tk.W, pady=9)
    tk.Button(window, text='Sair', command=lambda: window.destroy()).grid(row=4, column=0, sticky=tk.W, pady=2)

    window.mainloop()


def Cadastro(window):
    window.destroy()
    dados = tk.Tk()
    dados.title("Cadastro.exe")
    dados.geometry('700x500')
    dados.resizable(False, False)
    tk.Label(dados, text="usuario").grid(row=0)
    tk.Label(dados, text="Senha").grid(row=1)
    tk.Label(dados, text="CPF").grid(row=2)
    tk.Label(dados, text="Nome").grid(row=3)
    tk.Label(dados, text="E-mail").grid(row=4)
    uc = tk.Entry(dados)
    sc = tk.Entry(dados, show="*")
    cpf = tk.Entry(dados)
    nc = tk.Entry(dados)
    ec = tk.Entry(dados)

    uc.grid(row=0, column=1)
    sc.grid(row=1, column=1)
    cpf.grid(row=2, column=1)
    nc.grid(row=3, column=1)
    ec.grid(row=4, column=1)
    local = [uc, sc, cpf, nc, ec]
    tk.Button(dados, text='Salvar', command=lambda: [Validar(uc.get(), sc.get(), cpf.get(), nc.get(), ec.get())
        , Apga(local)]).grid(row=5, column=0, sticky=tk.W, pady=9)
    tk.Button(dados, text='Sair', command=lambda: [dados.destroy(), Init()]).grid(row=5, column=1, sticky=tk.W, pady=9)
