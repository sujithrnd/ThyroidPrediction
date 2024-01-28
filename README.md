## End To End ML Project

** created a environment**
conda create -p envci python==3.8
conda activate thyro/

** Install all necessary libraries**

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



**Design Training Validation**

![TRaining Validation](https://github.com/sujithrnd/ThyroidPrediction/blob/main/trainingValidation.png)

**Design deployment**
![Architecture](https://github.com/sujithrnd/ThyroidPrediction/assets/16643681/e7911203-82ab-436e-944d-78ce1b92b5e5)



**EC2 Instance**

![EC2 instance](https://github.com/sujithrnd/ThyroidPrediction/blob/main/EC2.png)

**ECR -Docker images**

![ECR  instance](https://github.com/sujithrnd/ThyroidPrediction/blob/main/ECR.png)

**CD/CI -Git -Action - Runner -Docker deployement to AWS ECR ,ECR to AWS EC2.**

![CD/CI Docker -ECr- EC2](https://github.com/sujithrnd/ThyroidPrediction/blob/main/Git_Action_Ecr_Docker_EC2_deployment.png)



