def bmi_without_zip():
    weight = [70, 60, 48]
    height = [170, 175, 161]
    bmi = [weight[i] / (height[i] / 100) ** 2 for i in range(len(weight))]
    return bmi

def bmi_with_zip():
    weight = [70, 60, 48]
    height = [170, 175, 161]
    [print(w,h) for w, h in zip(weight, height)]
    bmi = [w / (h / 100) ** 2 for w, h in zip(weight, height)]
    return bmi

def bmi_with_zip2():
    weight = [70, 60, 48]
    height = [170, 175, 161]
    name = ['Jame', 'Jane', 'Heiley']
    gender = ['M', 'F', 'F']
    
    # bmi = [[{n: w / (h / 100) ** 2}, g] for w, h, n, g in zip(weight, height, name, gender)]
    bmi = [[{n: w / (h / 100) ** 2}, g] for w, h, n, g in zip(weight, height, name, gender) if g == "F"]
    
    return bmi


print(bmi_without_zip())
print(bmi_with_zip())
print(bmi_with_zip2())