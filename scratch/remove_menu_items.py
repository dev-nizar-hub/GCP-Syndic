import os
import glob

def remove_element_by_class(html_str, target_class):
    while True:
        # Find the class
        class_idx = html_str.find(target_class)
        if class_idx == -1:
            break
            
        # Find the start of this tag
        start_idx = html_str.rfind("<li", 0, class_idx)
        if start_idx == -1:
            # If not an li, just break or handle (but we know it's an li)
            break
            
        # Find the matching closing tag
        depth = 0
        i = start_idx
        end_idx = -1
        while i < len(html_str):
            if html_str.startswith("<li", i):
                # Only count <li if it's a tag (not <link)
                # But to be safe, check if it's <li > or <li\s
                if html_str[i:i+4] == "<li>" or html_str[i:i+4].startswith("<li ") or html_str[i:i+4].startswith("<li\t") or html_str[i:i+4].startswith("<li\n") or html_str[i:i+4].startswith("<li\r") or html_str[i:i+4].startswith("<li\f") or html_str[i:i+4].startswith("<li\v") or html_str[i:i+3] == "<li":
                    # Let's just use startswith("<li") but make sure it's not <link
                    if not html_str.startswith("<link", i):
                        depth += 1
                        i += 3
                        continue
            elif html_str.startswith("</li>", i):
                depth -= 1
                if depth == 0:
                    end_idx = i + 5
                    break
                i += 5
                continue
            i += 1
            
        if end_idx != -1:
            html_str = html_str[:start_idx] + html_str[end_idx:]
        else:
            print(f"Warning: Could not find closing tag for {target_class}")
            break
            
    return html_str


public_dir = "c:/xampp/htdocs/GCP Syndic Website v2/public"
html_files = glob.glob(os.path.join(public_dir, '*.html'))

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        content = remove_element_by_class(content, 'm_espace_client')
        content = remove_element_by_class(content, 'm_agences')
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Removed from {os.path.basename(filepath)}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print("Done removing menu items.")
