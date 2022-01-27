# `environment.yml` instructions

1. Run `conda env create -f environment.yml` to create the environment.
2. Run `source activate intel_timeseries` to activate the environment.
3. Now, to add this environment to the list of available environments you'll
see in your Jupyter notebook, run:
```
python -m ipykernel install --user --name intel_timeseries --display-name "Python (intel_timeseries)"
```
4. Now run `jupyter notebook` to start your notebook.
5. In your notebook, select "Kernel -> Change kernel" and select
"Python (intel_timeseries)" as your kernel.

Now you'll be able to use all the libraries you'll need to complete the exercises!
