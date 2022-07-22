# การเขียนเท็กซ์ไฟล์แบบต่อท้ายไฟล์เดิม (write text file in append mode)
# การเขียนข้อมูลต่อท้ายไฟล์เดิมที่มีอยู่ (append mode)
# สาธิตการสร้าง cash register อย่างง่าย ที่เก็บรายการขายและวันเวลาเข้าไว้ในไฟล์

from cmath import cos
from datetime import datetime


def write_append(content: str):
    with open("write list demo.txt", mode='a', encoding='utf8') as fw:
        fw.write(content)
        

def cash_register():
    with open("write list demo.txt", encoding='utf8') as fr:
        data = fr.read()
        menus = data.splitlines()
    
    dictmenus = {"l": menus[0], "a": menus[1], "m": menus[2], "e": menus[3], "d": menus[4]}
    
    while True:
        costumer = input("[l]atte [a]mericano [m]ocha [e]spresso [d]irty coffee [q]iut: ")
        if costumer != "q":
            stamptime = datetime.now().strftime("%Y%m%d %H:%M:%S")
            with open("cafe cash register.txt", mode='a', encoding='utf8') as fw:
                fw.write(f"{dictmenus[costumer]} {stamptime}\n")
        else:
            break
            
        
    # return menus

# write_append("dirty coffee")
cash_register()