
#1א
def get_penta_num(n):
    return n*(3*n-1)/2

#1ב
def pentaNumRange(n1,n2):
    return [get_penta_num(num) for num in range(n1,n2)]

#2
def sum_digit(n):
    my_str=str(n)
    if not my_str.isdigit():
        return "invalid input"
    return sum(int(digit) for digit in my_str)

#3א
def normalize_text(str1):
    mystr = str1.lower()
    list2 = sorted(mystr)
    return "".join(list2)

#3ב
def are_anagrams(str1,str2):
    return normalize_text(str1) == normalize_text(str2)

#4
def gematria(my_str):
    GEMATRIA = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
        'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40, 'נ': 50, 'ן': 50, 'ס': 60, 'ע': 70,
        'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
    }
    return sum(GEMATRIA.get(letter,0) for letter in my_str)




def main():
#2
    input1 = input("enter number\n")
    print(sum_digit(input1))
#3ב
    first = input("enter first text:\n")
    second = input("enter second text:\n")
    if not first.strip() or not second.strip():
        print("invalid input")
        return
    print(are_anagrams(first,second))

if __name__ == '__main__':
    main()
