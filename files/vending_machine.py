# จำลองการบันทึกข้อมูลขายใน Vending machine (เขียน CSV file)

import csv
from datetime import datetime
import random

def vending_transaction(machine_id, product_id):
    timestamp = datetime.now().strftime("%Y%m%d %H:%M:%S")
    with open(r"data\vending transaction.txt", mode='a', encoding='utf8', newline='') as f:
        fw = csv.writer(f)
        fw.writerow([machine_id, product_id, timestamp])
        
def vending_machine():
    while True:
        costumer = input("input product id / [q]uit: ")
        if costumer != "q":
            machine_id = random.choice(["HUA", "SAM", "SIL", "SUK"])
            vending_transaction(machine_id, costumer)
        else:  
            break

vending_machine()     
    