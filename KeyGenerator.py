"""
Author: Oren Sitton
File: GenerateKeys.py
Python Version: 3
Description: 
"""

import errno
import os
from tkinter import *
import pyperclip
from tkinter.scrolledtext import *

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


def main():
    key = RSA.generate(1024)
    with open('privkey.der', 'wb') as f:
        f.write(key.exportKey('DER'))
    with open('pubkey.der', 'wb') as f:
        f.write(key.publickey().exportKey('DER'))

    with open('pubkey.der', 'rb') as f:
        key = RSA.importKey(f.read())
        pub_key = (key.publickey().exportKey('DER').hex())
        pass
    with open('privkey.der', 'rb') as f:
        key = RSA.import_key(f.read())
        priv_key = (key.exportKey('DER').hex())

    os.remove('privkey.der')
    os.remove('pubkey.der')

    root = Tk()
    root.title("Key Generator")

    Label(root, text="SittCoin RSA Key Pair", font=("Helvetica", 30, "bold")).pack(side=TOP)

    Button(root, text="Copy public key\nto clipboard", font=("Times New Roman", 15), command=lambda: pyperclip.copy(pub_key)).pack(side=LEFT, padx=20, pady=20)

    Button(root, text="Copy private key\nto clipboard", font=("Times New Roman", 15), command=lambda: pyperclip.copy(priv_key)).pack(side=RIGHT, padx=20, pady=20)

    root.mainloop()


if __name__ == '__main__':
    main()
