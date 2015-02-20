# OCT-Reader
This repository aims to read/write RAW exported OCTs from Heidelberg Engineering machines. Please, understand that to export the RAW format of an Spectralis OCT a legal copy of Spectralis software and the plugin to export in RAW mode must be purchased from Heidelberg Engineering.

For now the code is being implemented for version 103 of the RAW exported file.

Supported features:
+ Read .vol file header.
+ Read SLO Image.

Future features:
+ Read & Write B-Scans.
+ Write .vol file header.
+ Write SLO Image

Dependencies:
+ Numpy
