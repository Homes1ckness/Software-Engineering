import re

def process_tikz(match):
    content = match.group(0)
    
    if 'seqLifeline' not in content or 'seqFragment' not in content:
        return content
        
    lines = content.split('\n')
    
    fragments = []
    other_lines = []
    
    for line in lines:
        if 'seqFragment' in line or 'seqDivider' in line or 'seqLabel' in line:
            fragments.append(line)
        else:
            other_lines.append(line)
            
    insert_idx = -1
    for i, line in enumerate(other_lines):
        if 'seqLifeline' in line:
            insert_idx = i
            break
            
    if insert_idx != -1:
        new_lines = other_lines[:insert_idx] + fragments + other_lines[insert_idx:]
        return '\n'.join(new_lines)
    else:
        return content

with open('main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

new_text = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', process_tikz, text, flags=re.DOTALL)

with open('main.tex', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Done")
