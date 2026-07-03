'''
1. Elabore um programa em Python orientado a objetos que leia
um número n (o número de termos de uma progressão
aritmética), a1 (o primeiro termo da progressão) e r (razão) e
escreva todos os termos dessa progressão, bem como a
soma dos elementos (Fórmulas para descobrir um termo da P.A.: an = a1 + r x (n – 1) e
S = n * (a1 + an) / 2).
'''

class ProgressaoAritmetica:
    def __init__(self, n: int, a1: float, r: float) -> None:
        self.n = n
        self.a1 = a1
        self.r = r

    def somar(self) -> float:
        # ultimo_t = primeiro_t + razão * (qnt_t - 1)
        ultimo_termo = self.a1 + self.r * (self.n - 1)
        return self.n * (self.a1 + ultimo_termo) / 2
    
    def gerar_termos(self) -> list[float]:
        termos = [self.a1]
        value = self.a1
        for _ in range(self.n - 1):
            value += self.r
            termos.append(value)
        return termos

    def listar(self) -> None:
        print(*self.gerar_termos(), sep=", ")

if __name__ == "__main__":
    while True:
        print("\n\nPreencha as informações para calcular uma Progressão Aritmética (P.A)\n")

        try:
            n = int(input("\nQuantidade de termos (n): "))
            a1 = float(input("\nPrimeiro termo (a1): "))
            r = float(input("\nDiferença entre os termos (r) "))
        except ValueError:
            print("Somente valores numéricos são aceitos! Tente novamente\n")
            continue

        pa = ProgressaoAritmetica(n=n, a1=a1, r=r)

        while True:
            print("\n")
            print("[1] Listar termos \n[2] Somar termos \n[3] Voltar")
            escolha = input("Escolha: ")

            if not escolha.isdigit(): 
                print("Digite o número da opção desejada")
                continue

            match escolha:
                case "1":
                    print("\nOs termos são:")
                    pa.listar()
                case "2":
                    print("\nA soma dos termos é: ", pa.somar())
                case "3":
                    break