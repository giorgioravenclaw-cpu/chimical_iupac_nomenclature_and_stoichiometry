
di="di"

OH = "idrossido"
H = "idrogeno"
He = "elio"
Li = "litio"
Be = "berillio"
B = "boro"
C = "carbonio"
N = "nitro"
O = "ossigeno"
F = "fluoro"
Ne = "neon"
Na = "sodio"
Mg = "magnesio"
Al = "alluminio"
Si = "silicio"
P = "fosforo"
S = "zolfo"
Cl = "cloro"
Ar = "argon"
K = "potassio"
Ca = "calcio"
Sc = "scandio"
Ti = "titanio"
V = "vanadio"
Cr = "cromo"
Mn = "manganese"
Fe = "ferro"
Co = "cobalto"
Ni = "nichel"
Cu = "rame"
Zn = "zinco"
Ga = "gallio"
Ge = "germanio"
As = "arsenico"
Se = "selenio"
Br = "bromo"
Kr = "cripton"
Rb = "rubidio"
Sr = "stronzio"
Y = "ittrio"
Zr = "zirconio"
Nb = "niobio"
Mo = "molibdeno"
Tc = "tecnezio"
Ru = "rutenio"
Rh = "rodio"
Pd = "palladio"
Ag = "argento"
Cd = "cadmio"
In = "indio"
Sn = "stagno"
Sb = "antimonio"
Te = "tellurio"
I = "iodio"
Xe = "xeno"
Cs = "cesio"
Ba = "bario"
La = "lantanio"
Ce = "cerio"
Pr = "praseodimio"
Nd = "neodimio"
Pm = "promezio"
Sm = "samario"
Eu = "europio"
Gd = "gadolinio"
Tb = "terbio"
Dy = "disprosio"
Ho = "olmio"
Er = "erbio"
Tm = "tulio"
Yb = "itterbio"
Lu = "lutezio"
Hf = "afnio"
Ta = "tantalio"
W = "tungsteno"
Re = "renio"
Os = "osmio"
Ir = "iridio"
Pt = "platino"
Au = "oro"
Hg = "mercurio"
Tl = "tallio"
Pb = "piombo"
Bi = "bismuto"
Po = "polonio"
At = "astato"
Rn = "radon"
Fr = "francio"
Ra = "radio"
Ac = "attinio"
Th = "torio"
Pa = "protoattinio"
U = "uranio"
Np = "nettunio"
Pu = "plutonio"
Am = "americio"
Cm = "curio"
Bk = "berkelio"
Cf = "californio"
Es = "einsteinio"
Fm = "fermio"
Md = "mendelevio"
No = "nobelio"
Lr = "laurenzio"
Rf = "rutherfordio"
Db = "dubnio"
Sg = "seaborgio"
Bh = "bohrio"
Hs = "hassio"
Mt = "meitnerio"
Ds = "darmstadtio"
Rg = "roentgenio"
Cn = "copernicio"
Nh = "nihonio"
Fl = "flerovio"
Mc = "moscovio"
Lv = "livermorio"
Ts = "tennesso"
Og = "oganesson"


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

nome_composto="........"

N4=0
N3=0
N2=0
N1=0

numero_romano1=0
numero_romano2=0
numero_romano3=0
numero_romano4=0


composto=input("dimmi gli elementi del composto se ne ha dimeno scrivi nell quarto null (se hai un idrossido scrivi  OH tutto attaccato e metti 2 null)")
volte1=input("dimmi quante volte è preso il singolo elemento e se non è presente scrivi 1")
volte2=input("dimmi quante volte è preso il singolo elemento e se non è presente scrivi 1")
volte3=input("dimmi quante volte è preso il singolo elemento e se non è presente scrivi 1")
volte4=input("dimmi quante volte è preso il singolo elemento e se non è presente scrivi 1")




elementi=composto.split()


if elementi[0] == "H":
    numero_romano1 = 1
if elementi[1] == "H":
    numero_romano2 = 1
if elementi[2] == "H":
    numero_romano3 = 1
if elementi[3] == "H":
    numero_romano4 = 1

if elementi[0] == "O":
    numero_romano1 = -2
if elementi[1] == "O":
    numero_romano2 = -2
if elementi[2] == "O":
    numero_romano3 = -2
if elementi[3] == "O":
    numero_romano4 = -2



if elementi[0] == "Li":
    numero_romano1 = 1
if elementi[0] == "Na":
    numero_romano1 = 1
if elementi[0] == "K":
    numero_romano1 = 1
if elementi[0] == "Rb":
    numero_romano1 = 1
if elementi[0] == "Cs":
    numero_romano1 = 1
if elementi[0] == "Fr":
    numero_romano1 = 1
if elementi[0] == "Be":
    numero_romano1 = 2
if elementi[0] == "Mg":
    numero_romano1 = 2
if elementi[0] == "Ca":
    numero_romano1 = 2
if elementi[0] == "Sr":
    numero_romano1 = 2
if elementi[0] == "Ba":
    numero_romano1 = 2
if elementi[0] == "Ra":
    numero_romano1 = 2
if elementi[0] == "Al":
    numero_romano1 = 3
if elementi[0] == "Zn":
    numero_romano1 = 2
if elementi[0] == "Ag":
    numero_romano1 = 1
if elementi[0] == "Cd":
    numero_romano1 = 2
if elementi[0] == "F":
    numero_romano1 = 1


if elementi[1] == "Li":
    numero_romano2 = 1
if elementi[1] == "Na":
    numero_romano2 = 1
if elementi[1] == "K":
    numero_romano2 = 1
if elementi[1] == "Rb":
    numero_romano2 = 1
if elementi[1] == "Cs":
    numero_romano2 = 1
if elementi[1] == "Fr":
    numero_romano2 = 1
if elementi[1] == "Be":
    numero_romano2 = 2
if elementi[1] == "Mg":
    numero_romano2 = 2
if elementi[1] == "Ca":
    numero_romano2 = 2
if elementi[1] == "Sr":
    numero_romano2 = 2
if elementi[1] == "Ba":
    numero_romano2 = 2
if elementi[1] == "Ra":
    numero_romano2 = 2
if elementi[1] == "Al":
    numero_romano2 = 3
if elementi[1] == "Zn":
    numero_romano2 = 2
if elementi[1] == "Ag":
    numero_romano2 = 1
if elementi[1] == "Cd":
    numero_romano2 = 2
if elementi[1] == "F":
    numero_romano2 = 1


if elementi[2] == "Li":
    numero_romano3 = 1
if elementi[2] == "Na":
    numero_romano3 = 1
if elementi[2] == "K":
    numero_romano3 = 1
if elementi[2] == "Rb":
    numero_romano3 = 1
if elementi[2] == "Cs":
    numero_romano3 = 1
if elementi[2] == "Fr":
    numero_romano3 = 1
if elementi[2] == "Be":
    numero_romano3 = 2
if elementi[2] == "Mg":
    numero_romano3 = 2
if elementi[2] == "Ca":
    numero_romano3 = 2
if elementi[2] == "Sr":
    numero_romano3 = 2
if elementi[2] == "Ba":
    numero_romano3 = 2
if elementi[2] == "Ra":
    numero_romano3 = 2
if elementi[2] == "Al":
    numero_romano3 = 3
if elementi[2] == "Zn":
    numero_romano3 = 2
if elementi[2] == "Ag":
    numero_romano3 = 1
if elementi[2] == "Cd":
    numero_romano3 = 2
if elementi[2] == "F":
    numero_romano3 = 1


if elementi[3] == "Li":
    numero_romano4 = 1
if elementi[3] == "Na":
    numero_romano4 = 1
if elementi[3] == "K":
    numero_romano4 = 1
if elementi[3] == "Rb":
    numero_romano4 = 1
if elementi[3] == "Cs":
    numero_romano4 = 1
if elementi[3] == "Fr":
    numero_romano4 = 1
if elementi[3] == "Be":
    numero_romano4 = 2
if elementi[3] == "Mg":
    numero_romano4 = 2
if elementi[3] == "Ca":
    numero_romano4 = 2
if elementi[3] == "Sr":
    numero_romano4 = 2
if elementi[3] == "Ba":
    numero_romano4 = 2
if elementi[3] == "Ra":
    numero_romano4 = 2
if elementi[3] == "Al":
    numero_romano4 = 3
if elementi[3] == "Zn":
    numero_romano4 = 2
if elementi[3] == "Ag":
    numero_romano4 = 1
if elementi[3] == "Cd":
    numero_romano4 = 2
if elementi[3] == "F":
    numero_romano4 = 1


numero_romano1*=int(volte1)
numero_romano2*=int(volte2)
numero_romano3*=int(volte3)
numero_romano4*=int(volte4)


if volte1=="1":
    volte1=""
if volte1=="2":
    volte1="di"
if volte1=="3":
    volte1="tri"
if volte1=="4":
    volte1="tetra"
if volte1=="5":
    volte1="penta"
if volte1=="6":
    volte1="esa"
if volte1=="7":
    volte1="epta"
if volte1=="8":
    volte1="otta"


if volte2=="1":
    volte2=""
if volte2=="2":
    volte2="di"
if volte2=="3":
    volte2="tri"
if volte2=="4":
    volte2="tetra"
if volte2=="5":
    volte2="penta"
if volte2=="6":
    volte2="esa"
if volte2=="7":
    volte2="epta"
if volte2=="8":
    volte2="otta"


if volte3=="1":
    volte3=""
if volte3=="2":
    volte3="di"
if volte3=="3":
    volte3="tri"
if volte3=="4":
    volte3="tetra"
if volte3=="5":
    volte3="penta"
if volte3=="6":
    volte3="esa"
if volte3=="7":
    volte3="epta"
if volte3=="8":
    volte3="otta"


if volte4=="1":
    volte4=""
if volte4=="2":
    volte4="di"
if volte4=="3":
    volte4="tri"
if volte4=="4":
    volte4="tetra"
if volte4=="5":
    volte4="penta"
if volte4=="6":
    volte4="esa"
if volte4=="7":
    volte4="epta"
if volte4=="8":
    volte4="otta"







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





if elementi[0] == "O":
    elementi[0] = O
if elementi[0] == "OH":
    elementi[0] = OH
if elementi[0] == "H":
    elementi[0] = H
if elementi[0] == "He":
    elementi[0] = He
if elementi[0] == "Li":
    elementi[0] = Li
if elementi[0] == "Be":
    elementi[0] = Be
if elementi[0] == "B":
    elementi[0] = B
if elementi[0] == "C":
    elementi[0] = C
if elementi[0] == "N":
    elementi[0] = N
if elementi[0] == "O":
    elementi[0] = O
if elementi[0] == "F":
    elementi[0] = F
if elementi[0] == "Ne":
    elementi[0] = Ne
if elementi[0] == "Na":
    elementi[0] = Na
if elementi[0] == "Mg":
    elementi[0] = Mg
if elementi[0] == "Al":
    elementi[0] = Al
if elementi[0] == "Si":
    elementi[0] = Si
if elementi[0] == "P":
    elementi[0] = P
if elementi[0] == "S":
    elementi[0] = S
if elementi[0] == "Cl":
    elementi[0] = Cl
if elementi[0] == "Ar":
    elementi[0] = Ar
if elementi[0] == "K":
    elementi[0] = K
if elementi[0] == "Ca":
    elementi[0] = Ca
if elementi[0] == "Sc":
    elementi[0] = Sc
if elementi[0] == "Ti":
    elementi[0] = Ti
if elementi[0] == "V":
    elementi[0] = V
if elementi[0] == "Cr":
    elementi[0] = Cr
if elementi[0] == "Mn":
    elementi[0] = Mn
if elementi[0] == "Fe":
    elementi[0] = Fe
if elementi[0] == "Co":
    elementi[0] = Co
if elementi[0] == "Ni":
    elementi[0] = Ni
if elementi[0] == "Cu":
    elementi[0] = Cu
if elementi[0] == "Zn":
    elementi[0] = Zn
if elementi[0] == "Ga":
    elementi[0] = Ga
if elementi[0] == "Ge":
    elementi[0] = Ge
if elementi[0] == "As":
    elementi[0] = As
if elementi[0] == "Se":
    elementi[0] = Se
if elementi[0] == "Br":
    elementi[0] = Br
if elementi[0] == "Kr":
    elementi[0] = Kr
if elementi[0] == "Rb":
    elementi[0] = Rb
if elementi[0] == "Sr":
    elementi[0] = Sr
if elementi[0] == "Y":
    elementi[0] = Y
if elementi[0] == "Zr":
    elementi[0] = Zr
if elementi[0] == "Nb":
    elementi[0] = Nb
if elementi[0] == "Mo":
    elementi[0] = Mo
if elementi[0] == "Tc":
    elementi[0] = Tc
if elementi[0] == "Ru":
    elementi[0] = Ru
if elementi[0] == "Rh":
    elementi[0] = Rh
if elementi[0] == "Pd":
    elementi[0] = Pd
if elementi[0] == "Ag":
    elementi[0] = Ag
if elementi[0] == "Cd":
    elementi[0] = Cd
if elementi[0] == "In":
    elementi[0] = In
if elementi[0] == "Sn":
    elementi[0] = Sn
if elementi[0] == "Sb":
    elementi[0] = Sb
if elementi[0] == "Te":
    elementi[0] = Te
if elementi[0] == "I":
    elementi[0] = I
if elementi[0] == "Xe":
    elementi[0] = Xe
if elementi[0] == "Cs":
    elementi[0] = Cs
if elementi[0] == "Ba":
    elementi[0] = Ba
if elementi[0] == "La":
    elementi[0] = La
if elementi[0] == "Ce":
    elementi[0] = Ce
if elementi[0] == "Pr":
    elementi[0] = Pr
if elementi[0] == "Nd":
    elementi[0] = Nd
if elementi[0] == "Pm":
    elementi[0] = Pm
if elementi[0] == "Sm":
    elementi[0] = Sm
if elementi[0] == "Eu":
    elementi[0] = Eu
if elementi[0] == "Gd":
    elementi[0] = Gd
if elementi[0] == "Tb":
    elementi[0] = Tb
if elementi[0] == "Dy":
    elementi[0] = Dy
if elementi[0] == "Ho":
    elementi[0] = Ho
if elementi[0] == "Er":
    elementi[0] = Er
if elementi[0] == "Tm":
    elementi[0] = Tm
if elementi[0] == "Yb":
    elementi[0] = Yb
if elementi[0] == "Lu":
    elementi[0] = Lu
if elementi[0] == "Hf":
    elementi[0] = Hf
if elementi[0] == "Ta":
    elementi[0] = Ta
if elementi[0] == "W":
    elementi[0] = W
if elementi[0] == "Re":
    elementi[0] = Re
if elementi[0] == "Os":
    elementi[0] = Os
if elementi[0] == "Ir":
    elementi[0] = Ir
if elementi[0] == "Pt":
    elementi[0] = Pt
if elementi[0] == "Au":
    elementi[0] = Au
if elementi[0] == "Hg":
    elementi[0] = Hg
if elementi[0] == "Tl":
    elementi[0] = Tl
if elementi[0] == "Pb":
    elementi[0] = Pb
if elementi[0] == "Bi":
    elementi[0] = Bi
if elementi[0] == "Po":
    elementi[0] = Po
if elementi[0] == "At":
    elementi[0] = At
if elementi[0] == "Rn":
    elementi[0] = Rn
if elementi[0] == "Fr":
    elementi[0] = Fr
if elementi[0] == "Ra":
    elementi[0] = Ra
if elementi[0] == "Ac":
    elementi[0] = Ac
if elementi[0] == "Th":
    elementi[0] = Th
if elementi[0] == "Pa":
    elementi[0] = Pa
if elementi[0] == "U":
    elementi[0] = U
if elementi[0] == "Np":
    elementi[0] = Np
if elementi[0] == "Pu":
    elementi[0] = Pu
if elementi[0] == "Am":
    elementi[0] = Am
if elementi[0] == "Cm":
    elementi[0] = Cm
if elementi[0] == "Bk":
    elementi[0] = Bk
if elementi[0] == "Cf":
    elementi[0] = Cf
if elementi[0] == "Es":
    elementi[0] = Es
if elementi[0] == "Fm":
    elementi[0] = Fm
if elementi[0] == "Md":
    elementi[0] = Md
if elementi[0] == "No":
    elementi[0] = No
if elementi[0] == "Lr":
    elementi[0] = Lr
if elementi[0] == "Rf":
    elementi[0] = Rf
if elementi[0] == "Db":
    elementi[0] = Db
if elementi[0] == "Sg":
    elementi[0] = Sg
if elementi[0] == "Bh":
    elementi[0] = Bh
if elementi[0] == "Hs":
    elementi[0] = Hs
if elementi[0] == "Mt":
    elementi[0] = Mt
if elementi[0] == "Ds":
    elementi[0] = Ds
if elementi[0] == "Rg":
    elementi[0] = Rg
if elementi[0] == "Cn":
    elementi[0] = Cn
if elementi[0] == "Nh":
    elementi[0] = Nh
if elementi[0] == "Fl":
    elementi[0] = Fl
if elementi[0] == "Mc":
    elementi[0] = Mc
if elementi[0] == "Lv":
    elementi[0] = Lv
if elementi[0] == "Ts":
    elementi[0] = Ts
if elementi[0] == "Og":
    elementi[0] = Og


if elementi[1] == "O":
    elementi[1] = O
if elementi[1] == "OH":
    elementi[1] = OH
if elementi[1] == "H":
    elementi[1] = H
if elementi[1] == "He":
    elementi[1] = He
if elementi[1] == "Li":
    elementi[1] = Li
if elementi[1] == "Be":
    elementi[1] = Be
if elementi[1] == "B":
    elementi[1] = B
if elementi[1] == "C":
    elementi[1] = C
if elementi[1] == "N":
    elementi[1] = N
if elementi[1] == "O":
    elementi[1] = O
if elementi[1] == "F":
    elementi[1] = F
if elementi[1] == "Ne":
    elementi[1] = Ne
if elementi[1] == "Na":
    elementi[1] = Na
if elementi[1] == "Mg":
    elementi[1] = Mg
if elementi[1] == "Al":
    elementi[1] = Al
if elementi[1] == "Si":
    elementi[1] = Si
if elementi[1] == "P":
    elementi[1] = P
if elementi[1] == "S":
    elementi[1] = S
if elementi[1] == "Cl":
    elementi[1] = Cl
if elementi[1] == "Ar":
    elementi[1] = Ar
if elementi[1] == "K":
    elementi[1] = K
if elementi[1] == "Ca":
    elementi[1] = Ca
if elementi[1] == "Sc":
    elementi[1] = Sc
if elementi[1] == "Ti":
    elementi[1] = Ti
if elementi[1] == "V":
    elementi[1] = V
if elementi[1] == "Cr":
    elementi[1] = Cr
if elementi[1] == "Mn":
    elementi[1] = Mn
if elementi[1] == "Fe":
    elementi[1] = Fe
if elementi[1] == "Co":
    elementi[1] = Co
if elementi[1] == "Ni":
    elementi[1] = Ni
if elementi[1] == "Cu":
    elementi[1] = Cu
if elementi[1] == "Zn":
    elementi[1] = Zn
if elementi[1] == "Ga":
    elementi[1] = Ga
if elementi[1] == "Ge":
    elementi[1] = Ge
if elementi[1] == "As":
    elementi[1] = As
if elementi[1] == "Se":
    elementi[1] = Se
if elementi[1] == "Br":
    elementi[1] = Br
if elementi[1] == "Kr":
    elementi[1] = Kr
if elementi[1] == "Rb":
    elementi[1] = Rb
if elementi[1] == "Sr":
    elementi[1] = Sr
if elementi[1] == "Y":
    elementi[1] = Y
if elementi[1] == "Zr":
    elementi[1] = Zr
if elementi[1] == "Nb":
    elementi[1] = Nb
if elementi[1] == "Mo":
    elementi[1] = Mo
if elementi[1] == "Tc":
    elementi[1] = Tc
if elementi[1] == "Ru":
    elementi[1] = Ru
if elementi[1] == "Rh":
    elementi[1] = Rh
if elementi[1] == "Pd":
    elementi[1] = Pd
if elementi[1] == "Ag":
    elementi[1] = Ag
if elementi[1] == "Cd":
    elementi[1] = Cd
if elementi[1] == "In":
    elementi[1] = In
if elementi[1] == "Sn":
    elementi[1] = Sn
if elementi[1] == "Sb":
    elementi[1] = Sb
if elementi[1] == "Te":
    elementi[1] = Te
if elementi[1] == "I":
    elementi[1] = I
if elementi[1] == "Xe":
    elementi[1] = Xe
if elementi[1] == "Cs":
    elementi[1] = Cs
if elementi[1] == "Ba":
    elementi[1] = Ba
if elementi[1] == "La":
    elementi[1] = La
if elementi[1] == "Ce":
    elementi[1] = Ce
if elementi[1] == "Pr":
    elementi[1] = Pr
if elementi[1] == "Nd":
    elementi[1] = Nd
if elementi[1] == "Pm":
    elementi[1] = Pm
if elementi[1] == "Sm":
    elementi[1] = Sm
if elementi[1] == "Eu":
    elementi[1] = Eu
if elementi[1] == "Gd":
    elementi[1] = Gd
if elementi[1] == "Tb":
    elementi[1] = Tb
if elementi[1] == "Dy":
    elementi[1] = Dy
if elementi[1] == "Ho":
    elementi[1] = Ho
if elementi[1] == "Er":
    elementi[1] = Er
if elementi[1] == "Tm":
    elementi[1] = Tm
if elementi[1] == "Yb":
    elementi[1] = Yb
if elementi[1] == "Lu":
    elementi[1] = Lu
if elementi[1] == "Hf":
    elementi[1] = Hf
if elementi[1] == "Ta":
    elementi[1] = Ta
if elementi[1] == "W":
    elementi[1] = W
if elementi[1] == "Re":
    elementi[1] = Re
if elementi[1] == "Os":
    elementi[1] = Os
if elementi[1] == "Ir":
    elementi[1] = Ir
if elementi[1] == "Pt":
    elementi[1] = Pt
if elementi[1] == "Au":
    elementi[1] = Au
if elementi[1] == "Hg":
    elementi[1] = Hg
if elementi[1] == "Tl":
    elementi[1] = Tl
if elementi[1] == "Pb":
    elementi[1] = Pb
if elementi[1] == "Bi":
    elementi[1] = Bi
if elementi[1] == "Po":
    elementi[1] = Po
if elementi[1] == "At":
    elementi[1] = At
if elementi[1] == "Rn":
    elementi[1] = Rn
if elementi[1] == "Fr":
    elementi[1] = Fr
if elementi[1] == "Ra":
    elementi[1] = Ra
if elementi[1] == "Ac":
    elementi[1] = Ac
if elementi[1] == "Th":
    elementi[1] = Th
if elementi[1] == "Pa":
    elementi[1] = Pa
if elementi[1] == "U":
    elementi[1] = U
if elementi[1] == "Np":
    elementi[1] = Np
if elementi[1] == "Pu":
    elementi[1] = Pu
if elementi[1] == "Am":
    elementi[1] = Am
if elementi[1] == "Cm":
    elementi[1] = Cm
if elementi[1] == "Bk":
    elementi[1] = Bk
if elementi[1] == "Cf":
    elementi[1] = Cf
if elementi[1] == "Es":
    elementi[1] = Es
if elementi[1] == "Fm":
    elementi[1] = Fm
if elementi[1] == "Md":
    elementi[1] = Md
if elementi[1] == "No":
    elementi[1] = No
if elementi[1] == "Lr":
    elementi[1] = Lr
if elementi[1] == "Rf":
    elementi[1] = Rf
if elementi[1] == "Db":
    elementi[1] = Db
if elementi[1] == "Sg":
    elementi[1] = Sg
if elementi[1] == "Bh":
    elementi[1] = Bh
if elementi[1] == "Hs":
    elementi[1] = Hs
if elementi[1] == "Mt":
    elementi[1] = Mt
if elementi[1] == "Ds":
    elementi[1] = Ds
if elementi[1] == "Rg":
    elementi[1] = Rg
if elementi[1] == "Cn":
    elementi[1] = Cn
if elementi[1] == "Nh":
    elementi[1] = Nh
if elementi[1] == "Fl":
    elementi[1] = Fl
if elementi[1] == "Mc":
    elementi[1] = Mc
if elementi[1] == "Lv":
    elementi[1] = Lv
if elementi[1] == "Ts":
    elementi[1] = Ts
if elementi[1] == "Og":
    elementi[1] = Og


if elementi[2] == "O":
    elementi[2] = O
if elementi[2] == "OH":
    elementi[2] = OH
if elementi[2] == "H":
    elementi[2] = H
if elementi[2] == "He":
    elementi[2] = He
if elementi[2] == "Li":
    elementi[2] = Li
if elementi[2] == "Be":
    elementi[2] = Be
if elementi[2] == "B":
    elementi[2] = B
if elementi[2] == "C":
    elementi[2] = C
if elementi[2] == "N":
    elementi[2] = N
if elementi[2] == "O":
    elementi[2] = O
if elementi[2] == "F":
    elementi[2] = F
if elementi[2] == "Ne":
    elementi[2] = Ne
if elementi[2] == "Na":
    elementi[2] = Na
if elementi[2] == "Mg":
    elementi[2] = Mg
if elementi[2] == "Al":
    elementi[2] = Al
if elementi[2] == "Si":
    elementi[2] = Si
if elementi[2] == "P":
    elementi[2] = P
if elementi[2] == "S":
    elementi[2] = S
if elementi[2] == "Cl":
    elementi[2] = Cl
if elementi[2] == "Ar":
    elementi[2] = Ar
if elementi[2] == "K":
    elementi[2] = K
if elementi[2] == "Ca":
    elementi[2] = Ca
if elementi[2] == "Sc":
    elementi[2] = Sc
if elementi[2] == "Ti":
    elementi[2] = Ti
if elementi[2] == "V":
    elementi[2] = V
if elementi[2] == "Cr":
    elementi[2] = Cr
if elementi[2] == "Mn":
    elementi[2] = Mn
if elementi[2] == "Fe":
    elementi[2] = Fe
if elementi[2] == "Co":
    elementi[2] = Co
if elementi[2] == "Ni":
    elementi[2] = Ni
if elementi[2] == "Cu":
    elementi[2] = Cu
if elementi[2] == "Zn":
    elementi[2] = Zn
if elementi[2] == "Ga":
    elementi[2] = Ga
if elementi[2] == "Ge":
    elementi[2] = Ge
if elementi[2] == "As":
    elementi[2] = As
if elementi[2] == "Se":
    elementi[2] = Se
if elementi[2] == "Br":
    elementi[2] = Br
if elementi[2] == "Kr":
    elementi[2] = Kr
if elementi[2] == "Rb":
    elementi[2] = Rb
if elementi[2] == "Sr":
    elementi[2] = Sr
if elementi[2] == "Y":
    elementi[2] = Y
if elementi[2] == "Zr":
    elementi[2] = Zr
if elementi[2] == "Nb":
    elementi[2] = Nb
if elementi[2] == "Mo":
    elementi[2] = Mo
if elementi[2] == "Tc":
    elementi[2] = Tc
if elementi[2] == "Ru":
    elementi[2] = Ru
if elementi[2] == "Rh":
    elementi[2] = Rh
if elementi[2] == "Pd":
    elementi[2] = Pd
if elementi[2] == "Ag":
    elementi[2] = Ag
if elementi[2] == "Cd":
    elementi[2] = Cd
if elementi[2] == "In":
    elementi[2] = In
if elementi[2] == "Sn":
    elementi[2] = Sn
if elementi[2] == "Sb":
    elementi[2] = Sb
if elementi[2] == "Te":
    elementi[2] = Te
if elementi[2] == "I":
    elementi[2] = I
if elementi[2] == "Xe":
    elementi[2] = Xe
if elementi[2] == "Cs":
    elementi[2] = Cs
if elementi[2] == "Ba":
    elementi[2] = Ba
if elementi[2] == "La":
    elementi[2] = La
if elementi[2] == "Ce":
    elementi[2] = Ce
if elementi[2] == "Pr":
    elementi[2] = Pr
if elementi[2] == "Nd":
    elementi[2] = Nd
if elementi[2] == "Pm":
    elementi[2] = Pm
if elementi[2] == "Sm":
    elementi[2] = Sm
if elementi[2] == "Eu":
    elementi[2] = Eu
if elementi[2] == "Gd":
    elementi[2] = Gd
if elementi[2] == "Tb":
    elementi[2] = Tb
if elementi[2] == "Dy":
    elementi[2] = Dy
if elementi[2] == "Ho":
    elementi[2] = Ho
if elementi[2] == "Er":
    elementi[2] = Er
if elementi[2] == "Tm":
    elementi[2] = Tm
if elementi[2] == "Yb":
    elementi[2] = Yb
if elementi[2] == "Lu":
    elementi[2] = Lu
if elementi[2] == "Hf":
    elementi[2] = Hf
if elementi[2] == "Ta":
    elementi[2] = Ta
if elementi[2] == "W":
    elementi[2] = W
if elementi[2] == "Re":
    elementi[2] = Re
if elementi[2] == "Os":
    elementi[2] = Os
if elementi[2] == "Ir":
    elementi[2] = Ir
if elementi[2] == "Pt":
    elementi[2] = Pt
if elementi[2] == "Au":
    elementi[2] = Au
if elementi[2] == "Hg":
    elementi[2] = Hg
if elementi[2] == "Tl":
    elementi[2] = Tl
if elementi[2] == "Pb":
    elementi[2] = Pb
if elementi[2] == "Bi":
    elementi[2] = Bi
if elementi[2] == "Po":
    elementi[2] = Po
if elementi[2] == "At":
    elementi[2] = At
if elementi[2] == "Rn":
    elementi[2] = Rn
if elementi[2] == "Fr":
    elementi[2] = Fr
if elementi[2] == "Ra":
    elementi[2] = Ra
if elementi[2] == "Ac":
    elementi[2] = Ac
if elementi[2] == "Th":
    elementi[2] = Th
if elementi[2] == "Pa":
    elementi[2] = Pa
if elementi[2] == "U":
    elementi[2] = U
if elementi[2] == "Np":
    elementi[2] = Np
if elementi[2] == "Pu":
    elementi[2] = Pu
if elementi[2] == "Am":
    elementi[2] = Am
if elementi[2] == "Cm":
    elementi[2] = Cm
if elementi[2] == "Bk":
    elementi[2] = Bk
if elementi[2] == "Cf":
    elementi[2] = Cf
if elementi[2] == "Es":
    elementi[2] = Es
if elementi[2] == "Fm":
    elementi[2] = Fm
if elementi[2] == "Md":
    elementi[2] = Md
if elementi[2] == "No":
    elementi[2] = No
if elementi[2] == "Lr":
    elementi[2] = Lr
if elementi[2] == "Rf":
    elementi[2] = Rf
if elementi[2] == "Db":
    elementi[2] = Db
if elementi[2] == "Sg":
    elementi[2] = Sg
if elementi[2] == "Bh":
    elementi[2] = Bh
if elementi[2] == "Hs":
    elementi[2] = Hs
if elementi[2] == "Mt":
    elementi[2] = Mt
if elementi[2] == "Ds":
    elementi[2] = Ds
if elementi[2] == "Rg":
    elementi[2] = Rg
if elementi[2] == "Cn":
    elementi[2] = Cn
if elementi[2] == "Nh":
    elementi[2] = Nh
if elementi[2] == "Fl":
    elementi[2] = Fl
if elementi[2] == "Mc":
    elementi[2] = Mc
if elementi[2] == "Lv":
    elementi[2] = Lv
if elementi[2] == "Ts":
    elementi[2] = Ts
if elementi[2] == "Og":
    elementi[2] = Og


if elementi[3] == "O":
    elementi[3] = O
if elementi[3] == "OH":
    elementi[3] = OH
if elementi[3] == "H":
    elementi[3] = H
if elementi[3] == "He":
    elementi[3] = He
if elementi[3] == "Li":
    elementi[3] = Li
if elementi[3] == "Be":
    elementi[3] = Be
if elementi[3] == "B":
    elementi[3] = B
if elementi[3] == "C":
    elementi[3] = C
if elementi[3] == "N":
    elementi[3] = N
if elementi[3] == "O":
    elementi[3] = O
if elementi[3] == "F":
    elementi[3] = F
if elementi[3] == "Ne":
    elementi[3] = Ne
if elementi[3] == "Na":
    elementi[3] = Na
if elementi[3] == "Mg":
    elementi[3] = Mg
if elementi[3] == "Al":
    elementi[3] = Al
if elementi[3] == "Si":
    elementi[3] = Si
if elementi[3] == "P":
    elementi[3] = P
if elementi[3] == "S":
    elementi[3] = S
if elementi[3] == "Cl":
    elementi[3] = Cl
if elementi[3] == "Ar":
    elementi[3] = Ar
if elementi[3] == "K":
    elementi[3] = K
if elementi[3] == "Ca":
    elementi[3] = Ca
if elementi[3] == "Sc":
    elementi[3] = Sc
if elementi[3] == "Ti":
    elementi[3] = Ti
if elementi[3] == "V":
    elementi[3] = V
if elementi[3] == "Cr":
    elementi[3] = Cr
if elementi[3] == "Mn":
    elementi[3] = Mn
if elementi[3] == "Fe":
    elementi[3] = Fe
if elementi[3] == "Co":
    elementi[3] = Co
if elementi[3] == "Ni":
    elementi[3] = Ni
if elementi[3] == "Cu":
    elementi[3] = Cu
if elementi[3] == "Zn":
    elementi[3] = Zn
if elementi[3] == "Ga":
    elementi[3] = Ga
if elementi[3] == "Ge":
    elementi[3] = Ge
if elementi[3] == "As":
    elementi[3] = As
if elementi[3] == "Se":
    elementi[3] = Se
if elementi[3] == "Br":
    elementi[3] = Br
if elementi[3] == "Kr":
    elementi[3] = Kr
if elementi[3] == "Rb":
    elementi[3] = Rb
if elementi[3] == "Sr":
    elementi[3] = Sr
if elementi[3] == "Y":
    elementi[3] = Y
if elementi[3] == "Zr":
    elementi[3] = Zr
if elementi[3] == "Nb":
    elementi[3] = Nb
if elementi[3] == "Mo":
    elementi[3] = Mo
if elementi[3] == "Tc":
    elementi[3] = Tc
if elementi[3] == "Ru":
    elementi[3] = Ru
if elementi[3] == "Rh":
    elementi[3] = Rh
if elementi[3] == "Pd":
    elementi[3] = Pd
if elementi[3] == "Ag":
    elementi[3] = Ag
if elementi[3] == "Cd":
    elementi[3] = Cd
if elementi[3] == "In":
    elementi[3] = In
if elementi[3] == "Sn":
    elementi[3] = Sn
if elementi[3] == "Sb":
    elementi[3] = Sb
if elementi[3] == "Te":
    elementi[3] = Te
if elementi[3] == "I":
    elementi[3] = I
if elementi[3] == "Xe":
    elementi[3] = Xe
if elementi[3] == "Cs":
    elementi[3] = Cs
if elementi[3] == "Ba":
    elementi[3] = Ba
if elementi[3] == "La":
    elementi[3] = La
if elementi[3] == "Ce":
    elementi[3] = Ce
if elementi[3] == "Pr":
    elementi[3] = Pr
if elementi[3] == "Nd":
    elementi[3] = Nd
if elementi[3] == "Pm":
    elementi[3] = Pm
if elementi[3] == "Sm":
    elementi[3] = Sm
if elementi[3] == "Eu":
    elementi[3] = Eu
if elementi[3] == "Gd":
    elementi[3] = Gd
if elementi[3] == "Tb":
    elementi[3] = Tb
if elementi[3] == "Dy":
    elementi[3] = Dy
if elementi[3] == "Ho":
    elementi[3] = Ho
if elementi[3] == "Er":
    elementi[3] = Er
if elementi[3] == "Tm":
    elementi[3] = Tm
if elementi[3] == "Yb":
    elementi[3] = Yb
if elementi[3] == "Lu":
    elementi[3] = Lu
if elementi[3] == "Hf":
    elementi[3] = Hf
if elementi[3] == "Ta":
    elementi[3] = Ta
if elementi[3] == "W":
    elementi[3] = W
if elementi[3] == "Re":
    elementi[3] = Re
if elementi[3] == "Os":
    elementi[3] = Os
if elementi[3] == "Ir":
    elementi[3] = Ir
if elementi[3] == "Pt":
    elementi[3] = Pt
if elementi[3] == "Au":
    elementi[3] = Au
if elementi[3] == "Hg":
    elementi[3] = Hg
if elementi[3] == "Tl":
    elementi[3] = Tl
if elementi[3] == "Pb":
    elementi[3] = Pb
if elementi[3] == "Bi":
    elementi[3] = Bi
if elementi[3] == "Po":
    elementi[3] = Po
if elementi[3] == "At":
    elementi[3] = At
if elementi[3] == "Rn":
    elementi[3] = Rn
if elementi[3] == "Fr":
    elementi[3] = Fr
if elementi[3] == "Ra":
    elementi[3] = Ra
if elementi[3] == "Ac":
    elementi[3] = Ac
if elementi[3] == "Th":
    elementi[3] = Th
if elementi[3] == "Pa":
    elementi[3] = Pa
if elementi[3] == "U":
    elementi[3] = U
if elementi[3] == "Np":
    elementi[3] = Np
if elementi[3] == "Pu":
    elementi[3] = Pu
if elementi[3] == "Am":
    elementi[3] = Am
if elementi[3] == "Cm":
    elementi[3] = Cm
if elementi[3] == "Bk":
    elementi[3] = Bk
if elementi[3] == "Cf":
    elementi[3] = Cf
if elementi[3] == "Es":
    elementi[3] = Es
if elementi[3] == "Fm":
    elementi[3] = Fm
if elementi[3] == "Md":
    elementi[3] = Md
if elementi[3] == "No":
    elementi[3] = No
if elementi[3] == "Lr":
    elementi[3] = Lr
if elementi[3] == "Rf":
    elementi[3] = Rf
if elementi[3] == "Db":
    elementi[3] = Db
if elementi[3] == "Sg":
    elementi[3] = Sg
if elementi[3] == "Bh":
    elementi[3] = Bh
if elementi[3] == "Hs":
    elementi[3] = Hs
if elementi[3] == "Mt":
    elementi[3] = Mt
if elementi[3] == "Ds":
    elementi[3] = Ds
if elementi[3] == "Rg":
    elementi[3] = Rg
if elementi[3] == "Cn":
    elementi[3] = Cn
if elementi[3] == "Nh":
    elementi[3] = Nh
if elementi[3] == "Fl":
    elementi[3] = Fl
if elementi[3] == "Mc":
    elementi[3] = Mc
if elementi[3] == "Lv":
    elementi[3] = Lv
if elementi[3] == "Ts":
    elementi[3] = Ts
if elementi[3] == "Og":
    elementi[3] = Og





if tabella==4:
    if elementi[3] == "idrogeno":
        elementi[3] = "idruro"
    if elementi[3] == "O":
        elementi[3] = "ossido"


    nomenclatura="composto quaternario"



    
    
elementi[3]="."


if tabella==3:


    if N1==1 and N2==2 and elementi[2]== O :
        nomenclatura="sale ternario"
         
        
    
        elementi[1] = elementi[1][:-2]  #[2:]= elimino le prime 2 lettere  [:-2] elimino le ultime 2

        elementi[1]= elementi[1]+ "ato"

        
            
    
        
            
    
        elementi[1] = volte3 + "osso" + elementi[1]






        
    if N1 == 1 and elementi[1] == OH :
        nomenclatura = "idrossido"
    if elementi[0] == H and N2 == 2 and elementi[2] == O :
        nomenclatura = "ossiacido"
        elementi[0] = "osso" + elementi[1] + "ico"
        elementi[1] = "acido "
        numero_romano2=(numero_romano1+numero_romano3)*(-1)
        

    
    

    

if tabella==2:
    el1=elementi[1]
    
    if elementi[1] == "idrogeno":
        elementi[1] = "idruro"
    if elementi[1] == "ossigeno":
        elementi[1] = "ossido"

    elementi[2]="."
    elementi[3]="."

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
    
    
if nomenclatura == "ossiacido":
    print("il composto iupac è:",  elementi[1],volte3 + elementi[0], numero_romano2)

elif nomenclatura == "sale ternario":
    print("il composto iupac è:", volte2 + elementi[1], di, volte1 + elementi[0])    

else:
    print("il composto iupac è:",volte2 + elementi[1], di, elementi[0])  
        






