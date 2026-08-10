import glob
import os

def inject_chatbot():
    html_files = glob.glob('public/*.html')
    chatbot_script = '<script defer src="/assets/gcp-chatbot.js"></script>'
    
    injected_count = 0
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'gcp-chatbot.js' not in content:
            # Find the closing </body> tag
            body_close_idx = content.rfind('</body>')
            if body_close_idx != -1:
                # Inject just before </body>
                new_content = content[:body_close_idx] + chatbot_script + '\n' + content[body_close_idx:]
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                injected_count += 1
                print(f"Injected into {os.path.basename(filepath)}")
            else:
                # If no </body> tag (e.g. fragments), append at the end
                with open(filepath, 'a', encoding='utf-8') as f:
                    f.write('\n' + chatbot_script + '\n')
                injected_count += 1
                print(f"Appended to {os.path.basename(filepath)} (no </body> found)")
        else:
            print(f"Already has chatbot: {os.path.basename(filepath)}")
            
    print(f"Total files injected: {injected_count}")

if __name__ == '__main__':
    inject_chatbot()
