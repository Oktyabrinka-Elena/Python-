# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст:\n")

def del_abv(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = del_abv(text)
print(text)