# python script to test the correct installation of the slurm environment

import sys

py_version = sys.version
print("This environment is using Pyhton " + py_version)

try:
  import torch
  print("PyTorch has been installed successfully.")
except:
  print("An error has occured while installing PyTorch.")

if torch.cuda.is_available():
  print("You are using GPU.")
else:
  print("You are using CPU.")

try:
  import numpy
  print("NumPy has been installed successfully.")
except:
  print("An error has occured while installing NumPy.")	
