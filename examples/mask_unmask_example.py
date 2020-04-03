#!/usr/bin/env python

from polysdk import PolyClient

# you can generate it from "Developer API" under user icon
client_token = "<your_api_token_here>"

# masking key can be less than or equal to 16 characters
masking_key = "<your_masking_key_here>"

input_data = "Hey a@b.com!"

client = PolyClient(api_token=client_token)

masked_data = client.mask_data(data=input_data, key=masking_key)
print(masked_data.get_text())

unmasked_data = client.unmask_data(data=masked_data.get_text(), key=masking_key)
print(unmasked_data.get_text())