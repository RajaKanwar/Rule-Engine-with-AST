
### Rule Engine with AST

## Overview
Develop a simple 3-tier rule engine application(Simple UI, API and Backend, Data) to determine
user eligibility based on attributes like age, department, income, spend etc.The system can use
Abstract Syntax Tree (AST) to represent conditional rules and allow for dynamic
creation,combination, and modification of these rules.

## 🔗 Links
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RajaKanwar/Rule-Engine-with-AST.git)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raja-kanwar)


## Features

- Create rules with a unique ID and a defined structure.
- Evaluate rules based on user-provided data.
- Combine multiple rules into a single logical expression.
- Basic validation of rule syntax.

## Technologies Used
- Python 3.x
- Django 3.x or later
- PostgreSQL (or any other preferred database)

## Node Types
- Operator: Represents logical operators such as AND/OR.
- Operand: Represents conditions, e.g., comparisons like age > 30.

## Configure Database
- Update the database settings in settings.py to match your PostgreSQL configuration.
- Run the following commands to create the database tables:
bash
Copy code
```
python manage.py makemigrations
python manage.py migrate
```
- Run the Development Server
bash
Copy code
```
python manage.py runserver
```
Access the application at http://127.0.0.1:8000/rules/create/.
## Usage
### Creating a Rule

- Navigate to the Create Rule page.
- Enter a unique Rule ID and a rule string following the defined syntax.
- Click Create Rule to save the rule.

### Evaluating a Rule
- Navigate to the Evaluate Rule page.
- Provide the Rule ID and user data in dictionary format (e.g., {"age": 30}).
- Submit the form to evaluate the rule against the provided user data.

### Combining Rules
Daily Weather Summary:

- Navigate to the Combine Rules page (this feature can be added later based on user requirements).
- Select multiple rules to combine them into a single logical expression.


## Code Structure
- *ast.py* : Contains the logic for creating, evaluating, and combining rules.
- *views.py* : Handles user requests and interacts with the models to perform actions.
- *urls.py*: Defines the URL routes for the application.
- *templates/rules/*: Contains HTML templates for the views.

### Visualizations
- Implement visualizations to display daily weather summaries, historical trends, and triggered alerts.

## Screenshots

![Create rule](https://drive.google.com/file/d/139O49f_4z_JOFU_IlABt-IVOsOO3jghQ/view?usp=sharing)

![Evaluate rule](https://drive.google.com/file/d/1lAndPhENytsVtSEWFDF_Qdmx-eAFjVpv/view?usp=sharing)

![Combine rule](https://drive.google.com/file/d/1TciEYR_zI-ljnzulmx-9D21VHl68ZkJg/view?usp=sharing)

