def loop_return(amount, return_money):
    while amount >= return_money and amount > 0:
        print('returned money: ' + str(return_money))
        amount = amount - return_money
    
    return amount
    
def api_exchange2(price, amount):
    amount = amount - price 
    
    amount = loop_return(amount, 1000)
    amount = loop_return(amount, 500)
    amount = loop_return(amount, 100)
    amount = loop_return(amount, 50)
    amount = loop_return(amount, 20)
    amount = loop_return(amount, 10)
    amount = loop_return(amount, 5)
    amount = loop_return(amount, 2)
    amount = loop_return(amount, 1)
    amount = loop_return(amount, 0.5)
    amount = loop_return(amount, 0.25)

def api_exchange(price, amount):    
    
    amount = amount - price 
    
    while amount >= 1000 and amount > 0:
        print('returned money: 1000')
        amount = amount - 1000
    while amount >= 500 and amount > 0:
        print('returned money: 500')
        amount = amount - 500
    while amount >= 100 and amount > 0:
        print('returned money: 100')
        amount = amount - 100 
    while amount >= 50 and amount > 0:
        print('returned money: 50')
        amount = amount - 50
    while amount >= 20 and amount > 0:
        print('returned money: 20')
        amount = amount - 20 
    while amount >= 10 and amount > 0:
        print('returned money: 10')
        amount = amount - 10  
    while amount >= 5 and amount > 0:
        print('returned money: 5')
        amount = amount - 5
    while amount >= 2 and amount > 0:
        print('returned money: 2')
        amount = amount - 2    
    while amount >= 1 and amount > 0:
        print('returned money: 1')
        amount = amount - 1  
    while amount >= 0.5 and amount > 0:
        print('returned money: 0.5')
        amount = amount - 0.5  
    while amount >= 0.25 and amount > 0:
        print('returned money: 0.25')
        amount = amount - 0.25 

api_exchange2(41.25, 1000) 
