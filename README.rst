Blocks contributions
====================

The `blocks-contrib` contains a variety of models and dataset interfaces
implemented with [Blocks](https://github.com/bartvm/blocks).

This repository is meant to be a starting point if you want to:

* Learn to use Blocks by looking at implementations of simple models.
* Find reference implementations of research performed using Blocks.
* Use interfaces to datasets such as
  [MNIST](https://github.com/bartvm/blocks-contrib/blob/master/blocks/contrib/datasets/mnist.py)
  and the [One Billion Words dataset](https://github.com/bartvm/blocks-contrib/blob/master/blocks/contrib/datasets/billion.py).

## Installation

To start looking at the examples in this repository, clone it to a
directory of your choice

.. code-block:: bash

   $ git clone git@github.com:bartvm/blocks-contrib.git

If you want to install the datasets, install this package in development
mode by running the following command in the `blocks-contrib` folder:

.. code-block:: bash

   $ python setup.py develop

If you want to update to the latest version, simply pull the latest
changes from GitHub

.. code-block:: bash

   $ git pull
