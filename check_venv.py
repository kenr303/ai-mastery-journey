import sys
import os

print("=== Virtual Environment Check ===\n")

# Python executable path
print("Python executable:", sys.executable)

# Python version
print("Python version:", sys.version)

# Virtual environment info
venv_path = os.environ.get("VIRTUAL_ENV")
if venv_path:
    print("Virtual environment active at:", venv_path)
else:
    print("No virtual environment detected!")

# Installed libraries
try:
    import numpy
    import pandas
    import matplotlib
    print("\nInstalled libraries:")
    print("NumPy:", numpy.__file__)
    print("Pandas:", pandas.__file__)
    print("Matplotlib:", matplotlib.__file__)
except ImportError as e:
    print("\nSome libraries are missing:", e)