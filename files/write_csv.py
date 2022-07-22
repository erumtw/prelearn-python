# การเขียนไฟล์แบบ CSV ​(Comma-Separated Values) โดยใช้ module CSV

import csv

def write_csv():
    with open(r"data\write csv.txt", mode='w', encoding='utf8', newline='') as f:
        fw = csv.writer(f)
        # การเขีนนไฟล์ csv จะ writerows ต้องเป็น list or tuple
        fw.writerow(["americano", 30, 40, 55])
        fw.writerow(("latte", 35, 45, 60))

def write_csv2():
    menus = [
        [f'{"mocha":10}', 30, 40, 50],
        [f'{"latte":10}', 40, 50, 65],
        [f'{"espresso":10}', 50, 55, 70]
    ]
    
    with open(r'data\write csv2.txt', mode='w', encoding='utf8', newline='') as f:
        fw = csv.writer(f, delimiter='\t', quoting=csv.QUOTE_NONNUMERIC)
        fw.writerow(["menu", "s", "m", "l"])
        fw.writerows(menus)
        
write_csv()
write_csv2()