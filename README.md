# CS_Lab_6

## Overview
This repository contains Python implementations of cryptographic signing algorithms, specifically focusing on ElGamal and RSA signature schemes. These scripts demonstrate the fundamental concepts of digital signatures in cryptography.

## Contents
- `elgamal_sign.py`: Implements the ElGamal signature scheme.
- `rsa_sign.py`: Implements the RSA signature scheme.

## ElGamal Signature Scheme (`elgamal_sign.py`)
This script demonstrates the ElGamal signature process, including key generation, signing, and verification. It uses a predefined message and a hash function to create a digital signature.

### Key Features
- Generation of public and private keys.
- Creation of a signature for a given message.
- Verification of the signature.

## RSA Signature Scheme (`rsa_sign.py`)
This script illustrates the RSA signing and verification process. It includes the generation of RSA keys and the signing of a message using these keys.

### Key Features
- RSA key generation.
- Digital signature creation using RSA.
- Signature verification.

## Getting Started
To run these scripts, you need Python installed on your system. Clone the repository and execute the scripts individually:

```bash
git clone https://github.com/Ricigeroi/CS_Lab_6.git
cd CS_Lab_6
python elgamal_sign.py
python rsa_sign.py
