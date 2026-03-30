import re
ticket_number = input('введите шестизначный номер билета')
print(int(re.search("^(\d)(\d)(\d)(\d)(\d)(\d)$", ticket_number).group(4)))

first_3_figures = (int(re.search("^(\d)(\d)(\d)(\d)(\d)(\d)$", ticket_number).group(1)) + 
int(re.search("^(\d)(\d)(\d)(\d)(\d)(\d)$", ticket_number).group(2)) +
int(re.search("^(\d)(\d)(\d)(\d)(\d)(\d)$", ticket_number).group(3)))

last_3_figures = (int(re.search("^(\d)(\d)(\d)(\d)(\d)(\d)$", ticket_number).group(4)) + 
int(re.search("^(\d)(\d)(\d)(\d)(\d)(\d)$", ticket_number).group(5)) +
int(re.search("^(\d)(\d)(\d)(\d)(\d)(\d)$", ticket_number).group(6)))

if first_3_figures == last_3_figures:
    print("Счастливый билет")
else:
    print ("Несчастливый билет")