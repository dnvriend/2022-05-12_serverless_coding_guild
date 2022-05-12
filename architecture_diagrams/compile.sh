#!/bin/bash
echo "compiling all diagrams"
for f in *.py; do
  pipenv run python $f
done
