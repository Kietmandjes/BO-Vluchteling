def vraag1():
    print ("Je word wakker door mensen die buiten aan het schieten zijn wat ga je doen?\nA. Wachten\nB. Schuilen\nC. Vluchten")
    v1_1=input()
    v1 = v1_1.upper()
    if v1== 'A':
        dood()
    elif v1== 'B':
        dood()
    elif v1== 'C':
        vraag2()
    else:
        print ("Incorrect input")
        vraag1()
    
def vraag2():
    print ("Je word wakker door mensen die buiten aan het schieten zijn wat ga je doen?\nA. Wachten\nB. Schuilen\nC. Vluchten")
    v2_2=input()
    v2 = v2_2.upper()
    if v2== 'A':
        dood()
    elif v2== 'B':
        dood()
    elif v2== 'C':
        vraag2()
    else:
        print ("Incorrect input")
        vraag2()

