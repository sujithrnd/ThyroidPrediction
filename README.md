## End To End ML Project

### created a environment
conda create -p envci python==3.8
conda activate thyro/
```
### Install all necessary libraries
```
conda deactivate
pip install -r requirements.txt

conda info
conda deactivate
conda remove --name ENV_NAME --all

### Execution path
python src/pipeline/training_pipeline.py
python src/pipeline/prediction_pipeline.py
python application.py

Flask url http://127.0.0.1:9999/


