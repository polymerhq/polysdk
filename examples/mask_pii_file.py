#!/usr/bin/env python

from polysdk import PolyClient

"""
visit https://v1.polymerapp.io/ where
you can generate client_token from 
"Developer API" option under user icon
"""
client_token = 'bb35ff416cbdd64fe58cff92b953f9c5'

client = PolyClient(api_token=client_token)

masking_key = "1234567890123456"

text = """Hi Professor! Email: [[3TpPh25m/39RMO9mY6KnjnATDzkrzOKr8S/paE6Vpzg=]] This is confidential data file. If received, it should be deleted right away after being used once."""

umd = client.unmask_text(text=text, key=masking_key)
print(umd.get_text())

mdf = client.mask_csv_file("./us-500.csv", masking_key, ['email', 'last_name'])
print(mdf.get_text())

umdf = client.unmask_csv_file("./us-500.csv", masking_key)
print(umdf.get_text())
