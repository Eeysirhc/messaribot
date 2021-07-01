# messaribot

### Objective

**Messaribot** is a very simple bot which plots cryptocurrency data to assigned Discord channels.

This is written in Python, crytpo data is pulled from the [Messari API](https://messari.io/api), and relies on the [discord.py](https://discordpy.readthedocs.io/en/stable/) API wrapper to publish the finished graphs.

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

Line #30: create a [free account here](https://messari.io/).
```
api_key = "YOUR_MESSARI_API_KEY_HERE"
```

Line #102: change file path name.
```
plt.savefig("/YOUR/FILEPATH/NAME/HERE/toast.png")
```

#### messaribot.py

Line #9: if you want a different command prefix instead of using the $ sign.
```
client = commands.Bot(command_prefix = '$')
```

Line #10: instructions can be [found here](https://discordpy.readthedocs.io/en/stable/discord.html).
```
TOKEN = 'YOUR_DISCORD_SECRET_TOKEN_HERE'
```

Line #23: chnage file path name.
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

* [https://www.christopheryee.org/blog/messaribot-cryptocurrency-charts-for-discord/](https://www.christopheryee.org/blog/messaribot-cryptocurrency-charts-for-discord/)

