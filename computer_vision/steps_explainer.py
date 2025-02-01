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
