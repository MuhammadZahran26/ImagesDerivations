# Image Derivatives Project

This project implements different types of image derivatives (Zero-Order, First-Order, and Second-Order) using Python. Each derivative operation helps highlight specific aspects of the image, such as smoothness or edges, useful in various computer vision tasks.

## Overview

- **Zero-Order Derivative**: Gaussian smoothing to reduce noise.
- **First-Order Derivative**: Gradient magnitude, highlights edges.
- **Second-Order Derivative**: Laplacian, detects intensity changes.

## Prerequisites

This code is implemented without OpenCV and uses custom Python functions to apply Gaussian filtering, Sobel gradient calculation, and Laplacian filtering.

## Formulas and Explanations

### 1. Gaussian Filter (Zero-Order Derivative)

Gaussian smoothing is used to blur the image and reduce noise. This is achieved using the following Gaussian function:

\[
G(x, y, \sigma) = \frac{1}{2 \pi \sigma^2} e^{-\frac{x^2 + y^2}{2 \sigma^2}}
\]

where:
- \( \sigma \) is the standard deviation, controlling the blur amount.
- \( x \) and \( y \) represent pixel positions.

### 2. First-Order Derivative (Gradient Magnitude)

The gradient magnitude of an image detects edges by calculating the rate of intensity change. Using the Sobel operator, we calculate gradients in the x and y directions as follows:

\[
G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}, \quad
G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}
\]

The gradient magnitude \( M \) at each pixel is then given by:

\[
M = \sqrt{G_x^2 + G_y^2}
\]

### 3. Second-Order Derivative (Laplacian)

The Laplacian operator emphasizes areas of rapid intensity change, highlighting edges and corners. The Laplacian kernel is given by:

\[
L = \begin{bmatrix} 0 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 0 \end{bmatrix}
\]

This operation provides the second-order derivative, highlighting changes in the gradient.

## Results

Here are the outputs for each derivative type:

### Zero-Order Derivative (Gaussian Smoothing)

![Zero-Order Derivative (Gaussian Smoothing)](zero-order-derivative.jpg)

### First-Order Derivative (Gradient Magnitude)

![First-Order Derivative (Gradient Magnitude)](first-order-derivative.jpg)

### Second-Order Derivative (Laplacian)

![Second-Order Derivative (Laplacian)](second-order-derivative.jpg)

## Usage

1. Clone this repository and navigate to the project directory.
2. Load an image, and execute the Python code provided to observe the results of each derivative.

## How to Interpret the Results

- **Zero-Order (Gaussian Smoothing)**: Smooths the image by reducing high-frequency noise, making it useful for initial noise reduction.
- **First-Order (Gradient Magnitude)**: Highlights edges by identifying points where pixel intensity changes significantly, useful for edge detection.
- **Second-Order (Laplacian)**: Detects regions with rapid intensity changes, especially useful in identifying edges and corners.

## Applications

These techniques are foundational in image processing and computer vision applications, including:
- **Edge Detection**: Finding boundaries within images.
- **Image Smoothing**: Reducing noise for preprocessing.
- **Feature Detection**: Recognizing important structural elements.

## License

This project is open-source and available for educational purposes.

---

For additional details and to view the source code, please refer to the individual Python files in this repository.
