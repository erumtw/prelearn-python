# แปลงไฟล์ที่จัดเก็บด้วยรหัส TIS-620 เป็น Unicode

def tis_to_utf(tis: str) -> str:
    s = ''
    for c in tis:
        if 0xa0 <= ord(c) <= 0xfb:
            s += chr(ord(c) + 0xe00 - 0xa0)
        else:
            s += c
    return s

def tis_to_utf_v2(tis: str) -> str:
    s = [chr(ord(c) + 0xe00 - 0xa0) if 0xa0 <= ord(c) <= 0xfb else c for c in tis]
    
    return "".join(s)
    
def convert_file_tis2utf(file, newfile):
    
    with open(file, encoding='utf8') as fr:
        data = fr.read()
    
    with open(newfile, mode='w', encoding='utf8') as fw:
        fw.write(tis_to_utf(data))
        
    
        



# print(tis_to_utf("hello world »ÃÐà·Èä·Â Thailand เมืองยิ้ม"))
# print(tis_to_utf_v2("hello world »ÃÐà·Èä·Â Thailand เมืองยิ้ม"))
convert_file_tis2utf("data/tis.txt", "tist2utf.txt")