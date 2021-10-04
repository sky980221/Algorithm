
def payment(price, inputMoney):
    if inputMoney < price :
        return inputMoney


    else : 

        change = inputMoney-price

        man = change // 10000 
        change = change % 10000 

        Ochun = change // 5000
        change = change % 5000 
        
        chun = change // 1000 
        change = change % 1000 

        Obek = change // 500
        change = change % 500

        bek = change // 100
        change = change % 100 

        Oship = change // 50 
        change = change % 50
    
        ship = change // 10
        change = change % 10
    
        result = man + Ochun + chun + Obek + bek + Oship + ship 
    
        return result 


calling = payment(3953,5000) 

print(calling)