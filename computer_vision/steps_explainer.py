import urllib.request
import os

# Define steps of the model-building process
def get_project_steps():
    return {
        1: "Load & preprocess dataset",
        2: "Define the model architecture",
        3: "Train the model",
        4: "Evaluate the model",
        5: "Make predictions",
        6: "Visualize results"
    }

# Show available steps
def show_project_steps():
    steps = get_project_steps()
    print("\nModel Development Steps:")
    for step, description in steps.items():
        print(f"{step}. {description}")

    step_choice = int(input("\nWhich step do you need help with? Enter the step number: "))
    return step_choice

# Show details for a specific step
def explain_step(step_choice):
    explanations = {
        1: "Data is preprocessed by resizing images, normalizing pixel values, and augmenting training images.",
        2: "The model is defined using Convolutional Neural Networks (CNNs) with layers such as Conv2D, MaxPooling, and Dense.",
        3: "The model is trained using a dataset, optimizing using Adam optimizer, and monitoring loss and accuracy.",
        4: "Evaluation is done using test data, calculating accuracy, loss, and confusion matrices.",
        5: "The model makes predictions on new images by passing them through the trained network.",
        6: "Results are visualized using confusion matrices, accuracy/loss plots, and sample predictions."
    }
    
    print("\nStep Explanation:")
    print(explanations.get(step_choice, "Invalid step. Please enter a valid number."))

# Fetch the code from your IPYNB file
def show_code_for_step(step_choice):
    file_path = "/content/07_food_vision_milestone_project_1.ipynb"

    if not os.path.exists(file_path):
        print("\nNotebook file not found. Make sure it is uploaded in Colab.")
        return

    # Define search patterns to extract code from notebook cells
    step_code = {
        1: "### Load and Preprocess Data",
        2: "### Define the Model",
        3: "### Train the Model",
        4: "### Evaluate the Model",
        5: "### Make Predictions",
        6: "### Visualize Results"
    }

    selected_heading = step_code.get(step_choice, None)

    if not selected_heading:
        print("Invalid step number. Try again.")
        return

    import json

    with open(file_path, "r", encoding="utf-8") as f:
        notebook_data = json.load(f)

    code_snippets = []

    for cell in notebook_data["cells"]:
        if cell["cell_type"] == "code":
            source_code = "".join(cell["source"])
            if selected_heading in source_code:
                code_snippets.append(source_code)

    if code_snippets:
        print(f"\nCode for Step {step_choice}:\n")
        print(code_snippets[0])
    else:
        print("\nNo relevant code found for this step.")
