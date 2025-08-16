#!/bin/bash

# CONFIG
LOCAL_PORT=8000
GITHUB_URL="https://mangathpup.github.io/superpersonality_agi_site/"

echo "🚀 Starting site sync..."

# Step 1: Make sure we're in the project root
cd "$(dirname "$0")"

# Step 2: Optional rebuild steps (if you have a script for this)
if [ -f "./organize_images_auto.sh" ]; then
  echo "📂 Running image & HTML rebuild..."
  bash ./organize_images_auto.sh
fi

# Step 3: Git add & commit
echo "💾 Committing changes..."
git add .
git commit -m "Auto-sync site: rebuild HTML, CSS, images" || echo "No changes to commit"

# Step 4: Force push to GitHub
echo "🌐 Force-pushing to GitHub..."
git push -u origin main --force

# Step 5: Open localhost in browser
echo "🌟 Opening localhost..."
if command -v xdg-open &> /dev/null; then
    xdg-open "http://localhost:$LOCAL_PORT"
elif command -v start &> /dev/null; then
    start "http://localhost:$LOCAL_PORT"
fi

# Step 6: Open GitHub Pages
echo "🌍 Opening live GitHub Pages..."
if command -v xdg-open &> /dev/null; then
    xdg-open "$GITHUB_URL"
elif command -v start &> /dev/null; then
    start "$GITHUB_URL"
fi

# Step 7: Run local server
echo "🖥️ Starting local server on port $LOCAL_PORT..."
python -m http.server $LOCAL_PORT
