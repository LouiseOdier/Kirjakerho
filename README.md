# Kirjakerho

* [x] Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* [x] Käyttäjä pystyy lisäämään sovellukseen kuvauksia kirjoista. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään kuvauksia.
* [x] Käyttäjä näkee sovellukseen lisätyt kuvaukset. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät kuvaukset.
* [x] Käyttäjä pystyy etsimään kirjoja hakusanalla tai muulla perusteella. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä kirjoja.
* [x] Käyttäjä pystyy lisäämään oman arvioinsa muiden käyttäjien lisäämiin kirja-arvioihin mutta ei pysty muutoin muokkamaan niitä.
* [x] Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät kirjat.
* [x] Käyttäjä pystyy valitsemaan kirjoille yhden tai useamman luokittelun, jotka on valmiiksi määritelty.
* [x] Sovelluksessa on pääasiallisen kuvauksen lisäksi (määritellyt luokat) toissijainen kuvaus, joka täydentää pääasiallista kuvausta (vapaa kuvaus). Käyttäjä pystyy lisäämään oman arvioinsa (vapaa kuvaus) muiden käyttäjien lisäämiin kirja-arvioihin mutta ei pysty muutoin muokkamaan niitä.

# Sovelluksen kehitysvaihe

Sovellus on valmis.

# Sovelluksen asennus

Asenna flask-kirjasto:

<pre> pip install flask </pre>

Luo tietokannan taulut ja lisää alkutiedot:

<pre>sqlite3 database.db < scema.sql
sqlite3 database.bd < init.sql </pre>

Voit käynnistää sovelluksen näin:

<pre> flask run </pre>
