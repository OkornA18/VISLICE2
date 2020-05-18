import bottle

import model
#naredimo objekt vislice, ki nosi informacije o vseh igrah, ki jih igramo
vislice = model.Vislice()

@bottle.get('/') #to je dekorator
def index():
    return bottle.template('views/index.tpl')

@bottle.post('/igra/')
def nova_igra():
    id_nove_igre = vislice.nova_igra()
    bottle.redirect(f'/igra/{id_nove_igre}/')

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, poskus = vislice.igre[id_igre]

    return bottle.template('views/igra.tpl', igra=igra, poskus=poskus, id_igre=id_igre)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    # dibim crko
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect(f'/igra/{id_igre}/')


bottle.run(reloader=True, debug=True)
# reloader=True zato da k spremenimo v datotekah, da ne rabmo na novo programa pognat
# debug=True da izpiše na stran kaj je narobe