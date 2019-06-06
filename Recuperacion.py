Lista=[[12,5,98],[5,4,6],[7,8,8],[4,5,9]]
print("Lista")
funcion = list(map(lambda x:[x[0]]+[x[len(x)-1]],Lista))
print(funcion)

SuperPares=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
def SP(x):
    for num in SuperPares:
        #print(num)
        if num<=10:
            par=num%2
            if par==0:
                print(num)
        else:
            
print(SP(SuperPares))
