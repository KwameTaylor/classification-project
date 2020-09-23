## Codeup Classification Project

### Kwame Taylor, Darden Cohort

This is the repository where I will house the code for my Classification project.

This project will use statistical testing and classification to create 3 models that predict churn better than the baseline model, and see which of those 3 models is most accurate.

I will create an MVP and then iterate through the data science pipeline until I get to the evaluation stage, which I will only do once.

The deliverables are the following: telco-churn-classification-project.ipynb, README.md, predictions.csv, acquire.py, prepare.py, and a notebook walkthrough.

Data Dictionary:
churn: 0 = Customer has not churned, 1 = Customer has churned

contract_type: 0 = Month-to-Month, 2 = Yearly, 3 = Two Year

phone: 0 = No phone service, 1 = One or more phone lines

depend: 0 = No dependents, 1 = Customer has dependents

num_add_ons: Number of add-on services a customer has

is_male: 1 if customer is male, 0 = female

internet_type: 0 = No internet, 2 = DSL, 3 = Fiber Optic

monthly_charges: The customer's monthly bill

tenure: Tenure in months

tenure_yrs: Tenure in years

Hypothesises:
Churn is highest in month-to-month contracts.
Monthly charges is a driver of churn.
There is a significant difference in churn between cohorts identified by tenure.
There is a linear relationship between monthly charges and internet service type plus phone service type.