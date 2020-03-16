def api_roman(value):
    strTest = ''
    if ((value % 10) == 0):
        strTest = 'X'
    if (value > 10):
        strTest += 'X'        
    if ((value % 5) == 4):
        strTest += 'I' 
    if ((value % 9) == 0):
        strTest += 'X'
    if ((value % 19) == 0):
        strTest += 'X'
    if (((value % 10) >= 4) and ((value % 10) <= 8)):
        strTest += 'V'
    if ((value % 5) == 1):
        strTest += 'I'
    if ((value % 5) == 2):
        strTest += 'II'
    if ((value % 5) == 3):
        strTest += 'III'
    print(str(value) + ' ' + strTest)

def api_roman2(num):
    num_roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL'}
    
    result = ''
    for value, num_roman in sorted(num_roman.items(), reverse=True):
        while num >= value:
            result += num_roman
            num -= value
    print(result) 
    

i = 1
while (i <= 20):
    api_roman2(i)
    i = i + 1
