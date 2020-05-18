# Nominalizáció teszt

Kompatibilitás: A PsychoPy3 2020-al éppen nem kompatibilis a script, de a 3.2-es verziókkal még igen.

Innen tölthető le a program: [https://github.com/psychopy/psychopy/releases/download/3.2.4/StandalonePsychoPy3-3.2.4-win64.exe](https://github.com/psychopy/psychopy/releases/download/3.2.4/StandalonePsychoPy3-3.2.4-win64.exe)

A betűtípusok a _fonts_ mappában találhatóak, duplakattintással meg lehet ezeket nyitni és a telepítés gombra kattintva lehet telepíteni. 

A betűtípusok telepítése *szükséges* a teszt futtatásához.

A PsychoPy3 coderben kell megnyitni a `.py` fájlokat. A `full_test.py` a teljes teszt, a `trial_run.py` a tanítóteszt.

A kimenet a data mappában található. Minden teszthez 4 fájlt generál a program a `data` mappába: 

- egy `.csv` fájlt a válaszokkal, amelyeket a tesztalany adott (minden egyéb fájl ebből generálódik)
- egy `.xlsx` fájlt a válaszokkal, amelyeket a tesztalany adott (ez szabadon megnyitható, nézegethető, ebből számolja a statisztikát a program)
- egy `_commentary.txt` fájlt, melyben az alany szöveges viszajelzése van
- egy `_statistics.xlsx` fájlt, amelyben aggregált statisztikák vannak a válaszadó válaszaiból
- egy `.log` fájlt, amiben a teszt futásával kapcsolatos információk vannak (például hogy mely képeket mikor rajzolta ki)

