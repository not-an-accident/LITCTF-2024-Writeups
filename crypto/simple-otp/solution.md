# simple-otp
Points: 110, Solves: 550

Author: Stephanie

## Problem Description

We all know OTP is unbreakable...

```python
import random

encoded_with_xor = b'\x81Nx\x9b\xea)\xe4\x11\xc5 e\xbb\xcdR\xb7\x8f:\xf8\x8bJ\x15\x0e.n\\-/4\x91\xdcN\x8a'

random.seed(0)
key = random.randbytes(32)
```

## Solution

Let's analyze. We are given the encoded text, and some random seed code. `random.seed(0)` sets the seed number, and therefore, we can replicate the exact same scenario, allowing us to solve the question. 

> [!NOTE]
> The seed is set, which allows us to essentially repeat the scenario.

From here, it's just simple One Time Pad (OTP) Decryption.

```python
import random

encoded_with_xor = b'\x81Nx\x9b\xea)\xe4\x11\xc5 e\xbb\xcdR\xb7\x8f:\xf8\x8bJ\x15\x0e.n\\-/4\x91\xdcN\x8a'

random.seed(0)
key = random.randbytes(32)

decrypted_message = bytes([b ^ k for b, k in zip(encoded_with_xor, key)])

print(decrypted_message)
```

Flag: `LITCTF{sillyOTPlol!!!!sdfsgvkhf}`
