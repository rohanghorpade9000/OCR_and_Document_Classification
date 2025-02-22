import json

# Load predictions from JSON file
with open("../../data/predictions.json", "r") as file:
    predictions = json.load(file)

# Ground truth labels (actual classifications)
actual_classes = {
    "image_1_1.png": "Prescription",
    "image_2_1.png": "Discharge Summary",
    "image_3_1.png": "Cancelled Cheque",
    "image_4_1.png": "Pharmacy Bill",
    "image_5_1.png": "Pharmacy Bill",  # Expected class for image_5_1.png
    "image_6_1.png": "Bank Statement",
    "image_7_1.png": "Clinic payment Receipt",
    "image_8_1.png": "Lab Report"
}

# Calculate accuracy
correct_predictions = sum(1 for img, actual in actual_classes.items() if predictions.get(img) == actual)
total_documents = len(actual_classes)

accuracy = (correct_predictions / total_documents) * 100
print(f"Classification Accuracy: {accuracy:.2f}%")
