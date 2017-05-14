from unittest.mock import patch

from aiofiles import threadpool
from aiofiles.threadpool.binary import AsyncBufferedIOBase
from pyfakefs.fake_filesystem import FakeFileWrapper
from pyfakefs.fake_filesystem_unittest import Patcher
import pytest

from pytest_aiofiles.urandom import FakeFileOpen, FakeOsModule


def find_sync_open_attr():
    # fixme: depend on 0.3.2
    try:
        getattr(threadpool, 'sync_open')
        return 'sync_open'  # pragma: no cover
    except AttributeError as e:  # pragma: no cover
        try:
            getattr(threadpool, '_sync_open')
            return '_sync_open'
        except AttributeError:
            raise e


@pytest.fixture
def afs(request, monkeypatch):
    """ Fake filesystem. """
    patcher = Patcher()

    with patch.multiple('pyfakefs.fake_filesystem',
                        FakeOsModule=FakeOsModule,
                        FakeFileOpen=FakeFileOpen):
        patcher.setUp()

    attr = find_sync_open_attr()

    monkeypatch.setattr(threadpool, attr, patcher.fake_open)

    request.addfinalizer(patcher.tearDown)

    patcher.fs.fake_open = patcher.fake_open

    return patcher.fs


@threadpool.wrap.register(FakeFileWrapper)
def _(file, *, loop=None, executor=None):
    return AsyncBufferedIOBase(file, loop=loop, executor=executor)
