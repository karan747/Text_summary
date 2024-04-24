import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'Text_summary'

list_of_files = [
    ".github/workflow/.gitkeep/",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/traials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = os.path.dirname(filepath)
    if (filedir is not '') and (not os.path.exists(filedir)):
        os.makedirs(filedir)
        logging.info(f"Created directory: {filedir}")
    
    if  (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        
        with open(filepath, "w") as f:
            logging.info(f"Created file: {filepath}")
            pass
        
    else:
        logging.info(f"File already exists: {filepath}")
     