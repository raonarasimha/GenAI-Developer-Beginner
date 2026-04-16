# Workspace Setup Guide

This guide provides instructions for setting up a Python virtual environment. A virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

### 1. Create a Virtual Environment

Open your terminal or command prompt and navigate to the `Day-1` directory. Run the following command to create a virtual environment named `venv`:

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

*   **On Windows**:
    ```bash
    .\venv\Scripts\activate
    ```

*   **On macOS and Linux**:
    ```bash
    source venv/bin/activate
    ```

After activation, you will see `(venv)` at the beginning of your terminal prompt.

### 3. Install Packages

With the virtual environment active, you can install packages using `pip`. For example, to install the `requests` library, you would run:

```bash
pip install requests
```

### 4. Deactivate the Virtual Environment

When you are finished working, you can deactivate the environment by simply running:

```bash
deactivate
``` 