'''
2. Faça um programa em Python orientado a objetos que, a
partir de uma string digitada pelo usuário, imprima:
    ◦ O número de caracteres da string;
    ◦ A string com todas suas letras em maiúsculo;
    ◦ A string com todas suas letras em minúsculo;
    ◦ O número de vogais da string;
    ◦ Se a substring “IFB” aparece no texto (ignorando
    maiúsculas/minúsculas).
'''
class StringOperations:
    def __init__(self, subject: str) -> None:
        self.subject = subject

    def character_count(self) -> int: return len(self.subject) 
    
    def to_upper(self) -> str: return self.subject.upper() 
    
    def to_lower(self) -> str: return self.subject.lower()

    def has_substring(self, sub_string: str) -> bool:
        return sub_string.lower() in self.to_lower()

    def count_vowels(self) -> int:
        vowels = {"a", "á", "à", "ã", "â",
                  "e", "é", "ê",
                  "i", "í",
                  "o", "ó", "õ", "ô",
                  "u", "ú"}
        count = 0
        for i in self.to_lower():
            if i in vowels:
                count += 1
        return count
    
if __name__ == "__main__":
    resposta = StringOperations(subject=input("Digite uma frase: "))
    print("\nQuantidade de caracteres:",    resposta.character_count())
    print("Frase em letras maiúsculas:",    resposta.to_upper())
    print("Frase em letras minúsculas:",    resposta.to_lower())
    print("Quantidade de vogais:",          resposta.count_vowels())
    print("IFB está na frase:",             resposta.has_substring("IFB"))
    print()