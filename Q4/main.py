'''
4. Crie um programa em Python utilizando orientação a objetos
para gerenciar uma lista de produtos de um carrinho de
compras. Implemente uma classe chamada Produto, com
atributos privados (__nome, __preco e __quantidade) e
métodos públicos para acessar e modificar esses valores de
forma segura (getters e setters). Em seguida, implemente uma
classe CarrinhoDeCompras, que mantém uma lista de objetos
Produto e possui métodos para adicionar um produto ao
carrinho, remover um produto pelo nome, calcular o valor total
da compra e listar os produtos com suas quantidades e
preços individuais. O programa principal deve permitir que o
usuário adicione e remova produtos, visualize o conteúdo do
carrinho e o total da compra. Utilize encapsulamento para
proteger os dados dos produtos e boas práticas de
organização orientada a objetos.
'''
from functools import reduce

class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int) -> None:
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
        self.validate()
    
    def validate(self):
        #erros = ""
        if self.__preco <= 0:
            #erros += "Preço não pode ser negativo.\n"
            #erros.append(ValueError("Preço não pode ser negativo."))
            raise ValueError("Preço não pode ser negativo.")
        if self.__quantidade <= 0:
            #erros += "A quantidade não pode ser negativa\n"
            #erros.append(ValueError("Preço não pode ser negativo."))
            raise ValueError("A quantidade não pode ser negativa")
        #if erros:
        #    raise ValueError(erros)

    def get(self, attr: str) -> None:
        cls_name = self.__class__.__name__
        return self.__getattribute__(f"_{cls_name}__{attr}")

    def set(self, attr: str, value: any) -> None:
        self.validate()
        cls_name = self.__class__.__name__
        return self.__setattr__(f"_{cls_name}__{attr}", value)
    
class CarrinhoDeCompras():
    def __init__(self) -> None:
        self.__produtos: list[Produto] = []

    def get(self, attr: str) -> any:
        cls_name = self.__class__.__name__
        return self.__getattribute__(f"_{cls_name}__{attr}")

    def set(self, attr: str, value: any) -> None:
        cls_name = self.__class__.__name__
        return self.__setattr__(f"_{cls_name}__{attr}", value)
    
    def adicionar(self, produtos: list[Produto]) -> None:
        for produto in produtos:
            self.__produtos.append(produto)

    def remover(self, produtos: list[Produto]) -> None:
        for produto in produtos:
            self.__produtos.remove(produto)

    def listar(self) -> None:
        if not self.__produtos:
            print("Nenhum item no carrinho!")
            return
        maior_string = reduce(
            lambda x, p: x if x > len(p.get("nome")) else len(p.get("nome")),
            self.__produtos, 0)
        print("Produtos no carinho:")
        for p in self.__produtos:
            whitespace = " " * (maior_string - len(p.get("nome")))
            print(f"({p.get('quantidade')}) {p.get('nome')}{whitespace} - R${p.get('preco')}")

    def calcular_valor_total(self) -> float:
        return reduce(lambda x, p: x + p.get("preco"), self.__produtos, 0)

# Interface
def exibir_menu(options: dict[str, tuple[str, function]]):
    for key, value in options.items():
        print(f"[{key}] {value[0]}")

def mostrar_carrinho():
    carrinho.listar()
    pass

def adicionar_produtos():
    produtos = []
    while True:
        print("Adicionar produtos ao carrinho:")
        produto = Produto("", 0.0, 0)

        #for _, in range(3):
        #    try:
        
        try:
            nome = input("Nome: ")
            produto.set('nome', nome)


        try:
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            #produto = Produto(nome, preco, quantidade)
        except ValueError as e:
            print(f"{e}\nTente novamente.\n")
            continue
        else:
            produtos.append(produto)
        continuar = input("Adicionar mais um produto ao carrinho?\n[1] Sim\n[2] Não")
        if continuar == "1":
            continue
        else: break

    carrinho.adicionar(produtos)

def remover_produtos():
    pass

if __name__ == "__main__":
    
    p2 = Produto("Teste", 20.0, 1)

    carrinho = CarrinhoDeCompras()

    menu = {
        "1": ("Mostrar carrinho", carrinho.listar),
        "2": ("Adicionar produtos", adicionar_produtos),
        "3": ("Remover produtos", remover_produtos),
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