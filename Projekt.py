#Projekt-Geometrierechner
import math


print ("Geometrierechner")
print ("Es können mit diesem Rechner nun Berechnungen zum Flächeninhalt, Umfang, Volumen")
print ("und Oberflächeninhalt durchgeführt werden. Für die Auswahl immer die Zahl oder")
print ("den jeweiligen Buchstaben, der in der Klammer steht, eingeben.")
print ("Verfügbare Figuren/Körper:")    
print ("Ebene Figuren: - Quadrat [1]                        Körper: - Würfel [a]")
print ("               - Rechteck [2]                               - Quader [b]")
print ("               - Dreieck [3]                                - Prisma [c]")
print ("               - Parallelogramm [4]                         - Zylinder [d]")
print ("               - Trapez [5]                                 - Pyramide [e]")
print ("               - Kreis [6]                                  - Kegel [f]")
print ("               - Kreisbogen und Kreissektor [7]             - Kugel [g]")
    
def figurenauswahl():
        figurenauswahl =input("Bitte wähle eine Figur aus. ")
        if figurenauswahl == "1": quadrat()
        elif figurenauswahl == "2": rechteck()
        elif figurenauswahl =="3": dreieck()
        elif figurenauswahl =="4": parallelogramm()
        elif figurenauswahl =="5": trapez()
        elif figurenauswahl =="6": kreis()
        elif figurenauswahl =="7": kreisbogen_kreissektor()
        elif figurenauswahl =="a": würfel()
        elif figurenauswahl =="b": quader()
        elif figurenauswahl =="c":prisma()
        elif figurenauswahl =="d":zylinder()
        elif figurenauswahl =="e":pyramide()
        elif figurenauswahl =="f": kegel()
        elif figurenauswahl =="g":kugel()
        else:
            print ("Error:",figurenauswahl, "steht nicht zur Vefügung.")
    

def quadrat():
    while True:
        x= None
        while x not in ("f", "b","u"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Quadrat ausrechnen willst. ")       
        if x=="f":
            while True:
                try:
                    a=float(input("Gebe bitte die Länge des Quadrates an: "))
                    quadrata= a**2
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Flächeninhalt des Quadrats beträgt",quadrata,"Flächeneinheiten.")

        elif x=="u":
            while True:
                try:
                    a=float(input("Gebe bitte die Länge des Quadrates an: "))
                    quadratu= 4*a
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")                  
            print ("Der Umfang des Quadrates beträgt", quadratu,"Flächeneinheiten.")
            break
        else:
            while True:
                try:
                    a=float(input("Gebe bitte die Länge des Quadrates an. "))
                    quadratu= 4*a
                    quadrata= a**2
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Umfang des Quadrates beträgt", quadratu,"Flächeneinheiten.")
            print ("Der Flächeninhalt des Quadrats beträgt",quadrata,"Flächeneinheiten.")
            break
                

def rechteck():
    while True:
        x= None
        while x not in ("f", "b","u"):
            if x is not None:
                 print ("Sorry, aber das habe ich nicht verstanden.")
            x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Rechteck ausrechnen willst. ")           
        if x=="f":
            while True:
                try:
                    a= float(input("Gebe bitte die Länge des Rechtecks an: "))
                    b= float(input("Gebe bitte die Breite des Rechtecks an: "))
                    rechtecka= a*b
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Der Flächeninhalt des Rechtecks beträgt", rechtecka, "Flächeneinheiten.")
            break
        elif x=="u":
            while True:
                try:
                    a= float(input("Gebe bitte die Länge des Rechtecks an: "))
                    b= float(input("Gebe bitte die Breite des Rechtecks an: "))
                    rechtecku= 2*a+2*b
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Der Umfang des Rechtecks beträgt", rechtecku, "Flächeneinheiten.")
            break
        else:
            while True:
                try:
                    a= float(input("Gebe bitte die Länge des Rechtecks an: "))
                    b= float(input("Gebe bitte die Breite des Rechtecks an: "))
                    rechtecka= a*b
                    rechtecku= 2*a+2*b
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Der Flächeninhalt des Rechtecks beträgt", rechtecka, "Flächeneinheiten.")
            print("Der Umfang des Rechtecks beträgt", rechtecku, "Flächeneinheiten.")
            break
    
def dreieck():
    while True:
        x= None
        while x not in ("f", "b","u"):
            if x is not None:
                 print ("Sorry, aber das habe ich nicht verstanden.")
            x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Dreieck ausrechnen willst. ")
        if x=="f":
            while True:
                try:
                    g= float(input("Gebe bitte die Länge der Basis oder der Grundseite des Dreiecks an: "))
                    h= float(input("Gebe bitte die Höhe des Dreiecks an: "))
                    dreiecka= (g*h)/2
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Der Flächeninhalt des Dreiecks beträgt", dreiecka, "Flächeneinheiten.")
            break
        elif x=="u":
            while True:
                try:
                    a= float(input("Gebe bitte die Länge der 1. Seite (Kathete) des Dreiecks an: "))
                    b= float(input("Gebe bitte die Länge der 2. Seite (Kathete) des Dreiecks an: "))
                    c= float(input("Gebe bitte die Länge der 3. Seite (Hypotenuse) des Dreiecks an: "))
                    dreiecku= a+b+c
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Der Umfang des Dreiecks beträgt", dreiecku, "Flächeneinheiten.")
            break
        else:
            while True:
                try:
                    g= float(input("Gebe bitte die Länge der Basis oder der Grundseite des Dreiecks an: "))
                    h= float(input("Gebe bitte die Höhe des Dreiecks an: "))
                    dreiecka= (g*h)/2
                    a= float(input("Gebe bitte die Länge des 1. Schenkels des Dreiecks an: "))
                    b= float(input("Gebe bitte die Länge des 2. Schenkels des Dreiecks an: "))
                    dreiecku= a+b+g
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Der Flächeninhalt des Dreiecks beträgt", dreiecka, "Flächeneinheiten.")
            print("Der Umfang des Dreiecks beträgt", dreiecku, "Flächeneinheiten.")
            break
        
def parallelogramm():
    while True:
        x= None
        while x not in ("f", "b","u"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Parallelogramm ausrechnen willst. ")
        if x=="f":
            while True:
                try:
                    g= float(input("Gebe bitte die Länge der Grundseite des Parallelograms an: "))
                    h= float(input("Gebe bitte die Höhe des Parallelograms an: "))
                    parallelogramma= g*h
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Flächeninhalt des Paralellograms beträgt",parallelogramma,"Flächeneinheiten. ")
            break
        elif x=="u":
            while True:
                try:
                    a= float(input("Gebe bitte die Länge der 1. Seite des Parallelogramms an: "))
                    b= float(input("Gebe bitte die Länge der 2. Seite des Paralellogramms an: "))
                    parallelogrammu= 2*a+2*b
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Umfang des Parallelogramms beträgt", parallelogrammu,"Flächeneinheiten. ")
            break
        else:
            while True:
                try:
                    g= float(input("Gebe bitte die Länge der Grundseite des Parallelograms an: "))
                    h= float(input("Gebe bitte die Höhe des Parallelograms an: "))
                    parallelogramma= g*h
                    a= float(input("Gene bitte die Länge der 1. Seite des Parallelogramms an: "))
                    b=float(input("Gebe bitte die Länge der 2. Seite des Parallelogramms an: "))
                    parallelogrammu= 2*a+2*b
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Flächeninhalt des Paralellograms beträgt",parallelogramma,"Flächeneinheiten.")        
            print ("Der Umfang des Parallelogramms beträgt", parallelogrammu,"Flächeneinheiten.")
            break
    
def trapez():
    while True:
        x= None
        while x not in ("f", "b","u"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x= input ("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Trapez ausrechnen willst. ")
        if x=="f":
            while True:
                try:
                    a=float(input("Gebe bitte die Länge der 1. parallelen Seite des Trapez' an: "))
                    c=float(input("Gebe bitte die Länge der 2. parallelen Seite des Trapez' an: "))
                    h=float(input("Gebe bitte die Höhe des Trapez' an: "))
                    trapeza= ((a+c)/2)*h
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Flächeninhalt des Trapez' beträgt",trapeza,"Flächeneinheiten.")
            break
        elif x=="u":
            while True:
                try:
                    a=float(input("Gebe bitte die Länge der 1. Seite des Trapez' an: "))
                    b=float(input("Gebe bitte die Länge der 2. Seite des Trapez' an: "))
                    c=float(input("Gebe bitte die Länge der 3. Seite des Trapez' an: "))
                    d=float(input("Gebe bitte die Länge der 1. Seite des Trapez' an: "))
                    trapezu=a+b+c+d
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Umfang des Trapez' beträgt",trapezu,"Flächeneinheiten.")
            break
        else:
            while True:
                try:
                    a=float(input("Gebe bitte die Länge der 1. parallelen Seite des Trapez' an: "))
                    c=float(input("Gebe bitte die Länge der 2. parallelen Seite des Trapez' an: "))
                    h=float(input("Gebe bitte die Höhe des Trapez' an: "))
                    trapeza= ((a+c)/2)*h
                    a=float(input("Gebe bitte die Länge der 1. Seite des Trapez' an: "))
                    b=float(input("Gebe bitte die Länge der 2. Seite des Trapez' an: "))
                    c=float(input("Gebe bitte die Länge der 3. Seite des Trapez' an: "))
                    d=float(input("Gebe bitte die Länge der 1. Seite des Trapez' an: "))
                    trapezu=a+b+c+d
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Flächeninhalt des Trapez' beträgt",trapeza,"Flächeneinheiten.")
            print ("Der Umfang des Trapez' beträgt",trapezu,"Flächeneinheiten.")
            break

def kreis():
    while True:
        x= None
        while x not in ("f", "b","u", "a"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x= input ("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u], den Durchmesser[d] oder alles[a] vom Kreis ausrechnen willst. ")
        if x=="f":
            while True:
                y= None
                while y not in ("r","d"):
                    if y is not None:
                        print ("Diese Eingabe war leider ungültig. Neuer Versuch?")
                    y=input("Ist der Radius[r] oder der Durchmesser[d] vorhanden?")
            if y=="r":
                while True:
                    try:
                        r=float(input("Gebe bitte den Radius vom Kreis an: "))
                        kreisa= math.pi*r**2
                        break
                    except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            else:
                while True:
                    try:
                        d=float(input("Gebe bitte den Durchmesser vom Kreis an: "))
                        kreisa= math.pi*((d/2)**2)
                        break
                    except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Flächeninhalt vom Kreis beträgt", kreisa, "Flächeneinheiten.")
            break
        elif x=="u":
            while True:
                y= None
                while y not in ("r","d"):
                    if y is not None:
                        print ("Diese Eingabe war leider ungültig. Neuer Versuch?")
                    y=input("Ist der Radius[r] oder der Durchmesser[d] vorhanden?")
            if y=="r":
                while True:
                    try:
                        r=float(input("Gebe bitte den Radius vom Kreis an: "))
                        kreisu= 2*math.pi*r
                        break
                    except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            else:
                while True:
                    try:
                        d=float(input("Gebe bitte den Durchmesser vom Kreis an: "))
                        kreisa= math.pi*d
                        break
                    except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Umfang vom Kreis beträgt", kreisu, "Flächeneinheiten.")
            break
        elif x=="d":
            while True:
                 try:
                        r=float(input("Gebe bitte den Radius vom Kreis an: "))
                        kreisd= r*2
                        break
                 except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
                 print ("Der Durchmesser beträgt", kreisd,"Flächeneinheiten.")
                 break
        else:
            while True:
                try:
                        r=float(input("Gebe bitte den Radius vom Kreis an: "))
                        kreisa=math.pi*r**2
                        kreisu=2*math.pi*r
                        kreisd=r*2
                        break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
                print ("Der Flächeninhalt vom Kreis beträgt", kreisa, "Flächeneinheiten.")
                print ("Der Umfang vom Kreis beträgt", kreisu, "Flächeneinheiten.")
                print ("Der Durchmesser beträgt", kreisd,"Flächeneinheiten.")
                break
        
def kreisbogen_kreissektor():
    while True:
        x= None
        while x not in ("ks", "kb","b"):
            if x is not None:
               print ("Sorry, aber das habe ich nicht verstanden.")
            x=input ("Bitte gib an ob du den Kreissektor[ks], Kreisbogen[kb] oder beides[b] berechnen willst. ")
        if x=="ks":
            while True:
                try:
                    r=float(input("Gebe bitte den Radius des Kreises an: "))
                    α=float(input("Gebe bitte den Winkel α des Kreissektors an: "))
                    ks=math.pi*r**2*(math.radians(α)/math.radians(360))
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Kreissektor beträgt",ks,"Flächeneinheiten.")
            break
        elif x=="kb":
            while True:
                try:
                    r=float(input("Gebe bitte den Radius des Kreises an: "))
                    α=float(input("Gebe bitte den Winkel α des Kreissektors an: "))
                    kb=math.pi*r*(math.radians(α)/math.radians (180))
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Kreisbogen beträgt",kb,"Flächeneinheiten.")
            break
        else:
            while True:
                try:
                    r=float(input("Gebe bitte den Radius des Kreises an: "))
                    α=float(input("Gebe bitte den Winkel α des Kreissektors an: "))
                    ks=math.pi*r**2(*math.radians(α)/math.radians(360))
                    kb=math.pi*r*(math.radians(α)/math.radians (180))
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Kreissektor beträgt",ks,"Flächeneinheiten.")        
            print ("Der Kreisbogen beträgt",kb,"Flächeneinheiten.")
            break
        
def würfel():
    while True:
        x= None
        while x not in ("v", "o","b"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x=input("Möchtest du das Volumen[v], die Oberfläche[o] oder beides[b] vom Würfel berechnen? ")
        if x=="v":
            while True:
                try:
                    a=float(input("Gebe bitte die Kantenlänge des Würfels an: "))
                    würfelv=(a*a*a)
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Das Volumen des Würfels beträgt",würfelv,"Flächeneinheiten.")
            break

                                
        elif x=="o":
            while True:
                try:
                    a=float(input("Gebe bitte die Kantenlänge des Würfels an: "))
                    würfelo= 6*a**2
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Oberfläche des Würfels beträgt",würfelo,"Flächeneinheiten.")
            break
        elif x=="b":
            while True:
                try:
                    a=float(input("Gebe bitte die Kantenlänge des Würfels an: "))
                    würfelv=(a*a*a)
                    würfelo= 6*a**2
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Das Volumen des Würfels beträgt",würfelv,"Flächeneinheiten.")
            print ("Die Oberfläche des Würfels beträgt",würfelo,"Flächeneinheiten.")
            break

def quader():
    while True:
        x= None
        while x not in ("v", "o","b"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x=input ("Möchtest du das Volumen[v], die Oberfläche[o] oder beides[b] des Quaders berechnen? ")
        if x=="v":
            while True:
                try:
                    a= float(input("Gebe bitte die Länge des Quaders an: "))
                    b= float(input("Gebe bitte die Breite des Quaders an: "))
                    c= float (input("Gebe bitte die Höhe des Quaders an: "))
                    quaderv= a*b*c
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Das Volumen des Quaders beträgt",quaderv,"Flächeneinheiten.")
            break
        elif x=="o":
            while True:
                try:
                    a= float(input("Gebe bitte die Länge des Quaders an: "))
                    b= float(input("Gebe bitte die Breite des Quaders an: "))
                    c= float (input("Gebe bitte die Höhe des Quaders an: "))
                    quadero= 2*a*b+2*a*c+2*b*c
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Oberfläche des Quaders beträgt",quadero,"Flächeneinheiten.")
            break
        elif x=="b":
            while True:
                try:
                    a= float(input("Gebe bitte die Länge des Quaders an: "))
                    b= float(input("Gebe bitte die Breite des Quaders an: "))
                    c= float (input("Gebe bitte die Höhe des Quaders an: "))
                    quadero= 2*a*b+2*a*c+2*b*c
                    quaderv= a*b*c
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Das Volumen des Quaders beträgt",quaderv,"Flächeneinheiten.")
            print ("Die Oberfläche des Quaders beträgt",quadero,"Flächeneinheiten.")
            break
    
def prisma():
    while True:
        x= None
        while x not in ("v", "o","m","a"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x=input("Soll das Volumen[v], die Oberfläche[o], die Mantelfläche [m] oder alles [a] vom Prisma berechnet werden? ")
        if x=="v":
            while True:
                try:
                    g= float(input("Gebe bitte die Grundfläche des Prismas an: "))
                    h=float(input ("Gebe bitte die Höhe des Prismas an: "))
                    prismav= g*h
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
                                
            print ("Das Volumen des Prismas beträgt", prismav,"Flächeneinheiten.")
            break
        elif x=="o":
            while True:
                try:
                    g= float (input("Gebe bitte die Grundfläche des Prismas an: "))
                    m= float (input("Gebe die Mantelfläche des Prismas an: "))
                    prismao= 2*g+m
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Oberfläche des Prismas beträgt", prismao,"Flächeneinheiten.")
            break
        elif x=="m":
            while True:
                try:
                    h=float(input ("Gebe bitte die Höhe des Prismas an: "))
                    u=float(input("Gebe bitte den Umfang der Grundfläche des Prismas an: "))
                    prismam= h*u
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Mantelfläche des Prismas beträgt", prismam,"Flächeneinheiten.")
            break
        elif x=="a":
            while True:
                try:
                    g= float(input("Gebe bitte die Grundfläche des Prismas an: "))
                    h=float(input ("Gebe bitte die Höhe des Prismas an: "))
                    u=float(input("Gebe bitte den Umfang der Grundfläche des Prismas an: "))
                    m=h*u
                    prismav= g*h
                    prismao= 2*g+m
                    break
                except ValueError:
                         print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Mantelfläche des Prismas beträgt", m,"Flächeneinheiten.")
            print ("Die Oberfläche des Prismas beträgt", prismao,"Flächeneinheiten.")
            print ("Das Volumen des Prismas beträgt", prismav,"Flächeneinheiten.")
            break

def zylinder():
    while True:
        x= None
        while x not in ("u", "g","m","o", "v", "a"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x=input("Soll der Umfang [u], die Grundfläche [g], das Volumen[v], die Oberfläche[o], die Mantelfläche [m] oder alles [a] vom Zylinder berechnet werden? ")
        if x=="u":
            while True:
                try:
                    r=float(input("Gebe bitte den Zylinder Radius an: "))
                    zylinderu= 2*math.pi*r
                    break
                except ValueError:
                         print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Umfang des Zylinders beträgt",zylinderu,"Flächeneinheiten.")
            break
        elif x=="g":
            while True:
                try:
                    r=float(input("Gebe bitte den Zylinder Radius an: "))
                    zylinderg= math.pi*r**2
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Grundfläche des Zylinders beträgt",zylinderg, "Flächeneinheiten.")
            break
        elif x=="m":
            while True:
                try:
                    r=float(input("Gebe bitte den Zylinder Radius an: "))
                    h=float(input("Gebe bitte die Zylinder Höhe an: "))
                    zylinderm= 2*math.pi*r*h
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Mantelfläche des Zylinders beträgt",zylinderm, "Flächeneinheiten.")
            break
        elif x=="o":
            while True:
                try:
                    r=float(input("Gebe bitte den Zylinder Radius an: "))
                    h=float(input("Gebe bitte die Zylinder Höhe an: "))
                    zylindero= 2*math.pi*r**2+2*math.pi*r*h
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Oberfläche des Zylinders beträgt",zylindero,"Flächeneinheiten.")
            break
        elif x=="v":
            while True:
                try:
                    r=float(input("Gebe bitte den Zylinder Radius an: "))
                    h=float(input("Gebe bitte die Zylinder Höhe an: "))
                    zylinderv= math.pi*r**2*h
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Das Volumen des Zylinders beträgt",zylinderv,"Flächeneinheiten.")    
        elif x=="a":
            while True:
                try:
                    r=float(input("Gebe bitte den Zylinder Radius an: "))
                    h=float(input("Gebe bitte die Zylinder Höhe an: "))
                    zylinderv= math.pi*r**2*h
                    zylindero= 2*math.pi*r**2+2*math.pi*r*h
                    zylinderm= 2*math.pi*r*h
                    zylinderg= math.pi*r**2
                    zylinderu= 2*math.pi*r
                    break
                except ValueError:
                         print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Umfang des Zylinders beträgt",zylinderu,"Flächeneinheiten.")
            print ("Die Grundfläche des Zylinders beträgt",zylinderg, "Flächeneinheiten.")
            print ("Die Mantelfläche des Zylinders beträgt",zylinderm, "Flächeneinheiten.")
            print ("Die Oberfläche des Zylinders beträgt",zylindero,"Flächeneinheiten.")
            print ("Das Volumen des Zylinders beträgt",zylinderv,"Flächeneinheiten.")
            break

def pyramide():
    while True:
        x= None
        while x not in ("o", "v", "b"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x=input("Soll die Oberfläche[o], das Volumen [v] oder beides [b] von der Pyramide berechnet werden? ")
        if x=="o":
            while True:
                try:
                    g=float(input("Gebe bitte die Grundfläche der Pyramide an: "))
                    m=float(input("Gebe bitte die Mantelfläche der Pyramide an: "))
                    pyramideo=g+m
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Die Oberfläche der Pyramide beträgt",pyramideo,"Flächeneinheiten.")
            break
        elif x=="v":
            while True:
                try:
                    g=float(input("Gebe bitte die Grundfläche der Pyramide an: "))
                    h=float(input("Gebe bitte die Höhe der Pyramide an: "))
                    pyramidev= 1/3*g*h
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Das Volumen der Pyramide beträgt",pyramidev,"Flächeneinheiten.")
            break
        elif x=="b":
            while True:
                try:
                    g=float(input("Gebe bitte die Grundfläche der Pyramide an: "))
                    m=float(input("Gebe bitte die Mantelfläche der Pyramide an: "))
                    h=float(input("Gebe bitte die Höhe der Pyramide an: "))
                    pyramideo=g+m
                    pyramidev= 1/3*g*h
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Das Volumen der Pyramide beträgt",pyramidev,"Flächeneinheiten.")
            print("Die Oberfläche der Pyramide beträgt",pyramideo,"Flächeneinheiten.")
            break
     
def kegel():
    while True:
        x= None
        while x not in ("u", "g","s","m","o", "v", "a"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x=input("Soll der Umfang [u], die Grundfläche [g], , die Seitenlinie [s], das Volumen[v], die Oberfläche[o], die Mantelfläche [m] oder alles [a] vom Zylinder berechnet werden? ")
        if x=="u":
            while True:
                try:
                    r=float(input("Gebe bitte den Kegel Radius an: "))
                    kegelu= 2*math.pi*r
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Umfang des Kegels beträgt",kegelu,"Flächeneinheiten.")
            break
        elif x=="g":
            while True:
                try:
                    r=float(input("Gebe bitte den Kegel Radius an: "))
                    kegelg= math.pi*r**2
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Grundfläche des Kegels beträgt",kegelg, "Flächeneinheiten.")
            break
        elif x=="s":
            while True:
                try:
                    r=float(input("Gebe bitte den Kegel Radius an: "))
                    h=float(input("Gebe bitte die Kegel Höhe an: "))
                    kegels= math.sqrt(r**2+h**2)
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Seitenlinie des Kegels beträgt", kegels,"Flächeneinheiten.")
            break
        elif x=="m":
            while True:
                try:
                    r=float(input("Gebe bitte den Kegel Radius an: "))
                    h=float(input("Gebe bitte die Kegel Seitenlinie an: "))
                    kegelm= math.pi*r*s
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Mantelfläche des Kegels beträgt",kegelm, "Flächeneinheiten.")
            break
        elif x=="o":
            while True:
                try:
                    r=float(input("Gebe bitte den Kegel Radius an: "))
                    h=float(input("Gebe bitte die Kegel Seitenlinie an: "))
                    kegelo= math.pi*r**2+math.pi*r*s
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Oberfläche des Kegels beträgt",kegelo,"Flächeneinheiten.")
            break
        elif x=="v":
            while True:
                try:
                    r=float(input("Gebe bitte den Kegel Radius an: "))
                    h=float(input("Gebe bitte die Kegel Höhe an: "))
                    kegelv= 1/3*math.pi*r**2*h
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Das Volumen des Kegels beträgt",kegelv,"Flächeneinheiten.")
            break
        elif x=="a":
            while True:
                try:
                    r=float(input("Gebe bitte den Kegel Radius an: "))
                    h=float(input("Gebe bitte die Kegel Höhe an: "))
                    kegelv= 1/3*math.pi*r**2*h
                    kegelo= math.pi*r**2+math.pi*r*s
                    kegelm= math.pi*r*s
                    kegels= math.sqrt(r**2+h**2)
                    kegelg= math.pi*r**2
                    kegelu= 2*math.pi*r
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Umfang des Kegels beträgt",kegelu,"Flächeneinheiten.")
            print ("Die Grundfläche des Kegels beträgt",kegelg, "Flächeneinheiten.")
            print ("Die Seitenlinie des Kegels beträgt", kegels,"Flächeneinheiten.")
            print ("Die Mantelfläche des Kegels beträgt",kegelm, "Flächeneinheiten.")
            print ("Die Oberfläche des Kegels beträgt",kegelo,"Flächeneinheiten.")
            print ("Das Volumen des Kegels beträgt",kegelv,"Flächeneinheiten.")
            break
      
def kugel():
    while True:
        x= None
        while x not in ("o", "v", "b"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x=input("Soll die Oberfläche[o], das Volumen [v] oder beides [b] der Kugel berechnet werden? ")
        if x=="o":
            while True:
                try:
                    r=float(input("Gebe bitte den Kugel Radius an: "))
                    kugelo=4*math.pi*r**2
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Oberfläche der Kugel beträgt",kugelo, "Flächeneinheiten.")
            break
        
        elif x=="v":
            while True:
                try:
                    r=float(input("Gebe bitte den Kugel Radius an: "))
                    kugelv= 4/3*math.pi*r**3
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Das Volumen der Kugel beträgt",kugelv, "Flächeneinheiten.")
            break
   
        elif x=="b":
            while True:
                try:
                    r=float(input("Gebe bitte den Kugel Radius an: "))
                    kugelv= 4/3*math.pi*r**3
                    kugelo=4*math.pi*r**2
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Oberfläche der Kugel beträgt",kugelo, "Flächeneinheiten.")
            print ("Das Volumen der Kugel beträgt",kugelv, "Flächeneinheiten.")
            break
                    

#mainloop
            
while True:
        figurenauswahl()
        z = None
        while z not in ("ja","nein"):
                if z is not None:
                        print ("Sorry, das habe ich nicht verstanden.")
                z= input ("Sollen noch Berechnungen durchgeführt werden? ").lower()
        if z=="nein":
                print("Ok, bye!")
                input("Drücke eine beliebige Taste zum Schließen des Programms.") 
                break

                        
                            

        
        
    
        
            
        
        

        


