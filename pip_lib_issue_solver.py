import subprocess
import re

error_pattern = re.compile(r"ERROR: could not import (\S+)")

# Run the script and capture the output
result = subprocess.run(['python', 'pip_lib_error_tester.py'], capture_output=True, text=True)

# Extract the names of packages causing errors
error_packages = error_pattern.findall(result.stdout)

# Uninstall error-causing packages
for package in error_packages:
    subprocess.run(['pip', 'uninstall', package])
