import csv
from pprint import pprint
from this import d


def dict_file_nato():
    with open("D:/programming-learns/prelearn-python/dictionary/nato.txt") as f:
        d = {line[0]: line[:-1] for line in f}
        return d

def convert(text):
    d = dict_file_nato()
    # for c in text:
    #     print(dicts[c.upper()], end=" ")
    return " ".join([d[c.upper()] for c in text])
    
def dict_file2():
    with open("D:/programming-learns/prelearn-python/dictionary/abbr_province.txt", 
              encoding="utf8") as f:
        data = csv.reader(f)
        return {k: v for k,v in data}
    
# pprint(dict_file_nato())
# pprint(dict_file2())
print(convert("nato"))