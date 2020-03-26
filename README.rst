.. image:: https://travis-ci.org/bast/somepackage.svg?branch=master
   :target: https://travis-ci.org/bast/somepackage/builds
.. image:: https://img.shields.io/badge/license-%20MPL--v2.0-blue.svg
   :target: ../master/LICENSE


Somepackage
===========

Show how to structure a Python project.


Code style
----------

- Follow PEP8: https://www.python.org/dev/peps/pep-0008/
- Use ``pycodestyle`` to automatically check for PEP8.


Type checking
-------------

- Consider using type hints: https://docs.python.org/3/library/typing.html
- Consider using http://mypy-lang.org.
- Consider verifying type annotations at runtime: https://github.com/RussBaz/enforce


Share your package
------------------

- Choose a license and add a LICENSE file.
- Share your package on PyPI. For this you can follow https://github.com/bast/pypi-howto.


Documentation
-------------

I used to recommend reStructuredText for READMEs in contrast to Markdown but
PyPI no longer requires reStructuredText. You can use Markdown as noted on
https://pypi.org/help/ under "How can I upload a project description in a
different format?".

Example shown here: https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py


Suggestions? Corrections? Pull requests?
----------------------------------------

Yes please!
