from src.mini_biblioteca_poo.livros import Livro
from src.mini_biblioteca_poo.usuarios import Usuario
from src.mini_biblioteca_poo.emprestimos import Emprestimo

# Cria usuário
u1 = Usuario("João", 1)

# Cria livro
l1 = Livro("Frankenstein", "Mary Shelley", 123)

# Faz o empréstimo
e1 = Emprestimo(l1, u1)

# Verificação de estado 1
print(l1.disponivel)
print(e1.ativo)

# Verificação de estado 2
e1.devolver()
print(l1.disponivel)
print(e1.ativo)

