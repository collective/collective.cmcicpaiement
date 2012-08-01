#zope
from zope import schema
from zope import interface

#others
from collective.cmcicpaiement import i18n

_ = i18n.message_factory
contact_source_vocab = ['member', 'creator']

class Settings(interface.Interface):

    security_key = schema.Password(title=u"Security Key",
                                   description=u"This key is provided by the CM-CIC to the seller. Must be kept secret. This key is a 40 length of hexa caracters")

    TPE = schema.ASCIILine(title=_(u"TPE"))

    contact_source = schema.ASCIILine(title=_(u"Contact source"),
                                      vocabulary=contact_source_vocab)

    societe = schema.ASCIILine(title=_(u"Societe number"))
