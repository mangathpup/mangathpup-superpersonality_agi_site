from PIL import Image
import os
import sys

# --- CONFIG ---
# Default input image path (change this to your base thumbnail if no arg is given)
DEFAULT_INPUT = "../assets/images/SuperPersonalityThumbnail.png"

# Output directory
OUTPUT_DIR = "../assets/icons"

# Favicon sizes (browser + app icons)
FAVICON_SIZES = [16, 32, 48, 64, 128, 256]

# Apple Touch Icon sizes
APPLE_SIZES = [180, 167, 152, 120]

# Social media preview size (Facebook/Twitter/LinkedIn OG image)
SOCIAL_SIZE = (1200, 630)


def generate_icons(input_path):
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Open and convert image to RGBA (preserves transparency)
    img = Image.open(input_path).convert("RGBA")

    # --- FAVICONS ---
    for size in FAVICON_SIZES:
        icon = img.resize((size, size), Image.LANCZOS)
        icon.save(os.path.join(OUTPUT_DIR, f"favicon-{size}x{size}.png"))
    print("✅ Favicons generated.")

    # Save ICO file (Windows browsers expect favicon.ico)
    ico_path = os.path.join(OUTPUT_DIR, "favicon.ico")
    img.save(ico_path, sizes=[(s, s) for s in FAVICON_SIZES])
    print("✅ favicon.ico generated.")

    # --- APPLE TOUCH ICONS ---
    for size in APPLE_SIZES:
        apple_icon = img.resize((size, size), Image.LANCZOS)
        apple_icon.save(os.path.join(OUTPUT_DIR, f"apple-touch-icon-{size}x{size}.png"))
    print("✅ Apple Touch icons generated.")

    # --- SOCIAL MEDIA OG IMAGE ---
    social_img = img.resize(SOCIAL_SIZE, Image.LANCZOS)
    social_img.save(os.path.join(OUTPUT_DIR, "social-preview.png"))
    print("✅ Social preview image generated.")


if __name__ == "__main__":
    # Use CLI argument if provided, else fallback to default
    if len(sys.argv) > 1:
        input_image = sys.argv[1]
    else:
        input_image = DEFAULT_INPUT

    # Normalize path (remove stray spaces/tabs/newlines)
    input_image = input_image.strip()

    if not os.path.exists(input_image):
        print(f"❌ Error: File '{input_image}' not found.")
        sys.exit(1)

    generate_icons(input_image)
    print(f"🎯 All icons saved in: {os.path.abspath(OUTPUT_DIR)}")

	
