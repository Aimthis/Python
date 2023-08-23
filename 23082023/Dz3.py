k = input("Введите слово: ")
dictionary = {1:'AEIOULNSTRАВЕИНОРСТ',
              2:'DGДКЛМПУ',
              3:'BCMPБГЁЬЯ',
              4:'FHVWYЙЫ',
              5:'KЖЗХЦЧ',
              8:'JXШЭЮ',
              10:'QZФЩЪ'
}
summa = 0
for i in k.upper():
    for key, v in dictionary.items():
        if i in v:
            summa += key
print(summa)