#!/bin/bash

# Build the site using Hugo
# Assumes 'hugo' is installed or located in bin/hugo

echo "Building site to docs/ folder..."

if [ -f "./bin/hugo" ]; then
    ./bin/hugo --destination docs --buildDrafts
else
    hugo --destination docs --buildDrafts
fi

echo "Build complete. You can now commit and push the 'docs' folder."
echo "Remember to set GitHub Pages source to 'main' branch and '/docs' folder in repository settings."
