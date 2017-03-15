pytest-aiofiles
===============

pytest-aiofiles provides pytest fixtures for writing aiofiles tests
using pyfakefs, instead of real file IO.

Features
--------

- fake filesystem fixture attached to aiofiles
- automatic aiofiles monkey-patching

Library Installation
--------------------

.. code-block:: shell

    $ pip install pytest-aiofiles

Getting Started
---------------

.. code-block:: python

    import aiofiles
    import pytest

    @pytest.mark.asyncio
    async def test_stuff(afs):
        filename = 'test'

        async with aiofiles.open(test, 'w') as f:
            await f.seek(0)

        assert afs.Exists(filename)

Fixtures
--------

``afs``
~~~~~~~

An "asyncio filesystem" object, which is an instance of
:class:`pyfakefs.fake_filesystem.FakeFilesystem`. See pyfakefs_ for
more details.

.. _pyfakefs: http://jmcgeheeiv.github.io/pyfakefs/pyfakefs.html#pyfakefs.fake_filesystem.FakeFilesystem

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
