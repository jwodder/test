from datetime import datetime
import sys

stamp = 1762623296  # 2025-11-08 12:34:56-05:00
dt = datetime.fromtimestamp(stamp).astimezone()
tzname = dt.tzname()
print(f"Got {tzname!r}, expected 'EST'")

if tzname != "EST":
    sys.exit(1)
