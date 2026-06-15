import io
from PIL import Image
from rembg import remove

src_path = r"c:\WATERMELON\assets\resources\logo.png"

with open(src_path, "rb") as f:
    img_data = f.read()

print("Removing background...")
out_data = remove(img_data)

img = Image.open(io.BytesIO(out_data)).convert("RGBA")

bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

img.save(src_path)
print("Saved to " + src_path)
