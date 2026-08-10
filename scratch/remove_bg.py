from PIL import Image
import numpy as np

# Load image
img = Image.open('photo/maroc map.png').convert('RGBA')
data = np.array(img)

# The background is the beige/sand color - sample from corners
corners = [
    data[0, 0, :3],      # top-left
    data[0, -1, :3],     # top-right
    data[-1, 0, :3],     # bottom-left
    data[-1, -1, :3],    # bottom-right
]
bg_color = np.mean(corners, axis=0).astype(int)
print(f"Background color detected: RGB{tuple(bg_color)}")

# Create a mask: pixels within tolerance of background color become transparent
tolerance = 30
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
mask = (
    (np.abs(r.astype(int) - bg_color[0]) < tolerance) &
    (np.abs(g.astype(int) - bg_color[1]) < tolerance) &
    (np.abs(b.astype(int) - bg_color[2]) < tolerance)
)

# Apply transparency
data[mask, 3] = 0

# Save result
result = Image.fromarray(data)
result.save('public/maroc-map.png')
print("Saved transparent map to public/maroc-map.png")
print(f"Pixels made transparent: {mask.sum()} / {mask.size}")
