---=== História do Projeto: ===---
 --- Durante nosso período no HMD (Hospital Municipal de Diadema), eu e 2 estagiários fomos encarregados de desenvolver um aplicativo de Banco de Dados para uso local do Suporte Técnico da empresa Tecnocomp.
 --- Utilizamos da linguagem Python para desenvolver o back-end do aplicativo, SQLite como o Banco de Dados, QTDesign como UI(interface de usuário) e utilizamos a biblioteca do ReportLab para a criação de PDFs
 baseados na linha de itens selecionada.

---=== Antes de Usar o Aplicativo: ===---
--- Este projeto foi desenvolvido de forma corrida por estagiários e não pretendemos dar continuidade no aplicativo.
--- O projeto conta com 2 listas de Banco de Dados diferentes, a "Lista Entrada" e a "Lista Saída". 
-- A "Lista Entrada" foi criada para os dispositivos que a Tecnocomp recebeu do hospital para manutenção, ou seja, são dispositivos que ainda estão em manutenção e ainda não saíram da oficina.
-- A "Lista Saída" foi criada para os dispositivos que a Tecnocomp já finalizou a manutenção necessária, ou seja, já estão em funcionamento e já foram devolvidos para o setor que requer o dispositivo. Além
disso, a "Lista Saída" conta com uma função de "Gerar Relatório", que cria um Relatório em PDF com os dados da linha selecionada pelo usuário.

 
 
 ---=== Como Utilizar o Aplicativo: ===---
 --- Para inicializar o aplicativo, o usuário deverá executar o arquivo "relatorioti.exe" (caso seu dispositivo não permita a visualização de extensões, o arquivo em questão possui um ícone de disquete junto da
 logotipo do Python)

 ---== Inserindo Dados:
 --- Para a inserção de dados, o usuário deve digitar em todos os campos necessários, após isso, clicar no botão "Lista Entrada" OU "Lista Saída" dependendo de qual lista os dados deverão ir (Linha 8).

 ---== Editando Dados:
 --- A função de editar dados está presente tanto na "Lista Entrada" quanto na "Lista Saída", o usuário deve selecionar o item à editar, um menu irá aparecer com todos os itens da linha do item selecionado e
 qualquer um destes itens poderá ser editado.

 ---== Função "Gerar Relatório":
 --- Esta função não é necessária para o funcionamento do aplicativo e foi apenas um pedido da Tecnocomp para auxiliar o funcionário local. O usuário deve selecionar o item que servirá como base para os
 dados que serão retornados dentro do arquivo PDF, após gerar o PDF, o Prompt de Comando irá retornar o nome do arquivo, cujo estará localizado na mesma pasta do aplicativo. Conforme o usuário gerar PDFs
 o número índice do PDF aumentará caso já tenha um arquivo com o mesmo nome na pasta do aplicativo, como se fosse um ID.

 --== Função de "Pesquisar Nº Chamado":
 --- Caso o Banco de Dados tenha muitos itens, temos a função "Pesquisar Nº Chamado" (pode ser encontrada na "Lista Entrada" e na "Lista Saída" no canto superior direito da janela do aplicativo), a função
 permite a pesquisa da coluna "Chamado", pois esta é a forma mais rápida e eficaz para a Tecnocomp encontrar um item em específico no Banco de Dados.


---=== Como dito anteriormente, o projeto é longe de perfeito, mas foi feito com muito esforço e dedicação do time :D.
