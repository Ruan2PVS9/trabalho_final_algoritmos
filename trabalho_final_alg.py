# RUAN E MAURICIO
### agenda de compromissos ###
import os
import time
from datetime import datetime, date


lista_tarefas = [] 
sair = False
# encontrado = True

def input_date():
  while True:
    date = input('informe a data(formato DD/MM/AAAA):')
    try:
      date = datetime.strptime(date, '%d/%m/%Y')
    except ValueError as msg:
      print(msg)
    else:
      return date.strftime('%d/%m/%Y')

def input_hour():
  while True:
    hour = input('informe a horas (formato HH:MM):')
    try:
      hour = datetime.strptime(hour, '%H:%M')
    except ValueError as msg:
      print(msg)
    else:
      return hour.strftime('%H:%M')

class Tarefa:
    data = None
    hora = None
    duracao = None
    descricao = None

    def __init__(self, data, hora, duracao, descricao):
        self.data = data
        self.hora = hora
        self.duracao = duracao
        self.descricao = descricao

    def getTarefa(self):
      print(f"\n  Data: {self.data} | Hora: {self.hora} | Duração: {self.duracao} | Descrição: {self.descricao}")

    def setTarefa(self, duracao, descricao):
      print( duracao,descricao)
      self.duracao = duracao if not duracao == '' else self.duracao 
      self.descricao = descricao if not descricao == '' else self.descricao 



def menu(
  ops_menu = [
        { 
          "nome" : "Incluir tarefa" ,   
          "func" : "inserirTarefa"
        },
        {
          "nome" : "Remover tarefa" ,   
          "func" : "removerTarefa"
        },
        {
          "nome" : "Listar tarefas" ,   
          "func" : "listarTarefa"
        },
        {
          "nome" : "Consultar tarefa",   
          "func" :"consultarTarefa"
        },
        {
          "nome" :  "Alterar Tarefa" ,   
          "func" : "alterarTarefa"
        },
        {
          "nome" : "sair" ,   
          "func" : "finalizar"
        },
    ]
  ):
  while True:
    header()
    print('\n MENU:')
    for i in range(len(ops_menu)):
      print(f"\n [{i+1}]","|", ops_menu[i]["nome"])
    header()
    ops = input('\n ESCOLHA UMA OPÇÃO:')

    if int(ops) in range(1,len(ops_menu)+1): 
      globals()[ops_menu[int(ops)-1]['func']]()
      if sair:
        break
    else:
      header()
      print(f'"{ops}" não é uma opcão:')
      header()
      time.sleep(2)
      clear()

def header():
  for i in range(30) :
    print('*', end='')
  print()

def inserirTarefa():
    global lista_tarefas
    print('CADASTRANDO TAREFA:')
    t = Tarefa(
        data = input_date(),
        hora = input_hour(),
        duracao = input("Duração: "),
        descricao = input("Descrição: ")
    )

    vago, bvago = get_by_data_hora(t.data,t.hora, listar = False)

    if not bvago:
      lista_tarefas.append(t)  
      t.getTarefa()
      header()
      print('cadastrado com sucesso')
      header()
    else:
      print('ja há compromisso nessa data e horario:')
      listarTarefa(vago)
    time.sleep(1)
    clear()
  
def removerTarefa():
  global lista_tarefas
  header()
  if len(lista_tarefas) == 0: 
    print('não ha nenhuma tarefa')
  else:
    tarefa , encontrado= get_by_data_hora(listar = False)
    print(tarefa)
    if encontrado:
      if len(tarefa) == 1:
        print('tarefa a apagada é:')
        Tarefa.getTarefa(tarefa[0])
        lista_tarefas.remove(tarefa[0])
        print('tarefa a apagada com sucesso')
    else:
      print('Compromisso não encontrado')
  header()
  time.sleep(1)
  clear()

def listarTarefa(lista = 'all'):
  global lista_tarefas
  header()
  lista = lista_tarefas if lista == 'all' else lista
  if len(lista) == 0: 
    print('não ha nenhuma tarefa')
  else:
    for i in range(len(lista)):
      Tarefa.getTarefa(lista_tarefas[i])
  header()
  time.sleep(2)

def consultarTarefa():
  if len(lista_tarefas) == 0: 
    print('não ha nenhuma tarefa')
  else:
    menu( ops_menu = [
      {
        "nome":"Consultar por data",
        "func":"get_by_data"
      },
      {
        "nome":"Consultar por data e hora",
        "func":"get_by_data_hora"
      },
      {
        "nome":"Voltar",
        "func":"voltar"
      }
      ]
    )
  voltar()


def alterarTarefa():
  if len(lista_tarefas) == 0: 
    print('não ha nenhuma tarefa')
  else:
    tarefa , encontrado= get_by_data_hora(listar = False)
    if encontrado:
      if len(tarefa) == 1:
        print('tarefa a ser alterada é:')
        listarTarefa(tarefa)
        duracao = input('Caso queira muadar a duração informe a nova duracao:')
        descricao = input('Caso queira muadar a descrição informe a nova descrição:')
        Tarefa.setTarefa(tarefa[0], duracao,descricao)
        Tarefa.getTarefa(tarefa[0])
    else:
      print('Compromisso não encontrado')
  header()
  time.sleep(2)
  clear()

def finalizar():
  global sair
  sair = True
  clear()
  header()
  print('Obrigado e volte sempre!!')
  header()
  
def voltar():
  global sair
  sair = not sair
  clear()
  header()
  print('voltando')
  header()
  
def get_by_data(listar = True):
  filtro_data = input_date()
  filtrados = []
  for i in range(len(lista_tarefas)):
      if lista_tarefas[i].data == filtro_data:
          filtrados.append(lista_tarefas[i])
  if len(filtrados) == 0:
    encontrado = False
  else:
    encontrado = True
  if listar:
    if encontrado:
      listarTarefa(filtrados)
    else:
      header()
      print('Agenda Vazia')
  header()
  time.sleep(1)
  clear()

def get_by_data_hora(filtro_data = '', filtro_hora = '', listar = True ):
  filtro_data = input_date() if filtro_data == '' else filtro_data
  filtro_hora = input_hour() if filtro_hora == '' else filtro_hora
  filtrados = []
  for i in range(len(lista_tarefas)):
    if lista_tarefas[i].data == filtro_data and lista_tarefas[i].hora == filtro_hora:
        filtrados.append(lista_tarefas[i])
  if len(filtrados) == 0:
    encontrado = False
  else:
    encontrado = True
  if listar:
    if encontrado:
      listarTarefa(filtrados)
    else:
      header()
      print('Agenda Vazia')
      header()
      time.sleep(1)
      clear()

  return filtrados , encontrado
  
def clear():
    ''
    print("\n" * 130)
    print("\x1b[2J")
    os.system('cls' if os.name == 'nt' else 'clear')

# menu()
def agenda():
  print("bem vindo")
  menu()

agenda()
