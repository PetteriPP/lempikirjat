# Pylint-raportti


## Pylintin tuloste

```text
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:52:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:59:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:64:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:77:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:88:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:97:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:105:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:123:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:140:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:152:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:172:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:191:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:196:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:212:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:231:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module comments
comments.py:1:0: C0114: Missing module docstring (missing-module-docstring)
comments.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
comments.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:15:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:38:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:47:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:50:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:50:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module reviews
reviews.py:1:0: C0114: Missing module docstring (missing-module-docstring)
reviews.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:8:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:17:0: R0913: Too many arguments (6/5) (too-many-arguments)
reviews.py:17:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
reviews.py:24:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:28:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:43:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:43:0: R0913: Too many arguments (6/5) (too-many-arguments)
reviews.py:43:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
reviews.py:58:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:74:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module validation
validation.py:1:0: C0114: Missing module docstring (missing-module-docstring)
validation.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
validation.py:46:0: C0116: Missing function or method docstring (missing-function-docstring)
validation.py:56:0: C0116: Missing function or method docstring (missing-function-docstring)
validation.py:71:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 8.16/10 (previous run: 8.00/10, +0.16)
```

## Docstring-ilmoitukset

Suurin osa ilmoituksista koskee moduulien ja funktioiden puuttuvia docstringejä:

```text
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
```

Sovelluksessa on tietoisesti valittu tyyli, jossa moduuleihin ja funktioihin ei
lisätä docstringejä. Moduulien ja funktioiden nimet kuvaavat niiden tehtäviä, ja
sovelluksen ominaisuudet sekä käynnistämisohjeet on kuvattu `README.md`:ssä.

## Vakion nimi

```text
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
```

Pylint tulkitsee moduulin päätasolla määritellyn `secret_key`-muuttujan vakioksi,
jonka nimen pitäisi sen nimeämiskäytännön mukaan olla `SECRET_KEY`.

Nimi on säilytetty muodossa `secret_key`, koska sama nimeäminen on käytössä
kurssin esimerkkisovelluksessa. Sovelluksen asetuksen määrittely on tällöin
muotoa:

```python
app.secret_key = config.secret_key
```

Tämä on projektissa valittu nimeämiskäytäntö, minkä vuoksi nimeä ei ole muutettu
Pylintin ehdottamaan muotoon.

## Muuttuva oletusarvo

```text
db.py:15:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:50:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```

Huomautukset koskevat funktioiden `execute(sql, params=[])` ja
`query(sql, params=[])` parametrien oletusarvoja. Python luo oletusarvona olevan
listan kerran, ja sama lista on käytössä eri kutsuissa. Listan muuttaminen voisi
siksi vaikuttaa myöhempiin kutsuihin.

Nykyisessä toteutuksessa kumpikaan funktio ei muuta `params`-listaa, vaan lista
välitetään SQLite-kyselyn parametreiksi. Oletusarvona olevaan listaan ei siis
kerry tietoa kutsujen välillä. Oletusarvo on jätetty ennalleen, koska listaa
käytetään näissä funktioissa vain lukemiseen.

## Parametrien määrä

```text
reviews.py:17:0: R0913: Too many arguments (6/5) (too-many-arguments)
reviews.py:17:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
reviews.py:43:0: R0913: Too many arguments (6/5) (too-many-arguments)
reviews.py:43:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
```

Molemmat ilmoitustyypit koskevat samoja kahta funktiota:

```python
def add_review(title, author, description, rating, user_id, class_ids):
def update_review(review_id, title, author, description, rating, class_ids):
```

Funktioilla on kuusi parametria, kun Pylintin oletusraja on viisi. Parametreista
`title`, `author`, `description` ja `rating` ovat arvostelun sisältötietoja.
Lisäämisessä `user_id` kertoo kirjoittajan, ja muokkaamisessa `review_id` kertoo
muokattavan arvostelun. `class_ids` sisältää arvosteluun liitettävien
luokittelujen tunnisteet.

Parametrit on pidetty erillisinä, jotta funktion tarvitsemat tiedot näkyvät
suoraan sen määrittelyssä. Nykyisessä pienessä sovelluksessa kuusi kuvaavasti
nimettyä parametria on vielä selkeä kokonaisuus, joten niitä ei ole yhdistetty
esimerkiksi sanakirjaksi. Sama perustelu koskee molempia ilmoitustyyppejä ja
kumpaakin funktiota.
