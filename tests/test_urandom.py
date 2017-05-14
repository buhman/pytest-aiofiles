import os
from io import BufferedReader

from pyfakefs.fake_filesystem import FakeFileWrapper

from pytest_aiofiles.urandom import FakeFileOpen, FakeOsModule


def test_fake_os(fs):
    cls = FakeOsModule(fs)

    fd = cls.open('/dev/urandom', os.O_RDONLY, 0o777)
    assert isinstance(fd, int)

    fd = cls.open('blah', os.O_CREAT, 0o777)
    assert isinstance(fd, int)


def test_fake_open(fs):
    cls = FakeFileOpen(fs)

    f = cls('/dev/urandom', 'rb')
    assert isinstance(f, BufferedReader)

    f = cls('blah', 'wb')
    assert isinstance(f, FakeFileWrapper)
