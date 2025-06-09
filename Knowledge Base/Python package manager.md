---
Created: 2022-08-24T06:24
tags:
  - Productivity
  - Python
Last edited time: 2024-08-04T10:52
---
# Conda
```Bash
# To see a list of available python versions first, use the command
conda search "^python$"
# To create the virtual environment for python version x.y.z, use the command
conda create -n <yourenvname> python=<x.y.z> -y
# Activate venv with
conda activate <yourenvname>
# Deactivate with
conda deactivate
# To delete the virtual environment when done, use the command
conda remove -n <yourenvname> --all
```
### Change default python version
```JavaScript
conda update conda
conda install python=3.9
```
# VENV
```JavaScript
python -m venv .env
venv .env
```