class Hero:
    def __init__(self, nome, raca, cabelo, classe, porte):
        self.nome = nome
        self.raca = raca
        self.cabelo = cabelo
        self.classe = classe
        self.porte = porte
        self.vida = 100
        self.stamina = 100
        self.attack = 10
        self.anoes=100

    def mostrar_detalhes(self):
        print(f"Nome: {self.nome}")
        print(f"Raça: {self.raca}")
        print(f"Cabelo: {self.cabelo}")
        print(f"Classe: {self.classe}")
        print(f"Porte: {self.porte}")
        
    def atacar(self):
        print("Atacando o oponente")
        self.attack -= 1
        print(f"Você perdeu 1 ponto de ataque, agora seu saldo de pontos de ataque é: {self.attack}")

    def andar(self):
        print("Você deu 10 passos")
        self.stamina -= 10
        print(f"Você perdeu 10 pontos de stamina, agora seu saldo de pontos de stamina é: {self.stamina}")

    def sofrer_dano(self):
        print("Você levou 10 pontos de dano")
        self.vida -= 10
        print(f"Você perdeu 10 pontos de vida, agora seu saldo de pontos de vida é: {self.vida}")
    def apostar(self):
        print("Você apostou 10 anoes da sua coleção")
        self.anoes - 10
        print(f"Você perdeu 10 anoes, agora seu saldo de anoes é:")
        self.anoes
    def ganhar_aposta(self):
        print("PARABENS VOCE GANHOU A RINHA DE ANOES!!!!!")
        print("COMO RECOMPENSA VOCE GANHOU 10 ANOES!!!!")
        self.anoes + 10
        print("AGORA SEU SALDO DE ANOES É DE: ",self.anoes)
    def perder_aposta(self):
        print("VOCE PERDEU A RINHA DE ANOES!!!!!")
        print("COMO RECOMPENSA VOCE PERDEU 10 ANOES!!!!")
        self.anoes - 10
        print("AGORA SEU SALDO DE ANOES É DE: ",self.anoes)
        