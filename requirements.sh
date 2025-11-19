#!/bin/bash

# Install Quarto Extensions
# This script installs all required Quarto extensions for the website

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if quarto is installed
if ! command -v quarto &> /dev/null; then
    echo -e "${RED}❌ Error: Quarto is not installed${NC}"
    echo "Please install Quarto from: https://quarto.org/docs/get-started/"
    exit 1
fi

echo -e "${GREEN}Installing Quarto extensions...${NC}"
echo "================================="

# Array of extensions to install
declare -a extensions=(
    "quarto-ext/fontawesome"
    "shafayetShafee/black-formatter"
    "shafayetShafee/bsicons"
)

# Install each extension
for ext in "${extensions[@]}"; do
    echo -e "${YELLOW}Installing: ${ext}${NC}"
    if quarto add "$ext" --no-prompt; then
        echo -e "${GREEN}✅ ${ext} installed successfully${NC}"
    else
        echo -e "${RED}❌ Failed to install ${ext}${NC}"
        exit 1
    fi
done

echo ""
echo -e "${GREEN}✅ All extensions installed successfully!${NC}"
echo ""
echo "You can now run: quarto preview"

