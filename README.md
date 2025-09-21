# Kirjakerho

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään sovellukseen kuvauksia kirjoista. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään kuvauksia.
* Käyttäjä näkee sovellukseen lisätyt kuvaukset. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät kuvaukset.
* Käyttäjä pystyy etsimään kirjoja hakusanalla tai muulla perusteella. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä kirjoja.
* Käyttäjä pystyy lisäämään oman arvioinsa muiden käyttäjien lisäämiin kirja-arvioihin mutta ei pysty muutoin muokkamaan niitä.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät kirjat.
* Käyttäjä pystyy valitsemaan kirjoille yhden tai useamman luokittelun, jotka on valmiiksi määritelty
* Sovelluksessa on pääasiallisen kuvauksen lisäksi (määritellyt luokat) toissijainen kuvaus, joka täydentää pääasiallista kuvausta (vapaa kuvaus). Käyttäjä pystyy lisäämään oman arvioinsa (vapaa kuvaus) muiden käyttäjien lisäämiin kirja-arvioihin mutta ei pysty muutoin muokkamaan niitä.

# Sovelluksen kehitysvaihe

Sovellusta on lähdetty kehittämään hyvin pitkälle esimerkkiä noudattaen. Nyt kun sovelluksen "runko" alkaa olla
valmis, sovellukseen lähdetään lisäämään Kirjakerhon toiminnalle ominaisia elementtejä.

# Sovelluksen asennus

Asenna flask-kirjasto:

<pre> pip install flask </pre>

Luo tietokannan taulut ja lisää alkutiedot:

<pre>sqlite3 database.db < scema.sql
sqlite3 database.bd < init.sql </pre>

Voit käynnistää sovelluksen näin:

<pre> flask run </pre>
