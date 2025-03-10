## Block Cipher Encryption

### Requirements

To run the program, the **pycryptodome, opencv-python, numpy and matplotlib** libraries must be installed.

```
pip install pycryptodome opencv-python numpy matplotlib

```

### Running Code

```
python blockCiphers.py
```

The code can be run by writing the above script to the terminal.

### Working Logic and Used Inputs

In the application, a grayscale 1880 x 1024 .jpeg file was used and is named "gray.jpeg". This image was read using opencv.

As a result of the application, we have 3 main images and 2 side images that make it easier to compare these images:

- *original.png:* The original grayscale image. This image has been modified from the original to include 4 different shades of gray.

- *encryptedECB.png:* The image encrypted in ECB mode.

- *encryptedCBC.png:* The image encrypted in CBC mode.

- *originalAndECB.png:* Side-by-side comparison of the original and ECB-encrypted images.

- *originalAndCBC.png:* Side-by-side comparison of the original and CBC-encrypted images.

While some patterns of the original image can be understood in the ECB mode of the application, a completely incomprehensible image is created in the CBC mode.

