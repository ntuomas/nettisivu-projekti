# Django 2 -ohje: kehitysympäristön perustaminen sekä CRUD-toiminnallisuuksien luominen

###### Esimerkkisivusto on hyvin yksinkertainen CRUD-toiminnallisuudet sisältävä sivusto, jossa visuaalinen ilme on melko pelkistetty ja keskitytty näyttämään, miten käyttäjä voi luoda, lukea, päivittää sekä poistaa sisältöä. Esimerkkisivuston tapauksessa käyttäjä lisätä kirjoituksia, lukea, muokata ja poistaa niitä.

## _Kehitysympäristön perustaminen_
Työssä käytetään Django 2.x -versiota sekä Pythonista 3.x -versiota. Lisäksi käytössä on Mac, joten kehitysympäristön perustamiseen liittyvät toiminnot koskevat Mac-käyttäjiä, joskin toiminta on pieniä eroja lukuunottamatta hyvin samankaltaista Windowsilla. Itse Djangon sisällä tapahtuvat asiat ovat kuitenkin samoja riippumatta käyttöjärjestelmästä.

Jos et ole vielä asentanut Djangoa, niin uusimman version saat helposti kirjoittamalla päätteseen:
```
pip3 install Django
```
(huom! käytä pip3:sta pelkän pip:n sijaan, koska käytät Pythonin 3-versiota)

Nyt kun sinulla on tietokoneella asennettuna Python 3.x ja Django, niin pystyt aloittamaan Django-projektin vaikka heti. On kuitenkin suositeltavaa käyttää virtuaaliympäristöä, jolla tarkoitetaan siis omaa suljettua ympäristöä, jossa voit käyttää esimerkiksi Djangon eri versioita, vaikka koneellasi olisi toinen versio. Jos löydät vaikkapa netistä Django-ohjeen, jossa käytetään 1.x -versiota ja haluat testata koodia omalla koneella, sinun ei tarvitse asentaa uutta versiota Djangosta koneellesi, vaan riittää, että asennat sen uuteen virtuaaliympäristöön. (kannattaa silti keskittyä vain 2.x-versioon) Kyseessä on ikään kuin oma maailmansa, joka ei vaikuta sen ulkopuolella oleviin projekteihin. Asennus tapahtuu helposti kirjoittamalla päätteeseen:
```
pip3 install virtualenv
```
Tämän jälkeen olet valmis käyttämään virtuaaliympäristöä. Uuden virtuaaliympäristön perustaminen tehdään komennolla:
```
virtualenv mikänimitahansa
```
"mikänimitahansa" sijaan kannattaa käyttää jotain hieman järkevämpää, esimerkiksi "myvenv" tai "venv" ovat yleisesti käytettyjä nimiä. Älä perusta uutta virtuaaliympäristöä heti asentamisen perään, vaan mieti minne haluat sen laittaa. Itse tykkään tehdä asian seuraavasti: (huom! Virtuaaliympäristön sisällä ei tarvite käyttää pip3:sta eikä python3:sta vaan pelkkä pip ja python toimivat)
1. Luo työpöydälle uusi kansio, jonka nimeät selkeästi, esimerkiksi "Django-harjoitus"
2. Avaat päätteessä (terminaalissa) tekemäsi kansion
3. Luo uusi virtuaaliympäristö tekemääsi kansioon
4. Luo samaan kansioon uusi Django-projekti
5. Aktivoi virtuaaliympäristö
6. Asenna Django virtuaaliympäristöösi
7. Testaa toimivuus

Terminaalissa liikkuessa cd ja ls komennot ovat tarpeen. cd tarkoittaa, että siirrytään haluttuun kansioon ja ls-komennolla voit katsoa mitä kansio sisältää. Terminaalissa edellä mainittu näyttäisi tältä:

```
$ cd desktop
$ cd django-harjoitus
$ virtualenv myvenv
$ django-admin startproject nettisivu
$ source myvenv/bin/activate
(myvenv) $ pip install django
(myvenv) $ cd nettisivu
(myvenv) $ python manage.py runserver
```
Jos kaikki meni nappiin, niin nyt sinulla pitäisi olla Django-projekti toiminnassa. Tämän voit tarkistaa menemällä selaimellasi osoitteeseen "localhost:8000". Jos sivulla näkyy kuva raketista, niin kaikki pitäisi olla kunnossa. Komennolla django-admin startproject "nimi" django luo siis kaiken tarvittavan pohjan projektillesi. python manage.py runserver -komennolla käynnistät oman palvelimesi, jolloin voit katsoa nettisivuasi edellämainitusta osoitteesta. Kun avaat projektin tekstieditorissa (esim. Atom), niin valitse "nettisivu". Tätä ennen kannattaa myös uudelleennimetä nettisivu esimerkiksi nettisivu-projektiksi selkeyden vuoksi.  Django käyttää valmiina SQLite3-tietokantaa, joka riittää hyvin harjoitustyössä, mutta jos aiot laittaa työn esimerkiksi Herokuun, PostgreSQL:n tms. käyttäminen on järkevää.

Tässä vaiheessa on myös hyvä tehtä komennot:
```
(myvenv) $ python manage.py makemigrations
(myvenv) $ python manage.py migrate
```
Lisäksi luo admin-tunnukset komennolla:

```
(myvenv) $ python manage.py createsuperuser
```
## _CRUD-toiminnallisuus_
Create, Read, Update ja Delete eli CRUD-toiminnallisuudet ovat yleisesti käytettyjä ominaisuuksia web-sovelluksissa. Djangon avulla nämä ovat melko yksinkertaisia toteuttaa käyttäen valmiita näkymiä.

Kun olet terminaalissa virtuaaliympäristön sisällä nettisivu-kansiossa, saat luotua uuden App:n komennolla:
```
(myvenv) $ python manage.py startapp appinnimi
```
eli esimerkkitoteutuksessa
```
(myvenv) $ python manage.py startapp kirjoitukset
```
Nyt kun katsot tekstieditoriasi, näet uuden kirjoitukset-kansion nettisivu-projektin sisällä. Tässä vaiheessa kannattaa mennä lisäämään nettisivu-kansion settings.py-tiedoston INSTALLED_APPS-kohtaan 'kirjoitukset'.
Kirjoitukset-kansion muokattavat tiedostot ovat models.py ja views.py. Luo lisäksi urls.py-niminen tiedosto.

### models.py-tiedosto
```
from django.db import models
from django.urls import reverse


class Kirjoitus(models.Model):
    kirjoittaja = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    otsikko = models.CharField(max_length=100)
    teksti = models.TextField()

    def __str__(self):
        return self.otsikko

    def get_absolute_url(self):
        return reverse('koti')
```
class Kirjoitus tarkoittaa sitä, että luodaan tietokantaan uusi Kirjoitus-niminen taulu, jossa on kirjoittaja-, otsikko- ja teksti-sarakkeet. ForeignKey, CharField ja TextField ovat puolestaan Djangossa olevia ominaisuuksia eri sarakkeille. Esim. Otsikko voi kirjoittaa vain sata merkkiä. _ _str_ _  -funktion avulla voidaan määrittää, mitä admin-paneelissa halutaan näyttää kunkin kirjoituksen kohdalla. Tämä ei siis ole pakollinen, mutta selkeyttää. Funktio get_ _absolute_ _url taas tarkoittaa osoitetta mille ohjataan kun uusi kirjoitus lisätään.

### urls.py-tiedosto
Djangon url-toiminta on yksinkertaisesti selitettynä seuraavanlainen:
1. Django katsoo mitä selaimessa on localhost:8000/ (tai domainin) perässä.
2. Django katsoo urls.py.tiedostosta vastaavan polun ja sitä vastaavan luokan nimen.
3. Django katsoo views.py-tiedostosta oikean luokan.
4. Django tekee mitä luokka pyytää.

Kotisivu on helppo esimerkki. Osoitteen perässä ei ole mitään, joten Django katsoo urls.py:stä polun, jossa on ' ' . Views.KirjoitusListView.as_view() kertoo, että katsotaan views.py-tiedostosta KirjoitusListView-nimistä luokkaa. Luokassa on puolestaan ilmoitettu, että lähetetään HTTP-vastauksena "koti.html"-tiedosto.

### views.py-tiedosto
Tässä tiedostossa luodaan "back-end" CRUD-toiminnoille. Kaikki tapahtuu helposti käyttämällä Djangon valmiita näkymiä, joita ovat ListView, DetailView, CreateView, UpdateView, DeleteView.

```
class KirjoitusListView(ListView):
    model = Kirjoitus
    template_name = 'koti.html'
```
Etusivun näkymä, jossa kaikki kirjoitukset ovat listattuna. Ohjataan koti.html-sivulle, jossa kaikki kirjoitukset käydään läpi seuraavasti:
```
{% for kirjotus in object_list %}
<div class="kirjoitus">
  <h3><a href="{% url 'yksityiskohdat' kirjotus.pk %}">{{ kirjotus.otsikko}}</a></h3>
  <p>{{  kirjotus.teksti }}</p>
</div>
<hr />
{% endfor %}
```
Huom. object_list on Djangon oma nimitys, joten käytä sitä. Seuraavassa kohdassa näytetään, miten sitä voi muuttaa

```
class KirjoitusDetailView(DetailView):
    model = Kirjoitus
    template_name = "yksityiskohdat.html"
    context_object_name = 'kaikkikirjoitukset' #korvataan object_list-nimi
```
Tällä sivulla näet kirjoituksen tarkemmin "yksityiskohdat"-sivulla, sekä voit muokata ja poistaa kirjoituksen. context_object_name käyttämällä voit korvata object_list-nimen.

```
  <h3>{{ kaikkikirjoitukset.otsikko }}</h3>
  <br />
  <p>{{ kaikkikirjoitukset.teksti }}</p>

<hr />
<h5><a href="{% url 'muokkaa' kaikkikirjoitukset.pk %}">Muokkaa kirjoitusta!</a></h5>
<h5><a href="{% url 'poista' kaikkikirjoitukset.pk %}">Poista kirjoitus!</a></h5>
```
Tässä vaiheessa on olemassa CRUD-ominaisuuksista lukeminen. Seuraavaksi näytetään, miten uuden kirjoituksen voi luoda.

```
class KirjoitusCreateView(CreateView):
    model = Kirjoitus
    template_name = "uusi_kirjoitus.html"
    fields = '__all__'
```
CreateView noudattaa samaa kaavaa kuin edelliset näkymät. fields = '_ _all_ _' tarkoitetaan sitä, että valitaan tietokannan jokainen kenttä "uusi_kirjoitus.html" olevaan formiin. Näyttää siis tältä:

```
<form action="" method="POST">
  {% csrf_token %}

  {{ form.as_p }}

  <input type="submit" value="Tallenna!">

</form>
```
Eli pelkästään kirjoittamalla edellä olevan, Django luo automaattisesti kentän, johon voi syöttää kirjoittajan, otsikon ja tekstin. Hyvin yksinkertaista! Muokkaamiseen käytetään UpdateView-näkymää:

```
class KirjoitusUpdateView(UpdateView):
    model = Kirjoitus
    template_name = "muokkaa.html"
    fields = ['otsikko', 'teksti']
```
Eli sama kaava. Django ohjaa "muokkaa.html"-sivulle. Haluamme muokata vain otsikkoa ja tekstiä, joten fields-kohtaan valitaan ne. html-tiedosto on hyvin samankaltainen kuin edellinen
```
<form action="" method="POST">
{% csrf_token %}
{{ form.as_p }}

<input type="submit" value="Päivitä!">

</form>
```
Viimeisenä ominaisuutena tarvitaan kirjoituksen poisto -ominaisuus. Tässäkin tapauksessa käytetään Djangon valmista DeleteView-näkymää.
```
class KirjoitusDeleteView(DeleteView):
    model = Kirjoitus
    template_name = "poista.html"
    context_object_name = 'kaikkikirjoitukset'
    success_url = reverse_lazy('koti')
```
Ja sama toimintaperiaate. Uutena asiana on succes_url, jolla tarkoitetaan osoitetta, johon ohjataan, kun kirjoitus on poistettu.

###### Nyt siis on kaikki CRUD-toiminnallisuudet käytössä. Kuitenkin yksi oleellinen osa sivustoa puuttuu, nimittäin käyttäjät. Seuraavaksi käydään läpi uuden tunnuksen luonti, sisäänkirjautuminen sekä uloskirjautuminen. Ja kuten edellisessä kohtaa, käytetään tässäkin Djangon valmiita toimintoja.

## _Käyttäjät_

Luodaan heti aluksi uusi App nimeltä tilit. Samanlailla kuin kirjoitukset-app.
```
(myvenv) $ python manage.py startapp tilit
```
Lisäksi lisätään se settings.py-tiedoston INSTALLED_APPS-kohtaan.

Ainoat tiedostot joihin pitää koskea ovat urls.py ja views.py. Tarvittava tietokannan taulu on luotu jo aikaisemmin, joten models.py-tiedostoon ei kosketa. Toimintaperiaate on käytännössä sama kuin kirjoitukset-appissa. views.py-tiedostossa on vain yksi luokka nimeltä SignUpView:
```
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
```
Tässä käytetään siis valmista UserCreationForm:a. Ulkonäöllisesti kyseessä ei ole ehkä se kaunein vaihtoehto, mutta ajaa asiansa. Sisään- ja uloskirjautuminen on myös todella yksinkertaista. Luo templates-kansioon uusi registration-kansio, jonka sisään teet login.html-tiedoston, jolloin Djangon _django.contrib.auth.views.login_ automaattisesti hoitaa sisään-ja uloskirjautumiseen liittyvät asiat.
