#!/usr/bin/env python

from polysdk import PolyClient

"""
visit https://v1.polymerapp.io/ where
you can generate client_token from 
"Developer API" option under user icon
"""
client_token = "c4855ffe7c37cc4bb14f7d7988e03fff"

client = PolyClient(api_token=client_token)

masking_key = "1234567890123456"

fmd = client.mask_file(file_path="./pii_file.txt", key=masking_key)
print(fmd.get_text())

text = """Hi Professor! Email: [[3TpPh25m/39RMO9mY6KnjnATDzkrzOKr8S/paE6Vpzg=]] This is confidential data file. If received, it should be deleted right away after being used once."""

umd = client.unmask_text(text=text, key=masking_key)
print(umd.get_text())

md = client.mask_csv_file("./examples/us-500.csv", masking_key)

print(md.get_text())
