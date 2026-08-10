from PIL import Image, ImageDraw, ImageFont

img = Image.open('public/maroc-map.png').convert('RGBA')
draw = ImageDraw.Draw(img)

width, height = img.size

# Draw a 10x10 grid with lines every 10%
for i in range(1, 10):
    x = int(width * i / 10)
    draw.line([(x, 0), (x, height)], fill=(255, 0, 0, 128), width=2)
    
for i in range(1, 10):
    y = int(height * i / 10)
    draw.line([(0, y), (width, y)], fill=(255, 0, 0, 128), width=2)

# Draw 1% ticks for finer tuning
for i in range(1, 100):
    x = int(width * i / 100)
    if i % 10 != 0:
        draw.line([(x, 0), (x, 10)], fill=(0, 255, 0, 128), width=1)
        draw.line([(x, height-10), (x, height)], fill=(0, 255, 0, 128), width=1)
        
    y = int(height * i / 100)
    if i % 10 != 0:
        draw.line([(0, y), (10, y)], fill=(0, 255, 0, 128), width=1)
        draw.line([(width-10, y), (width, y)], fill=(0, 255, 0, 128), width=1)

img.save('scratch/grid_map.png')
print("Saved grid_map.png")
