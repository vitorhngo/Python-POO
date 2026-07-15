'''
Desenvolva uma classe Departamento com nome e um vetor
de objetos Funcionario, onde cada funcionário tem nome e
salário, permitindo que funcionários existam
independentemente do departamento para que possam ser
adicionados ou removidos livremente (agregação).
Implemente métodos no Departamento para adicionar
funcionários, calcular a média salarial e listar todos os
funcionários. Crie um programa com menu interativo no
console que permita criar departamentos, criar funcionários,
adicionar funcionários a departamentos, listar funcionários e
mostrar a média salarial, além de permitir sair do programa.
'''
from functools import reduce

class Departamento:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.funcionarios: list[Funcionario] = []

    def add_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)
    
    def calc_media_salarial(self) -> float:
        # Somar todos o salário de todos os funcionários depois dividir pela quantidade.
        salarios = reduce(lambda x, f: x + f.salario, self.funcionarios, 0)
        return salarios / len(self.funcionarios)

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f"{funcionario.nome} : R${funcionario.salario}")

class Funcionario:
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

# Interface
def exibir_menu(options: dict[str, tuple[str, function]]) -> None:
    for key, value in options.items():
        print(f"[{key}] {value[0]}")

def criar_departamento():
    print("\nCriar departamento\n")
    nome = input("Nome: ")
    departamentos[nome] = Departamento(nome)

def cadastrar_funcionario():
    print("\nCriar departamento\n")
    nome = input("Nome: ")
    salario = float(input("Salário: "))
    id = str(len(funcionarios) + 1)
    funcionarios[id] = Funcionario(nome, salario)
    
def adicionar_func_dep():
    print("\nAdicionar funcionário a departamentoS\n")
    
    nome = input("Departamento: ")
    departamento = departamentos[nome]

    exibir_funcionarios()
    id = input("Funcionário (ID): ")
    funcionario = funcionarios[id]
    
    departamento.add_funcionario(funcionario)

def exibir_funcionarios():
    print("\nFuncionários\n")
    for _, funcionario in funcionarios.items():
        print(funcionario.nome)

def exibir_media_salarial():
    print("\nMédia salarial\n")
    nome = input("Departamento: ")
    departamento = departamentos[nome]
    print(f"Média salarial: R${departamento.calc_media_salarial()}")
    
if __name__ == "__main__":
    departamentos: dict[str, Departamento] = {}
    funcionarios: dict[str, Funcionario] = {}
    menu = {
        "1": ("Criar departamento", criar_departamento),
        "2": ("Cadastrar funcionário", cadastrar_funcionario),
        "3": ("Adicionar funcionário a departamentoS", adicionar_func_dep),
        "4": ("Exibir funcionários", exibir_funcionarios),
        "5": ("Exibir média salarial", exibir_media_salarial),
        "0": ("Sair", quit)
    }

    while True:
        print()
        exibir_menu(menu)
        escolha = input("Escolha: ")
        try:
            menu[escolha][1]()
        except KeyError as e:
            print("Escolha uma opção válida.")