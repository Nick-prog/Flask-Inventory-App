# Flask Inventory App

This project is an initial test for a potential future updated inventory information storage method.

A simple Flask application for managing and viewing an inventory list stored in an Excel sheet. The inventory can be loaded from a local file or a remote server.

## Usage Example

1. **Configure the Inventory Source**
    - Edit `config.py`.
    - For a local file:
      ```python
      EXCEL_FILE = 'Inventory List.xlsx'  # path to your local file
      DEBUG = True
      ```
    - For a remote file (hosted on a server with public access):
      ```python
      EXCEL_FILE = 'https://my-server.com/path/to/inventory.xlsx'
      DEBUG = True
      ```

2. **Install Dependencies**
    ```bash
    pip install flask pandas requests openpyxl
    ```

3. **Run the Application**
    ```bash
    python app.py
    ```

4. **Access the App**
    - Open your browser and navigate to `http://localhost:5000/`.
    - View, check out, or check in inventory items directly through the web UI.
