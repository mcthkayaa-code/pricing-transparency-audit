#!/bin/bash
# Submits one URL to the Wayback Machine save API and prints the resulting
# snapshot URL (or FAILED). Max 2 retries (3 attempts total) per protocol.
# Usage: ./archive_one.sh "<url>"
URL="$1"
SAVE_URL="https://web.archive.org/save/${URL}"
for attempt in 1 2 3; do
  HEADERS=$(curl -s -D - -o /dev/null --max-time 90 "$SAVE_URL")
  LOC=$(echo "$HEADERS" | grep -i '^location:' | head -1 | sed 's/^[Ll]ocation: //' | tr -d '\r')
  if [[ -n "$LOC" ]]; then
    echo "SNAPSHOT: $LOC"
    exit 0
  fi
  echo "Attempt $attempt failed for $URL, retrying..." >&2
  sleep 3
done
echo "FAILED: could not archive $URL after 3 attempts"
exit 1
