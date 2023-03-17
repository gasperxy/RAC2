# =============================================================================
# Tekmovanje - Nahrbtnik
#
# Na vajah bomo izvedli tekmovanje v parih. Spodnje naloge se navezujejo na uporabo 0/1 nahrbtnika in 
# njegovih variacij. Par, ki bo rešil največ nalog v času (recimo dve šolski uri) bo dobil neko simbolično 
# nagrado v smislu oprostitve nekega dela poročila. Testni primeri so sestavljeni, da ob pravilni implementaciji funkcije
# trajajo nekje do 10-15 sekund. Če vaša funkcija deluje bistveno več časa potem prekinite delovanje in optimizirajte svojo
# rešite.
# 
# 
# Trgovec želi iz Evrope v Ameriko spravit večjo količino predmetov. Pri tem ima na 
# razpolago tovorno letalo, ki pa lahko prenese le omejeno količino blaga.
# Predmete predstavimo s seznamom elementov oblike $(c_i, v_i)$, kjer $c_i$ predstavlja
# ceno $i$-tega predmeta, $v_i$ pa njegovo težo.
# =====================================================================@033253=
# 1. podnaloga
# Implementiraj funkcijo `optimalni_tovor(predmeti, W)`, ki vrne največjo skupno ceno
# predmetov, ki jih lahko trgovec natovori na letalo z maksimalno nosilnostjo `W`.
# Na primer:
# 
#     >>> optimalni_tovor([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 7)
#     8
# =============================================================================
import math
from functools import lru_cache
def optimalni_tovor(predmeti, W):
    n = len(predmeti)
    
    @lru_cache(maxsize=None)
    def b(i,R):
        if i == -1 and R < 0:
            return float('-inf')
        if i == -1 and R >=0:
            return 0
        return max(predmeti[i][0] + b(i-1,R-predmeti[i][1]), b(i-1,R))
    return b(n-1,W)
# =====================================================================@033254=
# 2. podnaloga
# Implementiraj funkcijo `optimalni_predmeti(predmeti, W)`, ki vrne seznam predmetov
# ki dosežejo največjo vrednost, če lahko na letalo natovorimo skupno težo največ `W`.
# Če je možnosti več, vrni katerokoli.
# Na primer:
# 
#     >>> optimalni_predmeti([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 7)
#     [(3, 2), (5, 4)]
# =============================================================================
# def optimalni_predmeti(predmeti, W):
#     n = len(predmeti)
#     
#     @lru_cache(maxsize=None)
#     def s(prejsnji_s):
#         cena = predmeti[i][0]
#         velikost = predmeti[i][1]
#         z = []
#         for c1,v1 in prejsni_s:
#             nov_par = (c1+cena, v1+velikost)
#             z.append(nov_par)
#         skupaj = prejsnji_s+z
#         sorted(skupaj,key=lambda x:x[1])
#         nov_s = [(0,0)]
#         i = 1
#         while i < len(skupaj)-1:
#             if skupaj[i][1] == skupaj[i+1][1]:
#                 nov_s.append(skupaj[i][0] if skupaj[i][0] >= skupaj[i+1][0] else skupaj[i+1][0])
#                 i += 1
#             elif skupaj[i][0] > skupaj[i+1][0]:
#                 nov_s.append(skupaj[i][0])
#                 i += 1
#             else:
#                 nov_s.append(skupaj[i][0])
#             i += 1
# =====================================================================@033255=
# 3. podnaloga
# Trgovec je dobil dodatno pošiljko obstoječih predmetov. Tako ima sedaj na razpolago več
# kot en predmet posameznega tipa. Predmete tako predstavimo s seznamom elementov oblike
# $(c_i, v_i, z_i)$, kjer je:
# * $c_i$ cena
# * $v_i$ teža
# * $z_i$ zaloga
# $i$-tega predmeta.
# 
# Implementiraj funkcijo `optimalni_tovor_zaloga(predmeti, W)`, ki vrne največjo skupno ceno
# predmetov, ki jih lahko trgovec natovori na letalo z maksimalno nosilnostjo `W`.
# Na primer:
# 
#     >>> optimalni_tovor_zaloga([(2,3, 1), (4,4, 2), (5,4, 4), (3,2, 3), (1,2, 3), (15, 12, 2)], 7))
#     9
# =============================================================================
import math
from functools import lru_cache
def optimalni_tovor_zaloga(predmeti, W):
    n = len(predmeti)
    novi_predmeti = []
    for k in range(n):
        par = [(predmeti[k][0], predmeti[k][1])]*predmeti[k][2]
        novi_predmeti = novi_predmeti + par
    novi_n = len(novi_predmeti)
    
    @lru_cache(maxsize=None)
    def b(i,R):
        if i == -1 and R < 0:
            return float('-inf')
        if i == -1 and R >=0:
            return 0
        return max(novi_predmeti[i][0] + b(i-1,R-novi_predmeti[i][1]), b(i-1,R))
    return b(novi_n-1,W)
# =====================================================================@033256=
# 4. podnaloga
# Predpostavi, da ima sedaj trgovec na voljo neomejeno zalogo posameznih predmetov.
# implementiraj funkcijo `neomejena_zaloga(predmeti, W)`, ki vrne najvišjo skupno ceno tovora na letalu 
# z maksimalno nosilnostjo `W`
# Na primer:
# 
#     >>> neomejena_zaloga([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 23)
#     33
# =============================================================================
import math
from functools import lru_cache
def neomejena_zaloga(predmeti, W):
    n = len(predmeti)
    novi_predmeti = []
    for cena, volumen in predmeti:
        par = [(cena, volumen)]*round(W/volumen)
        novi_predmeti = novi_predmeti + par
    novi_n = len(novi_predmeti)
    
    @lru_cache(maxsize=None)
    def b(i,R):
        if i == -1 and R < 0:
            return float('-inf')
        if i == -1 and R >=0:
            return 0
        return max(novi_predmeti[i][0] + b(i-1,R-novi_predmeti[i][1]), b(i-1,R))
    return b(novi_n-1,W)