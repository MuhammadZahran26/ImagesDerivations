import cv2
import numpy as np
from scipy.ndimage import convolve

class ImageDerivatives:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise ValueError("Image not found or unable to read.")
    
        # Convert to grayscale if the image is in color
        if len(self.image.shape) == 3:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def apply_gaussian_filter(self, sigma=1):
        """Applies a Gaussian filter to the image."""
        size = int(2 * (3 * sigma) + 1)
        x, y = np.meshgrid(np.linspace(-size//2, size//2, size), np.linspace(-size//2, size//2, size))
        gaussian_filter = np.exp(-(x**2 + y**2) / (2 * sigma**2))
        gaussian_filter /= gaussian_filter.sum()  # Normalize
        return convolve(self.image, gaussian_filter)

    def zero_order_derivative(self):
        """Applies Gaussian smoothing (zero-order derivative)."""
        return self.apply_gaussian_filter()

    def first_order_derivative(self):
        """Calculates the first-order derivative (gradient magnitude) using Sobel filters."""
        # Define Sobel kernels for x and y directions
        sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        
        # Apply Gaussian filter before differentiation
        smoothed_image = self.apply_gaussian_filter()
        
        # Compute gradients
        grad_x = convolve(smoothed_image, sobel_x)
        grad_y = convolve(smoothed_image, sobel_y)
        
        # Gradient magnitude
        grad_magnitude = np.sqrt(grad_x**2 + grad_y**2)
        
        # Normalize to 0-255
        grad_magnitude = (grad_magnitude / grad_magnitude.max()) * 255
        return grad_magnitude.astype(np.uint8)

    def second_order_derivative(self):
        """Calculates the second-order derivative (Laplacian)."""
        # Define Laplacian kernel
        laplacian_kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
        
        # Apply Gaussian filter before applying Laplacian
        smoothed_image = self.apply_gaussian_filter()
        
        # Compute Laplacian
        laplacian = convolve(smoothed_image, laplacian_kernel)
        
        # Normalize to 0-255
        laplacian = (laplacian - laplacian.min()) / (laplacian.max() - laplacian.min()) * 255
        return laplacian.astype(np.uint8)
