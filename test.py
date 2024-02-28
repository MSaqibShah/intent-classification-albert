import torch
from transformers import AlbertForSequenceClassification, AlbertTokenizer
from datasets import ClassLabel

# Load the saved model
model_path = "./model"
model = AlbertForSequenceClassification.from_pretrained(model_path)

# Load the tokenizer
tokenizer = AlbertTokenizer.from_pretrained("albert-base-v2")

# Input text for testing
input_text =  "I'm still undecided, but leaning towards yes."
label_classes = ["yes_intent", "no_intent", "maybe_intent"]


# Tokenize and convert to tensor
inputs = tokenizer(input_text, return_tensors="pt")

# Make inference
with torch.no_grad():
    outputs = model(**inputs)

# Get the predicted class
logits = outputs.logits
predicted_class = torch.argmax(logits, dim=1).item()

print(f"Predicted Class: {predicted_class}")

c2l = ClassLabel(num_classes=3, names=label_classes)


print(c2l.int2str(predicted_class))


