import subprocess

# Run x.py
subprocess.run(['python', 'pip_lib_error_checker.py'])

# Prompt the user for input
user_input = input("Do you want to run fix the errors? (yes/no): ").lower()

if user_input == "yes":
    # Run y.py
    subprocess.run(['python', 'pip_lib_issue_solver.py'])
else:
    print("Exiting...")
