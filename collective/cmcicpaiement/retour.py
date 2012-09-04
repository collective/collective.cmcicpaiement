from zope import event
from zope import schema
from zope import interface
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from Products.Five.browser import BrowserView

from collective.cmcicpaiement import i18n

#module var
_ = i18n.message_factory

cvx_vocabulary = SimpleVocabulary([
    SimpleTerm('oui', 'oui', _(u'Le cryptogramme visuel a ete saisie')),
    SimpleTerm('non', 'non', _(u'Pas de cryptogramme'))
])


class RetourView(BrowserView):
    """Retour browser view is called by the CM CIC"""
    sceau_validated_accuse_reception = "version=2\ncdr=0\n"
    sceau_notvalidated_accuse_reception = "version=2\ncdr=1\n"

    def __call__(self):
        self.update()
        if self._is_sceau_valide:
            return self.sceau_validated_accuse_reception
        self.notify()
        return self.sceau_notvalidated_accuse_reception

    def update(self):
        #build retour object, validate it and notify the system
        #the paiement is accepted or not
        self.event = RetourEvent(self.request)
        self._validate_sceau()

    def _validate_sceau(self):
        self._is_sceau_valide = True

    def notify(self):
        event.notify(self.event)

RETOUR_ATTRS = {
  "MAC": None,
  "TPE": None,
  "date": {"strptime": "%d/%m/%Y_a_%H:%M:%S"},
  "montant": None,
  "texte_libre": {"name": "texte-libre"},
  "reference": None,
  "code-retour": {"name": "code-retour",
                  "constraints": ('payetest', 'paiement', 'Annulation')},
  "cvx": None,
  "vld": None,
  "brand": {"constraints": ('AM', 'CB', 'MC', 'VI', 'na')},
  "status3ds": {"constraints": ('-1', '1', '2', '3', '4')},
  "numauto": None,
  "motifrefus": {"constraints": ('Appel Phonie', 'Refus', 'Interdit', 'Filtrage')},
  "originecb": None, #TODO code iso 3166-1
  "bincb": None,
  "hpancb": None,
  "ipclient": None,
  "originetr": None, #TODO code iso 3166-1
  "veres": None,
  "pares": None,
  "montanttech": None,
  "filtragecause": {"constraints": ('1', '2', '3', '4', '5', '6', '7', '8',
                            '9', '10', '11', '12', '13', '14', '15', '16')},
  "filtragevaleur": None,
  "cbmasquee": None
}

class RetourEvent(object):
    """Retour event is throwed when the bank contact the server
    You have to subscribe to this event to manage bank return
    
    Notification happens on every try.
    """
    implements(IRetourDataSchema)

    def __init__(self, retour):
        self.retour = retour

    def __getattr__(self, name):
        if name in RETOUR_ATTRS:
            config = RETOUR_ATTRS[name]
            if config and "name" in config:
                value = self.retour[config['name']]
            else:
                value = self.retour[name]
            if config and "strptime" in config:
                value = datetime.strptime(value, config["strptime"])

            if config and 'constraints' in config:
                if value in config['constraints']:
                    return value
                else:
                    logger.error('wrong value for %s: %s' % (name, value))
            else:
                return value
        return super(RetourEvent, self).__getattr__(name)

