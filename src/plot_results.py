import matplotlib.pyplot as plt

# Your actual training data from the terminal output
epochs = [1, 2, 3, 4, 5]
loss = [0.9146, 0.3095, 0.2662, 0.1579, 0.1488]

plt.figure(figsize=(8, 5))
plt.plot(epochs, loss, marker='o', linestyle='-', color='blue', linewidth=2)

plt.title('Baseline CNN Training Loss', fontsize=14)
plt.xlabel('Epoch', fontsize=12)
plt.ylabel('Cross-Entropy Loss', fontsize=12)
plt.xticks(epochs)
plt.grid(True, linestyle='--', alpha=0.7)

# Save the graph as an image to paste into your presentation
plt.tight_layout()
plt.savefig('training_loss_graph.png', dpi=300)
print("Graph saved as 'training_loss_graph.png'")
plt.show()