import urllib.request
import os
import json

# GitHub raw file URL for the notebook
GITHUB_NOTEBOOK_URL = "https://raw.githubusercontent.com/rakeshravikumar-ML/ml_algorithm_helper/main/computer_vision/07_food_vision_milestone_project_1.ipynb"

def download_notebook():
    """
    Downloads the notebook from GitHub if it is not already available in Colab.
    """
    notebook_path = "/content/07_food_vision_milestone_project_1.ipynb"

    if not os.path.exists(notebook_path):
        print("\nDownloading notebook from GitHub...")
        urllib.request.urlretrieve(GITHUB_NOTEBOOK_URL, notebook_path)
        print("Download complete!")

    return notebook_path

def get_project_steps():
    """
    Returns a dictionary of model development steps.
    """
    return {
        1: "Load & preprocess dataset",
        2: "Define the model architecture",
        3: "Train the model",
        4: "Evaluate the model",
        5: "Make predictions",
        6: "Visualize results"
    }

def show_project_steps():
    """
    Displays the available model development steps and asks the user to select one.
    """
    steps = get_project_steps()
    print("\nModel Development Steps:")
    for step, description in steps.items():
        print(f"{step}. {description}")

    step_choice = int(input("\nWhich step do you need help with? Enter the step number: "))
    return step_choice

def explain_step(step_choice):
    """
    Provides an explanation of the selected model development step.
    """
    explanations = {
        1: "Data preprocessing includes resizing images, normalizing pixel values, and augmenting training data.",
        2: "The model architecture is defined using Convolutional Neural Networks (CNNs), including Conv2D, MaxPooling, and Dense layers.",
        3: "Model training is done using an optimizer (Adam), loss function (cross-entropy), and monitored using accuracy/loss metrics.",
        4: "Evaluation is performed using a test dataset, calculating metrics such as accuracy and loss.",
        5: "Predictions are made using the trained model on new input images.",
        6: "Results are visualized using loss/accuracy plots, confusion matrices, and sample predictions."
    }

    print("\nStep Explanation:")
    print(explanations.get(step_choice, "Invalid step. Please enter a valid number."))

def show_code_for_step(step_choice):
    """
    Fetches and displays relevant code from the notebook based on the selected step.
    """
    file_path = download_notebook()  # Ensure the notebook is available

    # Define search patterns for extracting code
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
