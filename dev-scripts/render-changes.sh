#!/bin/bash

# Render Changed Files Only
# This script renders only files that have been modified according to git diff

set -e  # Exit on error

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}=== Render Changed Files ===${NC}"

# Get changed files from git
echo -e "${YELLOW}Getting changed files from git...${NC}"
git diff --name-only > diff

# Tweak quarto configuration
echo -e "${YELLOW}Updating Quarto configuration...${NC}"
python build/tweak_render.py

# Render the site
echo -e "${YELLOW}Rendering site...${NC}"
quarto render

# Clean up diff file
rm -f diff

echo -e "${GREEN}✅ Render complete!${NC}"
echo ""
echo "Starting preview server..."
quarto preview --port 5000 --host 0.0.0.0
