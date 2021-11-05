def vraag1():
    print ("Je word wakker door mensen die buiten aan het schieten zijn wat ga je doen?\nA. Wachten\nB. Schuilen\nC. Vluchten")
    v1_1=input()
    v1 = v1_1.upper()
    if v1== 'A':
        print("Er zijn mensen je huis binnen gevallen en hebben je vermoord.")
        dood()
    elif v1== 'B':
        print("Mensen hebben je gevonden en hebben je vermoord.")
        dood()
    elif v1== 'C':
        vraag2()
    else:
        print ("Incorrect input")
        vraag1()
    
def vraag2():
    print ("Hoe ga je vluchten?\nA. Lopend\nB. Met de boot\nC. Met het vliegtuig")
    v2_2=input()
    v2 = v2_2.upper()
    if v2== 'A':
        vraag3()
    elif v2== 'B':
        vraag4()
    elif v2== 'C':
        vraag5()
    else:
        print ("Incorrect input")
        vraag2()

def vraag3():
    print ("Je wilt de grens over maar je word aangehouden. Wat ga je doen?\nA. Terug naar je dorp\cnB. Weg rennen")
    v3_3=input()
    v3 = v3_3.upper()
    if v3== 'A':
        vraag21()
    elif v3== 'B':
        vraag19()
    else:
        print ("Incorrect input")
        vraag3()
    
def vraag4():
    print ("Er zijn geen boten. Wat ga je doen?\nA. Naar het vliegveld\nB. Wachten")
    v4_4=input()
    v4 = v4_4.upper()
    if v4== 'A':
        vraag5()
    elif v4== 'B':
        vraag22()
    else:
        print ("Incorrect input")
        vraag4()

def vraag5():
    print ("Hoe wil je naar het vliegveld gaan?\nA. Met de auto\nB. Lopend")
    v5_5=input()
    v5 = v5_5.upper()
    if v5== 'A':
        vraag6()
    elif v5== 'B':
        print("Je word aangereden door een auto.")
        dood()
    else:
        print ("Incorrect input")
        vraag5()

def vraag6():
    print ("Je komt veilig aan bij het vliegveld maar er komt een storm. Wat ga je doen?\nA. Wachten tot de storm over is\nB. Het vliegtuig toch pakken")
    v6_6=input()
    v6 = v6_6.upper()
    if v6== 'A':
        vraag11()
    elif v6== 'B':
        vraag7()
    else:
        print ("Incorrect input")
        vraag6()

def vraag7():
    print ("Het vliegtuig stort neer op zee maar je overleeft het. Je wilt zo snel mogelijk naar veiligheid wat ga je doen?\nA. Een vlot maken\nB. Zwemmen")
    v7_7=input()
    v7 = v7_7.upper()
    if v7== 'A':
        vraag8()
    elif v7== 'B':
        print("Je verdrinkt")
        dood()
    else:
        print ("Incorrect input")
        vraag7()

def vraag8():
    print ("je ziet een boot in de verte. Wat ga je doen?\nA. Wachten tot de boot jou kant op komt\nB. Er heen zwemmen")
    v8_8=input()
    v8 = v8_8.upper()
    if v8== 'A':
        vraag9()
    elif v8== 'B':
        print("Je verdinkt.")
        dood()
    else:
        print ("Incorrect input")
        vraag8()

def vraag9():
    print ("De boot ziet je en komt naar je toe. Wanneer de boot bij je is zie je dat de boot helemaal vol zit. Wat doe je?\nA. Wachten\nB. Opstappen")
    v9_9=input()
    v9 = v9_9.upper()
    if v9== 'A':
        print("Er komt een storm en je vlot gaat kapot en je verdrinkt.")
        dood()
    elif v9== 'B':
        vraag10()
    else:
        print ("Incorrect input")
        vraag9()

def vraag10():
    print ("De boot komt aan in Nederland waar ga je heen?\nA. Platteland\nB. Stad")
    v10_10=input()
    v10 = v10_10.upper()
    if v10== 'A':
        einde1()
    elif v10== 'B':
        einde2()
    else:
        print ("Incorrect input")
        vraag10()
    
def vraag11():
    print ("Je heb een dag gewacht tot de storm over is en pakt nu het vliegtuig. Waar wil je heen?\nA. Nederland\nB. Duitsland")
    v11_11=input()
    v11 = v11_11.upper()
    if v11== 'A':
        vraag12()
    elif v11== 'B':
        vraag12()
    else:
        print ("Incorrect input")
        vraag11()

def vraag12():
    print ("Waar wil je overnachten?\nA. Straat\nB. Vluchtelingenkamp")
    v12_12=input()
    v12 = v12_12.upper()
    if v12== 'A':
        vraag13()
    elif v12== 'B':
        vraag14()
    else:
        print ("Incorrect input")
        vraag12()

def vraag13():
    print ("\nA. Bedelen\nB. Werk zoeken")
    v13_13=input()
    v13 = v13_13.upper()
    if v13== 'A':
        einde2()
    elif v13== 'B':
        einde3()
    else:
        print ("Incorrect input")
        vraag13()

def vraag14():
    print ("Ga je vrienden zoeken?\nA. Ja\nB. Nee")
    v14_14=input()
    v14 = v14_14.upper()
    if v14== 'A':
        einde4()
    elif v14== 'B':
        vraag15()
    else:
        print ("Incorrect input")
        vraag14()

def vraag15():
    print ("Je gaat de taal leren en werk zoeken. Wat wil je worden?\nA. Dokter\nB. Politie agent")
    v15_15=input()
    v15 = v15_15.upper()
    if v15== 'A':
        einde5()
    elif v15== 'B':
        vraag16()
    else:
        print ("Incorrect input")
        vraag15()

def vraag16():
    print ("Er word aangeboden of je hoofdcommesaris rang wilt. Wil je dat?\nA. Ja\nB. Nee")
    v16_16=input()
    v16 = v16_16.upper()
    if v16== 'A':
        vraag17()
    elif v16== 'B':
        einde6()
    else:
        print ("Incorrect input")
        vraag16()

def vraag17():
    print ("Je bent nu een hoofdcommesaris. Wil je nu mensen met een lagere rang pesten?\nA. Ja\nB. Nee")
    v17_17=input()
    v17 = v17_17.upper()
    if v17== 'A':
        vraag18()
    elif v17== 'B':
        einde7()
    else:
        print ("Incorrect input")
        vraag17()

def vraag18():
    print ("Je raakt je baan als hoofdcommesaris kwijt en word boos. Wil je nogsteeds bij de politie blijven?\nA. Ja\nB. Nee")
    v18_18=input()
    v18 = v18_18.upper()
    if v18== 'A':
        einde6()
    elif v18== 'B':
        einde2()
    else:
        print ("Incorrect input")
        vraag18()

def vraag19():
    print ("Ga je links of rechts?\nA. Links\nB. Rechts")
    v19_19=input()
    v19 = v19_19.upper()
    if v19== 'A':
        einde8()
    elif v19== 'B':
        vraag20()
    else:
        print ("Incorrect input")
        vraag19()

def vraag20():
    print ("Je bent net aan ontsnapt. Waar ga je heen?\nA. De boot\nB. Terug naar je dorp")
    v20_20=input()
    v20 = v20_20.upper()
    if v20== 'A':
        einde6()
    elif v20== 'B':
        vraag21()
    else:
        print ("Incorrect input")
        vraag20()

def vraag21():
    print ("Je bent terug in je dorp en je familie wilt in het dorp blijven. Naar wie ga je?\nA. Familie\nB. Vrienden")
    v21_21=input()
    v21 = v21_21.upper()
    if v21== 'A':
        print("Je bent doodgeschoten.")
        dood()
    elif v21== 'B':
        print("Je vrienden bestluiten om met het vliegtuig te gaan.")
        vraag5()
    else:
        print ("Incorrect input")
        vraag21() 

def vraag22():
    print ("Er komt een boot maar die zit snel overvol wat doe je?\nA. Wachten\nB. Opstappen")
    v22_22=input()
    v22 = v22_22.upper()
    if v22== 'A':
        print("Er valt een bom op je.")
        dood()
    elif v22== 'B':
        print("De boot zit overvol en zingt daardoor.")
        dood()
    else:
        print ("Incorrect input")
        vraag22()       

def dood():
    print ("Wil je opnieuw spelen? J/N")
    d1=input()
    d2 = d1.upper()
    if d2== 'J':
        vraag1()
    elif d2== 'N':
        ()
    else:
        print ("Incorrect input")
        vraag2()

def einde1():
    print ("Je word een boer.\nWil je opnieuw spelen? J/N")
    e1=input()
    e2 = e1.upper()
    if e2== 'J':
        vraag1()
    elif e2== 'N':
        ()
    else:
        print ("Incorrect input")
        vraag2()

def einde2():
    print ("Je word dakloos en moet moeite doen om te overleven.\nWil je opnieuw spelen? J/N")
    e3=input()
    e4 = e3.upper()
    if e4== 'J':
        vraag1()
    elif e4== 'N':
        ()
    else:
        print ("Incorrect input")
        vraag2()

def einde3():
    print ("Je krijgt een baan als schoonmaker en krijgt een prima leven.\nWil je opnieuw spelen? J/N")
    e5=input()
    e6 = e5.upper()
    if e6== 'J':
        vraag1()
    elif e6== 'N':
        ()
    else:
        print ("Incorrect input")
        vraag2()

def einde4():
    print ("Je heb veel plezier in het leven en krijgt een baan als schoonmaker.\nWil je opnieuw spelen? J/N")
    e7=input()
    e8 = e7.upper()
    if e8== 'J':
        vraag1()
    elif e8== 'N':
        ()
    else:
        print ("Incorrect input")
        vraag2()

def einde5():
    print ("Je word een hele goede dokter en red meerdere levens\nWil je opnieuw spelen? J/N")
    e9=input()
    e10 = e9.upper()
    if e10== 'J':
        vraag1()
    elif e10== 'N':
        ()
    else:
        print ("Incorrect input")
        vraag2()

def einde6():
    print ("Je blijft een normale politie agent.\nWil je opnieuw spelen? J/N")
    e11=input()
    e12 = e11.upper()
    if e12== 'J':
        vraag1()
    elif e12== 'N':
        ()
    else:
        print ("Incorrect input")
        vraag2()

def einde6():
    print ("Je blijft een normale politie agent.\nWil je opnieuw spelen? J/N")
    e11=input()
    e12 = e11.upper()
    if e12== 'J':
        vraag1()
    elif e12== 'N':
        ()
    else:
        print ("Incorrect input")
        vraag2()

def einde7():
    print ("Je blijft een hoofdcommesaris en word een icoon bij de politie.\nWil je opnieuw spelen? J/N")
    e13=input()
    e14 = e13.upper()
    if e14== 'J':
        vraag1()
    elif e14== 'N':
        ()
    else:
        print ("Incorrect input")
        vraag2()

def einde8():
    print ("Je word aangehouden en gaat de gevangenis in.\nWil je opnieuw spelen? J/N")
    e16=input()
    e17 = e16.upper()
    if e17== 'J':
        vraag1()
    elif e17== 'N':
        ()
    else:
        print ("Incorrect input")
        vraag2()

vraag1()