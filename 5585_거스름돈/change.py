

P =int(input())

def payment(price):

       
    change = 1000-price


    Ochun = change // 500
    change = change % 500 
        
    chun = change // 100 
    change = change % 100

    Obek = change // 50
    change = change % 50

    bek = change // 10
    change = change % 10 

    Oship = change // 5 
    change = change % 5
    
    ship = change // 1
    change = change % 1
    
    result = Ochun + chun + Obek + bek + Oship + ship 
    
    return result 


calling = payment(P) 

print(calling)