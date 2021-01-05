# Run me with . or source
# As part of automated installation!

conda env create -f environment.yml
conda activate mischiefdetector
conda uninstall --yes --force tensorflow
pip install tensorflow==2.0.0
