#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Создаем словарь numbers, который содержит числительные на русском языке и их числовые значения
def calc(expression):
    numbers = {
        "ноль": 0,
        "один": 1,
        "два": 2,
        "три": 3,
        "четыре": 4,
        "пять": 5,
        "шесть": 6,
        "семь": 7,
        "восемь": 8,
        "девять": 9,
        "десять": 10,
        "одиннадцать": 11,
        "двенадцать": 12,
        "тринадцать": 13,
        "четырнадцать": 14,
        "пятнадцать": 15,
        "шестнадцать": 16,
        "семнадцать": 17,
        "восемнадцать": 18,
        "девятнадцать": 19,
        "двадцать": 20,
        "тридцать": 30,
        "сорок": 40,
        "пятьдесят": 50,
        "шестьдесят": 60,
        "семьдесят": 70,
        "восемьдесят": 80,
        "девяносто": 90,
    }
#строка expression разбивается на слова, и создается список words
    words = expression.split()
    operand = ['плюс','минус','умножить','разделить']
#проверяется длина списка words
    if len(words)==3:
        num1 = numbers[words[0]]
        num2 = numbers[words[2]]
        oper = words[1]
    elif len(words)==4:
        if words[1] in operand:
            num1 = numbers[words[0]]
            num2 = numbers[words[2]]+numbers[words[3]]
            oper = words[1]
        else:
            num1 = numbers[words[0]]+numbers[words[1]]
            num2 = numbers[words[3]]
            oper = words[2]
    else:
        num1 = numbers[words[0]] + numbers[words[1]]
        num2 = numbers[words[3]] + numbers[words[4]]
        oper = words[2]
    if oper == 'плюс':
        result = num1 + num2
    elif oper == 'минус':
        result = num1 - num2
    elif oper == 'умножить':
        result = num1 * num2
    elif oper == 'разделить':
        result = num1 / num2

    res = ''
#функция перебирает числительные и их числовые значения в обратном порядке.
#если значение number совпадает с результатом вычислений, то возвращается соответствующее слово word.
#если значение number равно результату за вычетом остатка от деления на 10, то слово word добавляется в строку res с пробелом.
#если значение number равно остатку от деления на 10, то слово word добавляется к строке res.
    for word, number in numbers.items().__reversed__():
        if number == result:
            return word
        elif number == result - (result % 10):
            res += word + ' '
        elif number == result % 10:
            res += word
    return res
x = input()
print(calc(x))


# In[ ]:




