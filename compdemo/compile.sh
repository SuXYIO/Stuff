#!/bin/bash
set -euo pipefail

FLAGS='-O3'
DIR='tmp'
mkdir -p $DIR
TNAME="$DIR/$1"

gcc $FLAGS -E "$1.c" -o "$TNAME.i"
gcc $FLAGS -S "$TNAME.i" -o "$TNAME.s"
gcc $FLAGS -c "$TNAME.s" -o "$TNAME.o"
