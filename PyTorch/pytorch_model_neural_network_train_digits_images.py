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

# Convolutional Neural Network
class AdvancedCNN(nn.Module):
    def __init__(self):
        super(AdvancedCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)  # Output: 32x28x28
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)  # Output: 64x28x28
        self.pool = nn.MaxPool2d(2, 2) # Downsample by 2x: Output: 64x14x14
        self.dropout1 = nn.Dropout(0.25) # Dropout for regularization
        self.fc1 = nn.Linear(64 * 14 * 14, 128) # Fully connected layer
        self.dropout2 = nn.Dropout(0.5)
        self.fc2 = nn.Linear(128, 10) # Output layer

    def forward(self, x):
        x = torch.relu(self.conv1(x)) # First convolution + ReLU
        x = torch.relu(self.conv2(x)) # Second convolution + ReLU
        x = self.pool(x) # Pooling
        x = self.dropout1(x) # Dropout
        x = x.view(-1, 64 * 14 * 14) # Flatten the feature map
        x = torch.relu(self.fc1(x)) # Fully connected layer + ReLU
        x = self.dropout2(x) # Dropout
        x = self.fc2(x) # Output layer
        return x

# Training and Evaluation Function
def train_and_evaluate(model, model_name, num_epochs=5):
    # Define loss function (CrossEntropyLoss for classification tasks)
    criterion = nn.CrossEntropyLoss()
    # Define optimizer (Adam optimizer with a learning rate of 0.001)
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Training loop
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0 # Track loss for the epoch
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward() # Backward pass
            optimizer.step() # Update weights
            running_loss += loss.item()
        print(f"{model_name} - Epoch {epoch + 1}/{num_epochs}, Loss: {running_loss / len(train_loader):.4f}")

    # Evaluation
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad(): # Disable gradient computation
        for inputs, labels in test_loader:
            outputs = model(inputs) # forward pass
            _, predicted = torch.max(outputs, 1) # Get predicted class
            total += labels.size(0)
            correct += (predicted == labels).sum().item() # Count correct predictions
    accuracy = 100 * correct / total
    print(f"{model_name} Test Accuracy: {accuracy:.2f}%")
    return accuracy

# Main Execution
def main():
    print("Choose model(s) to train and evaluate:")
    print("1. Simple Neural Network")
    print("2. Advanced Convolutional Neural Network")
    print("3. Both")

    choice = int(input("Enter your choice (1/2/3): "))
    if choice == 1:
        print("\nTraining Simple Neural Network...\n")
        train_and_evaluate(SimpleNN(), "Simple Neural Network")
    elif choice == 2:
        print("\nTraining Advanced Convolutional Neural Network...\n")
        train_and_evaluate(AdvancedCNN(), "Advanced Convolutional Neural Network")
    elif choice == 3:
        print("\nTraining Simple Neural Network...\n")
        simple_acc = train_and_evaluate(SimpleNN(), "Simple Neural Network")
        print("\nTraining Advanced Convolutional Neural Network...\n")
        cnn_acc = train_and_evaluate(AdvancedCNN(), "Advanced Convolutional Neural Network")
        print(f"\nComparison: Simple NN Accuracy: {simple_acc:.2f}% vs CNN Accuracy: {cnn_acc:.2f}%")
    else:
        print("Invalid choice. Exiting.")

# Run the program
if __name__ == "__main__":
    main()

