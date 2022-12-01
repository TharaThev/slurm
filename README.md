# slurm

Clone this repository and follow these steps to setup a basic environment for using PyTorch with Cuda in SLURM. This environment installs
- python (3.6)
- PyTorch with Cuda (11.6)
- NumPy

## 1. Allocate a node
Allocate a node and log in to that node.<br>
``` salloc --particiton=gpu-2080ti-interactive --gres=gpu:1  ```

## 2. Conda environment
Create the environemnt from the ```slurm_env.yml``` file. <br>
``` conda env create -f slurm_env.yml ``` <br> <br>
The name of this enviroment is ```slurm_env```. Use it to activate the new environment. <br>
```conda activate slurm_env``` <br><br>
Verfiy that the new environment was installed correctly with <br>
``` conda env list ```

## 3. Test the environment
Run ``` python test_env.py``` to the whether the installation was succefull. If the installation was not successfull, you will receive error messages.
