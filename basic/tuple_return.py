def thai_area(sqwa):
    rai = sqwa // 400 # 1 ไร่ = 400 ตร.วา
    ngan = (sqwa - (rai * 400)) // 100 # 1 งาน = 100 ตร.วา
    wa = sqwa % 100
    return rai, ngan, wa

sqwa = int(input("Enter Square wa: "))
convert_result = thai_area(sqwa)
print(convert_result[0], convert_result[1], convert_result[2], sep = "-")
print("{} ไร่ {} งาน {} วา".format(convert_result[0], convert_result[1], convert_result[2]))