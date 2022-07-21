# การอ่านไฟล์ CSV (Comma-Separated Values)
# เทคนิคการอ่านไฟล์ CSV แบบที่มี header column และไม่มี header column
import csv

def read_text():
    with open(r"D:\programming-learns\prelearn-python\data\rio2016.csv") as f:
        print(f.read())

def read_csv():
    with open(r"D:\programming-learns\prelearn-python\data\rio2016.csv") as f:
        data = csv.reader(f)
        print(data)
        for row in data:
            # print(row)
            print(f"{row[0]:20}: {row[1]:2} {row[2]:2} {row[3]:2}")
        
def read_csv_tab():
    with open(r"D:\programming-learns\prelearn-python\data\rio2016tab.txt") as f:
        data = csv.reader(f, delimiter="\t")
        for row in data:
            print(row)
            # print(f"{row[0]:20}: {row[1]:2} {row[2]:2} {row[3]:2}")
        
def read_csv_header():
    with open(r"D:\programming-learns\prelearn-python\data\rio2016_header_column.csv") as f:
        data = csv.DictReader(f, delimiter=',')
        print(data)
        print(data.fieldnames)
        for row in data:
            print(f"{row['country']} {row['gold']}")
            
        
# read_text()
# read_csv()
# print()
# read_csv_tab()
read_csv_header()