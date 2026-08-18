#!/bin/bash
url="$1"
maxretries=2
attempt=0
while [ $attempt -le $maxretries ]; do
  attempt=$((attempt+1))
  headers=$(/usr/bin/curl -s -D - -o /dev/null --max-time 60 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36" "https://web.archive.org/save/$url")
  loc=$(echo "$headers" | grep -i "^location:" | tail -1 | sed -E 's/^[Ll]ocation: *//I' | tr -d '\r\n')
  if [ -n "$loc" ]; then
    echo "$loc"
    exit 0
  fi
  sleep 3
done
echo "ARCHIVE_FAILED"
exit 1
