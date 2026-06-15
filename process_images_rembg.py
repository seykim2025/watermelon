import os
from PIL import Image
from rembg import remove

original_images = {
    1: r"C:\Users\seyki\.gemini\antigravity\brain\c78bc68d-6fb9-4d93-b76a-ad4c619b0003\fruit_1_1781325764554.png",
    2: r"C:\Users\seyki\.gemini\antigravity\brain\c78bc68d-6fb9-4d93-b76a-ad4c619b0003\fruit_2_1781325804367.png",
    3: r"C:\Users\seyki\.gemini\antigravity\brain\c78bc68d-6fb9-4d93-b76a-ad4c619b0003\fruit_3_1781325814199.png",
    4: r"C:\Users\seyki\.gemini\antigravity\brain\c78bc68d-6fb9-4d93-b76a-ad4c619b0003\fruit_4_1781325826631.png",
    5: r"C:\Users\seyki\.gemini\antigravity\brain\c78bc68d-6fb9-4d93-b76a-ad4c619b0003\fruit_5_1781325847730.png",
    6: r"C:\Users\seyki\.gemini\antigravity\brain\c78bc68d-6fb9-4d93-b76a-ad4c619b0003\fruit_6_1781325859330.png",
    7: r"C:\Users\seyki\.gemini\antigravity\brain\c78bc68d-6fb9-4d93-b76a-ad4c619b0003\fruit_7_1781325873158.png",
    8: r"C:\Users\seyki\.gemini\antigravity\brain\c78bc68d-6fb9-4d93-b76a-ad4c619b0003\fruit_8_1781325884423.png",
    9: r"C:\Users\seyki\.gemini\antigravity\brain\c78bc68d-6fb9-4d93-b76a-ad4c619b0003\fruit_9_1781325903779.png",
    10: r"C:\Users\seyki\.gemini\antigravity\brain\c78bc68d-6fb9-4d93-b76a-ad4c619b0003\fruit_10_1781325915236.png",
    11: r"C:\Users\seyki\.gemini\antigravity\brain\c78bc68d-6fb9-4d93-b76a-ad4c619b0003\fruit_11_1781325927090.png"
}

target_sizes = {
    1: 52, 2: 80, 3: 108, 4: 119, 5: 153,
    6: 183, 7: 193, 8: 258, 9: 308, 10: 309, 11: 408
}

def make_square(im):
    # Padding to make it a square without stretching
    x, y = im.size
    size = max(x, y)
    new_im = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

def process_image(idx):
    src_path = original_images[idx]
    dst_path = f"assets/img/fruit_{idx}.png"
    target_size = target_sizes[idx]
    
    if not os.path.exists(src_path):
        print(f"File not found: {src_path}")
        return
    
    print(f"Processing {idx}...")
    with open(src_path, 'rb') as f:
        img_data = f.read()
    
    # 1. Remove background using rembg
    out_data = remove(img_data)
    
    import io
    img = Image.open(io.BytesIO(out_data)).convert("RGBA")
    
    # 2. Crop to bounding box
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    
    # 3. Make square and resize
    img = make_square(img)
    img = img.resize((target_size, target_size), Image.Resampling.LANCZOS)
    
    img.save(dst_path)
    print(f"Saved {dst_path}")

for i in range(1, 12):
    process_image(i)
