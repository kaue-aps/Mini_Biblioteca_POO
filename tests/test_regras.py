from src.mini_biblioteca_poo.livros import Livro
from src.mini_biblioteca_poo.usuarios import Usuario
from src.mini_biblioteca_poo.emprestimos import Emprestimo
import pytest

# Testando as regras de negócio

def test_emprestar_livro_indisponivel():
    l1 = Livro("Lobisomem", "desconhecido", 123)
    u1 = Usuario("Maria", 2)
    e1 = Emprestimo(l1, u1)

    assert l1.disponivel == False

    with pytest.raises(ValueError):
        e2 = Emprestimo(l1, u1)


def test_devolver_livro():
    l1 = Livro("Lobisomem", "desconhecido", 123)
    u1 = Usuario("Maria", 2)
    e1 = Emprestimo(l1, u1)

    e1.devolver()

    assert l1.disponivel == True
    assert e1.ativo == False