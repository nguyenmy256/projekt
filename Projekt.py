#Projekt-Geometrierechner
import math


print ("Geometrierechner")
print ("Es können mit diesem Rechner nun Berechnungen zum Flächeninhalt, Umfang, Volumen")
print ("und Oberflächeninhalt durchgeführt werden. Für die Auswahl immer die Zahl oder")
print ("den jeweiligen Buchstaben, der in der Klammer steht, eingeben.")
print ("Verfügbare Figuren/Körper:")
print ("Ebene Figuren: - Quadrat [1]        Körper: - Würfel [a]")
print ("               - Rechteck [2]               - Quader [b]")
print ("               - Dreieck [3]                - Prisma [c]")
print ("               - Parallelogramm [4]         - Zylinder [d]")
print ("               - Trapez [5]                 - Quadratische Pyramide [e]")
print ("               - Kreis [6]                  - Kegel [f]")
print ("               - Kreisbogen [7]             - Kugel [g]")

figurenauswahl= input ("Bitte wähle eine der oben aufgezählten Figuren aus: ")
if figurenauswahl == "1":
    x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] ausrechnen willst. ")
    if x=="f":
        a=int(input("Gib die Länge des Quadrates an. "))
        quadrata= a*a
        print ("Der Flächeninhalt des Quadrats beträgt",quadrata,"Flächeneinheiten.")
    elif x=="u":
        a=int(input("Gib die Länge des Quadrates an. "))
        quadratu= 4*a
        print ("Der Umfang des Quadrates beträgt", quadratu,"Flächeneinheiten.")
    else:
        a=int(input("Gib die Länge des Quadrates an. "))
        quadratu= 4*a
        quadrata= a*a
        print ("Der Umfang des Quadrates beträgt", quadratu,"Flächeneinheiten.")
        print ("Der Flächeninhalt des Quadrats beträgt",quadrata,"Flächeneinheiten.")

elif figurenauswahl=="2":
    x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] ausrechnen willst. ")
    if x=="f":
        a= int(input("Gib die Länge des Rechtecks an. "))
        b= int(input("Gib die Breite des Rechtecks an. "))
        rechtecka= a*b
        print("Der Flächeninhalt des Rechtecks beträgt", rechtecka, "Flächeneinheiten.")
    elif x=="u":
        a= int(input("Gib die Länge des Rechtecks an. "))
        b= int(input("Gib die Breite des Rechtecks an. "))
        rechtecku= 2*a+2*b
        print("Der Umfang des Rechtecks beträgt", rechtecku, "Flächeneinheiten.")
    else:
        a= int(input("Gib die Länge des Rechtecks an. "))
        b= int(input("Gib die Breite des Rechtecks an. "))
        rechtecka= a*b
        rechtecku= 2*a+2*b
        print("Der Flächeninhalt des Rechtecks beträgt", rechtecka, "Flächeneinheiten.")
        print("Der Umfang des Rechtecks beträgt", rechtecku, "Flächeneinheiten.")

elif figurenauswahl =="3":
    x= input("Bitte gib an ob du den Flächeninhalt[f], den Umfang[u] oder beides[b] ausrechnen willst. ")
    if x=="f":
        g= int(input("Gib die Länge der Basis oder der Grundseite des Dreiecks an. "))
        h= int(input("Gib die Höhe des Dreiecks an. "))
        dreiecka= (g*h)/2
        print("Der Flächeninhalt des Rechtecks beträgt", dreiecka, "Flächeneinheiten.")
    elif x=="u":
        a= int(input("Gib die Länge der 1. Seite des Dreiecks an. "))
        b= int(input("Gib die Länge der 2. Seite des Dreiecks an. "))
        c= int(input("Gib die Länge der 3. Seite des Dreiecks an. "))
        dreiecku= a+b+c
        print("Der Umfang des Dreiecks beträgt", dreiecku, "Flächeneinheiten.")
    else:
        g= int(input("Gib die Länge der Basis oder der Grundseite des Dreiecks an. "))
        h= int(input("Gib die Höhe des Dreiecks an. "))
        dreiecka= (g*h)/2
        a= int(input("Gib die Länge des 1. Schenkel des Dreiecks an. "))
        b= int(input("Gib die Länge der 2. Schenkel des Dreiecks an. "))
        dreiecku= a+b+g
        print("Der Flächeninhalt des Rechtecks beträgt", dreiecka, "Flächeneinheiten.")
        print("Der Umfang des Dreiecks beträgt", dreiecku, "Flächeneinheiten.")
        
        

    
    

        


