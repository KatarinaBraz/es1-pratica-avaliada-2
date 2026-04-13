## Requisitos Funcionais

| ID | Descrição | Prioridade |
|----|-----------|------------|
| RF01 | Cadastrar livros | Alta |
| RF02 | Consultar livros | Alta |
| RF03 | Cadastrar leitores | Alta |
| RF04 | Registrar empréstimo | Alta |
| RF05 | Registrar devolução | Alta |
| RF06 | Renovar empréstimo | Média |
| RF07 | Criar reserva | Alta |
| RF08 | Notificar leitor por email | Média |
| RF09 | Calcular multa | Alta |
| RF10 | Gerenciar exemplares disponíveis | Alta |

## Requisitos Não-Funcionais

| ID | Categoria | Descrição | Métrica |
|----|-----------|-----------|---------|
| RNF01 | Desempenho | Sistema deve responder rápido | < 2s |
| RNF02 | Segurança | Dados protegidos | criptografia |
| RNF03 | Usabilidade | Interface simples | fácil uso |
| RNF04 | Disponibilidade | Sistema disponível | 99% uptime |
| RNF05 | Escalabilidade | Suportar crescimento | +1000 usuários |

## Regras de Negócio

| ID | Descrição |
|----|-----------|
| RN01 | Empréstimo dura 14 dias |
| RN02 | Multa de R$2/dia |
| RN03 | Só emprestar se houver exemplar |
| RN04 | Reserva se indisponível |
| RN05 | Renovação só sem reserva |

## User Stories

Como bibliotecário  
Quero cadastrar livros  
Para organizar o acervo  

Critérios:
- [ ] Livro salvo
- [ ] Dados válidos

Story Points: 3

Como leitor  
Quero me cadastrar  
Para acessar o sistema  

Critérios:
- [ ] Cadastro salvo

Story Points: 2

Como bibliotecário  
Quero registrar empréstimo  
Para controlar livros  

Critérios:
- [ ] Empréstimo criado

Story Points: 5

Como leitor  
Quero reservar livro  
Para garantir acesso  

Critérios:
- [ ] Reserva criada

Story Points: 3

Como sistema  
Quero calcular multa  
Para penalizar atraso  

Critérios:
- [ ] Valor correto

Story Points: 3

Como sistema  
Quero notificar usuário  
Para avisar disponibilidade  

Critérios:
- [ ] Email enviado

Story Points: 2