# Parte Teórica - Construindo um Projeto Ágil no GitHub

## 1. Descrição do projeto e escopo inicial
Desenvolver um sistema simples de gerenciamento de tarefas (Task Manager) que permita:
- Criar, listar, atualizar e excluir tarefas;
- Priorizar tarefas (low, medium, high);
- Acompanhar status (todo, in-progress, done).

**Escopo Inicial:** CRUD de tarefas, API REST, testes automatizados e pipeline CI.

## 2. Metodologia Ágil utilizada
Foi adotado um **hybrid Kanban-Scrum**: quadro Kanban para o fluxo diário e sprints semanais curtos para entregas incrementais.

## 3. Importância da modelagem
Modelagem ajuda a mapear requisitos e identificar entidades essenciais (ex.: Task). Diagramas simplificam comunicação entre stakeholders.

## 4. Diagramas UML (representação textual / PlantUML)
### Diagrama de Casos de Uso (PlantUML)
```
@startuml
actor User
rectangle "Task Manager" {
  User --> (Create Task)
  User --> (List Tasks)
  User --> (Update Task)
  User --> (Delete Task)
}
@enduml
```

### Diagrama de Classes (simplificado)
```
+----------------+
|     Task       |
+----------------+
| - id: int      |
| - title: str   |
| - description: str |
| - status: str  |
| - priority: str|
+----------------+
| + create()     |
| + update()     |
| + delete()     |
+----------------+
```

## 5. Justificativa da mudança de escopo
Mudança: inclusão do campo `priority` e ordenação por prioridade.
Justificativa: startup de logística precisa priorizar entregas críticas. Impacto: pequenas alterações no modelo e na API; criação de novo cartão no Kanban.

## 6. Testes automatizados utilizados
Foram criados testes unitários básicos com pytest cobrindo criação, leitura, atualização e exclusão de tarefas.

## 7. Prints comentados do GitHub (instruções para obter)
- Vá até aba Projects → crie quadro Kanban com colunas To Do / In Progress / Done e crie 10 cards.
- Tire prints das ações: commits, card movido, workflow passando.
- Cole os prints na pasta /docs e faça comentários no Word final.

---

## Anotações do aluno (exemplo, aleatórias e realistas)
- "21/11: Não esquecer de explicar no pitch sobre o workflow do Actions."
- "Obs: testar o app com Postman antes de gravar o vídeo."
- "Dica pessoal: ao criar o repositório, marcar como público e criar a aba Projects manualmente."
