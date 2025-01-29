# PythonCalculator
A shunting yard and RPN calculator made in python with gui. 

Added How to document for operation.


HowTo_Firstname_Lastname.txt
## Description
This file provides instructions on how to run the Python-based GUI calculator application using the command line (CLI). The calculator can evaluate arithmetic, trigonometric, and logarithmic expressions with operator precedence and proper error checking.

## Prerequisites
1. **Python Installed**: Ensure that Python 3.x is installed on your system. You can check your Python version by running:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

2. **Tkinter Installed**: Tkinter is part of the standard Python library. If it's not installed, you can install it by running:
   ```bash
   sudo apt-get install python3-tk  # For Linux (Ubuntu/Debian)
   ```
   or
   ```bash
   brew install python-tk          # For macOS
   ```

## Files Required
1. `calculator.py`: The Python script containing the calculator code.
2. Any additional dependencies (none are required beyond the standard Python libraries).

## Running the Calculator
1. Open your terminal or command prompt.
2. Navigate to the directory containing the `calculator.py` file. For example:
   ```bash
   cd /path/to/your/code
   ```
3. Run the script using Python. Use the appropriate Python command depending on your system:
   - For Python 3:
     ```bash
     python3 calculator.py
     ```
   - For default Python:
     ```bash
     python calculator.py
     ```

4. The graphical user interface (GUI) of the calculator will launch. Use the buttons on the interface to input your expressions and perform calculations.

## Exiting the GUI Application
- To exit the calculator, click the **close button (X)** in the top-right corner of the GUI window.
- Alternatively, you can use the following keyboard shortcuts depending on your operating system:
  - **Windows/Linux**: `Alt + F4`
  - **macOS**: `Cmd + Q`

The terminal will return to the command prompt once the application closes.

## Example Usage
### Launching the Calculator
1. Run the command:
   ```bash
   python3 calculator.py
   ```

2. The calculator GUI will appear.

### Performing Calculations
- Enter expressions using the on-screen buttons.
- Example valid expressions:
  - `-5.78+-(4-2.23)+sin(0)*cos(1)/(1+tan(2*ln(-3+2*(1.23+99.111))))`
  - `(4+5) * (10 / 2)`
- Press `=` to compute the result.
- Use `C` to clear the current input.

## Common Errors
1. **Python Not Found**:
   - If the terminal says `command not found: python`, try `python3`.
   - Ensure Python is installed and added to your PATH.
2. **Missing Tkinter**:
   - If an error mentions `tkinter` is missing, install it as described in the prerequisites section.
3. **Invalid Characters**:
   - If you enter invalid characters in the calculator, an error message will pop up explaining the issue.

## Notes
- This application does not run entirely in the CLI but launches a graphical interface for user interaction.
- Ensure your Python environment includes the required standard libraries (`math` and `tkinter`).
