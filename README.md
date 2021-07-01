# messaribot

## Objective

**Messaribot** is a very simple bot which plots cryptocurrency data to assigned Discord channels.

## Dependencies

```
import os
import sys
import requests

from io import StringIO
from datetime import datetime, timedelta, date 

import pandas as pd 
import matplotlib.pyplot as plt

import discord
```

## Variables

### messari_fetch.py

Line #30
```
api_key = "YOUR_MESSARI_API_KEY_HERE"
```

Line #102
```
plt.savefig("/YOUR/FILEPATH/NAME/HERE/toast.png")
```



### messaribot.py

Line #10
```
TOKEN = 'YOUR_DISCORD_SECRET_TOKEN_HERE'
```

Line #23
```
ctx.send(file=discord.File(r'/YOUR/FILEPATH/NAME/HERE/toast.png'))
```
