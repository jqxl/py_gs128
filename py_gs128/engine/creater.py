from datetime import datetime
import random
import string

class Creater:
    '''Creator GS1-128 barcode values\n
    Example code:
    ```python
    print(1)
    ```
    '''
    def __init__(self):
        self.codes = []


    def get_value(self):
        return ''.join([f'{prefix}{value}' for prefix, value in self.codes])

    def get_text(self):
        return ''.join([f'({prefix}){value}' for prefix, value in self.codes])


    def code_add(self,
                 value: str,
                 prefix: str = '91'):
        '''`INTERNAL`: n2+an..30\n
        Internal company information\n
        Add custome `prefix` with `value`'''
        self._add_code(prefix=prefix, value=value, max_length=30)
        return self

    def _add_code(self, prefix: str, value: str, max_length: int = None):
        if  max_length:
            if len(value) > max_length:
                raise ValueError(f'Value too long for {prefix}, max length is {max_length}')
        self.codes.append((prefix, value))

    # Generate blocks
    def code_00(self, value: str):
        '''`SSCC`: n2+n18\n
         Serial Shipping Container Code'''
        self._add_code('00', value, 18)
        return self

    def code_01(self, value: str):
        '''`GTIN`: n2+n14\n
            Identification Number of the Trade Item'''
        self._add_code('01', value, 14)
        return self

    def code_02(self, value: str):
        '''`CONTENT`: n2+n14\n
            GTIN of Trade Items Contained in the Shipment'''
        self._add_code('02', value, 14)
        return self

    def code_10(self, date: datetime):
        '''`BATCH/LOT`: n2+an..20\n
        Batch (lot, group, package) Number'''
        formatted_date = date.strftime('%y%m%d')
        self._add_code('10', formatted_date, 20)
        return self

    def code_11(self, date: datetime):
        '''`PROD DATE`: n2+n6\n
        Production Date'''
        formatted_date = date.strftime('%y%m%d')
        self._add_code('11', formatted_date, 6)
        return self

    def code_12(self, date: datetime):
        '''`DUE DATE`: n2+n6\n
        Payment Due Date'''
        formatted_date = date.strftime('%y%m%d')
        self._add_code('12', formatted_date, 6)
        return self

    def code_13(self, date: datetime):
        '''`PACK DATE`: n2+n6\n
        Packaging Date'''
        formatted_date = date.strftime('%y%m%d')
        self._add_code('13', formatted_date, 6)
        return self

    def code_15(self, date: datetime):
        '''`BEST BEFORE` or `SELL BY`: n2+n6\n
        Minimum Shelf Life'''
        formatted_date = date.strftime('%y%m%d')
        self._add_code('15', formatted_date, 6)
        return self

    def code_17(self, date: datetime):
        '''`USE BY` or `EXPIRY`: n2+n6\n
        Maximum Shelf Life'''
        formatted_date = date.strftime('%y%m%d')
        self._add_code('17', formatted_date, 6)
        return self

    def code_20(self, date: datetime):
        '''`VARIANT`: n2+n2\n
        Product Variant'''
        formatted_date = date.strftime('%y%m%d')
        self._add_code('20', formatted_date, 2)
        return self

    def code_21(self, *,
                digs: int = 6,
                value: str = None):
        '''`SERIAL`: n2+an20\n
        Serial Number'''
        if not value:
            if digs:
                value = ''.join(random.choices(string.ascii_letters, k=digs))
            else:
                raise TypeError('missing required argument `digs` or `value`')
        self._add_code('21', value, 20)
        return self

    def code_22(self, value: str):
        '''`QTY/DATE/BATCH`: n2+an..29\n
        Serial Number'''
        self._add_code('22', value, 29)
        return self

    def code_23(self):
        raise NotImplementedError

    def code_240(self):
        raise NotImplementedError

    def code_241(self):
        raise NotImplementedError

    def code_250(self):
        raise NotImplementedError

    def code_251(self):
        raise NotImplementedError

    def code_30(self, value: str):
        '''`VAR.COUNT`: n2+n..8\n
        Serial Number'''
        self._add_code('30', value, 8)
        return self

    # Trade and Logistic Measurement Units
    def code_330(self, value: str):
        '''`GROSS WEIGHT (kg)`\n
        Gross Weight\n
        `example`:\n
        1 kg = (330)100
        '''
        self._add_code('330', value, len(value))
        return self

    def code_331(self):
        raise NotImplementedError

    def code_332(self):
        raise NotImplementedError

    def code_333(self):
        raise NotImplementedError

    def code_334(self):
        raise NotImplementedError

    def code_335(self):
        raise NotImplementedError

    def code_336(self):
        raise NotImplementedError

    # /Trade and Logistic Measurement Units

    def code_337(self):
        raise NotImplementedError

    def code_37(self):
        raise NotImplementedError

    def code_390(self):
        raise NotImplementedError

    def code_391(self):
        raise NotImplementedError

    def code_392(self):
        raise NotImplementedError

    def code_393(self):
        raise NotImplementedError

    def code_400(self):
        raise NotImplementedError

    def code_401(self):
        raise NotImplementedError

    def code_402(self):
        raise NotImplementedError

    def code_403(self):
        raise NotImplementedError

    def code_410(self):
        raise NotImplementedError

    def code_412(self):
        raise NotImplementedError

    def code_413(self):
        raise NotImplementedError

    def code_414(self):
        raise NotImplementedError

    def code_415(self):
        raise NotImplementedError

    def code_420(self):
        raise NotImplementedError

    def code_421(self):
        raise NotImplementedError

    def code_422(self):
        raise NotImplementedError

    def code_423(self):
        raise NotImplementedError

    def code_424(self):
        raise NotImplementedError

    def code_425(self):
        raise NotImplementedError

    def code_426(self):
        raise NotImplementedError

    # /Generate blocks
