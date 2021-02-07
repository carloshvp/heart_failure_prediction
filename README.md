# Predicting Heart Failure

Cardiovascular diseases are behind the death of approximately 18 million people every year. They mainly exhibit as myocardial infarctions and heart failures. Heart failure (HF) occurs when the heart cannot pump enough blood to meet the needs of the body.

If Heart Failure could be predicted with relatively high accuracy, the patient could receive preventive treatment before the actual event happens. In this project, we have used Azure ML for training several predictive models to achieve the desired target.

## Dataset

### Overview
The dataset we are using was obtained from the publication "Machine learning can predict survival of patients with heart failure from serum creatinine and ejection fraction alone". Davide Chicco, Giuseppe Jurman. BMC Medical Informatics and Decision Making 20, 16 (2020). ([link](https://doi.org/10.1186/s12911-020-1023-5))

The dataset contains the medical records of 299 heart failure patients collected at the Faisalabad Institute of Cardiology and at the Allied Hospital in Faisalabad (Punjab, Pakistan), during April–December 2015. The patients consisted of 105 women and 194 men, and their ages range between 40 and 95 years old. All 299 patients had left ventricular systolic dysfunction and
had previous heart failures that put them in classes III or IV of New York Heart Association (NYHA) classification of the stages of heart failure.

### Task
In the dataset we can find 12 features that can be used to predict heart failure mortality:
* age
* anemia (Decrease of red blood cells or hemoglobin
* creatinine_phosphokinase (Level of the CPK enzyme in the blood)
* diabetes (If the patient has diabetes)
* ejection_fraction (Percentage of blood leaving the heart at each contraction)
* high_blood_pressure (If the patient has hypertension)
* platelets (Platelets in the blood measured in kiloplatelets/mL)
* serum_creatinine (Level of serum creatinine in the blood measured in mg/dL)
* serum_sodium (Level of serum sodium in the blood measured in mEq/L)
* sex (Woman or man)
* smoking (If the patient smokes or not)
* time (Follow-up period in days)
* DEATH_EVENT (If the patient deceased during the follow-up period)

The target variable is DEATH_EVENT.

### Access
*TODO*: Explain how I am accessing the data in my workspace.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration I used for this experiment

### Results
*TODO*: What are the results I got with my automated ML model? What were the parameters of the model? How could I have improved it?

*TODO* Remember to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did I choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results I got with my model? What were the parameters of the model? How could I have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. The screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* If any...
