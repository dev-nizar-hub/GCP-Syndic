from PIL import Image

# Load image
img = Image.open('photo/maroc map.png').convert('RGBA')
pixels = img.load()
width, height = img.size

# Sample background color from corners
corner_samples = [
    pixels[0, 0],
    pixels[width-1, 0],
    pixels[0, height-1],
    pixels[width-1, height-1],
    pixels[width//2, 0],   # top-center
]
# Average the RGB values
bg_r = sum(p[0] for p in corner_samples) // len(corner_samples)
bg_g = sum(p[1] for p in corner_samples) // len(corner_samples)
bg_b = sum(p[2] for p in corner_samples) // len(corner_samples)
print(f"Background color detected: RGB({bg_r}, {bg_g}, {bg_b})")

tolerance = 30

def is_background(r, g, b):
    return (
        abs(r - bg_r) < tolerance and
        abs(g - bg_g) < tolerance and
        abs(b - bg_b) < tolerance
    )

# Make background pixels transparent
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        if is_background(r, g, b):
            pixels[x, y] = (r, g, b, 0)  # fully transparent

img.save('public/maroc-map.png', 'PNG')
print(f"Done! Saved to public/maroc-map.png")
