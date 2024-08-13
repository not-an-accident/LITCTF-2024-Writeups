enc = "࠴࠱࠼ࠫ࠼࠮ࡣࡋࡍࠨ࡛ࡍ࡚ࡇ࡛ࠩࡔࡉࡌࡥ"
shift = 0
dec = ""

while "LITCTF" not in dec:
    dec = ''.join(chr(ord(char) - shift) for char in enc)
    shift += 1
print(dec)
