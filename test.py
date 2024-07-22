import py_gs128

from datetime import datetime

# Create Barcode
my_code = py_gs128.Creater()
my_code.code_01('04645643854934')
my_code.code_11(datetime.now())
my_code.code_21(digs=6)

code_value = my_code.get_value()

print(code_value)  # -> 01046456438549341124072221AAAAAA
print(my_code.get_text())   # -> (01)04645643854934(11)240722(21)AAAAAA

# Decode barcode
decoded_barcode = py_gs128.decode_gs128(code_value)

for ai, description, data in decoded_barcode:
    print(f"AI: {ai}, Description: {description}, Data: {data}")