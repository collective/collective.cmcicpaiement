#zope
from zope import component
from zope import schema
from zope import interface
from Products.Five.browser import BrowserView

#plone
from plone.registry.interfaces import IRegistry

#others
from collective.cmcicpaiement import sceau
from collective.cmcicpaiement import settings
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IAllerDataSchema(interface.Interface):
    """Interface "Aller" define all the needed data to create the form"""
    
    version = schema.ASCIILine(title=u"version",
                               default="3.0")

    TPE = schema.ASCIILine(title=u"TPE",
                           description=u"Numero de TPE Virtuel du commerçant. Length : 7 caracters")

    montant = schema.ASCIILine(title=u"Montant",
                               description=u"Montant TTC de la commande formatee")

    reference = schema.ASCIILine(title=u"Reference ID",
                                 description=u"12 max")

    texte_libre = schema.Text(title=u"Some text",
                              description=u"3200 caracters max")

    mail = schema.ASCIILine(title=u"EMail address")

    lgue = schema.ASCIILine(title=u"Language")

    societe = schema.ASCIILine(title=u"Societe")

    url_retour = schema.URI(title=u"Visitor URL to come back")

    url_retour_ok = schema.URI(title=u"Visitor URL to come back",
                               description=u"next to an accepted paiement")

    url_retour_err = schema.URI(title=u"Visitor URL to come back",
                               description=u"next to a failed paiement")

    MAC = schema.ASCIILine(title=u"Sceau from the certification of data")

    options = schema.ASCIILine(title=u"URL encoded other options",
                               description=u"Options must be in aliascb,forcesaisiecb")


class IFractionnedAllerDataSchema(IAllerDataSchema):

    nbrech = schema.Int(title=u"How many echeances",
                        min_length=0,
                        max_length=4)

    dateech1 = schema.Date(title=u"Date of the first echeance")

    montantech1 = schema.ASCIILine(title=u"Amount echeance 1")

    dateech2 = schema.Date(title=u"Date of the second echeance")

    montantech2 = schema.ASCIILine(title=u"Amount echeance 2")

    dateech3 = schema.Date(title=u"Date of the third echeance")

    montantech3 = schema.ASCIILine(title=u"Amount echeance 3")

    dateech4 = schema.Date(title=u"Date of the fourth echeance")

    montantech4 = schema.ASCIILine(title=u"Amount echeance 4")


class AllerForm(BrowserView):
    interface.implements(IAllerDataSchema)
    aller_form_template = ViewPageTemplateFile('aller_form.pt')

    def __init__(self, context, request):
        self.version = "3"
        self.context = context
        self.request = request
        self.portal_state = None
        self.settings = None
        self._MAC = sceau.MAC()
        self.url_retour = None
        self.url_retour_ok = None
        self.url_retour_err = None
        self.lgue = None
        self.contact_source = None
        self.contact = None

    def __call__(self):
        self.update()
        return self.index()

    def update(self):
        if self.settings is None:
            registry = component.queryUtility(IRegistry)
            if registry:
                self.settings = registry.forInterface(settings.Settings)
        if self.portal_state is None:
            self.portal_state = component.getMultiAdapter((self.context,
                                                          self.request),
                                                     name="plone_portal_state")
        self._MAC.udpate()
        context_url = self.context.absolute_url()
        if self.url_retour is None:
            self.url_retour = context_url + '/@@cmcic_retour'
        if self.url_retour_ok is None:
            self.url_retour_ok = context_url + '/@@cmcic_retour_ok'
        if self.url_retour_err is None:
            self.url_retour_err = context_url + '/@@cmcic_retour_err'

        if self.lgue is None:
            self.lgue = self.context.Language()

        if self.contact_source is None:
            self.contact_source = self.settings.contact_source

        if self.contact is None:
            if self.contact_source == "member":
                self.contact = self.portal_state.member()
            elif self.contact_source == "creator":
                creator = self.Creators()[0]
                self.contact = self.membership_tool.getMemberById(creator)

    def action_url(self):
        return self.settings.url_paiement

    def date(self):
        return self.context.Modified.strftime('%d/%m/%Y:%H:%M:%S')

    def montant(self):
        raise NotImplementedError("must be implemented in subclass")

    def reference(self):
        raise NotImplementedError("must be implemented in subclass")

    def text_libre(self):
        return u""

    def mail(self):
        #Note: we may use the creator of hte context ...
        if self.contact is not None:
            return self.contact.getProperty('email')
        raise ValueError("can t get email contact")

    def options(self):
        return ""

    def aller_form(self):
        return self.aller_form_template()

    def TPE(self):
        return self.settings.TPE
