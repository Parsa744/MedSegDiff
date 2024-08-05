"""
Codebase for " Diffusion Models for Implicit Image Segmentation Ensembles".
"""
import os

# Paths to the necessary directories
directories = [
    '/kaggle/working/MedSegDiff/guided_diffusion',
]

# Create __init__.py in each directory if it doesn't exist
for directory in directories:
    init_path = os.path.join(directory, '__init__.py')
    if not os.path.exists(init_path):
        with open(init_path, 'w') as f:
            f.write('# This file is needed to treat the directory as a package')
