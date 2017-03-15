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

Contents
--------

.. toctree::
   :maxdepth: 2

   fixtures

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
