name = input("Какой ответ на главный вопрос жизни, вселенной и всего такого? ")
name = name.lower()
match name:
    case "42" | "сорок два":
        print("Да")
    case _:
        print("Нет")
