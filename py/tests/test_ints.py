from __future__ import absolute_import
from erlpack import pack
from pytest import raises
from six.moves import range

import struct


def test_smallint():
    for i in range(256):
        assert pack(i) == b'\x83a' + struct.pack('B', i)


def test_int():
    assert pack(1024) == b'\x83b\x00\x00\x04\x00'
    assert pack(-2147483648) == b'\x83b\x80\x00\x00\x00'
    assert pack(2147483647) == b'\x83b\x7f\xff\xff\xff'


def test_unsigned_long_long():
    assert pack(2147483648) == b'\x83n\x04\x00\x00\x00\x00\x80'
    assert pack(1230941823049123411) == b'\x83n\x08\x00S\xc6\x03\xf6\x10/\x15\x11'


def test_long_long():
    assert pack(-2147483649) == b'\x83n\x04\x01\x01\x00\x00\x80'
    assert pack(-123094182304912341) == b'\x83n\x08\x01\xd5\x933\xb2\x81Q\xb5\x01'


def test_really_big_ints():
    with raises(OverflowError):
        pack(123094182304912341123414)
