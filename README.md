# Lempikirjat

*  Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
*  Käyttäjä pystyy lisäämään sovellukseen kirja-arvioita lukemistaan kirjoista. Kirja-arviot sisältävät kirjan nimen, kirjailijan, arvosanan ja käyttäjän kirjoittaman arvion. Käyttäjä pystyy muokkaamaan ja poistamaan omia kirja-arvioitaan.
*  Käyttäjä näkee sovellukseen lisätyt kirja-arvostelut. Käyttäjä näkee sekä omat että muiden käyttäjien tekemät kirja-arvostelut.
*  Käyttäjä pystyy etsimään kirja-arvioita hakusanalla tai muulla perusteella. Käyttäjä pystyy etsimään kirja-arvioita esimerkiksi kirjan nimen, kirjailijan nimen tai arvosanan perusteella.
*  Sovelluksessa on käyttäjäsivut, jotka näyttävät käyttäjän lisäämät kirja-arviot sekä tilastoja, kuten lisättyjen kirja-arvioiden määrän.
*  Kirjoille on valittavissa useampia luokitteluja. Luokittelujen vaihtoehdot määritellään tietokannassa. Kirjalle voidaan valita esimerkiksi yksi tai useampi genre sekä yksi tai useampi teema.
* Käyttäjä pystyy lisäämään kommentteja omiin ja muiden käyttäjien kirja-arvioihin.

## Ohjeet sovelluksen käynnistämiseen

- Kloonaa repositorio omalle koneellesi:

```bash
git clone https://github.com/PetteriPP/lempikirjat
cd lempikirjat
```

- Luo virtuaaliympäristö ja aktivoi se:

```bash
python3 -m venv venv
source venv/bin/activate
```

- Asenna Flask:

```bash
pip install flask
```

- Luo tietokanta:

```bash
sqlite3 database.db < schema.sql
sqlite3 database.db < init.sql
```

- Käynnistä sovellus:

```bash
flask run
```

## Sovelluksen testaaminen

Sovellusta voi testata luomalla sovellukseen ainakin kaksi käyttäjätiliä. Sen jälkeen pystyy luomaan kirja-arvosteluja sekä kommentoimaan muiden käyttäjien kirja-arvosteluja. Kommenttien lisääminen kirja-arvosteluihin vaatii käyttäjätilin.

## Suuren tietomäärän käsittely

Etusivun arvostelut, hakutulokset, käyttäjän arvostelut ja arvostelun kommentit
näytetään 20 kohdetta kerrallaan. Sivua vaihdetaan Edellinen- ja Seuraava-linkeillä.
Hakusana säilyy sivua vaihdettaessa. Uuden kommentin lisäämisen jälkeen näytetään
viimeinen kommenttisivu, jolla lisätty kommentti näkyy.

Tiedostossa `schema.sql` on kaksi indeksiä:

- `idx_reviews_user_id` nopeuttaa käyttäjän arvostelujen hakemista ja laskemista.
- `idx_comments_review_id` nopeuttaa arvostelun kommenttien hakemista ja laskemista.

### Testiaineisto

`seed.py` lisää tyhjään tietokantaan 1 000 käyttäjää, 100 000 arvostelua,
200 000 luokitteluviittausta ja 1 000 000 kommenttia. Jokaiselle arvostelulle
valitaan genre ja teema. Testikäyttäjät ovat `user1`–`user1000`, ja kaikkien
salasana on `test-password`.

### Tulokset

Käyttäjällä `user1` oli 20 081 arvostelua ja arvostelulla 1 yhteensä 200 008 kommenttia. Näin myös
yksittäisen käyttäjän ja arvostelun sivutus testattiin suurella tietomäärällä.

Kaikki testatut sivut toimivat ja näyttivät enintään 20 kohdetta kerrallaan.
Etusivulta tarkistettiin ensimmäinen, keskimmäinen ja viimeinen sivu, hausta
osumat ja tyhjä tulos sekä käyttäjä- ja kommenttilistoista ensimmäinen ja
viimeinen sivu.
