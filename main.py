from hero import Hero
import random

def construir_heroi():
    nome = input("Digite o nome do herói: ")
    raca = input("Digite a raça que deseja [goblin, humano, anão, elfo]: ")
    cabelo = input("Digite a cor do cabelo que você deseja no seu personagem: ")
    classe = input("Digite a classe que você gostaria de ser [Cavaleiro, Viking, Mago, Samurai, Padre]: ")
    porte = input("Qual porte deseja ter [Magro, Gordo, Musculoso]: ")
    return Hero(nome, raca, cabelo, classe, porte)
def rinha_anoes():
    chance=random.randint(1,10000)
    return chance <= 10000
def inimigo_aleatorio():
    chance = random.randint(1, 100)
    return chance <= 30
def dano():
    probabilidade = random.randint(1, 10)
    return probabilidade <= 10

def jogo():
    heroi = construir_heroi()
    heroi.mostrar_detalhes()
    while True:
        acao = input("Qual ação deseja fazer [andar, descansar, sair]: ").strip().lower()
        if acao == 'sair':
            print("Você saiu do jogo.")
            break
        elif acao == 'andar':
            explorar = input("Você está explorando o local. Deseja continuar? S/N: ").strip().upper()
            if explorar == 'S':
                if inimigo_aleatorio():
                    print("Você encontrou um inimigo!")
                    lutar = input("Deseja lutar? S/N: ").strip().upper()
                    if lutar == 'S':
                        print("Você está lutando!")
                        heroi.atacar()
                        if dano():
                            print("Você foi atacado!")
                            heroi.sofrer_dano()
                        else:
                            print("Você derrotou o inimigo!")
                            if rinha_anoes():
                                print("*****Voce entrou em uma taverna onde esta tendo rinha ilegal de anoes *****")
                            aposta= input("Deseja apostar?  [S/N]")
                            if aposta == "S":
                                Hero.apostar
                                vitoria = random.randint(1,100)
                                if vitoria >= 100:
                                    Hero.perder_aposta
                                elif vitoria <= 100:
                                    Hero.ganhar_aposta
                            elif aposta == "N":
                                print("Voce nao apostou nada")
                                print("Voce continuo sua jornada lindamente caminhando pelos lindos vales")
                            else:
                                print("SIM OU NAO PORRA, QUER APOSTAR OU NAO?!!!!!!!!!")

                    elif lutar == 'N':
                        print("Você fugiu!")
                    else:
                        print("Opção inválida! Você foi atacado!")
                        heroi.sofrer_dano()
                else:
                    print("Você não encontrou nenhum inimigo.")
            else:
                print("Opção inválida. Tente novamente.")
        elif acao == 'descansar':
            print("Você está descansando.")
            heroi.vida += 10
            print(f"Sua vida agora é: {heroi.vida}")
        else:
            print("Opção inválida. Tente novamente.")

def mostrar_menu():
    menu = """
    ***************************************
    *                                     *
    *          BEM-VINDO AO JOGO          *
    *                                     *
    ***************************************
    * 1. Iniciar Jogo                     *
    * 2. Créditos                         *
    * 3. Sair do jogo                     *
    ***************************************
    """
    print(menu)

def main():
    while True:
        mostrar_menu()
        escolha = input("DIGITE A OPÇÃO DESEJADA: ").strip()
        if escolha == '1':
            jogo()
        elif escolha == '2':
            print("Desenvolvido por: ****LUCAS AMERICO DA SILVA****")
        elif escolha == '3':
            print("Obrigado por jogar! Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()