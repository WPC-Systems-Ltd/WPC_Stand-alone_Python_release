Introduction
============

Welcome to the API reference documentation for **WPC_Stand-alone_Python**. We provide excellent example codes to help you quickly get started with our products.

Our platform is beginner-friendly and open-source, specifically designed for microcontrollers and embedded systems.
It represents a compact implementation of Python 3, finely tuned to operate efficiently on resource-constrained hardware.
This makes it a favored choice among developers engaged in projects involving embedded devices.

Moreover, we also provide support for ``ulab``, a numerical computing library. For example, We are using the ``FFT`` function from it.
ulab offers a comprehensive suite of functions for working with numerical data, implementing a compact subset of ``numpy`` and scipy.
For detailed API support, please refer to the `ulab <https://micropython-ulab.readthedocs.io/en/latest/index.html>`_ documentation.


Quick start
===========
**Easy, fast, and just works!**

>>> import pywpc
>>> pywpc.Sys_getDriverName()
'WPC_Stand-alone_Python'
>>> pywpc.AI_readOnDemand()
[1.638031, 1.642151, 1.645813, 1.642303, 1.6362, 1.638489, 1.643829, 1.642761]

Products
========

+----------------+---------+---------+
| Product/module |PYCO-WIFI|PYCO-ETH |
+----------------+---------+---------+
| AI             |V        |V        |
+----------------+---------+---------+
| AO             |         |V        |
+----------------+---------+---------+
| DIO            |         |V        |
+----------------+---------+---------+
| TCP            |V        |         |
+----------------+---------+---------+
| Wifi           |V        |         |
+----------------+---------+---------+
| OLED           |V        |         |
+----------------+---------+---------+
| LED            |V        |         |
+----------------+---------+---------+

``V`` stands for support

License
=======

**WPC Stand-alone Python release** is licensed under an MIT-style license see `LICENSE <https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/blob/main/LICENSE>`_ Other incorporated projects may be licensed under different licenses.
All licenses allow for non-commercial and commercial use.
