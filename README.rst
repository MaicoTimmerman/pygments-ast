Pygments AST
==============

This implements a basic Pygments Lexer for the AST language defined by the
CoCoNut framework.


Install
+++++++

Using PyPI and pip
------------------

::

    $ (sudo) pip install pygments-ast


Manual
------

::

    $ git clone git://github.com/maicotimmerman/pygments-ast.git
    $ cd pygments-ast
    $ (sudo) python setup.py install


Using
+++++

Just use the **ast** "language".


Using in LaTeX documents
++++++++++++++++++++++++

See the minted package at http://minted.googlecode.com.


Extra information
+++++++++++++++++

Pygments supported languages
----------------------------

Pygments at the moment supports over 150 different programming languages,
template languages and other markup languages. To see an exhaustive list of the
currently supported languages, use the command::

    $ pygmentize -L lexers

Pygments styles avaible
-----------------------

To get a list of all available stylesheets, execute the following command on the
command line::

    $ pygmentize -L styles

Please read the `official documentation`_ for further information on the usage
of pygment styles.

.. _official documentation: http://pygments.org/docs/
