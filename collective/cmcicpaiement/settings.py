#zope
from zope import schema
from zope import interface

#others
from collective.cmcicpaiement import i18n

_ = i18n.message_factory
contact_source_vocab = ['member', 'creator']

url_paiement_vocabulary = SimpleVocabulary([
    SimpleTerm("https://paiement.creditmutuel.fr/test/paiement.cgi",
               "https://paiement.creditmutuel.fr/test/paiement.cgi",
               u"creditmutuel TEST"),
    SimpleTerm("https://paiement.creditmutuel.fr/paiement.cgi",
               "https://paiement.creditmutuel.fr/paiement.cgi",
               u"creditmutuel PRODUCTION"),
    SimpleTerm("https://ssl.paiement.cic-banques.fr/test/paiement.cgi",
               "https://ssl.paiement.cic-banques.fr/test/paiement.cgi",
               u"cic-banques TEST"),
    SimpleTerm("https://ssl.paiement.cic-banques.fr/paiement.cgi",
               "https://ssl.paiement.cic-banques.fr/paiement.cgi",
               u"cic-banques PRODUCTION"),
    SimpleTerm("https://ssl.paiement.banque-obc.fr/test/paiement.cgi",
               "https://ssl.paiement.banque-obc.fr/test/paiement.cgi",
               u"banque-obc TEST"),
    SimpleTerm("https://ssl.paiement.banque-obc.fr/paiement.cgi",
               "https://ssl.paiement.banque-obc.fr/paiement.cgi",
               u"banque-obc PRODUCTION"),
])

url_capture_vocabulary = SimpleVocabulary([
    SimpleTerm("https://paiement.creditmutuel.fr/test/capture_paiement.cgi",
               "https://paiement.creditmutuel.fr/test/capture_paiement.cgi",
               u"creditmutuel TEST"),
    SimpleTerm("https://paiement.creditmutuel.fr/capture_paiement.cgi",
               "https://paiement.creditmutuel.fr/capture_paiement.cgi",
               u"creditmutuel PRODUCTION"),
    SimpleTerm("https://ssl.paiement.cic-banques.fr/test/paiement.cgi",
               "https://ssl.paiement.cic-banques.fr/test/paiement.cgi",
               u"cic-banques TEST"),
    SimpleTerm("https://ssl.paiement.cic-banques.fr/capture_paiement.cgi",
               "https://ssl.paiement.cic-banques.fr/capture_paiement.cgi",
               u"cic-banques PRODUCTION"),
    SimpleTerm("https://ssl.paiement.banque-obc.fr/test/capture_paiement.cgi",
               "https://ssl.paiement.banque-obc.fr/test/capture_paiement.cgi",
               u"banque-obc TEST"),
    SimpleTerm("https://ssl.paiement.banque-obc.fr/capture_paiement.cgi",
               "https://ssl.paiement.banque-obc.fr/capture_paiement.cgi",
               u"banque-obc PRODUCTION"),
])

url_recredit_vocabulary = SimpleVocabulary([
    SimpleTerm("https://paiement.creditmutuel.fr/test/recredit_paiement.cgi",
               "https://paiement.creditmutuel.fr/test/recredit_paiement.cgi",
               u"creditmutuel TEST"),
    SimpleTerm("https://paiement.creditmutuel.fr/recredit_paiement.cgi",
               "https://paiement.creditmutuel.fr/recredit_paiement.cgi",
               u"creditmutuel PRODUCTION"),
    SimpleTerm("https://ssl.paiement.cic-banques.fr/test/recredit_paiement.cgi",
               "https://ssl.paiement.cic-banques.fr/test/recredit_paiement.cgi",
               u"cic-banques TEST"),
    SimpleTerm("https://ssl.paiement.cic-banques.fr/recredit_paiement.cgi",
               "https://ssl.paiement.cic-banques.fr/recredit_paiement.cgi",
               u"cic-banques PRODUCTION"),
    SimpleTerm("https://ssl.paiement.banque-obc.fr/test/recredit_paiement.cgi",
               "https://ssl.paiement.banque-obc.fr/test/recredit_paiement.cgi",
               u"banque-obc TEST"),
    SimpleTerm("https://ssl.paiement.banque-obc.fr/recredit_paiement.cgi",
               "https://ssl.paiement.banque-obc.fr/recredit_paiement.cgi",
               u"banque-obc PRODUCTION"),
])


class Settings(interface.Interface):

    security_key = schema.Password(title=u"Security Key",
                                   description=u"This key is provided by the CM-CIC to the seller. Must be kept secret. This key is a 40 length of hexa caracters")

    TPE = schema.ASCIILine(title=_(u"TPE"))

    contact_source = schema.ASCIILine(title=_(u"Contact source"),
                                      vocabulary=contact_source_vocab)

    societe = schema.ASCIILine(title=_(u"Societe number"))

    url_paiement = schema.URI(title=_(u"URL Paiement"),
                              vocabulary=url_paiement_vocabulary,
              default="https://paiement.creditmutuel.fr/test/paiement.cgi")

    url_capture = schema.URI(title=_(u"URL Capture"),
                             vocabulary=url_capture_vocabulary,
            default=DEFAULT_URL_CM['capture'])

    url_recredit = schema.URI(title=_(u"URL Recredit"),
                              vocabulary=url_recredit_vocabulary,
            default=DEFAULT_URL_CM['recredit'])
