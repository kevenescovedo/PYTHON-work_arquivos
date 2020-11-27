class Jogadores:
  posicao_jogador = ''
  altura = 0.0
  peso = 0.0
  imc = 0.0

def listar_info_jogadores():
  arquivo = open('Jogadores.txt', 'r')
  print('\n\033[0;32mLeitura do arquivo feita com sucesso!\033[m')
  for z in arquivo.readlines():
    jogador = Jogadores()
    jogador.posicao_jogador, jogador.altura, jogador.peso = z.strip().split(",")
    print("Posição: {}\t\tAltura: {}\t\tPeso: {}".format(jogador.posicao_jogador,jogador.altura, jogador.peso))
  print()
  arquivo.close()

def calcular_imc_criar_arq():
  arquivo = open('Jogadores.txt', 'r')
  arquivo2 = open('Jogadores_imc.txt', 'w')
  print('\033[0;32mNovo arquivo gerado com o atributo IMC de cada jogador\033[m')
  for z in arquivo.readlines():
    jogador = Jogadores()
    jogador.posicao_jogador, jogador.altura, jogador.peso = z.strip().split(",")
    jogador.imc = float (jogador.peso) / (float(jogador.altura)) ** 2
    arquivo2.write('{},{},{},{}\n'.format(jogador.posicao_jogador, jogador.altura, jogador.peso, jogador.imc))
    print("Posição: {}\t\tAltura: {:.2f}\t\tPeso: {:.2f}\t\tIMC: {:.2f}".format(jogador.posicao_jogador,float(jogador.altura), float(jogador.peso), jogador.imc))
  print()
  arquivo.close()
  arquivo2.close()

def main():
  listar_info_jogadores()
  calcular_imc_criar_arq()

main()
