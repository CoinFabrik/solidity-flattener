#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
FILE="$(basename -- $1)"
BRANCH=`git rev-parse --abbrev-ref HEAD`
DEST_DIR="$DIR/../flat/${PWD##*/}_$BRANCH"
mkdir -p "$DEST_DIR"
DEST="$DEST_DIR/${FILE%.*}Flat.${FILE#*.}"
echo "Saving flat version of $1 into $DEST"
python3 "$DIR/flattener.py" $1 > "$DEST"

