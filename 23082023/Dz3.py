k = 'NOTEBOOK'
dictionary = {1:'AEIOULNSTR',
              2:'DG',
              3:'BCMP',
              4:'FHVWY',
              5:'K',
              8:'JX',
              10:'QZ'
            }
for i in k:
    for key, v in dictionary.items():
        if i in key:
            summ =+ v
print(v)