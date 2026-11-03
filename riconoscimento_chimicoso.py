
# Metalli
metalli = {
    "Li","Be","Na","Mg","K","Ca","Rb","Sr","Cs","Ba",
    "Fr","Ra","Sc","Ti","V","Cr","Mn","Fe","Co","Ni",
    "Cu","Zn","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd",
    "Ag","Cd","Hf","Ta","W","Re","Os","Ir","Pt","Au",
    "Hg","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn"
}

# Non metalli
non_metalli = {
    "H","C","N","O","P","S","Se",
    "F","Cl","Br","I","At","Ts",
    "He","Ne","Ar","Kr","Xe","Rn","Og"
    "B","Si","Ge","As","Sb","Te","Po"
}

nomenclatura="non riconosco nessun composto"
tabella=4

N4=0
N3=0
N2=0
N1=0


composto=input("dimmi i composto elementi del composto se ne ha dimeno scrivi nell quarto null")

elementi=composto.split()



if elementi[0] in metalli:

    N1=1

if elementi[0] in non_metalli:
   
    N1=2

if elementi[1] in metalli:

    N2=1

if elementi[1] in non_metalli:
   
    N2=2
if elementi[2] in metalli:

    N3=1

if elementi[2] in non_metalli:
   
    N3=2
if elementi[3] in metalli:

    N4=1

if elementi[3] in non_metalli:
   
    N4=2

if N4==0 :
    tabella=3

if N3==0 :
    tabella=2


if tabella==4:
    nomenclatura="composto quaternario"

if tabella==3:
    if N1==1 and N2==2 and elementi[2]=="O":
        nomenclatura="sale ternario"
    
    if elementi[0]=="H" and N2==2 and elementi[2]=="O":
        nomenclatura="ossiacido"

    if N1==1 and elementi[1]=="O" and elementi[2]=="H":
        nomenclatura="idracido"

if tabella==2:

    if N1==1 and N2==2:
        nomenclatura="sale binario"
    if N1==1 and elementi[1]=="O":
        nomenclatura="ossido basico"
    if N1==2 and elementi[1]=="O":
        nomenclatura="anidride"
    if N1==1 and elementi[1]=="H":
        nomenclatura="idruro metallico"
    if N1==2 and elementi[1]=="H":
        nomenclatura="idruro coovalente"
    if elementi[0]=="H" and N2==2:
        nomenclatura="idracico"
    
    


print("il composto è:",N1,N2,N3,N4)
print("il composto è:",tabella,nomenclatura)

