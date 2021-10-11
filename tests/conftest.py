#!/usr/bin/python3
#
# pytest fixture definitions.

import pytest
from tests import util

@pytest.fixture
def bfuse(tmpdir):
    '''A test requesting a "bfuse" is given one via this fixture.'''

    dev = util.format_1g(tmpdir)
    mnt = util.mountpoint(tmpdir)
    bf = util.BFuse(dev, mnt)

    yield bf

    bf.unmount(timeout=5.0)
