# การลบรหัสขึ้นบรรทัดใหม่ (\n) จากข้อมูลแต่ละแถวที่ได้จากการอ่านเท็กซ์ไฟล์
# การใข้ strip() และ rstrip() ในการลบ white spaces (tab, new line, space) จากข้อมูลแต่ละบรรทัดที่อ่านมาจากเท็กซ์ไฟล์

def read1(file):
    with open(file) as f:
        data1 = f.readlines()
        print(data1)
        data2 = [i.strip() for i in data1]
        print(data2)

def read2(file):
    with open(file) as f:
        data = [line.strip() for line in f]
        print(data)

def read3(file):
    with open(file) as f:
        data = f.read()
    print(data)
    data2 = data.splitlines()
    [print(line.strip()) for line in data2]

# ex. Mercury,พุธ  --> ["Mercury", "พุธ"]
def read4(file):
    with open(file, encoding='utf8') as f:
        data = f.readlines()
    data2 = [line.strip() for line in data]
    data3 = [line.strip().split(',') for line in data]
    
    print(data2)
    print(data3)


filename1 = r"D:\programming-learns\prelearn-python\data\planet.txt"
filename2 = r"D:\programming-learns\prelearn-python\data\planet2.txt"

# read1(filename1))
# read2(filename1)
# read3(filename1)
read4(filename2)
