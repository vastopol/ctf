#!/bin/bash

# https://unix.stackexchange.com/questions/461275/bash-loop-unzip-passworded-file-script

zipfile="$1"
while unzip -Z1 "$zipfile" | head -n1 | grep "\.zip$"; do
    next_zipfile="$(unzip -Z1 "$zipfile" | head -n1)"
    unzip -P "${next_zipfile%.*}" "$zipfile"
    zipfile="$next_zipfile"
done
