# pope shuffle
Solves: 262, Points: 121

Author: halp
## Problem Description
it's like caesar cipher but better. Encoded: ࠴࠱࠼ࠫ࠼࠮ࡣࡋࡍࠨ࡛ࡍ࡚ࡇ࡛ࠩࡔࡉࡌࡥ
## Reading Material
[Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

## Solution
Upon reading the challenge, at first I thought there wasn't enough information to solve. All I had to push off of was "caesar cipher but better", which if you think about it is not a lot of information. AFter thinking through for over 30 minutes, I was stumped. But then, I realized that a key characteristic of the Caesar Cipher was that there is modulo.
>[!IMPORTANT]
>A key characteristic of the Caesar Cipher is that it loops back around if going over or under the limit.

Knowing this, we can craft a brute force approach to solve the question. My script runs through the code and moves down the shift line, checking if the flag format (LITCTF) is in the decrypted result, and if it is not, it keeps going until it finds one that works.

```python
enc = "࠴࠱࠼ࠫ࠼࠮ࡣࡋࡍࠨ࡛ࡍ࡚ࡇ࡛ࠩࡔࡉࡌࡥ"
shift = 0
dec = ""

while "LITCTF" not in dec:
    dec = ''.join(chr(ord(char) - shift) for char in enc)
    shift += 1
print(dec)
```

Eventually, we get the flag, which is achieved through a shift of 2024.

Flag: `LITCTF{ce@ser_sAlad}`
