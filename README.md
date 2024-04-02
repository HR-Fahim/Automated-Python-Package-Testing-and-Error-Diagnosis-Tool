# About

This repository contains code to identify and resolve error-prone Python packages installed via pip. By running the provided script, users can quickly detect which packages are causing import errors and seamlessly uninstall them to maintain a stable development environment.

# How to Run

## Execute the scripts sequentially:

   - Run `run.py` script:

     ```bash
     python run.py
     ```

   - Follow the prompt to decide whether to fixer code.

     ```bash
     Do you want to run fix the errors? (yes/no): 
     ```

     - If you choose "yes", issue fixer code will be executed.
     - If you choose "no" or any other input, the program will exit.

# Benefits

- **Error Detection**: Quickly identifies Python packages causing import errors, streamlining the debugging process.
- **Efficient Troubleshooting**: Facilitates the rapid resolution of errors by providing a clear list of problematic packages.
- **Maintaining Stability**: Ensures a stable development environment by enabling the removal of error-prone packages with ease.