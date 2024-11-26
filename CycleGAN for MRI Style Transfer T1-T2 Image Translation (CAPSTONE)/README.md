# CycleGAN for MRI Style Transfer: T1-T2 Image Translation

## Project Overview
This deep learning project implements a CycleGAN (Generative Adversarial Network) architecture to perform style transfer between T1 and T2 weighted MRI images. The model helps radiologists by generating artificial MRI images of different contrast levels from existing scans, potentially improving diagnostic accuracy without additional scanning costs.

## Problem Statement
Medical imaging diagnosis faces challenges due to:
- High misdiagnosis rates
- Need for multiple contrast variations
- Cost and accessibility of multiple MRI scans
- Complexity in interpretation

## Solution Approach
The project uses CycleGAN with modified U-Net architecture to:
- Transform T1 weighted images to T2 weighted images and vice-versa
- Work with unpaired image datasets
- Maintain structural integrity while changing contrast styles
- Generate high-quality synthetic MRI images

## Technical Architecture

### Model Components
1. **Generators**
   - Modified U-Net architecture
   - T1 to T2 generator
   - T2 to T1 generator

2. **Discriminators**
   - T1 image discriminator
   - T2 image discriminator

### Loss Functions
- Adversarial Loss
- Cycle Consistency Loss
- Identity Loss

## Project Pipeline

### 1. Data Understanding
- Dataset structure analysis
- Image loading and preprocessing
- Data validation and quality checks

### 2. Image Processing
- Image normalization
- Resizing and standardization
- Data augmentation
- Input pipeline optimization

### 3. Model Building
- Generator architecture implementation
- Discriminator network design
- Loss function implementation
- Training loop creation

### 4. Training and Validation
- Model training
- Performance monitoring
- Result visualization
- Quality assessment

## Dataset
- Unpaired T1 and T2 weighted MRI images
- Images are not directly corresponding
- Suitable for CycleGAN training approach

## Implementation Details

### Dependencies
```
tensorflow>=2.0.0
numpy
matplotlib
opencv-python
```

## Visualization
The notebook includes visualizations of:
- Original T1/T2 images (DATASET)
- Generated synthetic images
- Comparison analyses
- Training progress

## Authors
QAZI NOORUL MATEEN
