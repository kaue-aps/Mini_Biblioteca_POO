from src.mini_biblioteca_poo.livros import Livro
from src.mini_biblioteca_poo.usuarios import Usuario
from src.mini_biblioteca_poo.emprestimos import Emprestimo

# Testando instanciação básica

def test_instanciar_livro():
    l1 = Livro("Lobisomem", "desconhecido", 123)
    assert isinstance(l1, Livro)


def test_instanciar_usuario():
    u1 = Usuario("Maria", 2)
    assert isinstance(u1, Usuario)


def test_instanciar_emprestimo():
    l1 = Livro("Lobisomem", "desconhecido", 123)
    u1 = Usuario("Maria", 2)
    e1 = Emprestimo(l1, u1)
    assert isinstance(e1, Emprestimo)