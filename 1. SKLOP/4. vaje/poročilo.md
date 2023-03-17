# Matrično množenje

**Ime:** Hana Lukež

**Datum:** 8.3.2023

---

## <span style="color: red">Naloga 1</span> 

### __Navodilo__
_Spomnimo se problema matričnega množenja iz predavanj ter kako ga rešimo._

Podane imamo velikosti matrik. Pri množenju matrik mora veljati, da je število stolpcev prve matrike
enako številu vrstic druge matrika. Pri problemu matričnega množenja nas ne zanimajo množenja sama,
temveč način množenja tj. kako postaviti oklepaje, da bo množenj realnih števil kar se da malo.
Vemo tudi, da je množenje matrik asociativno, zato bo rezultat vedno enak. Problema se lotimo optimalno.
Torej imamo neko zaporedje matrik A1 ... An. Vemo, da bo zadnja operacija zmnožila dve matriki A * B, kjer 
je prvih nekaj matrik prvotnega zaporedja v levi matriki A, drugih nekaj matrik pa v desni matriki B. Vprašanje
je, koliko prvih matrik je v A matriki. Če znamo to vedno določiti imamo rešitev. Torej imamo problem, ki ga
ločimo na dva manjša podproblema iste vrste. Problema se lotimo z memoizacijo, saj je veliko hitreje kot z rekurzijo,
kjer bi enake probleme reševali večkrat po nepotrebnem.



_Opiši Bellmanovo enačbo oz. rekurzivno zvezo._

VHOD : A1,..., An
IZHOD: minimalno število množenj realnih števil

B(i,j)...optimalno število množenj od i-te do j-te matrike

B(i,j) = min (B(i,r) + B(r+1,j) + di x d r+1 x d j+1)
	i<=r<j	
R.P.

B(i,i) = 0



_Izračunajte problem za produkt matrik velikosti: 3x5, 5x4, 4x2, 2x3, 3x5, 5x4, 4x6, 6x3 v tem vrstnem redu._

### Reševanje



 i\j  |  3x5  |  5x4  |  4x2  |  2x3  |  3x5   |  5x4   |  4x6   |  6x3   |
---|---|---|---|---|---|---|---|---|
 3x5  |   0   | 60(0) | 70(0) | 88(2) | 130(2) | 164(2) | 224(2) | 242(2) |
 5x4  |       |   0   | 40(1) | 70(2) | 120(2) | 150(2) | 218(2) | 224(2) |
 4x2  |     |          |   0   | 24(2) |  70(2) | 102(2) | 166(2) | 178(2) |
 2x3  |		||	      |   0   |	 30(3) |  70(4) | 118(5) | 154(6) |
 3x5  |       |||                        |   0    |  60(4) | 132(5) | 168(5) |
 5x4  |          ||||                              |    0   | 120(5) | 132(5) |
 4x6  |              ||||     |                              |   0    |  72(6) |
 6x3  |					||||||			 |    0   |

- Optimalno število množenj realnih števil lahko razberemo iz (1,n)-mesta, in sicer v našem primeru je to 242 množenj.
- Pri našem primeru moramo paziti na to, da so matrike oštevilčene od 0 naprej
- Številke v oklepaju nam povejo, kam postaviti oklepaje. Za naš primer je postavitev oklepajev enolična:
		
		(A0 * (A1 * A2)) * (((A3 * A4) * A5) * A6) * A7





## <span style="color: red">Naloga 2</span> 

### __Navodilo__
_Recimo, da imamo izračunano tabelo N(i,j) = (v, idx) iz Bellmanove enačbe, kjer je v optimalno število operacij, idx pa je seznam indeksov k, kjer 
je bil dosežen minimum pri združevanju podproblemov. Kako bi izračunal število vseh optimalnih produktov? Kakšna je časovna zahtevnost?
 Kaj pa če bi želel izpisati vse optimalne produkte?_

O(i,j)...število optimalnih produktov matrik Ai,...,Aj

a) R.P. : 
	O(i,i) = 1
	O(i,i+1) = 1

	O(i,j) =  ∑ O(i,k) * O(k+1,j)
		k \in Ni(i,j)[x]

b) ČASOVNA ZAHTEVNOST:
O(n2 * n)
n2...število stanj
n...izračun stanja

c)





## <span style="color: red">Naloga 3</span> 

### __Navodilo__
_V spodnji tabeli imamo že izveden izračun za vse vrednosti N(i,j) za matrike podanih velikosti, kjer matrike štejemo od 1 dalje. 
V tabeli je v (i,j)-ti celici prikazano min_operacij(index kjer je bil dosežen min).
Koliko je optimalno število operacij? Na kakšne načine lahko zmnožimo te matrike, da imamo toliko operacij?_



a) To preberemo iz (1,n)-mesta matrike. Optimalno številno množenj je 1932.

b) Na tak način lahko dane matrike zmnožimo na dva načina:

1. možnost: (A1 * A2) * ((((A3 * A4) * A5) * A6) * (A7 * A8))

2. možnost: (A1 * A2) * (((((A3 * A4) * A5) * A6) * A7) * A8)



_KOMENTAR_: V splošnem binarno drevo z n listi <--> izraz z n členi in pravilno postavljenimi oklepaji.

## <span style="color: red">Naloga 4</span> 

### __Navodilo__
_Podobno kot pri prejšnji nalogi imamo izračunano spodnjo tabelo (le da se to tabele številčijo od 0 naprej).
Odgovori na naslednja vprašanja:
Koliko operacij potrebujemo, da jih optimalno zmnožimo?
Kako jih mormao množiti?
Kako optimalno zmnožimo matrike od 3 do 7?
Koliko operacij potrebujemo, da optimalno zmnožimo prvih 5 matrik?
Kako naj zmnožimo zadnje štiri matrike, da bo število operacij najmanjše?
Ali si lahko pomagamo z izračunanimi podatki, če spremenimo število stolpcev zadnje matrike iz 3 na 4, da izračunamo novo optimalno množenje? Kaj moramo narediti?_


a) 242 operacij

b) (A1 * (A2 * A3)) * ((((A4 * A5) * A6) * A7) * A8)

c) A3 * (((A4 * A5) * A6) * A7)

d) 130

e) N(5,8) = 168

f) Zadnji stolpec bi poračunali od spodaj navzgor.


## <span style="color: red">Naloga 5</span> 
### __Navodilo__
_Pri tej nalogi bomo obravnavali primer, ko imamo na razpolago več kot en računalnik oziroma procesor. Kot vzorčni primer lahko vzamemo primer iz prejšnje naloge, 
bomo pa poizkušali povedat čim bolj splošno.
Predstavi nekaj strategij kako bi si pomagal z dodatnim računalnikom. Obravnavaj možnosti:
en računalnik lahko obdela največ L (recimo 4) matrik.
vseeno koliko matrik lahko obdela en računalnik.
kaj če nas nekaj stane, da matriko prestavimo iz enega računalnika do drugega (recimo kopija matrike preko mreže v O(velikost matrike))?
Kaj se zgodi s številom operacij, ki jih moramo izvesti v zgornjih primerih? Ali se zmanjša/zveča? Kaj pa čas za izračun?
Kaj pa če imamo na razpolago tri računalnike. Lahko zgornje ideje posplošimo oz izboljšamo?_


a) Imamo omejen dostop in dva računalnika.

       1. računalnik        2. računalnik
      	     
             __                    __
            |__|                  |__|
	      
	         |                     |
	      
	      A1,...,A4              A5,...,A8


    ~	
    N = max { N(1,4), N(5,8)) + d1 x d5 x d9 + min { d1 x d5, d5 x d9 }
    | 	                        |___________|  |_______________________|
    "čas"			    izračun L in D matrike  pošljemo drugemu računalniku					
	


b) Imamo neomejen dostop in dva računalnika


    ~	
    N = min {max N(1,k), N(k+1,8)) + d1 x dk+1 x d9
      1<=k<8





















