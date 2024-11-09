import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

'''
This Python script is a deep learning program using PyTorch to train and evaluate a neural network model on the FashionMNIST dataset. 

1. Dataset: The script uses FashionMNIST, a dataset consisting of 28x28 grayscale images of 10 fashion categories (e.g., T-shirt, Dress, Sneaker).
2. Model Architecture: A simple fully connected feed-forward neural network with 2 hidden layers using ReLU activation.
3. Training: The model is trained for 200 epochs using Stochastic Gradient Descent (SGD).
4. Testing: The model is evaluated for accuracy on the test dataset.
5. Model Saving and Loading: The model is saved after each epoch, and there is a function to load and test specific models.
'''
# Epochs for training
## !!!!!!!!! TIME consuming in full version
epochs = 200


# ToTensor: Converts images to PyTorch tensors, normalizing pixel values to the [0, 1] range.
# Download training and test data
training_data = datasets.FashionMNIST(root="data", train=True, download=True, transform=ToTensor())
test_data = datasets.FashionMNIST(root="data", train=False, download=True, transform=ToTensor())

# DataLoader: Allows iterating through the dataset in mini-batches of size 64.
# Create data loaders
batch_size = 64
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

# Device configuration
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")

'''
Architecture:
Flatten Layer: Converts 28x28 images into a 1D tensor of size 784.
Linear Layers: Two hidden layers of 512 neurons each.
Activation: Uses ReLU (Rectified Linear Unit).
Output Layer: Has 10 neurons for the 10 fashion categories.
'''
# Define model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork().to(device)
loss_fn = nn.CrossEntropyLoss()
#Optimizer: Stochastic Gradient Descent (SGD) with a learning rate of 0.001.
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

# Train function
def train(dataloader, model, loss_fn, optimizer):
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)
        pred = model(X)
        loss = loss_fn(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

# Test function
def test(dataloader, model, loss_fn):
    model.eval()
    correct = 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    accuracy = 100 * correct / len(dataloader.dataset)
    print(f"Accuracy: {accuracy:>0.1f}%")

# Save model function with epoch number
def save_model(model, epoch, path="model_epoch_{}.pth"):
    torch.save(model.state_dict(), path.format(epoch))
    print(f"Model saved for epoch {epoch}")


# Load model function with epoch number
def load_model(model, epoch, path="model_epoch_{}.pth"):
    model.load_state_dict(torch.load(path.format(epoch), weights_only=True))
    model.eval()
    print(f"Model loaded from epoch {epoch}")

# Training loop for multiple epochs
for epoch in range(epochs):
    print(f"Epoch {epoch + 1}/{epochs}")
    train(train_dataloader, model, loss_fn, optimizer)
    test(test_dataloader, model, loss_fn)
    save_model(model, epoch)  # Save the model after each epoch

print("Training complete!")



def test_models(load_epoch):
    global model
    model = NeuralNetwork().to(device)
    load_model(model, load_epoch)
    # Example prediction on test data
    classes = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
    correct, incorrect = 0, 0
    for n in range(len(test_data)):
        x, y = test_data[n][0], test_data[n][1]
        with torch.no_grad():
            x = x.to(device).unsqueeze(0)  # Add batch dimension to match model input
            pred = model(x)
            predicted = classes[pred.argmax(1).item()]  # Selects the max index along dimension 1
            actual = classes[y]  # Convert y to an integer for indexing
            # print(f'{n} Predicted: "{predicted}", Actual: "{actual}"')

            if predicted == actual:
                correct += 1
            else:
                incorrect += 1

    accuracy = correct / (correct + incorrect) * 100
    print(f"Prediction complete for model_epoch_{load_epoch}. "
          f"Correct predictions: {correct}, Incorrect predictions: {incorrect}")
    print(f"Accuracy: {accuracy:.2f}%")

    return load_epoch, accuracy  # Return epoch and accuracy

accuracy_results = []
epoch_numbers = []
# Load a specific model based on epoch (you can limit to some smaller number)
for load_epoch in range(1,100):
    epoch, accuracy = test_models(load_epoch)
    accuracy_results.append(accuracy)
    epoch_numbers.append(epoch)

plt.plot(epoch_numbers, accuracy_results, marker = 'o')
plt.title('Model Accuracy vs Epochs')
plt.xlabel('Epoch')
plt.ylabel('Accuracy (%)')
plt.grid(True)
plt.show()
