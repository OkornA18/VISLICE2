import bottle

import model

ID_IGRE_COOKIE_NAME = "id_igre"
COOKIE_SECRET = "my_very_special - secret key and passphrase"
#naredimo objekt vislice, ki nosi informacije o vseh igrah, ki jih igramo
vislice = model.Vislice()

vislice.preberi_iz_datoteke()

@bottle.get('/') #to je dekorator
def index():
    return bottle.template('views/index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    id_nove_igre = vislice.nova_igra()

    bottle.response.set_cookie(
        ID_IGRE_COOKIE_NAME, str(id_nove_igre), path="/", secret=COOKIE_SECRET
    )

    bottle.redirect(f'/igra/')

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie(ID_IGRE_COOKIE_NAME, secret=COOKIE_SECRET))
    igra, poskus = vislice.igre[id_igre]

    return bottle.template('views/igra.tpl', igra=igra, poskus=poskus, id_igre=id_igre)


@bottle.post('/igra/')
def ugibaj():

    id_igre = int(bottle.request.get_cookie(ID_IGRE_COOKIE_NAME, secret=COOKIE_SECRET))
    # dobim crko
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect(f'/igra/')


bottle.run(reloader=True, debug=True)
# reloader=True zato da k spremenimo v datotekah, da ne rabmo na novo programa pognat
# debug=True da izpiše na stran kaj je narobe

