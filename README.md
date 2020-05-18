# Zimmerer-féle nominalizáció teszt

Kompatibilitás: A PsychoPy3 2020-al éppen nem kompatibilis a script, de a 3.2-es verziókkal még igen.

Innen tölthető le a program: [https://github.com/psychopy/psychopy/releases/download/3.2.4/StandalonePsychoPy3-3.2.4-win64.exe](https://github.com/psychopy/psychopy/releases/download/3.2.4/StandalonePsychoPy3-3.2.4-win64.exe)

A betűtípusok a _fonts_ mappában találhatóak, duplakattintással meg lehet ezeket nyitni és a telepítés gombra kattintva lehet telepíteni. 

A betűtípusok telepítése szükséges a szavak pontos elhelyezkedéséhez, de azok nélkül is lefut a teszt.

A PsychoPy3 **coderben** kell megnyitni a `.py` fájlokat, a builderben nem nyílik meg.

Kétféle billentyűkkel van megadva a teszt: X és O, vagy kétféle ismeretlen szimbólum. Otthoni használatra az előbbi javasolt, `XO.py` végű fájlnevek, az `UNK.py` az ismeretlen karaktereket tartalmazza.

Az `1_trial_run_XO.py` és `1_trial_run_UNK.py` a tanítótesztek, a `2_test_run_XO.py`, `2_test_run_UNK.py` az éles tesztek.

# Futtatás

TODO kettes lista! Kettes lista!

TODO, képekkel!

# Kimenet

A kimenet a data mappában található. Minden teszthez 4 fájlt generál a program a `data` mappába, a megadott név alapján: 

- egy `megadott_név.csv` fájlt a válaszokkal, amelyeket a tesztalany adott (minden egyéb fájl ebből generálódik)
- egy `megadott_név.xlsx` fájlt a válaszokkal, amelyeket a tesztalany adott (ez szabadon megnyitható, nézegethető, ebből számolja a statisztikát a program)
- egy `megadott_név_commentary.txt` fájlt, melyben az alany szöveges viszajelzése van
- egy `megadott_név_statistics.xlsx` fájlt, amelyben aggregált statisztikák vannak a válaszadó válaszaiból
- egy `megadott_név.log` fájlt, amiben a teszt futásával kapcsolatos információk vannak (például hogy mely képeket mikor rajzolta ki)

