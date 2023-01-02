# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

text = input("Введите текст для сжатия: ")

def zip_text(text):
    count = 1
    res = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        res = res + str(count) + text[-1]
    return res

def unzip_text(text):
    Num = ''
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            Num += text[i]
        else:
            res = res + text[i] * int(Num)
            Num = ''
    return res


print(f"Сжатый текст: {zip_text(text)}")
print(f"Текст восстановленный: {unzip_text(zip_text(text))}")
