import sqlite3
from PyQt5 import uic, QtWidgets

# conexão com sq lite
conn = sqlite3.connect('saidabanco.db')

def funcao_principal():
    print("teste")
    Linha1 = relatorioti.lineEdit.toPlainText()
    data_selecionada = relatorioti.dateEdit.date().toString("dd/MM/yyyy")

    cursor = conn.cursor()
    conn.execute('''
    INSERT OR REPLACE INTO tabela_relatorio (saida, solucao)
    VALUES (?,?) ''',
    (Linha1, data_selecionada ))
    
    
    
    conn.commit()
    cursor.close()

def voltar():
    segundatela.hide()
    relatorioti.show()

app=QtWidgets.QApplication([])
relatorioti=uic.loadUi("relatorios.ui")
segundatela=uic.loadUi("saida.ui")
relatorioti.benviar.clicked.connect(funcao_principal)
segundatela.bvoltar.clicked.connect(voltar)
segundatela.show()

app.exec()