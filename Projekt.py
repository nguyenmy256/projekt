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
    x= None
    while x not in ("f", "b","u"):
        if x is not None:
            print ("Sorry, aber das habe ich nicht verstanden.")
        x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Quadrat ausrechnen willst. ")
        
        if x=="f":
            a=float(input("Gebe bitte die Länge des Quadrates an: "))
            quadrata= a**2
            print ("Der Flächeninhalt des Quadrats beträgt",quadrata,"Flächeneinheiten.")
        elif x=="u":
            a=float(input("Gebe bitte die Länge des Quadrates an: "))
            quadratu= 4*a
            print ("Der Umfang des Quadrates beträgt", quadratu,"Flächeneinheiten.")
        else:
            a=float(input("Gebe bitte die Länge des Quadrates an. "))
            quadratu= 4*a
            quadrata= a**2
            print ("Der Umfang des Quadrates beträgt", quadratu,"Flächeneinheiten.")
            print ("Der Flächeninhalt des Quadrats beträgt",quadrata,"Flächeneinheiten.")

def rechteck():
    x= None
    while x not in ("f", "b","u"):
        if x is not None:
             print ("Sorry, aber das habe ich nicht verstanden.")
        x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Rechteck ausrechnen willst. ")
        if x=="f":
            a= float(input("Gebe bitte die Länge des Rechtecks an: "))
            b= float(input("Gebe bitte die Breite des Rechtecks an: "))
            rechtecka= a*b
            print("Der Flächeninhalt des Rechtecks beträgt", rechtecka, "Flächeneinheiten.")
        elif x=="u":
            a= float(input("Gebe bitte die Länge des Rechtecks an: "))
            b= float(input("Gebe bitte die Breite des Rechtecks an: "))
            rechtecku= 2*a+2*b
            print("Der Umfang des Rechtecks beträgt", rechtecku, "Flächeneinheiten.")
        else:
            a= float(input("Gebe bitte die Länge des Rechtecks an: "))
            b= float(input("Gebe bitte die Breite des Rechtecks an: "))
            rechtecka= a*b
            rechtecku= 2*a+2*b
            print("Der Flächeninhalt des Rechtecks beträgt", rechtecka, "Flächeneinheiten.")
            print("Der Umfang des Rechtecks beträgt", rechtecku, "Flächeneinheiten.")
    
def dreieck():
    x= None
    while x not in ("f", "b","u"):
        if x is not None:
             print ("Sorry, aber das habe ich nicht verstanden.")
        x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Dreieck ausrechnen willst. ")
        if x=="f":
            g= float(input("Gebe bitte die Länge der Basis oder der Grundseite des Dreiecks an: "))
            h= float(input("Gebe bitte die Höhe des Dreiecks an: "))
            dreiecka= (g*h)/2
            print("Der Flächeninhalt des Dreiecks beträgt", dreiecka, "Flächeneinheiten.")
        elif x=="u":
            a= float(input("Gebe bitte die Länge der 1. Seite (Kathete) des Dreiecks an: "))
            b= float(input("Gebe bitte die Länge der 2. Seite (Kathete) des Dreiecks an: "))
            c= float(input("Gebe bitte die Länge der 3. Seite (Hypotenuse) des Dreiecks an: "))
            dreiecku= a+b+c
            print("Der Umfang des Dreiecks beträgt", dreiecku, "Flächeneinheiten.")
        else:
            g= float(input("Gebe bitte die Länge der Basis oder der Grundseite des Dreiecks an: "))
            h= float(input("Gebe bitte die Höhe des Dreiecks an: "))
            dreiecka= (g*h)/2
            a= float(input("Gebe bitte die Länge des 1. Schenkels des Dreiecks an: "))
            b= float(input("Gebe bitte die Länge des 2. Schenkels des Dreiecks an: "))
            dreiecku= a+b+g
            print("Der Flächeninhalt des Dreiecks beträgt", dreiecka, "Flächeneinheiten.")
            print("Der Umfang des Dreiecks beträgt", dreiecku, "Flächeneinheiten.")
        
def parallelogramm():
    x= None
    while x not in ("f", "b","u"):
        if x is not None:
            print ("Sorry, aber das habe ich nicht verstanden.")
        x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Parallelogramm ausrechnen willst. ")
        if x=="f":
            g= float(input("Gebe bitte die Länge der Grundseite des Parallelograms an: "))
            h= float(input("Gebe bitte die Höhe des Parallelograms an: "))
            parallelogramma= g*h
            print ("Der Flächeninhalt des Paralellograms beträgt",parallelogramma,"Flächeneinheiten. ")
        elif x=="u":
            a= float(input("Gebe bitte die Länge der 1. Seite des Parallelogramms an: "))
            b= float(input("Gebe bitte die Länge der 2. Seite des Paralellogramms an: "))
            parallelogrammu= 2*a+2*b
            print ("Der Umfang des Parallelogramms beträgt", parallelogrammu,"Flächeneinheiten. ")
        else:
            g= float(input("Gebe bitte die Länge der Grundseite des Parallelograms an: "))
            h= float(input("Gebe bitte die Höhe des Parallelograms an: "))
            parallelogramma= g*h
            a= float(input("Gene bitte die Länge der 1. Seite des Parallelogramms an: "))
            b=float(input("Gebe bitte die Länge der 2. Seite des Parallelogramms an: "))
            parallelogrammu= 2*a+2*b
            print ("Der Flächeninhalt des Paralellograms beträgt",parallelogramma,"Flächeneinheiten.")        
            print ("Der Umfang des Parallelogramms beträgt", parallelogrammu,"Flächeneinheiten.")
    
def trapez():
    x= None
    while x not in ("f", "b","u"):
        if x is not None:
            print ("Sorry, aber das habe ich nicht verstanden.")
        x= input ("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Trapez ausrechnen willst. ")
        if x=="f":
            a=float(input("Gebe bitte die Länge der 1. parallelen Seite des Trapez' an: "))
            c=float(input("Gebe bitte die Länge der 2. parallelen Seite des Trapez' an: "))
            h=float(input("Gebe bitte die Höhe des Trapez' an: "))
            trapeza= ((a+c)/2)*h
            print ("Der Flächeninhalt des Trapez' beträgt",trapeza,"Flächeneinheiten.")
        elif x=="u":
            a=float(input("Gebe bitte die Länge der 1. Seite des Trapez' an: "))
            b=float(input("Gebe bitte die Länge der 2. Seite des Trapez' an: "))
            c=float(input("Gebe bitte die Länge der 3. Seite des Trapez' an: "))
            d=float(input("Gebe bitte die Länge der 1. Seite des Trapez' an: "))
            trapezu=a+b+c+d
            print ("Der Umfang des Trapez' beträgt",trapezu,"Flächeneinheiten.")
        else:
            a=float(input("Gebe bitte die Länge der 1. parallelen Seite des Trapez' an: "))
            c=float(input("Gebe bitte die Länge der 2. parallelen Seite des Trapez' an: "))
            h=float(input("Gebe bitte die Höhe des Trapez' an: "))
            trapeza= ((a+c)/2)*h
            a=float(input("Gebe bitte die Länge der 1. Seite des Trapez' an: "))
            b=float(input("Gebe bitte die Länge der 2. Seite des Trapez' an: "))
            c=float(input("Gebe bitte die Länge der 3. Seite des Trapez' an: "))
            d=float(input("Gebe bitte die Länge der 1. Seite des Trapez' an: "))
            trapezu=a+b+c+d
            print ("Der Flächeninhalt des Trapez' beträgt",trapeza,"Flächeneinheiten.")
            print ("Der Umfang des Trapez' beträgt",trapezu,"Flächeneinheiten.")

def kreis():
    x= None
    while x not in ("f", "b","u", "a"):
        if x is not None:
            print ("Sorry, aber das habe ich nicht verstanden.")
        x= input ("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u], den Durchmesser[d] oder alles[a] vom Kreis ausrechnen willst. ")
        if x=="f":
            y=input("Ist der Radius[r] oder der Durchmesser[d] vorhanden?")
            if y=="r":
                r=float(input("Gebe bitte den Radius vom Kreis an: "))
                kreisa= math.pi*r**2
            else:
                d=float(input("Gebe bitte den Durchmesser vom Kreis an: "))
                kreisa= math.pi*((d/2)**2)
            print ("Der Flächeninhalt vom Kreis beträgt", kreisa, "Flächeneinheiten.")
        elif x=="u":
            y=input("Ist der Radius[r] oder der Durchmesser[d] vorhanden?")
            if y=="r":
                r=float(input("Gebe bitte den Radius vom Kreis an: "))
                kreisu= 2*math.pi*r
            else:
                d=float(input("Gebe bitte den Durchmesser vom Kreis an: "))
                kreisa= math.pi*d
            print ("Der Umfang vom Kreis beträgt", kreisu, "Flächeneinheiten.")
        elif x=="d":
                r=float(input("Gebe bitte den Radius vom Kreis an: "))
                kreisd= r*2
                print ("Der Durchmesser beträgt", kreisd,"Flächeneinheiten.")
        else:
                r=float(input("Gebe bitte den Radius vom Kreis an: "))
                kreisa=math.pi*r**2
                kreisu=2*math.pi*r
                kreisd=r*2
                print ("Der Flächeninhalt vom Kreis beträgt", kreisa, "Flächeneinheiten.")
                print ("Der Umfang vom Kreis beträgt", kreisu, "Flächeneinheiten.")
                print ("Der Durchmesser beträgt", kreisd,"Flächeneinheiten.")
        
def kreisbogen_kreissektor():
    x= None
    while x not in ("ks", "kb","b"):
        if x is not None:
            print ("Sorry, aber das habe ich nicht verstanden.")
        x=input ("Bitte gib an ob du den Kreissektor[ks], Kreisbogen[kb] oder beides[b] berechnen willst. ")
        if x=="ks":
            r=float(input("Gebe bitte den Radius des Kreises an: "))
            α=float(input("Gebe bitte den Winkel α des Kreissektors an: "))
            ks=math.pi*r**2*(math.radians(α)/math.radians(360))
            print ("Der Kreissektor beträgt",ks,"Flächeneinheiten.")
        elif x=="kb":
            r=float(input("Gebe bitte den Radius des Kreises an: "))
            α=float(input("Gebe bitte den Winkel α des Kreissektors an: "))
            kb=math.pi*r*(math.radians(α)/math.radians (180))
            print ("Der Kreisbogen beträgt",kb,"Flächeneinheiten.")
        else:
            r=float(input("Gebe bitte den Radius des Kreises an: "))
            α=float(input("Gebe bitte den Winkel α des Kreissektors an: "))
            ks=math.pi*r**2(*math.radians(α)/math.radians(360))
            kb=math.pi*r*(math.radians(α)/math.radians (180))
            print ("Der Kreissektor beträgt",ks,"Flächeneinheiten.")        
            print ("Der Kreisbogen beträgt",kb,"Flächeneinheiten.")
        
def würfel():
    x= None
    while x not in ("v", "o","b"):
        if x is not None:
            print ("Sorry, aber das habe ich nicht verstanden.")
        x=input("Möchtest du das Volumen[v], die Oberfläche[o] oder beides[b] vom Würfel berechnen? ")
        if x=="v":
            a=float(input("Gebe bitte die Kantenlänge des Würfels an: "))
            würfelv=(a*a*a)
            print ("Das Volumen des Würfels beträgt",würfelv,"Flächeneinheiten.")
        elif x=="o":
            a=float(input("Gebe bitte die Kantenlänge des Würfels an: "))
            würfelo= 6*a**2
            print ("Die Oberfläche des Würfels beträgt",würfelo,"Flächeneinheiten.")
        elif x=="b":
            a=float(input("Gebe bitte die Kantenlänge des Würfels an: "))
            würfelv=(a*a*a)
            würfelo= 6*a**2
            print ("Das Volumen des Würfels beträgt",würfelv,"Flächeneinheiten.")
            print ("Die Oberfläche des Würfels beträgt",würfelo,"Flächeneinheiten.")

def quader():
    x= None
    while x not in ("v", "o","b"):
        if x is not None:
            print ("Sorry, aber das habe ich nicht verstanden.")
        x=input ("Möchtest du das Volumen[v], die Oberfläche[o] oder beides[b] des Quaders berechnen? ")
        if x=="v":
            a= float(input("Gebe bitte die Länge des Quaders an: "))
            b= float(input("Gebe bitte die Breite des Quaders an: "))
            c= float (input("Gebe bitte die Höhe des Quaders an: "))
            quaderv= a*b*c
            print ("Das Volumen des Quaders beträgt",quaderv,"Flächeneinheiten.")
        elif x=="o":
            a= float(input("Gebe bitte die Länge des Quaders an: "))
            b= float(input("Gebe bitte die Breite des Quaders an: "))
            c= float (input("Gebe bitte die Höhe des Quaders an: "))
            quadero= 2*a*b+2*a*c+2*b*c
            print ("Die Oberfläche des Quaders beträgt",quadero,"Flächeneinheiten.")
        elif x=="b":
            a= float(input("Gebe bitte die Länge des Quaders an: "))
            b= float(input("Gebe bitte die Breite des Quaders an: "))
            c= float (input("Gebe bitte die Höhe des Quaders an: "))
            quadero= 2*a*b+2*a*c+2*b*c
            quaderv= a*b*c
            print ("Das Volumen des Quaders beträgt",quaderv,"Flächeneinheiten.")
            print ("Die Oberfläche des Quaders beträgt",quadero,"Flächeneinheiten.")
    
def prisma():
    x= None
    while x not in ("v", "o","m","a"):
        if x is not None:
            print ("Sorry, aber das habe ich nicht verstanden.")
        x=input("Soll das Volumen[v], die Oberfläche[o], die Mantelfläche [m] oder alles [a] vom Prisma berechnet werden? ")
        if x=="v":
            g= float(input("Gebe bitte die Grundfläche des Prismas an: "))
            h=float(input ("Gebe bitte die Höhe des Prismas an: "))
            prismav= g*h
            print ("Das Volumen des Prismas beträgt", prismav,"Flächeneinheiten.")
        elif x=="o":
            g= float (input("Gebe bitte die Grundfläche des Prismas an: "))
            m= float (input("Gebe die Mantelfläche des Prismas an: "))
            prismao= 2*g+m
            print ("Die Oberfläche des Prismas beträgt", prismao,"Flächeneinheiten.")
        elif x=="m":
            h=float(input ("Gebe bitte die Höhe des Prismas an: "))
            u=float(input("Gebe bitte den Umfang der Grundfläche des Prismas an: "))
            prismam= h*u
            print ("Die Mantelfläche des Prismas beträgt", prismam,"Flächeneinheiten.")
        else:
            g= float(input("Gebe bitte die Grundfläche des Prismas an: "))
            h=float(input ("Gebe bitte die Höhe des Prismas an: "))
            u=float(input("Gebe bitte den Umfang der Grundfläche des Prismas an: "))
            prismav= g*h
            prismao= 2*g+m
            prismam= h*u
            print ("Die Mantelfläche des Prismas beträgt", prismam,"Flächeneinheiten.")
            print ("Die Oberfläche des Prismas beträgt", prismao,"Flächeneinheiten.")
            print ("Das Volumen des Prismas beträgt", prismav,"Flächeneinheiten.")

def zylinder():
    x= None
    while x not in ("u", "g","m","o", "v", "a"):
        if x is not None:
            print ("Sorry, aber das habe ich nicht verstanden.")
        x=input("Soll der Umfang [u], die Grundfläche [g], das Volumen[v], die Oberfläche[o], die Mantelfläche [m] oder alles [a] vom Zylinder berechnet werden? ")
    if x=="u":
        r=float(input("Gebe bitte den Zylinder Radius an: "))
        zylinderu= 2*math.pi*r
        print ("Der Umfang des Zylinders beträgt",zylinderu,"Flächeneinheiten.")
    elif x=="g":
        r=float(input("Gebe bitte den Zylinder Radius an: "))
        zylinderg= math.pi*r**2
        print ("Die Grundfläche des Zylinders beträgt",zylinderg, "Flächeneinheiten.")
    elif x=="m":
        r=float(input("Gebe bitte den Zylinder Radius an: "))
        h=float(input("Gebe bitte die Zylinder Höhe an: "))
        zylinderm= 2*math.pi*r*h
        print ("Die Mantelfläche des Zylinders beträgt",zylinderm, "Flächeneinheiten.")
    elif x=="o":
        r=float(input("Gebe bitte den Zylinder Radius an: "))
        h=float(input("Gebe bitte die Zylinder Höhe an: "))
        zylindero= 2*math.pi*r**2+2*math.pi*r*h
        print ("Die Oberfläche des Zylinders beträgt",zylindero,"Flächeneinheiten.")
    elif x=="v":
        r=float(input("Gebe bitte den Zylinder Radius an: "))
        h=float(input("Gebe bitte die Zylinder Höhe an: "))
        zylinderv= math.pi*r**2*h
        print ("Das Volumen des Zylinders beträgt",zylinderv,"Flächeneinheiten.")
    else:
        r=float(input("Gebe bitte den Zylinder Radius an: "))
        h=float(input("Gebe bitte die Zylinder Höhe an: "))
        zylinderv= math.pi*r**2*h
        zylindero= 2*math.pi*r**2+2*math.pi*r*h
        zylinderm= 2*math.pi*r*h
        zylinderg= math.pi*r**2
        zylinderu= 2*math.pi*r
        print ("Der Umfang des Zylinders beträgt",zylinderu,"Flächeneinheiten.")
        print ("Die Grundfläche des Zylinders beträgt",zylinderg, "Flächeneinheiten.")
        print ("Die Mantelfläche des Zylinders beträgt",zylinderm, "Flächeneinheiten.")
        print ("Die Oberfläche des Zylinders beträgt",zylindero,"Flächeneinheiten.")
        print ("Das Volumen des Zylinders beträgt",zylinderv,"Flächeneinheiten.")

def pyramide():
    x= None
    while x not in ("o", "v", "b"):
        if x is not None:
            print ("Sorry, aber das habe ich nicht verstanden.")
        x=input("Soll die Oberfläche[o], das Volumen [v] oder beides [b] von der Pyramide berechnet werden? ")
    if x=="o":
        g=float(input("Gebe bitte die Grundfläche der Pyramide an: "))
        m=float(input("Gebe bitte die Mantelfläche der Pyramide an: "))
        pyramideo=g+m
        print("Die Oberfläche der Pyramide beträgt",pyramideo,"Flächeneinheiten.")
    elif x=="v":
        g=float(input("Gebe bitte die Grundfläche der Pyramide an: "))
        h=float(input("Gebe bitte die Höhe der Pyramide an: "))
        pyramidev= 1/3*g*h
        print("Das Volumen der Pyramide beträgt",pyramidev,"Flächeneinheiten.")
    else:
        g=float(input("Gebe bitte die Grundfläche der Pyramide an: "))
        m=float(input("Gebe bitte die Mantelfläche der Pyramide an: "))
        h=float(input("Gebe bitte die Höhe der Pyramide an: "))
        pyramideo=g+m
        pyramidev= 1/3*g*h
        print("Das Volumen der Pyramide beträgt",pyramidev,"Flächeneinheiten.")
        print("Die Oberfläche der Pyramide beträgt",pyramideo,"Flächeneinheiten.")

def kegel():
   x= None
   while x not in ("u", "g","s","m","o", "v", "a"):
        if x is not None:
            print ("Sorry, aber das habe ich nicht verstanden.")
        x=input("Soll der Umfang [u], die Grundfläche [g], , die Seitenlinie [s], das Volumen[v], die Oberfläche[o], die Mantelfläche [m] oder alles [a] vom Zylinder berechnet werden? ")
   if x=="u":
        r=float(input("Gebe bitte den Kegel Radius an: "))
        kegelu= 2*math.pi*r
        print ("Der Umfang des Kegels beträgt",kegelu,"Flächeneinheiten.")
   elif x=="g":
        r=float(input("Gebe bitte den Kegel Radius an: "))
        kegelg= math.pi*r**2
        print ("Die Grundfläche des Kegels beträgt",kegelg, "Flächeneinheiten.")
   elif x=="s":
        r=float(input("Gebe bitte den Kegel Radius an: "))
        h=float(input("Gebe bitte die Kegel Höhe an: "))
        kegels= math.sqrt(r**2+h**2)
        print ("Die Seitenlinie des Kegels beträgt", kegels,"Flächeneinheiten.")       
   elif x=="m":
        r=float(input("Gebe bitte den Kegel Radius an: "))
        h=float(input("Gebe bitte die Kegel Seitenlinie an: "))
        kegelm= math.pi*r*s
        print ("Die Mantelfläche des Kegels beträgt",kegelm, "Flächeneinheiten.")
   elif x=="o":
        r=float(input("Gebe bitte den Kegel Radius an: "))
        h=float(input("Gebe bitte die Kegel Seitenlinie an: "))
        kegelo= math.pi*r**2+math.pi*r*s
        print ("Die Oberfläche des Kegels beträgt",kegelo,"Flächeneinheiten.")
   elif x=="v":
        r=float(input("Gebe bitte den Kegel Radius an: "))
        h=float(input("Gebe bitte die Kegel Höhe an: "))
        kegelv= 1/3*math.pi*r**2*h
        print ("Das Volumen des Kegels beträgt",kegelv,"Flächeneinheiten.")
   else:
        r=float(input("Gebe bitte den Kegel Radius an: "))
        h=float(input("Gebe bitte die Kegel Höhe an: "))
        kegelv= 1/3*math.pi*r**2*h
        kegelo= math.pi*r**2+math.pi*r*s
        kegelm= math.pi*r*s
        kegels= math.sqrt(r**2+h**2)
        kegelg= math.pi*r**2
        kegelu= 2*math.pi*r
        print ("Der Umfang des Kegels beträgt",kegelu,"Flächeneinheiten.")
        print ("Die Grundfläche des Kegels beträgt",kegelg, "Flächeneinheiten.")
        print ("Die Seitenlinie des Kegels beträgt", kegels,"Flächeneinheiten.")
        print ("Die Mantelfläche des Kegels beträgt",kegelm, "Flächeneinheiten.")
        print ("Die Oberfläche des Kegels beträgt",kegelo,"Flächeneinheiten.")
        print ("Das Volumen des Kegels beträgt",kegelv,"Flächeneinheiten.")

def kugel():
    x= None
    while x not in ("o", "v", "b"):
        if x is not None:
            print ("Sorry, aber das habe ich nicht verstanden.")
        x=input("Soll die Oberfläche[o], das Volumen [v] oder beides [b] der Kugel berechnet werden? ")
    if x=="o":
        r=float(input("Gebe bitte den Kugel Radius an: "))
        kugelo=4*math.pi*r**2
        print ("Die Oberfläche der Kugel beträgt",kugelo, "Flächeneinheiten.")
    elif x=="v":
        r=float(input("Gebe bitte den Kugel Radius an: "))
        kugelv= 4/3*math.pi*r**3
        print ("Das Volumen der Kugel beträgt",kugelv, "Flächeneinheiten.")
    else:
        r=float(input("Gebe bitte den Kugel Radius an: "))
        kugelv= 4/3*math.pi*r**3
        kugelo=4*math.pi*r**2
        print ("Die Oberfläche der Kugel beträgt",kugelo, "Flächeneinheiten.")
        print ("Das Volumen der Kugel beträgt",kugelv, "Flächeneinheiten.")
        

#mainloop
            
while True:
    start = None
    while start not in ("ja", "nein"):
        if start is not None:
            print("Sorry, aber das habe ich nicht verstanden.")
        start = input("Möchtest du geometrische Berechnungen durchführen?[ja/nein]: ")
    if start == "nein":
        print("Ok, bye!")
        input("Drücke eine beliebige Taste zum Schließen des Programms.") 
        break
    if start =="ja":
        figurenauswahl()        
    


    
    
        
        
        

        
        
    
        
            
        
        

        


