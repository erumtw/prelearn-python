# ==, != <>, <, >, and, or, not

def score(score):
    if score >= 0 and score <= 100: # or we can write 0 <= score <= 100
        if score > 80:
            return 'A'
        elif score >= 70:
            return 'B'
        elif score >= 60:
            return 'C'
        elif score >= 50:
            return 'D'
        else:
            return 'F'
    else:
        return "Invalid Score"

def ticket(age, is_local):
    if (age < 7 or age > 60) and is_local:
        return "Free"
    else:
        return "Paid"

def ticket2(age, is_local):
    return "Free" if (7 > a > 60) and is_local else "Paid" #Ternary
    # return (age < 7 || age > 60) && is_local ? "Free" : "Paid": # in java, c


print("Grade:", score(10))
print(ticket(5, False))
print(ticket(5, True))
