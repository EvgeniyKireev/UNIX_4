key = "01234567"
init_vector = "MIV00099"

input_text = input("Введите текст, который хотите закодировать:")

"""
Конвертация полученной строки в биты
isinstance()  True, если указанный объект является экземпляром указанного класса
"""


def сonversion(s):
    arraylist = list()
    for value in s:

        if isinstance(value, int):  # если число, то  сразу в биты
            bits = bin(value)[2:]  # bin - преобразование числа в строку
        else:
            bits = bin(ord(value))[2:]  # ord - числовое представление символа

        while len(bits) < 8:
            bits = "0" + bits

        for bit in bits:
            arraylist.append(int(bit))

    return arraylist


"""
конвертация битов в строку
"""


def convert_to_str(arraylist):
    result = ""

    for i in range(0, len(arraylist), 8):
        byte = arraylist[i:i + 8]  # беру по 8
        s = ""

        for b in byte:
            s += str(b)
        result = result + chr(int(s, 2))  # chr - возвращает символ по его числовому значению

    return result


"""
Исключительное или
"""

def xor(a, b):
    return [i ^ j for i, j in zip(a, b)]


"""
Зашифровка полученного слова 
"""


def encrypt(input_text, init_vector, key):
    result = list()
    blocks = list()
    for i in range(0, len(input_text), 8):
        line = input_text[i:i + 8]
        while len(line) < 8:
            line += "\x00"
        blocks.append(line)

    newIV = сonversion(init_vector)
    for j in blocks:
        if len(j) == 8:
            temp = xor(сonversion(j), newIV)  # сумма по модулю 2 между блоком и IV( вектор инициализации)
            if len(сonversion(key)) == len(temp):
                newIV = xor(сonversion(key), temp)  # сумма по модулю 2 между блоком и ключем
            result.append(convert_to_str(newIV))

    return result


"""
Дешифровка 
"""

def decode(cipher, init_vector, key):
    result = list()
    newIV = сonversion(init_vector)

    for val in cipher:
        block = xor(сonversion(key), сonversion(val))  # сумма по модулю 2 между ключом и зашифрованным блоком
        temp = xor(newIV, block)  # сумма по модулю 2 между IV и блоком
        newIV = сonversion(val)
        result.append(convert_to_str(temp).replace("\x00", ""))

    return result


print("Закодированный текст: ", encrypt(input_text, init_vector, key))
print("Раскодированный текст: ", "".join(decode(encrypt(input_text, init_vector, key), init_vector, key)))
