__author__ = "Sharkbyte Studios"
__copyright__ = "Copyright 2009, Sharkbyte Studios Ltd"
__email__ = "support@sharkbyte.co.uk"

import unittest
import doctest
import sys
from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc
from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite

import collective.twitterportlet

class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            zcml.load_config('configure.zcml',
                             collective.twitterportlet)
            fiveconfigure.debug_mode = False
            ztc.installPackage('collective.twitterportlet')

        @classmethod
        def tearDown(cls):
            pass

    def _setup(self):
        ztc.utils.setupCoreSessions(self.app)

ptc.setupPloneSite(products=['collective.twitterportlet'])

def test_suite():
    return unittest.TestSuite([
        ztc.ZopeDocFileSuite(
            'README.txt', package='collective.twitterportlet',
            test_class=TestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS)
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')