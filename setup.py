import setuptools

# Open and read the contents of README.md file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define version number
__version__ = "0.0.0"

# Define repository name and author details
REPO_NAME = "MLProjectWithMLFlow"
AUTHOR_USER_NAME = "naresh198457"
SRC_REPO = "MLProject"
AUTHOR_EMAIL = "naresh.sampara@gmail.com"

# Setup configuration for setuptools
setuptools.setup(
    name=SRC_REPO,  # Name of the package
    version=__version__,  # Version number
    author=AUTHOR_USER_NAME,  # Author name
    author_email=AUTHOR_EMAIL,  # Author email
    description="A small python package for ml app",  # Short description
    long_description=long_description,  # Long description (from README.md)
    long_description_content="text/markdown",  # Content type of long description
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL of the package
    project_urls={  # Additional project URLs (e.g., Bug Tracker)
        "Bug Tracker": f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # Directory structure of packages
    packages=setuptools.find_packages(where="src")  # Find packages in "src" directory
)
