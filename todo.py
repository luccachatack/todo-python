tarefas = []

print("Lista de tarefas")
print("Digite 'sair' para encerrar.")

while True:
    tarefa = input("Nova tarefa: ")

    if tarefa.lower() == "sair":
        break

    tarefas.append(tarefa)

print("\nSuas tarefas:")

for numero, tarefa in enumerate(tarefas, start=1):
    print(f"{numero}. {tarefa}")