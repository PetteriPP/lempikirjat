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
```

- Käynnistä sovellus:

```bash
flask run
```
