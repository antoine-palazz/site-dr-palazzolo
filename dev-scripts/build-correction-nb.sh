#!/bin/bash

git diff --name-only >> diff
python build/tweak_render.py

quarto render content
# quarto render content --to ipynb --execute
