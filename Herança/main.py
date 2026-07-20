'''Crie um programa em Python utilizando herança para
representar um sistema simples de funcionários. Implemente
uma classe base chamada Funcionario, com os atributos nome
(String) e salarioBase (double), além de um método
calcularSalario() que retorna o salário base e um método
exibirDados() que imprime o nome e o salário. Em seguida, crie
uma subclasse chamada FuncionarioComissionado, que herda
de Funcionario e possui o atributo adicional comissao (double).
Essa subclasse deve sobrescrever o método calcularSalario()
para retornar a soma do salário base com a comissão, e
também sobrescrever exibirDados() para incluir a comissão nas
informações exibidas. Por fim, instancie um objeto de cada
classe e utilize os métodos definidos para mostrar os dados dos
funcionários.'''

class Funcionario:
    def __init__(self, nome: str, salario_base: float) -> None:
        self.nome = nome
        self.salario_base = salario_base
    
    def calcular_salario(self) -> float:
        return self.salario_base

    def exibir_dados(self) -> None:
        print(f"Nome: {self.nome} | Salário base: {self.salario_base}", end="")

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome: str, salario_base: float, comissao: float) -> None:
        super().__init__(nome, salario_base)
        self.comissao = comissao

    def calcular_salario(self) -> float:
        return super().calcular_salario() + self.comissao

    def exibir_dados(self) -> None:
        super().exibir_dados()
        print(f" | Salário com comissão: {self.calcular_salario()}")

vitor = FuncionarioComissionado("Vitor", 4500, 500)
vitor.exibir_dados()