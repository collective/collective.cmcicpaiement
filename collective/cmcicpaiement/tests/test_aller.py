import unittest2 as unittest
from collective.cmcicpaiement.tests import base, utils


class UnitTestAllerForm(base.UnitTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def setUp(self):
        super(UnitTestAllerForm, self).setUp()
        from collective.cmcicpaiement import aller
        self.request.debug = False

        self.form = aller.AllerForm(self.context, self.request)
        self.form.settings = utils.EnvSettings()
        self.form.portal_state = utils.FakePortalState()
        self.form.portal_membership = utils.FakePortalMembership()
        self.form.update()

    def test_version(self):
        self.assertEqual(self.form.version, "3.0")

    def test_action_url(self):
        url = self.form.action_url()
        self.assertEqual(url,
                         "https://paiement.creditmutuel.fr/test/paiement.cgi")

    def test_urls(self):
        self.assertEqual(self.form.url_retour,
                         'http://nohost.com/myid/@@cmcic_retour')
        self.assertEqual(self.form.url_retour_err,
                         'http://nohost.com/myid/@@cmcic_retour_err')
        self.assertEqual(self.form.url_retour_ok,
                         'http://nohost.com/myid/@@cmcic_retour_ok')

    def test_MAC(self):
        mac = self.form.MAC()
        self.assertTrue(mac is not None)

    def test_date(self):
        dt = None
        d = self.form.date()
        from datetime import datetime
        try:
            dt = datetime.strptime(d, '%d/%m/%Y:%H:%M:%S')
        except ValueError:
            pass
        self.assertTrue(dt is not None)

    def test_montant(self):
        self.assertRaises(NotImplementedError, self.form.montant)

    def test_reference(self):
        self.assertRaises(NotImplementedError, self.form.reference)

    def test_text_libre(self):
        #TODO: whats up their ?
        pass

    def test_mail(self):
        self.assertEqual(self.form.mail(), "fakemember@gmail.com")

    def test_option(self):
        #TODO: whats up their ?
        pass

    def test_aller_form(self):
        #CAN T BE TEST IN UNITTEST
        pass

    def test_TPE(self):
        self.assertEqual(self.form.TPE(),
                         self.form.settings.TPE)


class IntegrationTestAllerForm(base.UnitTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def setUp(self):
        super(IntegrationTestAllerForm, self).setUp()

    def test_version(self):
        pass

    def test_action_url(self):
        pass

    def test_urls(self):
        pass

    def test_MAC(self):
        pass

    def test_date(self):
        pass

    def test_montant(self):
        pass

    def test_reference(self):
        pass

    def test_text_libre(self):
        #TODO: whats up their ?
        pass

    def test_mail(self):
        pass

    def test_option(self):
        #TODO: whats up their ?
        pass

    def test_aller_form(self):
        #CAN T BE TEST IN UNITTEST
        pass

    def test_TPE(self):
        pass


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
