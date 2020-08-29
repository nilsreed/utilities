import pickle
import time

class Product:
    def __init__(self, name, qty): #qty means quantity
        self.name = name
        self.qty = qty

    def __add__(self,other):
        qty = self.qty + other.qty
        return Product(self.name, qty)

    def __sub__(self,other):
        qty = self.qty - other.qty
        return Product(self.name, qty)

    def __str__(self):
        return str(self.qty) + "x " + self.name

def save_list(catalog, filename):
    pickle_out = open(filename, 'wb')
    pickle.dump(catalog, pickle_out)
    pickle_out.close
    

def add_item(catalog, item, number):
    
    for p in catalog:
        if p.name == item:
            p.qty += number
            return
    catalog.append(Product(item, number))

def remove_item(catalog, item, number, index):
    catalog[index].qty -= number
    if catalog[index].qty == 0:
        catalog.remove(Product(item, 0))


def print_list(catalog):
    print("Her er innhaldet i frysen din:")
    for p in catalog:
        print(p)


def test():
    p = Product("Milk", 15)
    print("Product milk, quantity 15 is made. Now we try to print")
    print(p)
    print("Now we add more milk")
    print(p+Product("Milk", 15))
    print("And the subtract")
    print(p-Product("Milk", 14))

def main():

    err = 0 #For feilsjekk ved opning av fil
    try:
        frysliste = pickle.load(open("frys.pickle", "rb"))
    except (OSError, IOError) as e:
        err = 1
        frysliste = []
        pickle.dump(frysliste, open("frys.pickle", "wb"))

    if err == 0:
        print("1 list found, load successful")

    else:
        print("No list found, new list created")
    #Legg inn innlasting av lista, sjekk om den lastar liktig
    #Viss ja: print "1 list found, loaded into the program"
    #Viss nei: print "no list found, new list created for your convenience"
    counter = 0 # For å gjere menyen betre
    choice = -1 # For å ha meny
    print("===================================================")
    print("  Velkomen til freezerGuardian - programmet som")
    print("held oversikt over innhaldet i frysaren din for deg")
    print("===================================================")
    print("")
    while choice != 4:
        if counter == 0:
            print("Kva kan eg hjelpa deg med i dag?")
            counter += 1
        else:
            print("Kva meir kan eg hjelpa deg med?")

        
        print(" 1) Syn meg kva eg har i frysaren")
        print(" 2) Leggja inn meir i frysaroversikta")
        print(" 3) Fjerne noko frå frysaroversikta")
        print(" 4) Avslutte programmet")
        print("")
        choice = int(input("Ditt val: "))
        print("")
        print("")

        if choice == 1:
            if len(frysliste) == 0:
                print("Frysaren er tom, fyll han opp!")
            else:
                print_list(frysliste)
            print("")
            print("")
            

        elif choice == 2:
            name = input("Kva produkt skal du leggja i frysen? ")
            number = int(input("Kor mange " + name + " skal du leggja i frysen? "))
            add_item(frysliste, name.capitalize(), number)
            print("")
            print("Værsågod neste!")
            print("")
            print("")
            
            
        elif choice == 3:
            name = input("Kva produkt skal du ta ut av frysen? ")
            name = name.capitalize()
            number = int(input("Kor mange " + name + " skal du ta ut av frysen? "))

            match = 0
            index = -1
            for i in range(0, len(frysliste)):
                if frysliste[i].name == name:
                    match += 1
                    index = i

            if match == 0:
                print("Beklagar, du har ikkje " + name + " i frysen")
                print("Eg anbefalar deg å sjekke fryslista og sjå om du har stava produktnamnet riktig")
                print("Om du meinar eg tek feil, og at du faktisk har " + name + " i frysen, står du fritt til å leggja det inn i fryslista.")
            else:
                if frysliste[index].qty < number:
                    print("Beklagar, men du har ikkje " + str(number) + " " + name + " i frysen")
                    print("Per no har du " + str(frysliste[index].qty) + " " + name + " i frysen")
                else:
                    print("Du har no " + str(frysliste[index].qty-number) + " " + name + " igjen i frysen")
                    remove_item(frysliste, name, number, index)
                
            print("")
            print("Værsågod neste!")
            print("")
            print("")

        elif choice == 4:
            print("Greit, hade!")
            save_list(frysliste, "frys.pickle")
            print("")
            print("")

        else:
            print("Ugyldig val, programmet startar om att")
            counter = 0
            print("")
            time.sleep(1)
            print("RESTARTING PROGRESS:")
            time.sleep(0.3)
            print("[----------] (0%)")
            time.sleep(0.3)
            print("[#---------] (10%)")
            time.sleep(0.3)
            print("[##--------] (20%)")
            time.sleep(0.3)
            print("[###-------] (30%)")
            time.sleep(0.3)
            print("[####------] (40%)")
            time.sleep(0.3)
            print("[#####-----] (50%)")
            time.sleep(0.3)
            print("[######----] (60%)")
            time.sleep(0.3)
            print("[#######---] (70%)")
            time.sleep(0.3)
            print("[########--] (80%)")
            time.sleep(0.3)
            print("[#########-] (90%)")
            time.sleep(0.3)
            print("[##########] (100%)")
            print("")
            print("")

    #Lag meny for å lagre, printe, ta ut frå og legge til element i (kanskje lage ny liste og?)
    #test()

main()
