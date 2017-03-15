import aiofiles
from aiofiles import base, threadpool
from asynctest import mock
from pyfakefs import fake_filesystem
import pytest


@pytest.mark.asyncio
async def test_plugin_dispatcher(fs):
    with open('test', 'w') as f:
        wrapped = threadpool.wrap(f)

    assert isinstance(f, fake_filesystem.FakeFileWrapper)
    assert isinstance(wrapped, base.AsyncBase)


@pytest.mark.asyncio
@mock.patch.object(fake_filesystem.FakeFileWrapper, 'seek')
async def test_plugin_fixture(mock_write, afs):
    filename = 'test'
    value = 0

    async with aiofiles.open(filename, 'w') as f:
        await f.seek(value)

    assert afs.Exists(filename)

    mock_write.assert_called_with(value)
