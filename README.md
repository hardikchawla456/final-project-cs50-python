
# Food Ordering System

## Description

A Python-based food ordering system that allows users to:
- Display a menu with items and prices.
- Place orders by selecting items from the menu.
- View an order summary, including a total cost.

This project also includes unit tests to ensure its functionality and reliability.

---

## Project Structure

```
.
├── main.py              # Main application code
├── test_main.py         # Unit tests for the application
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

---

## How to Install

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install Python**:
   Ensure Python 3.7 or later is installed on your system. Verify the installation by running:
   ```bash
   python --version
   ```

3. **Install Dependencies**:
   Use `pip` to install the dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run

1. **Run the Main Application**:
   Navigate to the directory containing `main.py` and execute:
   ```bash
   python main.py
   ```

2. **Interact with the Program**:
   The program will display a menu with options:
   - Display Menu
   - Take Order
   - Display Order
   - Exit

   Enter the corresponding number to interact with the system.

---

## How to Run Tests

1. **Run All Tests**:
   Navigate to the directory containing `test_main.py` and execute:
   ```bash
   pytest
   ```

2. **Check the Output**:
   If all tests pass, you will see output similar to:
   ```
   =================== test session starts =====================
   collected 3 items

   test_main.py ...                                       [100%]

   ==================== 3 passed in 0.02s =====================
   ```

---

## Tested Environments

- **Python Version**: Python 3.7, Python 3.9, Python 3.10
- **Test Framework**: `pytest`

---

## Dependencies

- `pytest`: For running unit tests. Install it via `pip install pytest`.

---

## License

This project is open-source and free to use under the MIT License.
