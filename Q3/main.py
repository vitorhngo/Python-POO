'''
3. Faça um programa em Python orientado a objetos que receba
uma frase dada pelo usuário e a criptografe. A criptografia
consistirá na troca das vogais da frase por um número
correspondente: A – 4, E – 3, I – 1, O – 0, U – 8.
'''

class Secret:
    def __init__(self, subject: str) -> None:
        self.subject = subject
        self.vowels = {
            "a": 4,
            "e": 3,
            "i": 1,
            "o": 0,
            "u": 8
        }
    
    def encrypt(self) -> str:
        temp_subject = ""
        for s in self.subject.lower():
            try:
                temp_subject += str(self.vowels[s])
            except KeyError:
                temp_subject += s
        self.subject = temp_subject
        return self.subject
    
    def decrypt(self) -> str:
        for s, c in self.vowels.items():
            self.subject = self.subject.replace(str(c), s)
        return self.subject

if __name__ == "__main__":
    segredo = Secret(input("Digite um texto: "))
    print("\nTexto criptografado:   ", segredo.encrypt())
    print("\nTexto descriptografado:", segredo.decrypt())