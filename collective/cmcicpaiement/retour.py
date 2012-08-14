from zope import schema
from zope import interface

from collective.cmcicpaiement import i18n
from Products.Five.browser import BrowserView
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

#module var
_ = i18n.message_factory
cvx_vocabulary = SimpleVocabulary([
    SimpleTerm('oui', 'oui', _(u'Le cryptogramme visuel a ete saisie')),
    SimpleTerm('non', 'non', _(u'Pas de cryptogramme'))
])


class IRetourDataSchema(interface.Interface):
    """Retour definition"""

    MAC = schema.ASCIILine(title=_(u"MAC"),
                           description=i18n.retour_MAC_desc)

    date = schema.Date(title=_(u"Date"))

    #these data are returned as they has been received in "Aller"
    TPE = schema.ASCIILine(title=_(u"TPE"))

    montant = schema.ASCIILine(title=_(u"Montant"))

    reference = schema.ASCIILine(title=_(u"Reference"))

    texte_libre = schema.Text(title=_(u"Texte libre"))

    code_retour = schema.ASCIILine(title=_(u"Code retour"))

    cvx = schema.Choice(title=_(u"CVX"),
                           vocabulary=cvx_vocabulary)

    vld = schema.ASCIILine(title=_(u"VLD"))

    brand = schema.ASCIILine(title=_(u"Brand"))

    status3ds = schema.ASCIILine(title=_(u"status3ds"))

    numauto = schema.ASCIILine(title=_(u"numauto"),
                           description=i18n.retour_numauto_desc,
                           required=False)

    motifrefus = schema.ASCIILine(title=_(u"motifrefus"),
                                  required=False)

    originecb = schema.ASCIILine(title=_(u"originecb"))

    bincb = schema.ASCIILine(title=_(u"bincb"))

    hpancb = schema.ASCIILine(title=_(u"hpancb"))

    ipclient = schema.ASCIILine(title=_(u"ipclient"))

    originetr = schema.ASCIILine(title=_(u"originetr"))

    veres = schema.ASCIILine(title=_(u"veres"))

    pares = schema.ASCIILine(title=_(u"pares"))

    montantech = schema.ASCIILine(title=_(u"montantech"))

    filtragecause = schema.ASCIILine(title=_(u"filtragecause"))

    cbenregistree = schema.ASCIILine(title=_(u"cbenregistree"))

    cbmasquee = schema.ASCIILine(title=_(u"cbmasquee"))




class Retour(object):
    def __init__(self):
        self._MAC = None
        pass

    def from_dict(self, value):
        """value must be a dict. Call this method will load
        all values from a dict"""
        pass


    def get_MAC(self):
        return self._MAC

    def set_MAC(self, value):
        self._MAC = value

    MAC = property(get_MAC, set_MAC)


class RetourView(BrowserView):
    """Retour browser view is called by the CM CIC"""

    def __call__(self):
        self.update()
        return self.index()

    def update(self):
        #build retour object, validate it and notify the system
        #the paiement is accepted or not
        pass

