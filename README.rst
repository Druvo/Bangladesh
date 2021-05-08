==================================================
bangladesh -- information
==================================================

Bangladesh information like ``District``, ``Division``, ``Thana``, ``post code`` etc.
This package allows you to direct use those data into the python code.



:Author: zhdruvo (Zahid Hasan)
:License: MIT License
:Home Page: https://github.com/Druvo/Bangladesh


Installing
----------

The easiest way to install the library is to execute (possibly in a
`virtualenv`_) the command::

    pip install bangladesh

.. _virtualenv: https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments


Features
----------

.. code:: python

    from bangladesh import *


    print(get_divisions())
    print(get_districts())
    print(get_upazilas())
    print(get_postcodes())
