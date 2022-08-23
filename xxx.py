import csv
import re
with open('test_data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
         dialog_id = row[0]
         line = row[1]
         position = row[2]
         message = row[3]
         if position == 'manager':
             if re.search(r'\bздравствуйте\b', message) or re.search(r'\bдобрый день\b', message)\
                     or re.search(r'\Добрый\b', message):
                 print(f'a. {message}')
             if re.search(r'\bМеня зовут\b', message) or re.search(r'\bменя\b', message):
                 print(f'b. {message}')
                 name_1 = 'ангелина'
                 name_2 = 'максим'
                 company_name_1 = 'диджитал'
                 company_name_2 = 'китобизнес'
                 pattern = re.compile(r'\w+')
                 print(f'c. {pattern.search(name_1).group()}')
                 print(f'c.{pattern.search(name_2).group()}')
                 print(f'd. {pattern.search(company_name_1).group()}')
                 print(f'd. {pattern.search(company_name_2).group()}')
             if re.search(r'\bдо свидания\b', message) or re.search(r'\bДо свидания\b', message)\
                     or re.search(r'\bвсего доброго\b', message):
                 check = True
                 print(f'e. {message}')


