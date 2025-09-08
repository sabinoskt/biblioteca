class Livro:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def __str__(self):
        return f"Título: {self.title} Autor: {self.author} Ano: {self.year}"

    def emprestado(self):
        if self.available:
            self.available = False
            return True
        return False

    def devolvido(self):
        self.available = True


class Pessoa:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self):
        return f"Nome: {self.name}"
    

class Cliente(Pessoa):
    def __init__(self, name):
        super().__init__(name)
    
        self.lista_de_cliente = []
        self.lista_de_livros = []
        self.lista_de_cliente.append(self.name)


    def emprestar(self, livro: Livro):
        if livro.emprestado():
            self.lista_de_livros.append(livro)
            return True
        return False

    def devolver(self, livro: Livro):
        if livro in self.lista_de_livros:
            livro.devolvido()
            self.lista_de_livros.remove(livro)



# Listar livros
def mostrar_listar_livros():
    # Cria lista de objetos Livro
    lista_livros = [
    Livro("1984", "George Orwell", 1949),
    Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967),
    Livro("O Cortiço", "Aluísio Azevedo", 1890),
    Livro("Sapiens", "Yuval Noah Harari", 2011),
    Livro("Dom Casmurro", "Machado de Assis", 1899),
]
    print(20 * '=' + " LIVROS " + 20 * '=')
    for i, chave in enumerate(lista_livros):
        print(f"{i} - {chave}")
    print(26 * '=' + 3 * '#' + 20 * '=' + '\n')

    return lista_livros

# input/output
def io(prompt: str = None, minino: int = None, maximo: int = None) -> str:
    entrada = input(f'\n{prompt}: ')
    return entrada


# cadastrar cliente
def cadastrar_cliente():
    customer = io(prompt='Nome do cliente')
    cliente = Cliente(customer)
    return cliente



# Pegar emprestar livro
def emprestar_livro():
    print('Quais livros?')
    dados = mostrar_listar_livros()
    entrada = io('Escola a opção')
    cliente = cadastrar_cliente()
    cliente.emprestar(dados[int(entrada)])


# Devolver livro que foi emprestado
...




def opcoes_escolhida(opcao):
    match opcao:
        case 1:
            mostrar_listar_livros()
        case 2:
            cadastrar_cliente()
        case 3:
            emprestar_livro()
        case _:
            print("Não encontrado!!!")

# Menu
def menu():
    while True:
        opcoes = [
            '[1] - Listar livros',
            '[2] - Cadastrar cliente',
            '[3] - Emprestar livro',
            '[4] - Devolver livro',
            '[5] - Sair'
        ]

        for i in opcoes:
            print(i)

        entrada = int(io(prompt='Escolha a opção'))
        if entrada == 5:
            break
        opcoes_escolhida(entrada)


if __name__ == '__main__':
    menu()
