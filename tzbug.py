import sys
import time

stamp = 1762623296  # 2025-11-08 12:34:56-05:00
tzname = time.strftime("%Z", time.localtime(stamp))
print(f"Got {tzname!r}, expected 'EST'")

if tzname != "EST":
    sys.exit(1)
