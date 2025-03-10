from Crypto.Cipher import AES
import cv2
import numpy as np
from Crypto.Util.Padding import pad
import os
import matplotlib.pyplot as plt

imagePath = "gray.jpeg"

image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
image = (image // 64) * 64

def concatenateImages(image1, image2, title1, title2, outputName):
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(image1, cmap='gray')
    plt.title(title1)
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(image2, cmap='gray')
    plt.title(title2)
    plt.axis('off')
    
    plt.savefig(outputName, bbox_inches='tight')
    plt.close()


def encryptImageECB(image, key):
    cipher = AES.new(key, AES.MODE_ECB)
    imageToByte = image.tobytes()
    paddedImage = pad(imageToByte, AES.block_size)
    encryptedBytes = cipher.encrypt(paddedImage)
    encryptedImg = np.frombuffer(encryptedBytes, dtype=np.uint8)
    return encryptedImg[:image.size].reshape(image.shape)

def encryptImageCBC(image, key):
    cipher = AES.new(key, AES.MODE_CBC)
    imageToByte = image.tobytes()
    paddedImage = pad(imageToByte, AES.block_size)
    encryptedBytes = cipher.encrypt(paddedImage)
    encryptedImg = np.frombuffer(encryptedBytes, dtype=np.uint8)
    return encryptedImg[:image.size].reshape(image.shape)

def main():
    key = os.urandom(16)
    cv2.imwrite("original.png", image)

    encryptedECB = encryptImageECB(image, key)
    cv2.imwrite("encryptedECB.png", encryptedECB)

    encryptedCBC = encryptImageCBC(image, key)
    cv2.imwrite("encryptedCBC.png", encryptedCBC)

    concatenateImages(image, encryptedECB,"Original", "ECB Encrypted" , "originalAndECB.png")
    concatenateImages(image, encryptedCBC, "Original", "CBC Encrypted", "originalAndCBC.png")

if __name__ == "__main__":
    main()