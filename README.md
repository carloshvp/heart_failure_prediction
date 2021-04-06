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

As part of the AutoML configuration, we are going to select:

- Problem type: Classification
- Experiment timeout: 20 minutes
- Maximum concurrent iterations: 4
- Primary metric: AUC weighted. This has been selected as we have seen that the dataset is imbalanced (203 cases in one class, versus 96 in the other class)
- k value for k-fold Validation: 5. We split the data in train-test with 80-20 proportion, which combined with 5 cross-validations, we cover the whole dataset
- Early stopping: enabled

### Results
*TODO*: What are the results I got with my automated ML model? What were the parameters of the model? How could I have improved it?

*TODO* Remember to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

SCREENSHOT OF RUNDETAILS


## Hyperparameter Tuning

For the Hyperdrive configuration we are selecting:

- Algorithm: Logistic regression with SKLearn
- Sampling method: random
- Hyperparameters to optimize: Regularization strength (C) and maximum number of iterations to converge (max_iter)
- Regularization strength (C): continuous range from 0.1 to 1.0 (lower values make stronger regularization)
- Maximum number of iterations to converge (max_iter): fixed values 50, 80, 100, 120 and 150
- Early termination policy: Bandit policy with slack factor of 0.1, evaluation interval of 3 and delay of evaluation of 3
- Metric to optimize: Accuracy
- Maximum total runs: 100

As we can see, the algorithm selected is Logistic regression, as the problem is a regression and Logistic regression, though simple, may do the job correctly in the relationships between the features and the output are lineal.

### Results
*TODO*: What are the results I got with my model? What were the parameters of the model? How could I have improved it?
The result of the Hyperparameter search with Hyperdrive resulted in an accuracy of 0.78333333.

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

From the 2 hyperparameters that we are optimizing, these are the found values by Hyperdrive:
- Regularization strength: 0.7052588371678538
- Maximum number of iterations to converve: 80

The Maximum number of iterations to converge values were sampled at will (choice), and could be improved if the value is set for the search as a range, where Hyperdrive has a wider search space.

PICTURE OF RUNDETAILS
PICTURE OF BEST MODEL


## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. The screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* If any...
