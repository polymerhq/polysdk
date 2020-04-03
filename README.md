# polysdk

Install (in Python >= 2.7)

```
pip install polysdk==0.0.1
```

Use

```python

from polysdk import PolyClient

client = PolyClient(api_token=client_token)

# to mask, use `.mask_data(data=, key=)
masked_data = client.mask_data(data=input_data, key=masking_key)

# to unmask, use `.unmask_data(data=, key=)
unmasked_data = client.unmask_data(data=masked_data.get_text(), key=masking_key)
```
