# messaribot

### Objective

**Messaribot** is a very simple bot which plots cryptocurrency data to assigned Discord channels.

### Dependencies

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

### Variables

#### messari_fetch.py

Line #30: create a [free account here](https://messari.io/)
```
api_key = "YOUR_MESSARI_API_KEY_HERE"
```

Line #102
```
plt.savefig("/YOUR/FILEPATH/NAME/HERE/toast.png")
```

#### messaribot.py

Line #9: if you want a different command prefix instead of $ sign
```
client = commands.Bot(command_prefix = '$')
```

Line #10: instructions can be [found here](https://discordpy.readthedocs.io/en/stable/discord.html)
```
TOKEN = 'YOUR_DISCORD_SECRET_TOKEN_HERE'
```

Line #23
```
ctx.send(file=discord.File(r'/YOUR/FILEPATH/NAME/HERE/toast.png'))
```


### Launching Messaribot

#### Logging in to Discord

```
python3 messaribot.py
```

#### Running commands

Assumes you are using the default command prefix and function name.

```
$messaribot btc
```




### Appendix

* [article link](https://www.christopheryee.org/)



