# การเขียนเท็กซ์ไฟล์เบื้องต้น (write text file)
from csv import writer

def write_demo():
    f = open(r"test text write.txt", "w", encoding='utf8')
    f.write("hello world\n")
    f.write("im learning python")
    f.close()

def write_demo2():
    # context manager
    with open("demo write 02.txt", mode='w', encoding='utf8') as f:
        f.write("write with context manager")

def write_list():
    lists = ['latte', 'americano', 'mocha', 'espresso']
    
    with open('write list demo.txt', mode='w', encoding='utf8') as fw:
        for i in lists:
            fw.write(i + '\n')
            

# write_demo()
# write_demo2()
write_list()