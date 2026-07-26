import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import os

# Define the paths to the specific image folders
train_dir = '../dataset/train/images' # Adjust if your script is not inside a 'src' folder
val_dir = '../dataset/validation/images'

# 1. Define the transformations: Resize to 224x224 and Normalize pixels
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# 2. Load the datasets using PyTorch's ImageFolder
print("Loading datasets...")
train_dataset = datasets.ImageFolder(root=train_dir, transform=transform)
val_dataset = datasets.ImageFolder(root=val_dir, transform=transform)

# 3. Create DataLoaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# Print out the stats for your Presentation (Slides 2 & 3)
print("-" * 30)
print(f"Total training images: {len(train_dataset)}")
print(f"Total validation images: {len(val_dataset)}")
print(f"Classes mapped: {train_dataset.classes}")
print("-" * 30)
print("Preprocessing pipeline is ready!")