import os
import glob

assets_dir = 'public/assets'

for root, dirs, files in os.walk(assets_dir):
    for f in files:
        if 'Atrium' in f:
            new_f = f.replace('Atrium', 'GCP Syndic')
            old_path = os.path.join(root, f)
            new_path = os.path.join(root, new_f)
            os.rename(old_path, new_path)
            print(f"Renamed: {f} -> {new_f}")
        elif 'atrium' in f:
            new_f = f.replace('atrium', 'gcpsyndic')
            old_path = os.path.join(root, f)
            new_path = os.path.join(root, new_f)
            os.rename(old_path, new_path)
            print(f"Renamed: {f} -> {new_f}")

print("Image renaming complete.")
