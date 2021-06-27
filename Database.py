import sqlite3
from sqlite3 import Error
import os

def Cone():
    con= sqlite3.connect("jogador.db")
    curs= con.cursor()
    return con,curs

def Criar():
    con,curs = Cone()
    query = """CREATE TABLE IF NOT EXISTS "jogador" (
	"usuario"	TEXT NOT NULL UNIQUE,
	"senha"	TEXT NOT NULL,
	"cpf"	TEXT NOT NULL UNIQUE,
	"nome"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	"partidas"	INTEGER DEFAULT 0,
	"vitorias"	INTEGER DEFAULT 0,
	"empates"	INTEGER DEFAULT 0,
	"derrotas"	INTEGER DEFAULT 0,
	PRIMARY KEY("cpf")
);
"""
    curs.execute(query)
    con.commit()


def Botar(usuario,senha,cpf,nome,email):
    con, curs = Cone()
    query= f"INSERT INTO jogador (usuario,senha, cpf, nome, email) VALUES ('{usuario}', '{senha}', '{cpf}', '{nome}','{email}')"
    curs.execute(query)
    con.commit()

def Show():
    con, curs = Cone()
    query= "SELECT * FROM jogador WHERE 1"
    curs.execute(query)
    con.commit()
    pimba= curs.fetchall()
    return pimba

def Muda(change,valor, cpf):
    con, curs = Cone()
    query= f"UPDATE jogador SET '{change}' = '{valor}' WHERE cpf= '{cpf}'"
    curs.execute(query)
    con.commit()

def Ver_bank(usuario,senha):
    con, curs = Cone()
    query = f"SELECT * FROM jogador WHERE usuario = '{usuario}' AND senha = '{senha}'"
    curs.execute(query)
    res = curs.fetchone()
    con.commit()
    return res

def Get_cpf(usuario,senha):
    con, curs = Cone()
    query = f"SELECT cpf FROM jogador WHERE usuario = '{usuario}' AND senha = '{senha}'"
    curs.execute(query)
    res = curs.fetchone()
    res = res[0]
    con.commit()
    return res

def Get_geral(procurado,cpf):
    con, curs = Cone()
    query = f"SELECT {procurado} FROM jogador WHERE cpf = '{cpf}'; "
    curs.execute(query)
    res = curs.fetchone()
    res = res[0]
    con.commit()
    return res


fileName = r"jogador.db"
if not os.path.isfile(fileName):
    Criar()


