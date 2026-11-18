from src.mini_biblioteca_poo.livros import Livro
from src.mini_biblioteca_poo.usuarios import Usuario

class Emprestimo:

    def __init__(self, livro: Livro, usuario: Usuario):
        # Só empresta livro disponível
        if livro.disponivel == True:
            self.livro = livro
            self.livro.disponivel = False
        else:
            raise ValueError
        
        self.usuario = usuario
        self.ativo = True


    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True


    # Só para facilitar a verificação do estado na main
    def __str__(self):
        return f"Livro: {self.livro.titulo}\nUsuário: {self.usuario.nome}"

