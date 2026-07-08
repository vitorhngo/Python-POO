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
    
    def get(self, attr: str) -> None:
        cls_name = self.__class__.__name__
        return self.__getattribute__(f"_{cls_name}__{attr}")

    def set(self, attr: str, value: any) -> None:
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


if __name__ == "__main__":
    p = Produto("Algodão", 10.0, 2)
    p2 = Produto("Teste", 20.0, 1)

    carrinho = CarrinhoDeCompras()
    carrinho.adicionar([p, p2])
    total = carrinho.calcular_valor_total()
    print(total)
    carrinho.listar()