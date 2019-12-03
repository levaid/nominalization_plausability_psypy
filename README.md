# Nominalizáció teszt

A betűtípusok a _fonts_ mappában találhatóak, duplakattintással meg lehet ezeket nyitni és a telepítés gombra kattintva lehet telepíteni. 

A betűtípusok telepítése *szükséges* a teszt futtatásához.

A PsychoPy3 coderben kell megnyitni a `.py` fájlokat. A `full_test.py` a teljes teszt, a `trial_run.py` a tanítóteszt.

A kimenet a data mappában található. Minden teszthez 4 fájlt generál a program: 
- egy `.csv` fájlt a válaszokkal, amelyeket a tesztalany adott (ezt az Excel megnyitja)
- egy `_commentary.txt` fájlt, melyben az alany szöveges viszajelzése van
- egy `_statistics.xlsx` fájlt, amelyben aggregált statisztikák vannak a válaszadó válaszaiból
- egy `.log` fájlt, amiben a teszt futásával kapcsolatos információk vannak (például hogy mely képeket mikor rajzolta ki)