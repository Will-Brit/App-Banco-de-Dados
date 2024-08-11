import sqlite3
from PyQt5 import uic, QtWidgets

conn = sqlite3.connect('saidabanco.db')

def funcao_principal():
    print("teste")

def voltar():
    terceiratela.hide()
    relatorioti.show()

app=QtWidgets.QApplication([])
relatorioti=uic.loadUi("relatorios.ui")
terceiratela=uic.loadUi("terceiratela.ui")
terceiratela.benviar.clicked.connect(funcao_principal)
relatorioti.bvoltar.clicked.connect(voltar)
terceiratela.bvoltar.clicked.connect(voltar)
terceiratela.show()

app.exec()