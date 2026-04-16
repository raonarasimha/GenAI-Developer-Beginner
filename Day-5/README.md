# 🕒 Day 5: Working with Jupyter Notebook

🏁 **Goal**: Learn how to use Jupyter Notebook for interactive Python development and data exploration.

---

### ✅ 1. Introduction to Jupyter Notebook (10 mins)

* **Topics**:
    * What is Jupyter Notebook?
    * Key features and use cases
* **Summary**: Jupyter Notebook is an interactive environment for writing and running code, visualizing data, and documenting your workflow.
* **Prompt**: "Jupyter Notebooks are perfect for experimentation, visualization, and sharing code with explanations."
* **Example**: [See `01_introduction_to_jupyter_notebook.md`](./01_introduction_to_jupyter_notebook.md)
![Jupyter Notebook Logo](./assets/Jupyter%20Logo.svg)

---

### ✅ 2. Installing Jupyter Notebook (10 mins)

* **Topics**:
    * Installing via `pip`
    * Launching Jupyter Notebook
* **Summary**: Install Jupyter using pip and start the notebook server from your terminal.
* **Prompt**: "Use `pip install notebook` and run `jupyter notebook` to get started."
* **Example**:  
    [See `02_installing_jupyter_notebook.md`](./02_installing_jupyter_notebook.md)
    ```bash
    pip install notebook
    jupyter notebook
    ```
![Jupyter Install](./assets/Jupyter%20Install.svg)

---

### ✅ 3. Navigating the Jupyter Interface (10 mins)

* **Topics**:
    * Notebook dashboard
    * Creating and renaming notebooks
    * Saving and checkpointing
* **Summary**: Learn how to create, open, and manage notebooks from the Jupyter dashboard.
* **Prompt**: "The dashboard helps you organize and access your notebooks easily."
* **Example**: [See `03_navigating_jupyter_interface.md`](./03_navigating_jupyter_interface.md)
![Jupyter Dashboard](./assets/Jupyter%20Dashboard.svg)

---

### ✅ 4. Working with Cells (10 mins)

* **Topics**:
    * Code cells vs Markdown cells
    * Running cells (`Shift+Enter`)
    * Editing and adding cells
* **Summary**: Use code cells to run Python code and Markdown cells to add formatted text, headings, and explanations.
* **Prompt**: "Mix code and text to create rich, interactive documents."
* **Example**:  
    [Open `04_working_with_cells.ipynb`](./04_working_with_cells.ipynb)
    ```python
    # This is a code cell
    print("Hello, Jupyter!")
    ```
    ```markdown
    # This is a Markdown cell
    **Bold text**, *italic*, and `inline code`
    ```
![Jupyter Cells](./assets/Jupyter%20Cells.svg)

---

### ✅ 5. Importing Libraries and Visualizing Data (10 mins)

* **Topics**:
    * Importing libraries (e.g., numpy, pandas, matplotlib)
    * Displaying plots inline
* **Summary**: Import Python libraries and visualize data directly in your notebook.
* **Prompt**: "Use `%matplotlib inline` to show plots inside your notebook."
* **Example**:  
    [Open `05_importing_libraries_and_visualizing_data.ipynb`](./05_importing_libraries_and_visualizing_data.ipynb)
    ```python
    import matplotlib.pyplot as plt
    %matplotlib inline
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.show()
    ```
![Jupyter Visualization](./assets/Jupyter%20Visualization.svg)

---

### ✅ 6. Running Notebooks in VS Code with Virtual Environments (5 mins)

* **Topics**:
    * Setting up a virtual environment for Jupyter in VS Code
    * Selecting the correct Python interpreter/kernel
* **Summary**: Learn how to run Jupyter notebooks inside VS Code using a virtual environment for package isolation.
* **Prompt**: "Always select your virtual environment as the notebook kernel in VS Code."
* **Example**: [See `06_running_notebooks_in_vscode.md`](./06_running_notebooks_in_vscode.md)
![VS Code Notebook Kernel](./assets/VSCode%20Notebook%20Kernel.svg)

---

### ✅ 7. Exporting and Sharing Notebooks (5 mins)

* **Topics**:
    * Exporting to HTML, PDF, etc.
    * Sharing notebooks via GitHub or nbviewer
* **Summary**: Share your work by exporting notebooks or uploading them to version control platforms.
* **Prompt**: "Jupyter Notebooks are easy to share and review with others."
* **Example**: [See `07_exporting_and_sharing_notebooks.md`](./07_exporting_and_sharing_notebooks.md)
![Jupyter Export](./assets/Jupyter%20Export.svg)
