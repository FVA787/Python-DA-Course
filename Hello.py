import re
text = '''Разработка языка Python была начата в конце 1980-х годов в Голландии'''
res = re.search('\w+', text)
print (res)