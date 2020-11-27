
""""
Elabore uma estrutura para representar e armazenar 10 alunos
(matricula, nome, telfone). Utilize os recursos de arquivo para armazenar estes dados
permanentemente. O nome do arquivo deve ser o mesmo da estrutura. Construa um menu com as seguintes opções,
cada uma delas deve ter uma função e a main para chamar todas elas.
Menu de opções:

Cadastrar produtos
Visualizar todos os dados
Sair
"""



import emoji

class Alunos:
  matricula = 0
  nome = ''
  telfone = ''

def cadastrar():
  arquivo = open('Alunos.txt', 'w')
  aluno = Alunos()
  for x in range(10):
    aluno.matricula = int(input("Digite a matricula, do {}º aluno -> ".format(x + 1)))
    aluno.nome = (input("Digite o nome do {}º aluno -> ".format(x + 1))
    aluno.telefone = input("Digite o número de telefone do aluno do {}º aluno -> ".format(x + 1))
    print()
    arquivo.write('{} {} {:.2f}\n'.format( aluno.matricula, aluno.nome, aluno.telefone))
  arquivo.close()
  print("\033[0;32mCadastro realizado com sucesso.\033[m")
  input('\33[41mDigite qualquer tecla para voltar ao menu...\33[m')
  return main()

def listar():
  arquivo = open('Alunos.txt', 'r')
  for z in arquivo.readlines():
    print("-" * 120)
    aluno = Alunos()
    aluno.matricula, aluno.nome,  aluno.telefone = z.strip().split(" ")
    print("Matricula: {}\t\tNome do Aluno: {}\t\t Telefone do Aluno: {}".format( aluno.matricula, aluno.nome,  aluno.matricula))
  arquivo.close()
  input('\33[7m\nDigite qualquer tecla para voltar ao menu...\33[m')
  return main()

def sair():
  print(emoji.emojize("\n\033[0;32mObrigado por usar nosso sistema! :sunglasses: \033[m", use_aliases=True))

def main():
  print("-" * 100)
  print("\t\t\t\t\t\033[95mMenu\033[00m")
  print("-" * 100)
  print("1 - Cadastrar Alunos")
  print("2 - Consultar Alunos")
  print("3 - Sair")
  escolha = int(input("\033[41mDigite uma das opções acima para continuar -> \033[m"))
  print()
  if escolha != 1 and escolha !=2  and escolha != 3:
    print('\033[41mDigite 1, 2 ou 3. Sem espaços ou pontos.\033[m\n')
    input('\33[41mDigite qualquer tecla para voltar ao menu...\033[m')
    return main()
  elif escolha == 1:
    cadastrar()
  elif escolha == 2:
    listar()
  elif escolha == 3:
    sair()

main()
