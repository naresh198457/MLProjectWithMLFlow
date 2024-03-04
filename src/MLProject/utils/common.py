import os  # Importing the os module for operating system related functionalities
from box.exceptions import BoxValueError  # Importing BoxValueError from box.exceptions module
import yaml  # Importing yaml module for YAML file handling
from MLProject import logger  # Importing logger from MLProject module
import json  # Importing json module for JSON file handling
import joblib  # Importing joblib module for binary file handling
from ensure import ensure_annotations  # Importing ensure_annotations decorator from ensure module
from box import ConfigBox  # Importing ConfigBox from box module
from pathlib import Path  # Importing Path from pathlib module
from typing import Any  # Importing Any type from typing module


@ensure_annotations  # Decorator to ensure type annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads YAML file and returns ConfigBox type.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If YAML file is empty.
        e: Any other exception.

    Returns:
        ConfigBox: ConfigBox type representing the YAML content.
    """
    try:
        with open(path_to_yaml) as yaml_file:  # Open YAML file
            content = yaml.safe_load(yaml_file)  # Load YAML content
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")  # Log successful loading
            return ConfigBox(content)  # Return content as ConfigBox
    except BoxValueError:  # If YAML file is empty
        raise ValueError("yaml file is empty")
    except Exception as e:  # Catch any other exceptions
        raise e
    

@ensure_annotations  # Decorator to ensure type annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories.

    Args:
        path_to_directories (list): List of paths of directories to be created.
        verbose (bool, optional): If True, logs directory creation. Defaults to True.
    """
    for path in path_to_directories:  # Iterate over directory paths
        os.makedirs(path, exist_ok=True)  # Create directory if not exists
        if verbose:  # If verbose is True
            logger.info(f"created directory at: {path}")  # Log directory creation


@ensure_annotations  # Decorator to ensure type annotations
def save_json(path: Path, data: dict):
    """Save data as JSON.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in JSON format.
    """
    with open(path, "w") as f:  # Open file in write mode
        json.dump(data, f, indent=4)  # Write JSON data to file with indentation

    logger.info(f"json file saved at: {path}")  # Log successful saving


@ensure_annotations  # Decorator to ensure type annotations
def load_json(path: Path) -> ConfigBox:
    """Load JSON file data.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data loaded from JSON file as class attributes.
    """
    with open(path) as f:  # Open JSON file
        content = json.load(f)  # Load JSON content

    logger.info(f"json file loaded successfully from: {path}")  # Log successful loading
    return ConfigBox(content)  # Return content as ConfigBox


@ensure_annotations  # Decorator to ensure type annotations
def save_bin(data: Any, path: Path):
    """Save binary data.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)  # Save data as binary using joblib

    logger.info(f"binary file saved at: {path}")  # Log successful saving


@ensure_annotations  # Decorator to ensure type annotations
def load_bin(path: Path) -> Any:
    """Load binary data.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Object stored in the binary file.
    """
    data = joblib.load(path)  # Load binary data using joblib

    logger.info(f"binary file loaded from: {path}")  # Log successful loading
    return data  # Return loaded data


@ensure_annotations  # Decorator to ensure type annotations
def get_size(path: Path) -> str:
    """Get size of file in KB.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size of file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Calculate size in KB
    return f"~ {size_in_kb} KB"  # Return size as string
