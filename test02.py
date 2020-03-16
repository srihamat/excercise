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

i = 1
while (i <= 20):
    api_roman(i)
    i = i + 1
