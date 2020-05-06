# polysdk

## Package Installation

```
pip install polysdk
```

## Usage

```python
#!/usr/bin/env python

"""
make sure to run
pip install polysdk to be able 
to import from the package polysdk below
"""
from polysdk import PolyClient

"""
visit https://v1.polymerapp.io/ where
you can generate client_token from 
"Developer API" option under user icon
"""
client_token = "<your_client_token_here>"

# initializing client using client_token
client = PolyClient(api_token=client_token)

# masking key can be less than or equal to 16 characters
masking_key = "<your_masking_key_here>"

"""
masking/unmasking text
"""
input_data = "Hey a@b.com!"
masked_data = client.mask_text(text=input_data, key=masking_key)
masked_data.get_text()

unmasked_data = client.unmask_text(text=masked_data.get_text(), key=masking_key)
unmasked_data.get_text()

"""
masking/unmasking file
"""
fmd = client.mask_text_file(file_path="<your_file_path>", key=masking_key)
fmd.get_text()

fumd = client.unmask_text_file(file_path="<your_file_path>", key=masking_key)
fumd.get_text()
```
