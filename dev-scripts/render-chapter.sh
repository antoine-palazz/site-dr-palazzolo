#!/bin/bash

SECTION=$1
CHAPTER=$2

SECTION_PATH="content/${SECTION}"
CHAPTER_PATH="${SECTION_PATH}/${CHAPTER}"

quarto preview -port 5000 --host 0.0.0.0
