# 6. Running Notebooks in VS Code with Virtual Environments

## Steps

1. **Create and activate a virtual environment** (if not already done):
    ```bash
    python -m venv .venv
    # On Windows:
    .venv\Scripts\activate
    # On Mac/Linux:
    source .venv/bin/activate
    ```

2. **Install Jupyter in your virtual environment**:
    ```bash
    pip install notebook
    ```

3. **Open VS Code in your project folder**.

4. **Open or create a `.ipynb` notebook file**.

5. **Select the correct Python interpreter**:
    - Click the kernel name (top right of the notebook editor).
    - Choose the interpreter from your `.venv` (it should match your virtual environment path).

6. **Run notebook cells** using the play/run button or `Shift+Enter`.

## Tips

- If you don't see your virtual environment, reload VS Code or run `Python: Select Interpreter` from the Command Palette.
- Installing additional packages? Always do it inside your virtual environment.

**Reference:** [VS Code Jupyter Notebooks Docs](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
