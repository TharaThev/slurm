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
  print("Cuda has been installed successuflly. You are using GPU.")
else:
  print("An error has occured. You are either using CPU or you had troubles installing Cuda.")

try:
  import numpy
  print("NumPy has been installed successfully.")
except:
  print("An error has occured while installing NumPy.")	
