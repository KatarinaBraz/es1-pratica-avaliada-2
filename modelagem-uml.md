## Diagrama de Classes

```mermaid
classDiagram
class Livro {
  +isbn
  +titulo
  +autor
  +categoria
  +buscar()
  +atualizar()
}

class Leitor {
  +cpf
  +nome
  +email
  +cadastrar()
  +consultar()
}

class Emprestimo {
  +id
  +data
  +registrar()
  +finalizar()
}

Livro "1" --> "*" Emprestimo
Leitor "1" --> "*" EmprestimosequenceDiagram
actor Bibliotecario
Bibliotecario ->> Sistema: solicitar empréstimo
Sistema ->> Livro: verificar disponibilidade
Sistema ->> Leitor: validar
Sistema ->> Emprestimo: registrar
Sistema -->> Bibliotecario: confirmaçãoflowchart TD
A[Devolver livro] --> B{Atraso?}
B -- Sim --> C[Calcular multa]
B -- Não --> D[Sem multa]
C --> E{Reserva?}
D --> E
E -- Sim --> F[Notificar leitor]
E -- Não --> G[Fim]
F --> G