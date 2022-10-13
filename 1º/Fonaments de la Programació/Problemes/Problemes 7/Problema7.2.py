
def KelvinToFarenheit(temperatura):
    assert(temperatura>=0), "Inferior al zero absolut"
    return ((temperatura - 273) *1.8)+32

try:
    tempK = float(input("Introdueix la temperatura en Kelvin: "))
    tempF = KelvinToFarenheit(tempK)
except ValueError:
    print("ERROR:  Temperatura ha de ser un nombre")
except AssertionError as missatge:
    print("ERROR:", missatge)
else:
    print(tempK,"graus Kelvin equivalen a",tempF,"graus Fahrenheit")


