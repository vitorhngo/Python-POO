class Livro:
    def __init__(self, titulo, autor, id):
        self.__titulo = titulo
        self.__autor = autor
        self.__id = id
    
    def get(self, atr: str):
        cls_name = self.__class__.__name__
        return self.__getattribute__(f"_{cls_name}__{atr}")

    def set(self, atr: str, value: str):
        cls_name = self.__class__.__name__
        return self.__setattr__(f"_{cls_name}__{atr}", value)

class Usuario:
    def __init__(self, nome: str, matricula: int):
        self.__nome = nome
        self.__matricula = matricula
        self.__livros_emprestados = []

    # -- Auxiliar
    def get(self, atr: str) -> any:
        cls_name = self.__class__.__name__
        return self.__getattribute__(f"_{cls_name}__{atr}")
    
    def set(self, atr: str, value: str) -> None:
        cls_name = self.__class__.__name__
        return self.__setattr__(f"_{cls_name}__{atr}", value)

    # -- Consulta
    def emprestar_livro(self, livro: any) -> None:
        self.__livros_emprestados.append(livro)

    def devolver_livro(self, id_livro: int) -> None:
        for livro in self.__livros_emprestados:
            if livro.get("id") == id_livro:
                self.__livros_emprestados.remove(livro)
                print(f"\n{self.__nome} devolveu o livro '{livro.get("titulo")}'\n")
                return
        print(f"{self.__nome} não possui um livro com ID {id_livro}")
    
    def listar_livros_emprestados(self) -> None:
        if not self.__livros_emprestados:
            print(f"Nenhum livro emprestado.")
        else:
            a = self.__livros_emprestados
            print(*a, sep="\n")
            print("\nLivros emprestados:")
            for livro in self.__livros_emprestados:
                print(f"- {livro.get("titulo")} (id: {livro.get("id")})")
            print()



def main():
    # cadastrar livro
    # cadastrar usuário
    # emprestar livro
    # devolver livro
    # listar livros emprestados
    livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1)
    livro2 = Livro("Capitães da Areia", "Jorge Amado", 2)

    usuario = Usuario("Vitor", 1)

    usuario.emprestar_livro(livro1)
    usuario.emprestar_livro(livro2)

    usuario.listar_livros_emprestados()

    usuario.devolver_livro(1)

    usuario.listar_livros_emprestados()

if __name__ == "__main__":
    main()