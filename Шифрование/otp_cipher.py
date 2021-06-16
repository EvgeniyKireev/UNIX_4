word = input("Введите слово, которое хотите зашифровать: ")
key = input("Введите ключ шифрования: ")

"""
словарь с кодами зашифровки
"""


def dicOfValue():
    d = {}
    value = 0
    for i in range(0, 127):
        d[value] = chr(i)  # chr - возвращает символ по его числовому значению
        value += 1
    return d


"""
функция заполнения списка с кодами
для каждого символа слова
"""


def encoding(text):
    listOfCode = []  # список закодированных символов слова, которое кодируем
    dic = dicOfValue()

    for w in range(len(text)):
        for value in dic:
            if text[w] == dic[value]:
                listOfCode.append(value)
    return listOfCode


"""
функция группирования(сопоставления) символов слова со символами ключа
кол-во значений словаря == кол-во символов в закодированном слове
"""


def group(value, key):
    len_key = len(key)
    dic = {}
    key_value = 0
    full = 0

    for i in value:
        dic[full] = [i, key[key_value]]
        full += 1
        key_value += 1
        if key_value >= len_key:
            key_value = 0
    return dic


"""
полное шифрование. 
символ шифровки = остаток от деления суммы значений на 127
заменяю изначальный сивол на закодированный
"""


def encode(value, key):
    dic = group(value, key)
    print('Полный шифр : ', dic)
    lis = []

    for v in dic:
        cipher = (dic[v][0] + dic[v][1]) % 127
        lis.append(cipher)
    return lis


"""
группировка для декодирования (такая же, как group(), только в обратном порядке)
"""


def decodeGroup(list_in):
    list_code = []
    d = dicOfValue()

    for i in range(len(list_in)):
        for value in d:
            if list_in[i] == value:
                list_code.append(d[value])
    return list_code


"""
функция дешифрования
сложить зашифрованное значение с 127 и отнять элемент значения ключа

"""


def decode(value, key):
    dic = group(value, key)
    print('Дешифровка =', dic)
    lis = []

    for v in dic:
        decipher = (dic[v][0] + 127 - dic[v][1])
        lis.append(decipher)
    return lis


print("группировка", group(word, key))
print('Шифр=', ''.join(decodeGroup(encode(encoding(word), encoding(key)))))

decoded_word = decode(encode(encoding(word), encoding(key)), encoding(key))
decodeList = decodeGroup(decoded_word)
print('Декодировка=', decoded_word)
print('Декодированное слово=', ''.join(decodeList))
