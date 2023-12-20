#!/bin/bash

git diff --name-only >> diff
python build/tweak_render.py

quarto render
find . -name "index.qmd" | rename -f -d 's/^/_/'

quarto preview --port 5000 --host 0.0.0.0
