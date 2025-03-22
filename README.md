## End To End Thyroid Disease Prediction ML Project (Git -Action -Runner -Docker -AWS ECR - AWS EC2)
Linkedin : https://www.linkedin.com/posts/sujith-ks-1447b218_datascience-artificialintelligence-kaggle-activity-7156404662869364736-SKXL?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAOtXUQBZi70f8GWkrU83hpfD457TpxhrrU

# Thyroid Disease Prediction Project

This project aims to develop a machine learning model capable of predicting thyroid disease based on patient medical data. It utilizes a dataset containing various attributes related to thyroid function and patient demographics to train and evaluate predictive models.

## Project Overview

* **Objective:** To build a reliable and accurate model for predicting thyroid disease.
* **Dataset:** [Specify the dataset used, e.g., UCI Thyroid Disease Dataset, or a custom dataset]
* **Methods:** We explored various machine learning algorithms, including [List algorithms used, e.g., Logistic Regression, Random Forest, Gradient Boosting, Support Vector Machines].
* **Tools:** Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn.
* **Evaluation:** Model performance was evaluated using metrics such as accuracy, precision, recall, F1-score, and AUC-ROC.

## Project Structure - Design Training Validation

![TRaining Validation](https://github.com/sujithrnd/ThyroidPrediction/blob/main/trainingValidation.png)

**Design deployment**
![Architecture](https://github.com/sujithrnd/ThyroidPrediction/assets/16643681/e7911203-82ab-436e-944d-78ce1b92b5e5)



**EC2 Instance**

![EC2 instance](https://github.com/sujithrnd/ThyroidPrediction/blob/main/EC2.png)

**ECR -Docker images**

![ECR  instance](https://github.com/sujithrnd/ThyroidPrediction/blob/main/ECR.png)

**CD/CI -Git -Action - Runner -Docker deployement to AWS ECR ,ECR to AWS EC2.**

![CD/CI Docker -ECr- EC2](https://github.com/sujithrnd/ThyroidPrediction/blob/main/Git_Action_Ecr_Docker_EC2_deployment.png)

![image](https://github.com/user-attachments/assets/941da9ed-7ebf-439f-8259-df4703980bf5)





Environemnent Createion
conda create -p envci python==3.8
conda activate thyro/

Install Libraries

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
AWS EC2 URl - http://ec2-18-232-57-65.compute-1.amazonaws.com:9999/predict

Create user in aws & download the  Acceskey csv file - sujith_accessKeys.csv
Create ECR - Note down the  repo name and  UI
Create EC2 instance
sudo apt-get update -y
sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
EC2 instance>security group>Inboundconnection - add ‘Custome TCP with app port in app.py
Configure EC2 as self-hosted runner:Github>Actions>Runners>SelfHostedRunner>Exe commands from here  there in EC2


Setup github secrets in Github>Security>Cred as per the aws.yml in workflow in GitHub>Actuins>Runners>selfhostedrunner:
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION = us-east-1
AWS_ECR_LOGIN_URI = demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com
ECR_REPOSITORY_NAME = simple-app





