import io
from PIL import Image
from rembg import remove

src_path = r"C:\Users\seyki\.gemini\antigravity\brain\c78bc68d-6fb9-4d93-b76a-ad4c619b0003\toss_logo_solid_1781488154888.png"
dst_path = r"c:\WATERMELON\build\web-mobile\splash.85cfd.png"

with open(src_path, "rb") as f:
    img_data = f.read()

print("Removing background...")
out_data = remove(img_data)

img = Image.open(io.BytesIO(out_data)).convert("RGBA")

bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

# Resize it to a reasonable logo size for the splash screen
img.thumbnail((300, 300), Image.Resampling.LANCZOS)
img.save(dst_path)
print("Saved splash logo to " + dst_path)
