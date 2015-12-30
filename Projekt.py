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
print ("               - Trapez [5]                                 - Quadratische Pyramide [e]")
print ("               - Kreis [6]                                  - Kegel [f]")
print ("               - Kreisbogen und Kreissektor [7]             - Kugel [g]")

figurenauswahl= input ("Bitte wähle eine der oben aufgezählten Figuren aus: ")
if figurenauswahl == "1":

    x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Quadrat ausrechnen willst. ")
    if x=="f":
        try:
                a=float(input("Gib die Länge des Quadrates an. "))
                quadrata= a*a
                print ("Der Flächeninhalt des Quadrats beträgt",quadrata,"Flächeneinheiten.")
        except ValueError:
            pass
    elif x=="u":
        a=float(input("Gib die Länge des Quadrates an. "))
        quadratu= 4*a
        print ("Der Umfang des Quadrates beträgt", quadratu,"Flächeneinheiten.")
    else:
        a=float(input("Gib die Länge des Quadrates an. "))
        quadratu= 4*a
        quadrata= a*a
        print ("Der Umfang des Quadrates beträgt", quadratu,"Flächeneinheiten.")
        print ("Der Flächeninhalt des Quadrats beträgt",quadrata,"Flächeneinheiten.")

elif figurenauswahl=="2":
    x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Rechteck ausrechnen willst. ")
    if x=="f":
        a= float(input("Gib die Länge des Rechtecks an. "))
        b= float(input("Gib die Breite des Rechtecks an. "))
        rechtecka= a*b
        print("Der Flächeninhalt des Rechtecks beträgt", rechtecka, "Flächeneinheiten.")
    elif x=="u":
        a= float(input("Gib die Länge des Rechtecks an. "))
        b= float(input("Gib die Breite des Rechtecks an. "))
        rechtecku= 2*a+2*b
        print("Der Umfang des Rechtecks beträgt", rechtecku, "Flächeneinheiten.")
    else:
        a= float(input("Gib die Länge des Rechtecks an. "))
        b= float(input("Gib die Breite des Rechtecks an. "))
        rechtecka= a*b
        rechtecku= 2*a+2*b
        print("Der Flächeninhalt des Rechtecks beträgt", rechtecka, "Flächeneinheiten.")
        print("Der Umfang des Rechtecks beträgt", rechtecku, "Flächeneinheiten.")

elif figurenauswahl =="3":
    x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Dreieck ausrechnen willst. ")
    if x=="f":
        g= float(input("Gib die Länge der Basis oder der Grundseite des Dreiecks an. "))
        h= float(input("Gib die Höhe des Dreiecks an. "))
        dreiecka= (g*h)/2
        print("Der Flächeninhalt des Dreiecks beträgt", dreiecka, "Flächeneinheiten.")
    elif x=="u":
        a= float(input("Gib die Länge der 1. Seite des Dreiecks an. "))
        b= float(input("Gib die Länge der 2. Seite des Dreiecks an. "))
        c= float(input("Gib die Länge der 3. Seite des Dreiecks an. "))
        dreiecku= a+b+c
        print("Der Umfang des Dreiecks beträgt", dreiecku, "Flächeneinheiten.")
    else:
        g= float(input("Gib die Länge der Basis oder der Grundseite des Dreiecks an. "))
        h= float(input("Gib die Höhe des Dreiecks an. "))
        dreiecka= (g*h)/2
        a= float(input("Gib die Länge des 1. Schenkel des Dreiecks an. "))
        b= float(input("Gib die Länge der 2. Schenkel des Dreiecks an. "))
        dreiecku= a+b+g
        print("Der Flächeninhalt des Dreiecks beträgt", dreiecka, "Flächeneinheiten.")
        print("Der Umfang des Dreiecks beträgt", dreiecku, "Flächeneinheiten.")

elif figurenauswahl =="4":
    x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Parallelogramm ausrechnen willst. ")
    if x=="f":
        g= float(input("Gib die Länge der Grundseite des Parallelograms an. "))
        h= float(input("Gib die Höhe des Parallelograms an. "))
        parallelogramma= g*h
        print ("Der Flächeninhalt des Paralellograms beträgt",paralellogramma,"Flächeneinheiten. ")
    elif x=="u":
        a= float(input("Gib die Länge der 1. Seite des Paralleogramms an"))
        b=float(input("Gib die Länge der 2. Seite des Paralellogramms an"))
        parallelogrammu= 2*a+2*b
        print ("Der Umfang des Parallelogramms beträgt", parallelogrammu,"Flächeneinheiten. ")
    else:
        g= float(input("Gib die Länge der Grundseite des Parallelograms an. "))
        h= float(input("Gib die Höhe des Parallelograms an. "))
        parallelogramma= g*h 
        a= float(input("Gib die Länge der 1. Seite des Paralleogramms an. "))
        b=float(input("Gib die Länge der 2. Seite des Paralellogramms an. "))
        parallelogrammu= 2*a+2*b
        print ("Der Flächeninhalt des Paralellograms beträgt",paralellogramma,"Flächeneinheiten.")        
        print ("Der Umfang des Parallelogramms beträgt", parallelogrammu,"Flächeneinheiten.")

elif figurenauswahl=="5":
    x= input ("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] vom Trapez ausrechnen willst. ")
    if x=="f":
        a=float(input("Gib die Länge der 1. parallelen Seite des Trapez' an. "))
        c=float(input("Gib die Länge der 2. parallelen Seite des Trapez' an. "))
        h=float(input("Gib die Höhe des Trapez' an. "))
        trapeza= ((a+c)/2)*h
        print ("Der Flächeninhalt des Trapez' beträgt",trapeza,"Flächeneinheiten.")
    elif x=="u":
        a=float(input("Gib die Länge der 1. Seite des Trapez' an"))
        b=float(input("Gib die Länge der 2. Seite des Trapez' an. "))
        c=float(input("Gib die Länge der 3. Seite des Trapez' an. "))
        d=float(input("Gib die Länge der 1. Seite des Trapez' an. "))
        trapezu=a+b+c+d
        print ("Der Umfang des Trapez' beträgt",trapezu,"Flächeneinheiten.")
    else:
        a=float(input("Gib die Länge der 1. parallelen Seite des Trapez' an. "))
        c=float(input("Gib die Länge der 2. parallelen Seite des Trapez' an. "))
        h=float(input("Gib die Höhe des Trapez' an. "))
        trapeza= ((a+c)/2)*h
        a=float(input("Gib die Länge der 1. Seite des Trapez' an. "))
        b=float(input("Gib die Länge der 2. Seite des Trapez' an. "))
        c=float(input("Gib die Länge der 3. Seite des Trapez' an. "))
        d=float(input("Gib die Länge der 1. Seite des Trapez' an. "))
        trapezu=a+b+c+d
        print ("Der Flächeninhalt des Trapez' beträgt",trapeza,"Flächeneinheiten.")
        print ("Der Umfang des Trapez' beträgt",trapezu,"Flächeneinheiten.")

elif figurenauswahl=="6":
    x= input ("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u], den Durchmesser[d] oder alles[a] vom Kreis ausrechnen willst. ")
    if x=="f":
        y=input("Ist der Radius[r] oder der Durchmesser[d] vorhanden?")
        if y=="r":
            r=float(input("Gib den Radius vom Kreis an. "))
            kreisa= math.pi*(r*r)
        else:
            d=float(input("Gib den Durchmesser vom Kreis an "))
            kreisa= math.pi*((d*d)/4)
        print ("Der Flächeninhalt vom Kreis beträgt", kreisa, "Flächeneinheiten.")
    elif x=="u":
         y=input("Ist der Radius[r] oder der Durchmesser[d] vorhanden?")
         if y=="r":
            r=float(input("Gib den Radius vom Kreis an. "))
            kreisu= 2*math.pi*r
         else:
            d=float(input("Gib den Durchmesser vom Kreis an. "))
            kreisa= math.pi*d
         print ("Der Umfang vom Kreis beträgt", kreisu, "Flächeneinheiten.")
    elif x=="d":
         r=float(input("Gib den Radius vom Kreis an."))
         kreisd= r*2
         print ("Der Durchmesser beträgt", kreisd,"Flächeneinheiten.")
    else:
        r=float(input("Gib den Radius vom Kreis an. "))
        kreisa=math.pi*(r*r)
        kreisu=2*math.pi*r
        kreisd=r*2
        print ("Der Flächeninhalt vom Kreis beträgt", kreisa, "Flächeneinheiten.")
        print ("Der Umfang vom Kreis beträgt", kreisu, "Flächeneinheiten.")
        print ("Der Durchmesser beträgt", kreisd,"Flächeneinheiten.")

elif figurenauswahl=="7":
    x=input ("Bitte gib an ob du den Kreissektor[ks], Kreisbogen[kb] oder beides[b] berechnen willst. ")
    if x=="ks":
        r=float(input("Gib den Radius des Kreises an. "))
        α=float(input("Gib den Winkel α des Kreissektors an. "))
        ks=((math.pi*(r*r)*math.radians(α)))/math.radians(360)
        print ("Der Kreissektor beträgt",ks,"Flächeneinheiten.")
    elif x=="kb":
        r=float(input("Gib den Radius des Kreises an. "))
        α=float(input("Gib den Winkel α des Kreissektors an. "))
        kb=(math.pi*r*math.radians(α))/math.radians (180)
        print ("Der Kreisbogen beträgt",kb,"Flächeneinheiten.")
    else:
        r=float(input("Gib den Radius des Kreises an. "))
        α=float(input("Gib den Winkel α des Kreissektors an. "))
        ks=((math.pi*(r*r)*math.radians(α)))/math.radians(360)
        kb=(math.pi*r*math.radians(α))/math.radians (180)
        print ("Der Kreissektor beträgt",ks,"Flächeneinheiten.")        
        print ("Der Kreisbogen beträgt",kb,"Flächeneinheiten.")

elif figurenauswahl=="a":
    x=input("Möchtest du das Volumen[v], die Oberfläche[o] oder beides[b] vom Würfel berechnen? ")
    if x=="v":
        a=float(input("Gib die Länge einer Seite des Würfels an. "))
        würfelv=(a*a*a)
        print ("Das Volumen des Würfels beträgt",würfelv,"Flächeneinheiten.")
    elif x=="o":
        a=float(input("Gib die Länge einer Seite des Würfels an. "))
        würfelo= (6*(a*a))
        print ("Die Oberfläche des Würfels beträgt",würfelo,"Flächeneinheiten.")
    elif x=="b":
        a=float(input("Gib die Länge einer Seite des Würfels an. "))
        würfelv=(a*a*a)
        würfelo= (6*(a*a))
        print ("Das Volumen des Würfels beträgt",würfelv,"Flächeneinheiten.")
        print ("Die Oberfläche des Würfels beträgt",würfelo,"Flächeneinheiten.")

elif figurenauswahl=="b":
    x=input ("Möchtest du das Volumen[v], die Oberfläche[o] oder beides[b] des Quaderss berechnen? ")
    if x=="v":
        a= float(input("Gib die Länge des Quaders an. "))
        b= float(input("Gib die Breite des Quaders an. "))
        c= float (input("Gib die Höhe des Quaders an. "))
        quaderv= a*b*c
        print ("Das Volumen des Quaders beträgt",quaderv,"Flächeneinheiten.")
    elif x=="o":
        a= float(input("Gib die Länge des Quaders an. "))
        b= float(input("Gib die Breite des Quaders an. "))
        c= float (input("Gib die Höhe des Quaders an. "))
        quadero= 2*a*b+2*a*c+2*b*c
        print ("Die Oberfläche des Quaders beträgt",quadero,"Flächeneinheiten.")
    elif x=="b":
        a= float(input("Gib die Länge des Quaders an. "))
        b= float(input("Gib die Breite des Quaders an. "))
        c= float (input("Gib die Höhe des Quaders an. "))
        quadero= 2*a*b+2*a*c+2*b*c
        quaderv= a*b*c
        print ("Das Volumen des Quaders beträgt",quaderv,"Flächeneinheiten.")
        print ("Die Oberfläche des Quaders beträgt",quadero,"Flächeneinheiten.")

elif figurenauswahl=="c":
    x=input("Soll das Volumen[v], die Oberfläche[o] oder beides[b] vom Prisma berechnet werden? ")
    if x=="v":
        g= float(input("Gib die Grundfläche des Prismas an"))
        h=float(input ("Gib die Höhe des Prismas an"))
        prismav= g*h
        print ("Das Volumen des Prismas beträgt", prismav,"Flächeneinheiten.")
    elif x=="o":
        g= float (input("Gib die Grundseite des Prismas an. "))
        m= float (input("Gib die Mantelfläche des Prismas an. "))
        prismao= 2*g+m
        print ("Die Oberfläche des Prismas beträgt", prismao,"Flächeneinheiten.")
    elif x=="b":
        
    


    
    
        
        
        

        
        
    
        
            
        
        

        


