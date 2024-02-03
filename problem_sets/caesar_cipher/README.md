# Caesar Cipher

Create a program that can _encrypt_ or _decrypt_ a message using the [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

If _encrypting_ a message, the program should:

- take as input:
  - the plaintext message to be encrypted
  - the shift or offset to be used
- return the encrypted or "ciphertext" message.

If _decrypting_ a message, the program should:

- take as input:
  - the ciphertext message to be decrypted
  - the shift or offset to be used
- return the decrypted or "plaintext" message.

## What's a Caesar Cipher?

A _cipher_ is a method of disguising a message by encoding it. The _Caesar Cipher_
is a type of substitution cipher where each letter in a message is 'shifted' a
certain number of places down or up the alphabet.

For example:

- with a shift of 1, A would be replaced by B, B would become C, and so on.
- with a shift of 3, D would be replaced by G, E would become H, and so on.

If the shift or offset extends past the end of the alphabet, the letter wraps
around to the beginning.

For example:

- if you shift Z by 1, you would get A.
- if you shift Y by 4, you would get C.

For our purposes, we will only be shifting letters. All other characters (numbers,
punctuation, spaces, etc.) should remain unchanged.

Thus the message "BUZZ OFF" encrypted with a shift of 2 would become "DWBB QHH".
