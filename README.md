
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

### Output

```plaintext
01046456438549341124072221AAAAAA
(01)04645643854934(11)240722(21)AAAAAA
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

### Output

```plaintext
AI: 01, Description: GTIN, Data: 04645643854934
AI: 11, Description: PROD DATE, Data: 240722
AI: 21, Description: SERIAL, Data: AAAAAA
```

## Application Identifiers (AIs)

Here are some of the AIs used in the examples:

- `01`: GTIN (Global Trade Item Number)
- `11`: Production Date (YYMMDD)
- `21`: Serial Number

<details>
<summary>AI Dictionary</summary>

- `00`: SSCC (Serial Shipping Container Code)
- `01`: GTIN (Identification Number of the Trade Item)
- `02`: CONTENT (GTIN of Trade Items Contained in the Shipment)
- `10`: BATCH/LOT (Batch/Lot Number)
- `11`: PROD DATE (Production Date)
- `12`: DUE DATE (Payment Due Date)
- `13`: PACK DATE (Packaging Date)
- `15`: BEST BEFORE (Minimum Shelf Life)
- `17`: USE BY (Maximum Shelf Life)
- `20`: VARIANT (Product Variant)
- `21`: SERIAL (Serial Number)
- `22`: QTY/DATE/BATCH (Auxiliary Data for Special Pharmaceutical Products)
- `240`: ADDITIONAL ID (Additional Product Identification)
- `241`: CUST.PART NO (Customer Part Number)
- `250`: SECONDARY SERIAL (Additional Serial Number)
- `251`: REF TO SOURCE (Reference to Source)
- `30`: VAR.COUNT (Variable Count)
- `330`: GROSS WEIGHT (kg) (Gross Weight in kg)
- `337`: KG PER m2 (Kilograms per square meter)
- `37`: COUNT (Number of Trade Units in Shipment)
- `390`: AMOUNT (Amount payable - single currency)
- `391`: AMOUNT (Amount payable - with ISO currency code)
- `392`: PRICE (Amount payable for variable measure trade item - single currency)
- `393`: PRICE (Amount payable for variable measure trade item)
- `400`: ORDER NUMBER (Order Number)
- `401`: CONSIGNMENT (Consignment Number)
- `402`: SHIPMENT NO. (Shipment Identification Number)
- `403`: ROUTE (Route Code)
- `410`: SHIP TO LOC (EAN/UCC Global Location Number (GLN) of the Ship-to party)
- `411`: BILL TO (EAN/UCC Global Location Number (GLN) of the Bill-to party)
- `412`: PURCHASE FROM (EAN/UCC Global Location Number (GLN) of the supplier)
- `413`: SHIP FOR LOC (EAN/UCC Global Location Number (GLN) of the Ship-for party)
- `414`: LOC No (EAN/UCC Global Location Number (GLN))
- `415`: PAY TO (EAN/UCC Global Location Number (GLN) of the party to be paid)
- `420`: SHIP TO POST (Postal code of the Ship-to location)
- `421`: SHIP TO POST (Postal code of the Ship-to location with ISO country code)
- `422`: ORIGIN (Country of origin of the trade item)
- `423`: COUNTRY - INITIAL PROCESS (Country of initial processing)
- `424`: COUNTRY - PROCESS. (Country of processing)
- `425`: COUNTRY - DISASSEMBLY (Country of disassembly)
- `426`: COUNTRY – FULL PROCESS (Country of full processing)
- `7001`: NSN (NATO Stock Number)
- `7002`: MEAT CUT (UNECE carcass or cuts classification)
- `8001`: DIMENSIONS (Roll products - Width, Length, Diameter, Direction, Splices)
- `8002`: CMT NO (Cellular mobile telephone serial number)
- `8003`: GRAI (Global Returnable Asset Identifier)
- `8004`: GIAI (Global Individual Asset Identifier)
- `8005`: PRICE PER UNIT (Price per unit of measure)
- `8006`: GCTIN (Identification of component of a trade item)
- `8007`: IBAN (International Bank Account Number)
- `8008`: PROD TIME (Date and time of production)
- `8018`: GSRN (Global Service Relation Number)
- `8020`: REF NO (Reference number)
- `8100`: COUPON EXTENDED CODE (Extended coupon code)
- `8101`: COUPON EXTENDED CODE (Extended coupon code)
- `8102`: COUPON EXTENDED CODE (Extended coupon code)
- `903`: INTERNAL (Information mutually agreed between trading partners)
- `91`: INTERNAL (Internal company information)

</details>
