import sqlite3
import os
from reportlab.lib.pagesizes import A4, letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QDate, QSortFilterProxyModel
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyQt5.QtGui import QStandardItem,QStandardItemModel

numero_id = 0
# conexão com sq lite
conn = sqlite3.connect('banco.db')
bancosaida = sqlite3.connect('saidabanco.db')


# Criando um cursor para executar consultas SQL

# Fechando a conexão


def funcao_principal():
    print("Programa Iniciado com Sucesso.")
    
    
    combobox1 = relatorioti.cctipodeequipamento.currentText()
    Linha1 = relatorioti.lemarca.text()
    Linha2 = relatorioti.lemodelo.text()
    Linha3 = relatorioti.lechamado.text()
    Linha4 = relatorioti.lesolicitante.text()
    Linha5 = relatorioti.lepatrimonio.text()
    Linha6 = relatorioti.tedefeito.toPlainText()
    Linha7 = relatorioti.teatividade.toPlainText()
    data_selecionada = relatorioti.QDateEdit.date().toString("dd/MM/yyyy")
    

    cursor = conn.cursor()
    conn.execute('''
    INSERT INTO tabela_relatorio (tipo_equipamento,marca, modelo, chamado, solicitante, patrimonio, atividade, defeito, entrada)
    VALUES (?,?, ?, ?, ?, ?, ?, ?, ?) ''',
    (combobox1,Linha1, Linha2, Linha3, Linha4, Linha5, Linha6, Linha7, data_selecionada))
    
    
    conn.commit()
    cursor.close()

def limpatexto():
    relatorioti.lemarca.setText("")
    relatorioti.lechamado.setText("")
    relatorioti.lepatrimonio.setText("")
    relatorioti.lesolicitante.setText("")
    relatorioti.lemodelo.setText("")
    relatorioti.tedefeito.setText("")
    relatorioti.teatividade.setText("")
    relatorioti.lesolucao.setText("")

def chama_segunda_tela():
    print("Seguda Tela funcionando.")
    segundatela.show()
    relatorioti.hide()
    
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tabela_relatorio")
    dados_lidos = cursor.fetchall()
    segundatela.tableWidget.setRowCount(len(dados_lidos))
    segundatela.tableWidget.setColumnCount(10)
    
    
    for i in range(0, len(dados_lidos)):
       for k in range(0, 10):
        segundatela.tableWidget.setItem(i,k,QtWidgets.QTableWidgetItem(str(dados_lidos[i][k]))) 
         
    conn.commit()
    cursor.close()
    
def enviar_segunda_tela():
    print("Registro Enviado com Sucesso!")
    cursor = conn.cursor()

    cursor.execute("SELECT saida, solucao FROM tabela_relatorio")
    dados_lidos = cursor.fetchall()
    segundatela.tableWidget.setRowCount(len(dados_lidos))
    segundatela.tableWidget.setColumnCount(2)

def chama_terceira_tela():
    terceiratela.show()
    relatorioti.hide()
    
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM R2")
    dados_lidos = cursor.fetchall()
    terceiratela.tableWidget.setRowCount(len(dados_lidos))
    terceiratela.tableWidget.setColumnCount(12)
    
    
    for i in range(0, len(dados_lidos)):
       for m in range(0, 12):
         terceiratela.tableWidget.setItem(i,m,QtWidgets.QTableWidgetItem(str(dados_lidos[i][m]))) 

         
    conn.commit()
    cursor.close()


def voltar():
    segundatela.hide()
    relatorioti.show()

def voltar2():
   terceiratela.hide()
   relatorioti.show()

def editar_dados():
    global numero_id
    linha = segundatela.tableWidget.currentRow()

    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tabela_relatorio")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM tabela_relatorio WHERE id="+ str(valor_id))
    chamado = cursor.fetchall()
    telaeditar.show()

    numero_id = valor_id
    
    telaeditar.elineEdit.setText(str(chamado[0][1]))
    telaeditar.elineEdit_2.setText(str(chamado[0][2]))
    telaeditar.elineEdit_3.setText(str(chamado[0][3]))
    telaeditar.elineEdit_4.setText(str(chamado[0][4]))
    telaeditar.elineEdit_5.setText(str(chamado[0][5]))
    telaeditar.elineEdit_6.setText(str(chamado[0][6]))
    telaeditar.elineEdit_7.setText(str(chamado[0][7]))
    telaeditar.elineEdit_8.setText(str(chamado[0][8]))
    telaeditar.elineEdit_11.setText(str(chamado[0][9]))


def salvardadoseditados():
        global numero_id
        tipo_equipamento = telaeditar.elineEdit.text()
        marca = telaeditar.elineEdit_2.text()
        modelo = telaeditar.elineEdit_3.text()
        patrimonio = telaeditar.elineEdit_4.text()
        chamado = telaeditar.elineEdit_5.text()
        solicitante = telaeditar.elineEdit_6.text()
        entrada = telaeditar.elineEdit_11.text()
        defeito = telaeditar.elineEdit_7.toPlainText()
        atividade = telaeditar.elineEdit_8.toPlainText()
        cursor = conn.cursor()
        cursor.execute("UPDATE tabela_relatorio SET tipo_equipamento = '{}', marca = '{}', modelo = '{}', patrimonio = '{}', chamado = '{}', solicitante = '{}', entrada = '{}', defeito = '{}', atividade = '{}' WHERE id = {}".format(tipo_equipamento, marca, modelo, patrimonio, chamado, solicitante, entrada, defeito, atividade, numero_id))
        telaeditar.close()
        segundatela.close()
        chama_segunda_tela()


def enviarsaida():
    print("Registro de Saída Enviado com Sucesso!")
    
    
    combobox1 = relatorioti.cctipodeequipamento.currentText()
    Linha1 = relatorioti.lemarca.text()
    Linha2 = relatorioti.lemodelo.text()
    Linha3 = relatorioti.lechamado.text()
    Linha4 = relatorioti.lesolicitante.text()
    Linha5 = relatorioti.lepatrimonio.text()
    Linha6 = relatorioti.tedefeito.toPlainText()
    Linha7 = relatorioti.teatividade.toPlainText()
    data_selecionadae = relatorioti.QDateEdit.date().toString("dd/MM/yyyy")
    data_selecionadas = relatorioti.QDateEdit2.date().toString("dd/MM/yyyy")
    Linha8 = relatorioti.lesolucao.toPlainText()

    cursor = conn.cursor()
    conn.execute('''
    INSERT INTO R2 (saida, entrada, tipo_equipamento, marca, modelo, chamado, solicitante, patrimonio, atividade, defeito, solucao)
    VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ''',
    (data_selecionadas,data_selecionadae,combobox1,Linha1, Linha2, Linha3, Linha4, Linha5, Linha6, Linha7, Linha8))
    
    
    conn.commit()
    cursor.close()


def editarsaida(): 
    global numero_id
    linhas = terceiratela.tableWidget.currentRow()

    cursor = conn.cursor()
    cursor.execute("SELECT id FROM R2")
    dados_lidos2 = cursor.fetchall()
    valor_id = dados_lidos2[linhas][0]
    cursor.execute("SELECT * FROM R2 WHERE id="+ str(valor_id))
    chamado = cursor.fetchall()
    telaeditar2.show()

    numero_id = valor_id
    
    telaeditar2.elineEdit.setText(str(chamado[0][1]))
    telaeditar2.elineEdit_11.setText(str(chamado[0][2]))
    telaeditar2.elineEdit_3.setText(str(chamado[0][3]))
    telaeditar2.elineEdit_4.setText(str(chamado[0][4]))
    telaeditar2.elineEdit_5.setText(str(chamado[0][5]))
    telaeditar2.elineEdit_6.setText(str(chamado[0][6]))
    telaeditar2.elineEdit_7.setText(str(chamado[0][7]))
    telaeditar2.elineEdit_8.setText(str(chamado[0][8]))
    telaeditar2.elineEdit_9.setText(str(chamado[0][9]))
    telaeditar2.elineEdit_10.setText(str(chamado[0][10]))
    telaeditar2.elineEdit_2.setText(str(chamado[0][11]))
    


def salvardadoseditadoss():
        global numero_id
        saida = telaeditar2.elineEdit.text()
        entrada = telaeditar2.elineEdit_11.text()
        tipo_equipamento = telaeditar2.elineEdit_3.text()
        marca = telaeditar2.elineEdit_4.text()
        modelo = telaeditar2.elineEdit_5.text()
        chamado = telaeditar2.elineEdit_6.text()
        solicitante = telaeditar2.elineEdit_7.text()
        patrimonio = telaeditar2.elineEdit_8.text()
        defeito = telaeditar2.elineEdit_10.toPlainText()
        atividade = telaeditar2.elineEdit_9.toPlainText()
        solucao = telaeditar2.elineEdit_2.toPlainText()
        
        cursor = conn.cursor()
        cursor.execute("UPDATE R2 SET saida = '{}', entrada = '{}', tipo_equipamento = '{}', marca = '{}', modelo = '{}', chamado = '{}', solicitante = '{}', patrimonio = '{}', defeito = '{}', atividade = '{}',solucao = '{}' WHERE id = {}".format(saida, entrada, tipo_equipamento, marca, modelo, chamado, solicitante, patrimonio, defeito, atividade, solucao, numero_id))
        telaeditar2.close() 
        terceiratela.close()
        chama_terceira_tela()


def excluirdados():
    print("Registro Excluído com Sucesso!")
    linha = segundatela.tableWidget.currentRow()
    segundatela.tableWidget.removeRow(linha)

    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tabela_relatorio")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM tabela_relatorio WHERE id=" + str (valor_id))

def excluirdadossaida():
    print("Registro Excluído com Sucesso!")
    linha = terceiratela.tableWidget.currentRow()
    terceiratela.tableWidget.removeRow(linha)

    cursor = conn.cursor()
    cursor.execute("SELECT id FROM R2")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM R2 WHERE id=" + str (valor_id))


def gerar_nome_arquivo(base_name, extension):
    contador = 1
    novo_nome = f"{base_name}.{extension}"
    
    while os.path.exists(novo_nome):
        novo_nome = f"{base_name}_{contador}.{extension}"
        contador += 1
    
    return novo_nome



def gerar_pdf():
    global numero_id
    linha = terceiratela.tableWidget.currentRow()
    base_name = "Relatório"
    extension = "pdf"
    nome_arquivo = gerar_nome_arquivo(base_name, extension)
    
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM R2")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT id, tipo_equipamento, marca, modelo, patrimonio, chamado, solicitante, entrada, saida FROM R2 WHERE id=" + str(valor_id))
    dados_lidos = cursor.fetchall()

    cursor2 = conn.cursor()
    cursor2.execute("SELECT atividade, defeito, solucao FROM R2 WHERE id=" + str(valor_id))
    dados_lidos2 = cursor2.fetchall()

    pdf = SimpleDocTemplate(nome_arquivo, pagesize=landscape(letter))
    
    elements = []

    estilo_paragrafo = ParagraphStyle(
        name='CustomParagrahStyle',
        fontName='Helvetica',
        fontSize=10,
        leading=12,  # Espaçamento entre linhas
    )

    # Adicionando os dados da tabela R2
    if dados_lidos:
        headers = [desc[0] for desc in cursor.description]  # Recupera os nomes das colunas
        normal_headers = [h for h in headers if h not in ['Atividade', 'Defeito', 'Solução']]
        data_normal = []
        
        for row in dados_lidos:
            normal_row = []
            for idx, value in enumerate(row):
                if headers[idx] not in ['Atividade', 'Defeito', 'Solução']:
                    normal_row.append(value)
            data_normal.append(normal_row)
        
        # Tabela normal
        table_normal = Table([normal_headers] + data_normal)
        table_normal.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table_normal)
        elements.append(Spacer(1, 24))
        
        # Tabela com colunas maiores
        data_large = [['Atividade', 'Defeito', 'Solução']] + dados_lidos2
        table_large_data = []
        for row in data_large:
            table_large_row = []
            for cell_content in row:
                if isinstance(cell_content, str):
                    paragrafo = Paragraph(cell_content, estilo_paragrafo)
                    table_large_row.append(paragrafo)
                else:
                    table_large_row.append(cell_content)
            table_large_data.append(table_large_row)
        
        # Cria a tabela com os dados modificados
        table_large = Table(table_large_data, colWidths=[3*inch, 3*inch, 3*inch])
        table_large.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table_large)
    else:
        no_data = Paragraph("No data available in the R2 table.", ['CustomNormal'])
        elements.append(no_data)
    
    pdf.build(elements)
    print(f"Arquivo salvo como: {nome_arquivo}")
    cursor.close()
    cursor2.close()

    
def procurar():
    search_text = segundatela.lineEditSearch.text()
    cursor = conn.cursor()

    query = f"SELECT * FROM tabela_relatorio WHERE chamado LIKE ?"
    cursor.execute(query, ('%' + search_text + '%',))
    results = cursor.fetchall()


    segundatela.tableWidget.setRowCount(len(results))
    segundatela.tableWidget.setColumnCount(len(results[0]) if results else 0)
    
    for row_num, row_data in enumerate(results):
        for col_num, col_data in enumerate(row_data):
            segundatela.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

    cursor.close()



def procurarsaida():
    search_text = terceiratela.lineEditSearch.text()
    cursor = conn.cursor()

    query = f"SELECT * FROM R2 WHERE chamado LIKE ?"
    cursor.execute(query, ('%' + search_text + '%',))
    results = cursor.fetchall()


    terceiratela.tableWidget.setRowCount(len(results))
    terceiratela.tableWidget.setColumnCount(len(results[0]) if results else 0)
    
    for row_num, row_data in enumerate(results):
        for col_num, col_data in enumerate(row_data):
            terceiratela.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

    cursor.close()



app=QtWidgets.QApplication([])
relatorioti=uic.loadUi("relatorios.ui")
segundatela=uic.loadUi("saida.ui")
terceiratela=uic.loadUi("terceiratela.ui")
telaeditar=uic.loadUi("telaeditar.ui")
telaeditar2=uic.loadUi("telaeditar2.ui")
relatorioti.benviar.clicked.connect(funcao_principal)
relatorioti.benviar2.clicked.connect(enviarsaida)
relatorioti.benviar.clicked.connect(limpatexto)
relatorioti.benviar2.clicked.connect(limpatexto)
relatorioti.babrirlista.clicked.connect(chama_segunda_tela)
relatorioti.bsaidas.clicked.connect(chama_terceira_tela)
segundatela.bvoltar.clicked.connect(voltar)
terceiratela.bvoltar.clicked.connect(voltar2)
segundatela.beditar.clicked.connect(editar_dados)
terceiratela.seditar.clicked.connect(editarsaida)
relatorioti.cctipodeequipamento.addItems(["Monitor","Desktop","Impressora","Estabilizador"])
telaeditar.bsalvaredicao.clicked.connect(salvardadoseditados)
telaeditar2.bsalvaredicaos.clicked.connect(salvardadoseditadoss)
segundatela.bexcluir.clicked.connect(excluirdados)
terceiratela.bexcluirsaida.clicked.connect(excluirdadossaida)
terceiratela.bgerarpdf.clicked.connect(gerar_pdf)
segundatela.lineEditSearch.textChanged.connect(procurar)
terceiratela.lineEditSearch.textChanged.connect(procurarsaida)


relatorioti.show()
app.exec()