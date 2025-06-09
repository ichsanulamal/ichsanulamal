import nbformat as nbf

# Read the content of your Python script
with open('notebook.py', 'r') as f:
    script = f.read()

# Split the script into code and markdown sections
lines = script.split('\n')
cells = []
current_cell = []
is_code = False

for line in lines:
    if line.startswith('# In['):
        if current_cell:
            cell_type = 'code' if is_code else 'markdown'
            cells.append(nbf.v4.new_code_cell('\n'.join(current_cell)) if is_code else nbf.v4.new_markdown_cell('\n'.join(current_cell)))
            current_cell = []
        is_code = True
    elif line.startswith('#') and not is_code:
        current_cell.append(line[2:])
    elif line.startswith('#'):
        current_cell.append(line)
    else:
        is_code = True
        current_cell.append(line)

if current_cell:
    cell_type = 'code' if is_code else 'markdown'
    cells.append(nbf.v4.new_code_cell('\n'.join(current_cell)) if is_code else nbf.v4.new_markdown_cell('\n'.join(current_cell)))

# Create the notebook
nb = nbf.v4.new_notebook()
nb['cells'] = cells

# Write the notebook to a file
with open('notebook.ipynb', 'w') as f:
    nbf.write(nb, f)
