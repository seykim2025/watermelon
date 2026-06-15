from PIL import Image, ImageDraw
import os

target_sizes = {
    1: 52,
    2: 80,
    3: 108,
    4: 119,
    5: 153,
    6: 183,
    7: 193,
    8: 258,
    9: 308,
    10: 309,
    11: 408
}

def process_image(idx, size):
    path = f"assets/img/fruit_{idx}.png"
    if not os.path.exists(path):
        print(f"Skipping {path}, not found.")
        return
    
    img = Image.open(path).convert("RGBA")
    
    # 1. crop to center square
    width, height = img.size
    min_dim = min(width, height)
    left = (width - min_dim) / 2
    top = (height - min_dim) / 2
    right = (width + min_dim) / 2
    bottom = (height + min_dim) / 2
    img = img.crop((left, top, right, bottom))
    
    # 2. resize
    img = img.resize((size, size), Image.Resampling.LANCZOS)
    
    # 3. create circular mask
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    
    # 4. apply mask
    output = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    output.paste(img, (0, 0), mask)
    
    output.save(path)
    print(f"Processed {path} to size {size}x{size} with circular mask.")

for i in range(1, 12):
    process_image(i, target_sizes.get(i, 100))
