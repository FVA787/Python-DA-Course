import re
text = '''Разработкааааааа   %    а языкааааа Python была начата в конце 1980-х % годов в Голландии'''
res = re.search('\W+[ ]{1,10}', text)
print (res)