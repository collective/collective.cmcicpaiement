# -*- coding: utf-8 -*-
"""Le sceau (à mettre dans le champ MAC) est calculé à l’aide d’une fonction
de hachage cryptographique en combinaison avec une clé secrète respectant
les spécifications de la RFC 2104.
Cette fonction générera le sceau à partir de données à certifier et
de la clé de sécurité commerçant sous sa forme opérationnelle.
Les données à certifier seront présentées sous la forme d’une concaténation
dans un ordre précis des informations du formulaire :

  <TPE>*<date>*<montant>*<reference>*<texte-libre>*
  <version>*<lgue>*<societe>*<mail>*<nbrech>*<dateech1>*<monta
  ntech1>*<dateech2>*<montantech2>*<dateech3>*<montantech3>*<d
  ateech4>*<montantech4>*<options>"""

#python
import hmac  # the python implementation of RFC 2104

#zope
from zope import component

#plone
from plone.registry.interfaces import IRegistry

#others
from collective.cmcicpaiement import settings

KEYS_ORDER = ('TPE','date','montant','reference','texte-libre',
'version','lgue','societe','mail','nbrech','dateech1',
'montantech1','dateech2','montantech2','dateech3','montantech3',
'dateech4','montantech4','options')

SEPARATOR = '*'


class MAC(object):
    """Wrapper around hmac library to load key from plone registry"""
    def __init__(self, key=None, msg=None, digestmod=None):
        self._wrapped = None
        self.digestmod = digestmod  # not used atm
        self._key = None
        if msg is not None:
            self.update(msg)
        if key is not None:
            self.set_key(key)

    def update(self, message=None):
        if self._key is None:
            registry = component.queryUtility(IRegistry)
            records = registry.forInterface(settings.Settings)
            self.set_key(records.security_key)

        if message and not self._wrapped:
            raise ValueError('can set a message in HMAC without a key')
        elif message:
            self._wrapped.update(message)

    def set_key(self, value):
        self._key = value
        self._wrapped = hmac.new(self._key)

    def digest(self):
        return self._wrapped.digest()

    def hexdigest(self):
        return self._wrapped.hexdigest()

    def __repr__(self):
        return self._wrapped.hexdigest()


def format_data(data):
    """Return a string from a dict supposed to have all waited keys"""
    concatened = ""
    for KEY in KEYS_ORDER:
        if KEY in data:
            concatened += data[KEY]
    return concatened
