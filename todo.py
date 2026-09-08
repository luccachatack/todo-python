tarefas = []

print("Lista de tarefas")
print("Digite 'sair' para encerrar.")

while True:
    tarefa = input("Nova tarefa: ").strip()

    if tarefa.lower() == "sair":
        break

    if not tarefa:
        print("A tarefa não pode ficar vazia.")
        continue

    tarefas.append(tarefa)

print("\nSuas tarefas:")

for numero, tarefa in enumerate(tarefas, start=1):
    print(f"{numero}. {tarefa}")
    