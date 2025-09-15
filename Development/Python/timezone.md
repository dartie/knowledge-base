# Timezone

## Pure Python solution with `zoneinfo` (recommended, since you’re on Python 3.13):
```python
from datetime import datetime
from zoneinfo import ZoneInfo

# Example: parse naive datetime from MFT log
dt = datetime.strptime("2025-08-28 09:23:00", "%Y-%m-%d %H:%M:%S")

# Tell Python this time is in UTC (because MFT server logs in UTC)
dt_aware = dt.replace(tzinfo=ZoneInfo("UTC"))

print("Stored datetime:", dt_aware)  # 2025-08-28 09:23:00+00:00

# Convert to Europe/Rome (for display)
dt_rome = dt_aware.astimezone(ZoneInfo("Europe/Rome"))
print("Rome time:", dt_rome)  # 2025-08-28 11:23:00+02:00

```
---

## Pure Python solution with `pytz` (if you already use it):

```python
from datetime import datetime
import pytz

utc = pytz.UTC
rome = pytz.timezone("Europe/Rome")

# Parse naive datetime
dt = datetime.strptime("2025-08-28 09:23:00", "%Y-%m-%d %H:%M:%S")

# Localize as UTC
dt_aware = utc.localize(dt)

# Convert to Europe/Rome
dt_rome = dt_aware.astimezone(rome)
```
