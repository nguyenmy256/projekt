#Projekt-Geometrierechner
#import math für Pi und Gradzahlen
import math

"""
Menü
Das Programm wird am Anfang erstmal vorgestellt:
- Sinn und Zweck des Programms (Berechnungen von Körpern und Figuren)
- Wie eine Auswahl getroffen wird
- Auswahl über die verfügbaren Körpern und Figuren wird vorgestellt
"""

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

#Zuordnung der Figuren zu ihrer jeweiligen Zahl oder Buchstaben    
def figurenauswahl():
#Benutzer wählt eine Figur aus
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
#Dafür, wenn der Benutzer eine falsche Eingabe getätigt hat
        else:
                print ("Ups. Da ist wohl was falsch gelaufen. Wähle demnächst bitte ein Objekt aus der Liste aus.")
                
                
    
#Berechnungen zum Quadrat
def quadrat():
    while True:
        x= None
#while-loop für die Ermittlung von falschen Eingaben
        while x not in ("f", "b","u"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
#Der Benutzer wählt aus was er berechnen will
            x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Quadrat ausrechnen willst. ")
#Flächeninhalt (Quadrat)
        if x=="f":
            while True:
                try:
                    a=float(input("Gebe bitte die Länge des Quadrates an: "))
#Formel zum Flächeninhalt (Quadrat)
                    quadrata= a**2
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Flächeninhalt des Quadrats beträgt",quadrata,"Flächeneinheiten.")
#Umfang (Quadrat)
        elif x=="u":
            while True:
                try:
                    a=float(input("Gebe bitte die Länge des Quadrates an: "))
#Formel für den Umfang (Quadrat)
                    quadratu= 4*a
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")                  
            print ("Der Umfang des Quadrates beträgt", quadratu,"Flächeneinheiten.")
            break
#Flächeninhalt+Umfang
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
                
#Berechnungen zum Rechteck
def rechteck():
    while True:
        x= None
#while-loop für die Ermittlung von falschen Eingaben
        while x not in ("f", "b","u"):
            if x is not None:
                 print ("Sorry, aber das habe ich nicht verstanden.")
            x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Rechteck ausrechnen willst. ")           
#Flächeninhalt (Rechteck)
        if x=="f":
            while True:
                try:
                    a= float(input("Gebe bitte die Länge des Rechtecks an: "))
                    b= float(input("Gebe bitte die Breite des Rechtecks an: "))
#Formel für den Flächeninhalt (Rechteck)
                    rechtecka= a*b
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Der Flächeninhalt des Rechtecks beträgt", rechtecka, "Flächeneinheiten.")
            break
#Umfang (Rechteck)
        elif x=="u":
            while True:
                try:
                    a= float(input("Gebe bitte die Länge des Rechtecks an: "))
                    b= float(input("Gebe bitte die Breite des Rechtecks an: "))
#Formel für den Umfang (Rechteck)
                    rechtecku= 2*a+2*b
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Der Umfang des Rechtecks beträgt", rechtecku, "Flächeneinheiten.")
            break
#Flächeninhalt+Umfang (Rechteck)
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

#Berechnungen zum Dreieck    
def dreieck():
    while True:
        x= None
        while x not in ("f", "b","u"):
            if x is not None:
                 print ("Sorry, aber das habe ich nicht verstanden.")
            x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Dreieck ausrechnen willst. ")
#Flächeninhalt (Dreieck)
        if x=="f":
            while True:
                try:
                    g= float(input("Gebe bitte die Länge der Basis oder der Grundseite des Dreiecks an: "))
                    h= float(input("Gebe bitte die Höhe des Dreiecks an: "))
#Formel für den Flächeninhalt (Dreieck)
                    dreiecka= (g*h)/2
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Der Flächeninhalt des Dreiecks beträgt", dreiecka, "Flächeneinheiten.")
            break
#Umfang
        elif x=="u":
            while True:
                try:
                    a= float(input("Gebe bitte die Länge der 1. Seite (Kathete) des Dreiecks an: "))
                    b= float(input("Gebe bitte die Länge der 2. Seite (Kathete) des Dreiecks an: "))
                    c= float(input("Gebe bitte die Länge der 3. Seite (Hypotenuse) des Dreiecks an: "))
#Formel für den Umfang (Dreieck)
                    dreiecku= a+b+c
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Der Umfang des Dreiecks beträgt", dreiecku, "Flächeneinheiten.")
            break
#Umfang+Flächeninhalt (Dreieck)
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
        
#Berechnungen zum Parallelogramm        
def parallelogramm():
    while True:
        x= None
        while x not in ("f", "b","u"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Parallelogramm ausrechnen willst. ")
#Flächeninhalt (Parallelogramm)
        if x=="f":
            while True:
                try:
                    g= float(input("Gebe bitte die Länge der Grundseite des Parallelograms an: "))
                    h= float(input("Gebe bitte die Höhe des Parallelograms an: "))
#Formel für den Flächeninhalt (Parallelogramm)
                    parallelogramma= g*h
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Flächeninhalt des Paralellograms beträgt",parallelogramma,"Flächeneinheiten. ")
            break
#Umfang (Parallelogramm)
        elif x=="u":
            while True:
                try:
                    a= float(input("Gebe bitte die Länge der 1. Seite des Parallelogramms an: "))
                    b= float(input("Gebe bitte die Länge der 2. Seite des Paralellogramms an: "))
#Formel für den Umfang (Parallelogramm)
                    parallelogrammu= 2*a+2*b
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Umfang des Parallelogramms beträgt", parallelogrammu,"Flächeneinheiten. ")
            break
#Flächeninhalt+Umfang (Parallelogramm)
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

#Berechnungen zum Trapez    
def trapez():
    while True:
        x= None
        while x not in ("f", "b","u"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x= input ("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Trapez ausrechnen willst. ")
#Flächeninhalt (Trapez)
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
#Umfang (Trapez)
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
#Umfang+Flächeninhalt (Trapez)
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

#Berechnungen zum Kreis
def kreis():
    while True:
        x= None
        while x not in ("f", "b","u", "a"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x= input ("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u], den Durchmesser[d] oder alles[a] vom Kreis ausrechnen willst. ")
#Flächeninhalt (Kreis)
        if x=="f":
            while True:
                y= None
                while y not in ("r","d"):
                    if y is not None:
                        print ("Diese Eingabe war leider ungültig. Neuer Versuch?")
                    y=input("Ist der Radius[r] oder der Durchmesser[d] vorhanden?")
#Berechnungen zum Flächeninhalt, wenn der Radius vorhanden ist
            if y=="r":
                while True:
                    try:
                        r=float(input("Gebe bitte den Radius vom Kreis an: "))
                        kreisa= math.pi*r**2
                        break
                    except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
#Berechnungen zum Flächeninhalt, wenn der Durchmesser vorhanden ist
                        
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
#Umfang (Kreis)
        elif x=="u":
            while True:
                y= None
                while y not in ("r","d"):
                    if y is not None:
                        print ("Diese Eingabe war leider ungültig. Neuer Versuch?")
                    y=input("Ist der Radius[r] oder der Durchmesser[d] vorhanden?")
#Berechnungen zum Umfang, wenn der Radius vorhanden ist
            if y=="r":
                while True:
                    try:
                        r=float(input("Gebe bitte den Radius vom Kreis an: "))
                        kreisu= 2*math.pi*r
                        break
                    except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
#Berechnungen zum Umfang, wenn der Radius vorhanden ist
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
#Durchmesser (Kreis)
        elif x=="d":
            while True:
                 try:
                        r=float(input("Gebe bitte den Radius vom Kreis an: "))
#Formel für den Durchmesser (Kreis)
                        kreisd= r*2
                        break
                 except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
                 print ("Der Durchmesser beträgt", kreisd,"Flächeneinheiten.")
                 break
#Durchmesser+Flächeninhalt+Umfang (Kreis)
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

#Berechnungen zum Kreisbogen bzw. Kreissektor        
def kreisbogen_kreissektor():
    while True:
        x= None
        while x not in ("ks", "kb","b"):
            if x is not None:
               print ("Sorry, aber das habe ich nicht verstanden.")
            x=input ("Bitte gib an ob du den Kreissektor[ks], Kreisbogen[kb] oder beides[b] berechnen willst. ")
#Kreissektor
        if x=="ks":
            while True:
                try:
                    r=float(input("Gebe bitte den Radius des Kreises an: "))
                    α=float(input("Gebe bitte den Winkel α des Kreissektors an: "))
#Formel für den Kreissektor
                    ks=math.pi*r**2*(math.radians(α)/math.radians(360))
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Kreissektor beträgt",ks,"Flächeneinheiten.")
            break
#Kreisbogen
        elif x=="kb":
            while True:
                try:
                    r=float(input("Gebe bitte den Radius des Kreises an: "))
                    α=float(input("Gebe bitte den Winkel α des Kreissektors an: "))
#Formel für den Kreisbogen
                    kb=math.pi*r*(math.radians(α)/math.radians (180))
                    break
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Kreisbogen beträgt",kb,"Flächeneinheiten.")
            break
#Kreisbogen+Kreissektor
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

#Berechnungen zum Würfel        
def würfel():
    while True:
        x= None
        while x not in ("v", "o","b"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x=input("Möchtest du das Volumen[v], die Oberfläche[o] oder beides[b] vom Würfel berechnen? ")
#Volumen (Würfel)
        if x=="v":
            while True:
                try:
                    a=float(input("Gebe bitte die Kantenlänge des Würfels an: "))
#Formel fürs Volumen (Würfel)
                    würfelv=(a*a*a)
                except ValueError:
                    print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Das Volumen des Würfels beträgt",würfelv,"Flächeneinheiten.")
            break
#Oberfläche (Würfel)                               
        elif x=="o":
            while True:
                try:
                    a=float(input("Gebe bitte die Kantenlänge des Würfels an: "))
#Formel für die Oberfläche (Würfel)
                    würfelo= 6*a**2
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Oberfläche des Würfels beträgt",würfelo,"Flächeneinheiten.")
            break
#Oberfläche+Volumen (Würfel)
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

#Berechnungen zum Quader
def quader():
    while True:
        x= None
        while x not in ("v", "o","b"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x=input ("Möchtest du das Volumen[v], die Oberfläche[o] oder beides[b] des Quaders berechnen? ")
#Volumen (Quader)
        if x=="v":
            while True:
                try:
                    a= float(input("Gebe bitte die Länge des Quaders an: "))
                    b= float(input("Gebe bitte die Breite des Quaders an: "))
                    c= float (input("Gebe bitte die Höhe des Quaders an: "))
#Formel fürs Volumen (Quader)
                    quaderv= a*b*c
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Das Volumen des Quaders beträgt",quaderv,"Flächeneinheiten.")
            break
#Oberfläche (Quader)
        elif x=="o":
            while True:
                try:
                    a= float(input("Gebe bitte die Länge des Quaders an: "))
                    b= float(input("Gebe bitte die Breite des Quaders an: "))
                    c= float (input("Gebe bitte die Höhe des Quaders an: "))
#Formel für die Oberfläche (Quader)
                    quadero= 2*a*b+2*a*c+2*b*c
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Oberfläche des Quaders beträgt",quadero,"Flächeneinheiten.")
            break
#Oberfläche+Volumen (Quader)
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

#Berechnungen zum Prisma    
def prisma():
    while True:
        x= None
        while x not in ("v", "o","m","a"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x=input("Soll das Volumen[v], die Oberfläche[o], die Mantelfläche[m] oder alles[a] vom Prisma berechnet werden? ")
#Volumen (Prisma)
        if x=="v":
            while True:
                try:
                    g= float(input("Gebe bitte die Grundfläche des Prismas an: "))
                    h=float(input ("Gebe bitte die Höhe des Prismas an: "))
#Formel fürs Volumen (Prisma)
                    prismav= g*h
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")                               
            print ("Das Volumen des Prismas beträgt", prismav,"Flächeneinheiten.")
            break
#Oberfläche (Prisma)
        elif x=="o":
            while True:
                try:
                    g= float (input("Gebe bitte die Grundfläche des Prismas an: "))
                    m= float (input("Gebe die Mantelfläche des Prismas an: "))
#Formel für die Oberfläche (Prisma)
                    prismao= 2*g+m
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Oberfläche des Prismas beträgt", prismao,"Flächeneinheiten.")
            break
#Mantelfläche (Prisma)
        elif x=="m":
            while True:
                try:
                    h=float(input ("Gebe bitte die Höhe des Prismas an: "))
                    u=float(input("Gebe bitte den Umfang der Grundfläche des Prismas an: "))
#Formel für die Mantelfläche (Prisma)
                    prismam= h*u
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Mantelfläche des Prismas beträgt", prismam,"Flächeneinheiten.")
            break
#Mantelfläche+Oberfläche+Volumen
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

#Berechnungen zum Zylinder
def zylinder():
    while True:
        x= None
        while x not in ("u", "g","m","o", "v", "a"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x=input("Soll der Umfang[u], die Grundfläche[g], das Volumen[v], die Oberfläche[o], die Mantelfläche[m] oder alles[a] vom Zylinder berechnet werden? ")
#Umfang (Zylinder)
        if x=="u":
            while True:
                try:
                    r=float(input("Gebe bitte den Zylinder Radius an: "))
#Formel für den Umfang (Zylinder)
                    zylinderu= 2*math.pi*r
                    break
                except ValueError:
                         print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Umfang des Zylinders beträgt",zylinderu,"Flächeneinheiten.")
            break
#Grundfläche (Zylinder)
        elif x=="g":
            while True:
                try:
                    r=float(input("Gebe bitte den Zylinder Radius an: "))
#Formel für die Grundfläche (Zylinder)
                    zylinderg= math.pi*r**2
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Grundfläche des Zylinders beträgt",zylinderg, "Flächeneinheiten.")
            break
#Mantelfläche (Zylinder)
        elif x=="m":
            while True:
                try:
                    r=float(input("Gebe bitte den Zylinder Radius an: "))
                    h=float(input("Gebe bitte die Zylinder Höhe an: "))
#Formel für die Mantelfläche (Zylinder)
                    zylinderm= 2*math.pi*r*h
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Mantelfläche des Zylinders beträgt",zylinderm, "Flächeneinheiten.")
            break
#Oberfläche
        elif x=="o":
            while True:
                try:
                    r=float(input("Gebe bitte den Zylinder Radius an: "))
                    h=float(input("Gebe bitte die Zylinder Höhe an: "))
#Formel für die Oberfläche (Zylinder)
                    zylindero= 2*math.pi*r**2+2*math.pi*r*h
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Oberfläche des Zylinders beträgt",zylindero,"Flächeneinheiten.")
            break
#Volumen (Zylinder)
        elif x=="v":
            while True:
                try:
                    r=float(input("Gebe bitte den Zylinder Radius an: "))
                    h=float(input("Gebe bitte die Zylinder Höhe an: "))
#Formel für das Volumen (Zylinder)
                    zylinderv= math.pi*r**2*h
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Das Volumen des Zylinders beträgt",zylinderv,"Flächeneinheiten.")    
#Volumen+Oberfläche+Mantelfläche+Grundfläche+Umfang
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

#Berechnungen zur Pyramide
def pyramide():
    while True:
        x= None
        while x not in ("o", "v", "b"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x=input("Soll die Oberfläche[o], das Volumen[v] oder beides[b] von der Pyramide berechnet werden? ")
#Oberfläche (Pyramide)
        if x=="o":
            while True:
                try:
                    g=float(input("Gebe bitte die Grundfläche der Pyramide an: "))
                    m=float(input("Gebe bitte die Mantelfläche der Pyramide an: "))
#Formel für die Oberfläche (Pyramide)
                    pyramideo=g+m
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Die Oberfläche der Pyramide beträgt",pyramideo,"Flächeneinheiten.")
            break
#Volumen (Pyramide)
        elif x=="v":
            while True:
                try:
                    g=float(input("Gebe bitte die Grundfläche der Pyramide an: "))
                    h=float(input("Gebe bitte die Höhe der Pyramide an: "))
#Formel für das Volumen (Pyramide)
                    pyramidev= 1/3*g*h
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print("Das Volumen der Pyramide beträgt",pyramidev,"Flächeneinheiten.")
            break
#Volumen+Oberfläche (Pyramide)
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

#Berechnungen zum Kegel    
def kegel():
    while True:
        x= None
        while x not in ("u", "g","s","m","o", "v", "a"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x=input("Soll der Umfang[u], die Grundfläche[g], die Seitenlinie[s], das Volumen[v], die Oberfläche[o], die Mantelfläche[m] oder alles[a] vom Kegel berechnet werden? ")
#Umfang (Kegel)
        if x=="u":
            while True:
                try:
                    r=float(input("Gebe bitte den Kegel Radius an: "))
#Formel für den Umfang (Kegel)
                    kegelu= 2*math.pi*r
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Umfang des Kegels beträgt",kegelu,"Flächeneinheiten.")
            break
#Grundfläche (Kegel)
        elif x=="g":
            while True:
                try:
                    r=float(input("Gebe bitte den Kegel Radius an: "))
#Formel für die Grundfläche (Kegel)
                    kegelg= math.pi*r**2
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Grundfläche des Kegels beträgt",kegelg, "Flächeneinheiten.")
            break
#Seitenlinie (Kegel)
        elif x=="s":
            while True:
                try:
                    r=float(input("Gebe bitte den Kegel Radius an: "))
                    h=float(input("Gebe bitte die Kegel Höhe an: "))
#Formel für die Seitenlinie (Kegel)
                    kegels= math.sqrt(r**2+h**2)
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Seitenlinie des Kegels beträgt", kegels,"Flächeneinheiten.")
            break
#Mantelfläche (Kegel)
        elif x=="m":
            while True:
                try:
                    r=float(input("Gebe bitte den Kegel Radius an: "))
                    h=float(input("Gebe bitte die Kegel Seitenlinie an: "))
#Formel für die Mantelfläche (Kegel)
                    kegelm= math.pi*r*s
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Mantelfläche des Kegels beträgt",kegelm, "Flächeneinheiten.")
            break
#Oberfläche (Kegel)
        elif x=="o":
            while True:
                try:
                    r=float(input("Gebe bitte den Kegel Radius an: "))
                    h=float(input("Gebe bitte die Kegel Seitenlinie an: "))
#Formel für die Oberfläche (Kegel)
                    kegelo= math.pi*r**2+math.pi*r*s
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Oberfläche des Kegels beträgt",kegelo,"Flächeneinheiten.")
            break
#Volumen (Kegel)       
        elif x=="v":
            while True:
                try:
                    r=float(input("Gebe bitte den Kegel Radius an: "))
                    h=float(input("Gebe bitte die Kegel Höhe an: "))
#Formel fürs Volumen (Kegel)
                    kegelv= 1/3*math.pi*r**2*h
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Das Volumen des Kegels beträgt",kegelv,"Flächeneinheiten.")
            break
#Volumen+Oberfläche+Mantelfläche+Seitenlinie+Grundfläche+Umfang
        elif x=="a":
            while True:
                try:
                    r=float(input("Gebe bitte den Kegel Radius an: "))
                    h=float(input("Gebe bitte die Kegel Höhe an: "))
                    s= math.sqrt(r**2+h**2)
                    kegelv= 1/3*math.pi*r**2*h
                    kegelo= math.pi*r**2+math.pi*r*s
                    kegelm= math.pi*r*s
                    kegelg= math.pi*r**2
                    kegelu= 2*math.pi*r
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Der Umfang des Kegels beträgt",kegelu,"Flächeneinheiten.")
            print ("Die Grundfläche des Kegels beträgt",kegelg, "Flächeneinheiten.")
            print ("Die Seitenlinie des Kegels beträgt", s,"Flächeneinheiten.")
            print ("Die Mantelfläche des Kegels beträgt",kegelm, "Flächeneinheiten.")
            print ("Die Oberfläche des Kegels beträgt",kegelo,"Flächeneinheiten.")
            print ("Das Volumen des Kegels beträgt",kegelv,"Flächeneinheiten.")
            break

#Berechnungen zur Kugel      
def kugel():
    while True:
        x= None
        while x not in ("o", "v", "b"):
            if x is not None:
                print ("Sorry, aber das habe ich nicht verstanden.")
            x=input("Soll die Oberfläche[o], das Volumen[v] oder beides[b] der Kugel berechnet werden? ")
#Oberfläche (Kugel)
        if x=="o":
            while True:
                try:
                    r=float(input("Gebe bitte den Kugel Radius an: "))
#Formel für die Oberfläche (Kugel)
                    kugelo=4*math.pi*r**2
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Die Oberfläche der Kugel beträgt",kugelo, "Flächeneinheiten.")
            break
#Volumen       
        elif x=="v":
            while True:
                try:
                    r=float(input("Gebe bitte den Kugel Radius an: "))
#Formel fürs Volumen (Kugel)
                    kugelv= 4/3*math.pi*r**3
                    break
                except ValueError:
                        print ("Das war leider eine ungültige Eingabe. Bitte versuche es noch einmal.")
            print ("Das Volumen der Kugel beträgt",kugelv, "Flächeneinheiten.")
            break
#Volumen+Oberfläche   
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
                    

"""
main-loop des Programms
Programm wird, nach dem aufzeigen des obigen Menüs, erst richtig mit dem aufrufen der "figurenauswahl" gestartet.
z-Variable fragt den Benutzer ab, ob er noch weitere Berechnungen durchführen will oder nicht.
"""
            
while True:
        figurenauswahl()
        z = None
        while z not in ("ja","nein"):
                if z is not None:
                        print ("Sorry, das habe ich nicht verstanden.")
                z= input ("Sollen noch Berechnungen durchgeführt werden?[ja/nein] ").lower()
        if z=="nein":
                print("Ok, bye!")
                input("Drücke eine beliebige Taste zum Schließen des Programms.") 
                break

                        
                            

        
        
    
        
            
        
        

        


