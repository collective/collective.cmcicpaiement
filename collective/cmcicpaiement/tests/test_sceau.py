import unittest2 as unittest
from collective.cmcicpaiement.tests import base, utils


class TestMAC(base.UnitTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def setUp(self):
        super(TestMAC, self).setUp()
        from collective.cmcicpaiement import sceau

        self.mac = sceau.MAC()
        self.settings = utils.EnvSettings()
        self.mac.set_key(self.settings.security_key)

    def test_update(self):
        self.assertTrue(self.mac._wrapped is not None)
        self.mac.update()
        self.assertEqual(self.mac._key, self.settings.security_key)

    def test_set_key(self):
        self.mac.set_key('key1')
        self.assertEqual(self.mac._key, 'key1')

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
