import re

class AI(str):
    '''Application Identifier (AI)'''

class Description(str):
    '''Description of AI'''

class Value(str):
    '''Information that follows each AI'''

AI_DICT = {
    "00": {"description": "SSCC", "length": 18},  # Serial Shipping Container Code
    "01": {"description": "GTIN", "length": 14},  # Identification Number of the Trade Item
    "02": {"description": "CONTENT", "length": 14},  # GTIN of Trade Items Contained in the Shipment
    "10": {"description": "BATCH/LOT", "length": None},  # Batch/Lot Number
    "11": {"description": "PROD DATE", "length": 6},  # Production Date
    "12": {"description": "DUE DATE", "length": 6},  # Payment Due Date
    "13": {"description": "PACK DATE", "length": 6},  # Packaging Date
    "15": {"description": "BEST BEFORE", "length": 6},  # Minimum Shelf Life
    "17": {"description": "USE BY", "length": 6},  # Maximum Shelf Life
    "20": {"description": "VARIANT", "length": 2},  # Product Variant
    "21": {"description": "SERIAL", "length": None},  # Serial Number
    "22": {"description": "QTY/DATE/BATCH", "length": None},  # Auxiliary Data for Special Pharmaceutical Products
    "240": {"description": "ADDITIONAL ID", "length": None},  # Additional Product Identification
    "241": {"description": "CUST.PART NO", "length": None},  # Customer Part Number
    "250": {"description": "SECONDARY SERIAL", "length": None},  # Additional Serial Number
    "251": {"description": "REF TO SOURCE", "length": None},  # Reference to Source
    "30": {"description": "VAR.COUNT", "length": 8},  # Variable Count
    "330": {"description": "GROSS WEIGHT (kg)", "length": 6},  # Gross Weight in kg
    "337": {"description": "KG PER m2", "length": 6},  # Kilograms per square meter
    "37": {"description": "COUNT", "length": 8},  # Number of Trade Units in Shipment
    "390": {"description": "AMOUNT", "length": None},  # Amount payable - single currency
    "391": {"description": "AMOUNT", "length": None},  # Amount payable - with ISO currency code
    "392": {"description": "PRICE", "length": None},  # Amount payable for variable measure trade item - single currency
    "393": {"description": "PRICE", "length": None},  # Amount payable for variable measure trade item
    "400": {"description": "ORDER NUMBER", "length": None},  # Order Number
    "401": {"description": "CONSIGNMENT", "length": None},  # Consignment Number
    "402": {"description": "SHIPMENT NO.", "length": 17},  # Shipment Identification Number
    "403": {"description": "ROUTE", "length": None},  # Route Code
    "410": {"description": "SHIP TO LOC", "length": 13},  # EAN/UCC Global Location Number (GLN) of the Ship-to party
    "411": {"description": "BILL TO", "length": 13},  # EAN/UCC Global Location Number (GLN) of the Bill-to party
    "412": {"description": "PURCHASE FROM", "length": 13},  # EAN/UCC Global Location Number (GLN) of the supplier
    "413": {"description": "SHIP FOR LOC", "length": 13},  # EAN/UCC Global Location Number (GLN) of the Ship-for party
    "414": {"description": "LOC No", "length": 13},  # EAN/UCC Global Location Number (GLN)
    "415": {"description": "PAY TO", "length": 13},  # EAN/UCC Global Location Number (GLN) of the party to be paid
    "420": {"description": "SHIP TO POST", "length": None},  # Postal code of the Ship-to location
    "421": {"description": "SHIP TO POST", "length": None},  # Postal code of the Ship-to location with ISO country code
    "422": {"description": "ORIGIN", "length": 3},  # Country of origin of the trade item
    "423": {"description": "COUNTRY - INITIAL PROCESS", "length": None},  # Country of initial processing
    "424": {"description": "COUNTRY - PROCESS.", "length": 3},  # Country of processing
    "425": {"description": "COUNTRY - DISASSEMBLY", "length": 3},  # Country of disassembly
    "426": {"description": "COUNTRY – FULL PROCESS", "length": 3},  # Country of full processing
    "7001": {"description": "NSN", "length": 13},  # NATO Stock Number
    "7002": {"description": "MEAT CUT", "length": None},  # UNECE carcass or cuts classification
    "8001": {"description": "DIMENSIONS", "length": 14},  # Roll products - Width, Length, Diameter, Direction, Splices
    "8002": {"description": "CMT NO", "length": 20},  # Cellular mobile telephone serial number
    "8003": {"description": "GRAI", "length": None},  # Global Returnable Asset Identifier
    "8004": {"description": "GIAI", "length": None},  # Global Individual Asset Identifier
    "8005": {"description": "PRICE PER UNIT", "length": 6},  # Price per unit of measure
    "8006": {"description": "GCTIN", "length": None},  # Identification of component of a trade item
    "8007": {"description": "IBAN", "length": None},  # International Bank Account Number
    "8008": {"description": "PROD TIME", "length": None},  # Date and time of production
    "8018": {"description": "GSRN", "length": 18},  # Global Service Relation Number
    "8020": {"description": "REF NO", "length": 25},  # Reference number
    "8100": {"description": "COUPON EXTENDED CODE", "length": None},  # Extended coupon code
    "8101": {"description": "COUPON EXTENDED CODE", "length": None},  # Extended coupon code
    "8102": {"description": "COUPON EXTENDED CODE", "length": None},  # Extended coupon code
    "903": {"description": "INTERNAL", "length": None},  # Information mutually agreed between trading partners
    "91": {"description": "INTERNAL", "length": None},  # Internal company information
}


def decode_gs128(barcode:str) -> dict[AI, Description, Value]:
    '''
    Method to decode GS1-128 barcode\n
    `Example`:
    ```python
    decoded_barcode = decode_gs128('01046456438549341124072221uikPbH')
    ```\n
    `Then you can print parts of barcode`
    ```python
    for ai, description, data in decoded_barcode:
        print(f"AI: {ai}, Description: {description}, Data: {data}")
    ```'''
    results = []
    index = 0
    while index < len(barcode):
        # Find AI (2, 3, or 4 digits long)
        ai = barcode[index:index+2]
        if ai not in AI_DICT:
            ai = barcode[index:index+3]
            if ai not in AI_DICT:
                ai = barcode[index:index+4]
                if ai not in AI_DICT:
                    raise ValueError(f"Unknown Application Identifier (AI) at index {index}")

        index += len(ai)
        ai_info = AI_DICT[ai]

        if ai_info["length"]:
            data_length = ai_info["length"]
        else:
            match = re.search(r'(\d{2,4})', barcode[index:])
            if match:
                data_length = match.start()
            else:
                data_length = len(barcode) - index

        # Extract the data
        value = barcode[index:index+data_length]
        results.append((ai, ai_info["description"], value))
        index += data_length

    return results

