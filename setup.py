from setuptools import setup, find_packages
from pathlib import Path

# This reads the content of your README.md file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="fincalc-lib",
    version="1.0.4", # Increment version to update PyPI
    packages=find_packages(),
    
    # --- This part adds the description ---
    long_description=long_description,
    long_description_content_type="text/markdown",
    # --------------------------------------
    
    description="A professional finance analytics calculator library.",
    author="Akansha Rana",
    license="MIT",
    project_urls={
        "Source": "https://github.com/Akansha9821/finance_calculator.git",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
