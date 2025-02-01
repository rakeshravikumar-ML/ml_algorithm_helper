def explain_step(step_choice):
    """
    Fetches and displays the explanation from the notebook for the selected step.
    """
    file_path = download_notebook()
    if not file_path:
        return
    
    step_headers = get_project_steps()
    selected_heading = step_headers.get(step_choice, None)

    if not selected_heading:
        print("Invalid step number. Try again.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        notebook_data = json.load(f)

    found_heading = False
    extracted_explanation = []

    for cell in notebook_data["cells"]:
        if cell["cell_type"] == "markdown":
            markdown_text = "".join(cell["source"]).strip()

            # ✅ Check if the markdown cell CONTAINS the step heading, not just starts with it
            if selected_heading in markdown_text:
                found_heading = True  # Start collecting text
                extracted_explanation.append(markdown_text)  # Include the header cell itself
                continue
            elif found_heading and markdown_text.startswith("## Step"):  # Stop at the next step heading
                break
            elif found_heading:
                extracted_explanation.append(markdown_text)  # Collect all markdown content

    print(f"\nStep Explanation: {selected_heading[3:]}\n")  # Display step title without "## "
    if extracted_explanation:
        print("\n".join(extracted_explanation))
    else:
        print("⚠️ No detailed explanation found in the notebook. Check the markdown formatting.")
