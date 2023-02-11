# RUAN E MAURICIO
### agenda de compromissos ###
import os
import time

lista_tarefas = []
sair = False
encontrado = True


class Tarefa:
    data = None
    hora = None
    duracao = None
    descricao = None
    def __init__(self, data, hora,duracao, descricao):
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

def agenda():
  print("bem vindo")
  menu()

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
    cabesalho()
    print('\n MENU:')
    for i in range(len(ops_menu)):
      print(f"\n [{i+1}]","|", ops_menu[i]["nome"])
    cabesalho()
    ops = input('\n ESCOLHA UMA OPÇÃO:')

    if int(ops) in range(1,len(ops_menu)+1): 
      globals()[ops_menu[int(ops)-1]['func']]()
      if sair:
        break
    else:
      cabesalho()
      print(f'"{ops}" não é uma opcão:')
      cabesalho()

def cabesalho():
  for i in range(30) :
    print('*', end='')
  print()

def inserirTarefa():
    global lista_tarefas
    print('CADASTRANDO TAREFA:')
    t = Tarefa(
        data = input("\nData: "),
        hora = input("\nHora: "),
        duracao = input("\nDuração: "),
        descricao = input("\nDescrição: ")
    )
    vago = get_by_data_hora(t.data,t.hora)
    if len(vago) == 0:
      lista_tarefas.append(t)  
      t.getTarefa()
      print('cadastrado com sucesso')
    else:
      print('ja há compromisso nessa data e horario:')
      listarTarefa(vago)
    time.sleep(1)
  
def removerTarefa():
  get_by_data_hora()
  if encontrado:
    ''
  else:
    print('Compromisso não encontrado')

def listarTarefa(lista = 'all'):
    lista = lista_tarefas if lista == 'all' else lista
    for i in range(len(lista)):
        Tarefa.getTarefa(lista_tarefas[i])
    cabesalho()
    time.sleep(3)

def consultarTarefa():
  global encontrado
  tarefa = menu( ops_menu = [
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
  if encontrado:
    listarTarefa(tarefa)
  else:
    print('Agenda Vazia')
  voltar()


def alterarTarefa():
  global encontrado
  tarefa = get_by_data_hora()
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
    encontrado = True

def finalizar():
  global sair
  sair = True
  clear()
  cabesalho()
  print('Obrigado e volte sempre!!')
  cabesalho()
  
def voltar():
  global sair
  sair = not sair
  clear()
  cabesalho()
  # print('Obrigado e volte sempre!!')
  print('voltando')
  cabesalho()
  
def get_by_data():
  global encontrado 
  filtro_data = input('informe a data:')
  filtrados = []
  for i in range(len(lista_tarefas)):
      if lista_tarefas[i].data == filtro_data:
          filtrados.append(lista_tarefas[i])
  if len(filtrados) == 0:
    encontrado = False
    time.sleep(1)
  else:
    encontrado = True
  return filtrados



def get_by_data_hora(filtro_data = '', filtro_hora = ''):
  global encontrado 
  global lista_tarefas 
  filtro_data = input('informe a data:') if filtro_data == '' else filtro_data
  filtro_hora = input('informe a hora:') if filtro_hora == '' else filtro_hora
  filtrados = []
  listarTarefa(lista_tarefas)
  for i in range(len(lista_tarefas)):
    if lista_tarefas[i].data == filtro_data and lista_tarefas[i].hora == filtro_hora:
        filtrados.append(lista_tarefas[i])
  if len(filtrados) == 0:
    encontrado = False
    time.sleep(1)
  else:
    encontrado = True
  return filtrados
  
def clear():
    ''
    # print("\n" * 130)
    # print("\x1b[2J")
    # os.system('cls' if os.name == 'nt' else 'clear')

# menu()
agenda()
