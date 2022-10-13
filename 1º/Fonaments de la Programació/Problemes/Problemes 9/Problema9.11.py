

llista_companyies = [["Acciona","ANA",0.80],["Acerinox","ACX",0.42],["ACS","ACS",2.29],["Aena","AENA",2.71],["Amadeus","AMS",5.96],["Arcelor Mittal","MTS",0.88],["Banc Sabadell","SAB",1.36],["Banco Santander","SAN",14.49],["Bankia","BKIA",1.16],["Bankinter","BKT",1.42],["BBVA","BBVA",7.18], ["Caixabank","CABK",4.66],["Cellnex","CLNX",0.97], ["Cie Automotive","CIE",0.37],["Dia","DIA",0.09],["Enagás","ENG",1.24],["Endesa","ELE",1.79],["Ferrovial","FER",2.88],["Grifols","GRF",2.26],["IAG","IAG",3.02],["Iberdrola","IBE",9.04], ["Inditex","ITX",10.87],["Indra","IDR",0.35],["Inmobiliaria Colonial","COL",0.35],["Mapfre","MAP",1.00],["Mediaset","TL5",0.35],["Meliá Hotels","MEL",0.35],["Merlin Properties","MRL",1.12],["Naturgy","NTGY",1.88], ["Red Eléctrica","REE",2.21],["Repsol","REP",5.22],["Siemens Gamesa","SGRE",1.09],["Técnicas Reunidas","TRE",0.28],["Telefónica","TEF",8.83],["Viscofan","VIS",0.50]]

preus = input("Introdueix llista preus: ")
preus = preus.split(",")

llista_preus = []
for e in preus:
    llista_preus.append(float(e))
    
Valor_IBEX = 0
for companyia,valor in zip(llista_companyies,llista_preus):
    Valor_IBEX += companyia[2]*valor
    
print(Valor_IBEX)