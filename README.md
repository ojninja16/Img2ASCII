# Image to ASCII Art Generator Using Neural Networks

This project aims to generate ASCII art representations of images using a neural network. The model processes grayscale image chunks and predicts corresponding ASCII characters for each chunk based on pixel intensity. The dataset consists of pairs of original grayscale images and their corresponding ASCII art images.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Requirements](#requirements)
- [Usage](#usage)
- [Future Improvements](#future-improvements)

## Overview

The primary goal of this project is to convert images into ASCII art using machine learning techniques. The neural network model takes image chunks (30x30 pixels) as input and predicts the corresponding ASCII character from a predefined character lookup table based on the average intensity of the chunk.

### Key Components:
- **Dataset**: The dataset contains original grayscale images and their corresponding ASCII art images.
- **Preprocessing**: Images are broken down into smaller chunks, and the pixel values are normalized to improve model performance.
- **Neural Network**: A custom neural network model predicts the most suitable ASCII character for each chunk.
- **Loss Function**: The model uses cross-entropy loss to optimize predictions during training.

## Dataset

The dataset consists of:

- Original grayscale images stored in the `data/original_images/` directory.
- Corresponding ASCII art images stored in the `data/ascii_art_images/` directory.

During preprocessing, each image is resized to a standard size of 360x360 pixels and split into 30x30 pixel chunks. Each chunk's intensity determines which ASCII character is used to represent it.

## Model Architecture

The model is a simple feedforward neural network with the following layers:

1. **Flatten Layer**: Converts the input 30x30 pixel image chunk into a 1D tensor.
2. **Fully Connected Layer 1**: A linear layer with 129,600 inputs and 900 outputs.
3. **ReLU Activation**: Introduces non-linearity after the first linear layer.
4. **Fully Connected Layer 2**: A linear layer with 900 inputs and 64 outputs.
5. **Fully Connected Layer 3**: Outputs 16 predictions, corresponding to the 16 possible ASCII characters in the lookup table.

## Training

- **Loss Function**: Cross-Entropy Loss is used to calculate the error between the predicted and actual ASCII characters.
- **Optimizer**: Stochastic Gradient Descent (SGD) is used for optimization with a learning rate of 0.01.

### Training Loop
The training process iterates over the dataset for 10 epochs. In each epoch, the model:

1. Retrieves image chunks and their corresponding ASCII labels.
2. Passes them through the network.
3. Calculates loss using Cross-Entropy Loss.
4. Updates the model weights via backpropagation.

## Requirements

To run the project, you need the following libraries:

- `torch`
- `torchvision`
- `opencv-python`
- `matplotlib`

You can install them using:

```bash
pip install torch torchvision opencv-python matplotlib
