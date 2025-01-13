import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Preprocessing transformations
# 1. Convert images to tensors
# 2. Normalize pixel values to have mean 0.5 and std deviation 0.5
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Load MNIST dataset
# https://en.wikipedia.org/wiki/MNIST_database
# The MNIST database  is a large database of handwritten digits
# that is commonly used for training various image processing systems
train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)

# Create DataLoaders for batching and shuffling
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# Define a simple neural network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        # Fully connected layers
        self.fc1 = nn.Linear(28 * 28, 128)  # Input: 28x28 flattened image, Output: 128 neurons
        self.fc2 = nn.Linear(128, 64)       # Hidden layer: 128 -> 64 neurons
        self.fc3 = nn.Linear(64, 10)        # Output layer: 64 -> 10 neurons (digits 0-9)

    def forward(self, x):
        # Flatten input tensor to (batch_size, 28*28)
        x = x.view(-1, 28 * 28)
        # Apply ReLU activation to each layer
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)  # No activation for output layer (handled by loss function)
        return x

# Initialize the model
model = SimpleNN()

# Define loss function (CrossEntropyLoss for classification tasks)
criterion = nn.CrossEntropyLoss()

# Define optimizer (Adam optimizer with a learning rate of 0.001)
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training the model
num_epochs = 5
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0  # Track loss for the epoch

    for inputs, labels in train_loader:
        optimizer.zero_grad()  # Reset gradients
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()  # Backward pass
        optimizer.step()  # Update weights
        running_loss += loss.item()

    # Print average loss for the epoch
    print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {running_loss / len(train_loader):.4f}")

# Evaluate the model
model.eval()  # Set the model to evaluation mode
correct = 0
total = 0

with torch.no_grad():  # Disable gradient computation
    for inputs, labels in test_loader:
        outputs = model(inputs)  # Forward pass
        _, predicted = torch.max(outputs, 1)  # Get predicted class
        total += labels.size(0)  # Total number of samples
        correct += (predicted == labels).sum().item()  # Count correct predictions

# Print final accuracy
accuracy = 100 * correct / total
print(f"Test Accuracy: {accuracy:.2f}%")
