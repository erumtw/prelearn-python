# 4957 7692 1332 987
# 

def get_card_digit(card_nums):
    return [int(digit) for digit in card_nums if digit.isdigit()]

def print_digit(digit):
    [print(f" {d:>2} |", end="") for d in digit]
    print()
    
# def calculate_with_21(card_nums, two_one):
#     # result = []
#     # x = 1
#     # for i, e in enumerate(card_nums):
#     #     if i % 2 == 0:
#     #         x = 2
#     #     else:
#     #         x = 1 
#     #     result.append(e*x)
#     # return result
#     result = []
#     for i, j in zip(card_nums, two_one):
#         result.append(i*j)
#     return result

            
if __name__ == '__main__':
    
    card = input("Enter first 15 digit card number: ")
    # card = "9900 6631 0236 129"
    card_digit = get_card_digit(card)
    two_one = [2,1]*7 + [2]
    cal1 = [i*j for i,j in zip(card_digit, two_one)]
    cal2 = [i if i < 10 else i//10 + i%10 for i in cal1]
    # Luhn mod 10
    r = sum(cal2) % 10 
    check_digit = 0 if r == 10 else 10 - r 
    
    print_digit(range(15))
    print_digit(card_digit)
    print_digit(two_one)
    print('-'*76)
    print_digit(cal1)
    print_digit(cal2)
    print("\nSum =", sum(cal2))
    print("Check Digit =", check_digit)
    print("Card Number = ", end='')
    [print(i, end="") for i in card_digit]
    print(check_digit)