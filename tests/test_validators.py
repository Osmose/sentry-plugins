from __future__ import absolute_import

import pytest

from sentry.exceptions import PluginError
from sentry.testutils import TestCase

from sentry_plugins.validators import OptionalURLValidator


class OptionalURLValidatorTest(TestCase):
    def test_empty(self):
        assert OptionalURLValidator('') == ''

    def test_invalid_url(self):
        with pytest.raises(PluginError):
            OptionalURLValidator('foj3n3on2')
