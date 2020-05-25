# Zimmerer-féle nominalizáció teszt

## Általános tudnivalók

Kompatibilitás: A PsychoPy3 2020-al éppen nem kompatibilis a script, de a 3.2-es verziókkal még igen.

Innen tölthető le a megfelelő verziójú program: [https://github.com/psychopy/psychopy/releases/download/3.2.4/StandalonePsychoPy3-3.2.4-win64.exe](https://github.com/psychopy/psychopy/releases/download/3.2.4/StandalonePsychoPy3-3.2.4-win64.exe)  
Telepítése egyszerű next-next-install.

A betűtípusok a _fonts_ mappában találhatóak, duplakattintással meg lehet ezeket nyitni és a telepítés gombra kattintva lehet telepíteni. Amennyiben nem működik olyan egyszerűen, Windowson a vezérlőpultban rá lehet keresni a betűtípusok kulcsszóra, és oda drag&dropolva lehet telepíteni.

A betűtípusok telepítése szükséges a szavak pontos elhelyezkedéséhez, de azok nélkül is lefut a teszt.

A PsychoPy3 **coderben** kell megnyitni a `.py` fájlokat, a builderben nem nyílik meg.

Kétféle billentyűkkel van megadva a teszt: X és O, vagy kétféle ismeretlen szimbólum. Otthoni használatra az előbbi javasolt, `XO.py` végű fájlnevek, az `UNK.py` az ismeretlen karaktereket tartalmazza.

Az `1_trial_run_XO.py` és `1_trial_run_UNK.py` a tanítótesztek, a `2_test_run_XO.py`, `2_test_run_UNK.py` az éles tesztek.

## Github repó letöltése

Először szükségünk lesz magára a tesztre. 

A jobb felső sarokban van egy nagy zöld gomb **Clone or download** felirattal, utána **Download as ZIP**, majd ki kell tömöríteni egy tetszőleges mappába.

Az alábbi ábra segít a letöltésben:

![a Github oldala](readme/github_site.png)

## Futtatás

1. Először meg kell nyitni a PsychoPy **Coder**t. Nagyon fontos, hogy a **Coder**t, és ne a **Builder**t nyissuk meg. Pirossal alá van húzva a lenti ábrán.

2. Amennyiben megnyitottuk a Codert, be kell tallózni a tanítóteszt fájlát, ami ott van, ahova kitömörítettük a Github repót. (`1_trial_run_XO.py` otthoni használatra). 
Ezt a File -> Open menüpontban vagy a zölddel kékkel bekeretezett ikonnál tudjuk megtenni.
3. Amennyiben betallóztuk a fájlt, a program megnyitja fülként fájlt és látjuk a tanítóteszt nevét a fülön. (az ábrán zölddel van kijelölve)

4. Ezután, a nagy zöld, futó emberre kattintva elindul a teszt. (pirossal be van keretezve az ábrán)


TODO kettes lista! Kettes lista!

TODO, képekkel!

## Kimenet

A kimenet a data mappában található. Minden teszthez 4 fájlt generál a program a `data` mappába, a megadott név alapján: 

- egy `megadott_név.csv` fájlt a válaszokkal, amelyeket a tesztalany adott (minden egyéb fájl ebből generálódik)
- egy `megadott_név.xlsx` fájlt a válaszokkal, amelyeket a tesztalany adott (ez szabadon megnyitható, nézegethető, ebből számolja a statisztikát a program)
- egy `megadott_név_commentary.txt` fájlt, melyben az alany szöveges viszajelzése van
- egy `megadott_név_statistics.xlsx` fájlt, amelyben aggregált statisztikák vannak a válaszadó válaszaiból
- egy `megadott_név.log` fájlt, amiben a teszt futásával kapcsolatos információk vannak (például hogy mely képeket mikor rajzolta ki)

