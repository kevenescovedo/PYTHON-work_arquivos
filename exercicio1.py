import emoji

class Produtos:
  codigo = 0
  nome = ''
  preco = 0.0

def cadastrar():
  arquivo = open('Produtos.txt', 'w')
  produto = Produtos()
  for x in range(10):
    produto.codigo = int(input("Digite o código do {}º produto -> ".format(x + 1)))
    produto.nome = str(input("Digite o nome do {}º produto -> ".format(x + 1)))
    produto.preco = float(input("Digite o valor do {}º produto -> ".format(x + 1)))
    print()
    arquivo.write('{} {} {:.2f}\n'.format(produto.codigo, produto.nome, produto.preco))
  arquivo.close()
  print("\033[0;32mCadastro realizado com sucesso.\033[m")
  input('\33[41mDigite qualquer tecla para voltar ao menu...\33[m')
  return main()

def listar():
  arquivo = open('Produtos.txt', 'r')
  for z in arquivo.readlines():
    print("-" * 120)
    produto = Produtos()
    produto.codigo, produto.nome, produto.preco = z.strip().split(" ")
    print("Código do produto: {}\t\tNome do produto: {}\t\tPreço do produto: {}".format(produto.codigo,produto.nome, produto.preco))
  arquivo.close()
  input('\33[7m\nDigite qualquer tecla para voltar ao menu...\33[m')
  return main()

def sair():
  print(emoji.emojize("\n\033[0;32mObrigado por usar nosso sistema! :sunglasses: \033[m", use_aliases=True))

def main():
  print("-" * 100)
  print("\t\t\t\t\t\033[95mMenu\033[00m")
  print("-" * 100)
  print("1 - Cadastrar produtos")
  print("2 - Consultar produtos")
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
