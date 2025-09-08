Introduction
============

Welcome to the API reference documentation for **WPC_Stand-alone_Python**. We provide excellent example codes to help you quickly get started with our products.

Our platform is beginner-friendly and open-source, specifically designed for microcontrollers and embedded systems.
It represents a compact implementation of Python 3, finely tuned to operate efficiently on resource-constrained hardware.
This makes it a favored choice among developers engaged in projects involving embedded devices.

Amazingly, we could employ `TinyML <https://wpc-systems-ltd.github.io/WPC_Stand-alone_Python_release/examples/PYCO_WIFI/TinyML/acceleration_movement.html>`_ to meet up with machine learning requirements.
One such application is the real-time movement classification from time-series data.

Moreover, we also provide support for ``ulab``, a numerical computing library. For example, We are using the ``FFT`` function from it.
ulab offers a comprehensive suite of functions for working with numerical data, implementing a compact subset of ``numpy`` and scipy.
For detailed API support, please refer to the `ulab <https://micropython-ulab.readthedocs.io/en/latest/index.html>`_ documentation.


Quick start
===========
**Easy, fast, and just works!**

.. code-block:: console

    >>> import pywpc
    >>> pywpc.Sys_getDriverName()
    'WPC_Stand-alone_Python'
    >>> pywpc.AI_readOnDemand()
    [1.638031, 1.642151, 1.645813, 1.642303, 1.6362, 1.638489, 1.643829, 1.642761]

Startup Sequence
================
When the PYCO board is powered on, it will first execute ``boot.py``, followed by ``main.py``.

- ``boot.py`` is typically used for system or environment initialization.
- ``main.py`` contains your main application logic and will run automatically after ``boot.py``.

How to Prevent or Stop main.py Execution
========================================
If your ``main.py`` script enters an infinite loop, or you want to prevent it from running on boot, you have two options:

**Software Method:**
- Use the command ``Sys_disableMain`` to disable the automatic execution of ``main.py`` on startup.

**Hardware Method:**
- On the PYCO board, short the ``Save`` pin before powering on. This will prevent ``main.py`` from being executed at boot.

These methods help you get control back if your program gets stuck or if you want to upload new code to the board.


Products
========

+----------------+-----------------+-----------------+---------+---------+
| Product/module |PYCO-WIFI-MINI-AI|PYCO-WIFI-MINI-AO|PYCO-WIFI|PYCO-ETH |
+----------------+-----------------+-----------------+---------+---------+
| AHRS           |V                |V                |         |         |
+----------------+-----------------+-----------------+---------+---------+
| AI             |V                |                 |V        |V        |
+----------------+-----------------+-----------------+---------+---------+
| AO             |                 |V                |V        |V        |
+----------------+-----------------+-----------------+---------+---------+
| DIO            |                 |                 |V        |V        |
+----------------+-----------------+-----------------+---------+---------+
| FUNC Button    |                 |                 |V        |         |
+----------------+-----------------+-----------------+---------+---------+
| LED control    |V                |V                |V        |         |
+----------------+-----------------+-----------------+---------+---------+
| Modbus master  |V                |V                |V        |         |
+----------------+-----------------+-----------------+---------+---------+
| Modbus slave   |V                |V                |V        |         |
+----------------+-----------------+-----------------+---------+---------+
| OLED           |V                |V                |V        |V        |
+----------------+-----------------+-----------------+---------+---------+
| SD card        |V                |V                |V        |         |
+----------------+-----------------+-----------------+---------+---------+
| TCP Client     |V                |V                |V        |         |
+----------------+-----------------+-----------------+---------+---------+
| TinyML         |V                |V                |V        |         |
+----------------+-----------------+-----------------+---------+---------+

``V`` stands for support


License
=======

**WPC Stand-alone Python** is licensed under an MIT-style license see `LICENSE <https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/blob/main/LICENSE>`_ Other incorporated projects may be licensed under different licenses.
All licenses allow for non-commercial and commercial use.