
# py_gs128

`py_gs128` is a Python library for creating and decoding GS1-128 barcodes. GS1-128 barcodes are used in various industries for encoding complex information using Application Identifiers (AIs).

## Installation

To install `py_gs128`, use pip:

```bash
pip install git+https://github.com/jqxl/py_gs128.git
```

## Usage

### Create Barcode

You can create a GS1-128 barcode using the `Creater` class. Here’s an example of how to generate a barcode:

```python
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
```

### Decode Barcode

You can decode a GS1-128 barcode using the `decode_gs128` function. Here’s an example of how to decode a barcode:

```python
import py_gs128

# Example barcode value
code_value = "01046456438549341124072221AAAAAA"

# Decode barcode
decoded_barcode = py_gs128.decode_gs128(code_value)

for ai, description, data in decoded_barcode:
    print(f"AI: {ai}, Description: {description}, Data: {data}")
```

## Example

```python
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
```

### Output

```plaintext
01046456438549341124072221AAAAAA
(01)04645643854934(11)240722(21)AAAAAA
AI: 01, Description: GTIN, Data: 04645643854934
AI: 11, Description: PROD DATE, Data: 240722
AI: 21, Description: SERIAL, Data: AAAAAA
```

## Application Identifiers (AIs)

Here are some of the AIs used in the examples:

- `01`: GTIN (Global Trade Item Number)
- `11`: Production Date (YYMMDD)
- `21`: Serial Number

## License

This project is licensed under the MIT License.
```

This `README.md` file provides installation instructions, usage examples for creating and decoding GS1-128 barcodes, and details about some common Application Identifiers (AIs). Adjust the details as needed to fit your specific library's functionality and additional features.
