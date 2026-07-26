import torch
import torch.nn as nn
import torch.optim as optim
from dataset_setup import train_loader, val_loader

# 1. Define the Simple CNN Architecture
class SimpleBaselineCNN(nn.Module):
    def __init__(self):
        super(SimpleBaselineCNN, self).__init__()
        # Convolutional layers to extract features
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.relu = nn.ReLU()
        
        # Fully connected layers for classification (6 classes)
        self.fc1 = nn.Linear(64 * 28 * 28, 128)
        self.fc2 = nn.Linear(128, 6)

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x))) # 224x224 -> 112x112
        x = self.pool(self.relu(self.conv2(x))) # 112x112 -> 56x56
        x = self.pool(self.relu(self.conv3(x))) # 56x56 -> 28x28
        x = x.view(-1, 64 * 28 * 28)            # Flatten the image
        x = self.relu(self.fc1(x))
        x = self.fc2(x)                         # Output 6 classes
        return x

# 2. Setup the Model, Loss Function, and Optimizer
model = SimpleBaselineCNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 3. Train the Model (for 5 epochs just to get baseline results)
epochs = 5
print("\n--- Starting Training ---")

for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    
    for images, labels in train_loader:
        optimizer.zero_grad()       # Clear old gradients
        outputs = model(images)     # Forward pass
        loss = criterion(outputs, labels) # Calculate error
        loss.backward()             # Backpropagation
        optimizer.step()            # Update weights
        
        running_loss += loss.item()
        
    print(f"Epoch {epoch+1}/{epochs} - Loss: {running_loss/len(train_loader):.4f}")

# 4. Quick Validation Check
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for images, labels in val_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total
print("\n--- Training Complete ---")
print(f"Baseline Validation Accuracy: {accuracy:.2f}%")