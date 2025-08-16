#!/bin/bash

# Step 1: Go to your site folder
cd /c/dev/superpersonality_agi_site/public || exit

# Step 2: Open localhost in browser
start "" http://localhost:8000

# Step 3: Start the local server
python -m http.server 8000
