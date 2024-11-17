strd = input(str("введтье строку для поиска "))
filename = "text.txt"
count = 0
seartch = []
# Чтение файла построчно
with open(filename, "r",encoding="utf-8") as file:
    for line in file:
        if strd in line: # Проверка, содержится ли искомая подстрока в строке
          seartch.append(line.strip)
          count +=1
    if count == 0:
        print("Подстрока не найдена")
    else:
        print("Найденные строки (отсортированные):")
        print("\n".join(sorted(seartch))) 
