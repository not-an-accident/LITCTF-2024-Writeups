import random
encoded_with_xor = b'\x81Nx\x9b\xea)\xe4\x11\xc5 e\xbb\xcdR\xb7\x8f:\xf8\x8bJ\x15\x0e.n\\-/4\x91\xdcN\x8a'
#sets the same seed
random.seed(0)
key = random.randbytes(32)

decrypted_message = bytes([b ^ k for b, k in zip(encoded_with_xor, key)])

print(decrypted_message)
