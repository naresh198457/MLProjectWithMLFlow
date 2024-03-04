import os  # Importing os module for operating system related functionalities
from pathlib import Path  # Importing Path from pathlib module for path manipulation
import logging  # Importing logging module for logging purposes

# Configure logging to display INFO level messages with a specific format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = "MLProject"  # Define project name

# List of files to be created or checked
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",  # __init__.py constructor file
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html",
    "test.py"
]

# Loop through the list of files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert file path to Path object for better manipulation
    filedir, filename = os.path.split(filepath)  # Split the file path into directory and filename

    if filedir != "":  # Check if directory is specified
        os.makedirs(filedir, exist_ok=True)  # Create directory if it doesn't exist
        logging.info(f"Creating directory; {filedir} for the file: {filename}")  # Log directory creation

    # Check if the file doesn't exist or if it's empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Open file in write mode (create if it doesn't exist)
            pass  # Do nothing, creating an empty file
            logging.info(f"Creating empty file: {filepath}")  # Log empty file creation
    
    else:  # If file already exists
        logging.info(f"{filename} already exists")  # Log file existence
