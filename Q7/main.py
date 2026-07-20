'''
Implemente uma classe Casa que contenha vários objetos do
tipo Comodo, sendo que cada cômodo possui nome (ex: sala,
cozinha, banheiro) e área. Os cômodos devem ser
implementados de forma que só existam se a casa existir
(relação de composição), e não devem ser acessados ou
manipulados diretamente de fora. Implemente um método na
casa para calcular a área total, somando as áreas de todos os
cômodos. Desenvolva um programa com menu interativo no
console que permita criar uma casa, adicionar cômodos à
casa, listar os cômodos da casa, calcular e exibir a área total
da casa e encerrar o programa.
'''
class Casa:
    class __Comodo:
        def __init__(self, nome: str, area: float) -> None:
            self.__nome = nome
            self.__area = area

        def get_nome(self):
            return self.__nome

        def get_area(self):
            return self.__area
        
        def set_nome(self, nome: str):
            self.__nome = nome
        
        def set_area(self, area: float):
            self.__area = area

    def __init__(self) -> None:
        self.__comodos = []

    def adcionar_comodo(self, nome: str, area: float):
        comodo = self.__Comodo(nome, area)
        self.__comodos.append(comodo)

    def listar_comodos(self):
        if not self.__comodos:
            print("\nNenhum cômodo foi adicionado ainda")
        else:
            for comodo in self.__comodos:
                print(f"- {comodo.get_nome()} ({comodo.get_area()}m²)")
    
    def calcular_area_total(self):
        total = 0
        for comodo in self.__comodos:
            total += comodo.get_area()

# Interface
def exibir_menu(options: dict[str, list]) -> None:
    for key, value in options.items():
        if value[2] == False: continue
        print(f"[{key}] {value[0]}")

def criar_casa():
    print("\nCriar casa\n")

    menu["2"][2] = True
    menu["3"][2] = True
    pass

if __name__ == "__main__":
    casas: list[Casa] = []
    menu = {
        "1": ["Criar casa", criar_casa, True],
        "2": ["Adicionar cômodo", criar_casa, False],
        "3": ["Listar cômodos", criar_casa, False],
        "0": ["Sair", quit, True]
    }

    while True:
        print()
        exibir_menu(menu)
        escolha = input("Escolha: ")
        try:
            menu[escolha][1]()
        except KeyError as e:
            print("Escolha uma opção válida.")