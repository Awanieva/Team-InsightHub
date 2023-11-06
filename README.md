# Team-InsightHub Premier Project

# Topic Here

## Introduction
In an era where quick meals are paramount, breakfast cereals stand out for their convenience. However, with this convenience comes a question of nutritional value, which varies greatly among different cereals. The US Food and Drug Administration (FDA) is amplifying efforts to educate consumers about nutritionally deficient options. The label "healthy" is not just a marketing term; it's a regulated claim that can only be used if the product meets specific nutritional criteria. Against the backdrop of heightened health consciousness and the crucial role of breakfast cereals in dietary patterns—particularly in underprivileged homes where food diversity is scant—our project seeks to navigate the cereal aisle effectively, ensuring food security and combating malnutrition.

## Objectives:
Analysis of nutritional content provided.
Predict ratings of cereals based on their nutritional makeup, providing a reliable guide for consumers.
Systematically categorize cereals into 'Healthy' and 'Unhealthy' groups based on established nutritional criteria.
Share insights from the analysis to enhance consumer understanding of cereal nutrition.


## Flow of Project:
Exploratory Data Analysis  --> Data Preprocessing --> Feature Engineering --> Model Selection & Training --> Evaluation & ValidationDeployment Strategy 


## Data Source:
The data set was taken from the Kaggle competition page - https://www.kaggle.com/datasets/crawford/80-cereals/data


## Feature Description
The dataset contains a list of 77 different cereals, their manufacturer, the measurement of food nutrients present, the display shelf, the weight of each serving, the number of cups per serving, and the ratings of each cereal. The description of the fields is as follows:

- name: Name of cereal
- mfr: Manufacturer of cereal
- A = American Hpme Food Products
- G = General Mills
- K = Kelloggs
- N = Nabisco
- P = Post
- Q = Quaker oats
- R = Ralston Purina
type:
- C = Cold
- H = Hot
- calories: calories per serving
- protein: grams of protein
- fat: grams of fat
- sodium: milligrams of sodium
- fiber: grams of dietary fiber
- carbo: grams of complex carbohydrates
- sugars: grams of sugars
- potass: milligrams of potassium
- vitamins: vitamins and minerals - 0, 25, 100, indicating the typical percentage of FDA recommended
- shelf: display shelf (1, 2, or 3, counting from the floor)
- weight: weight in ounces of one serving
- cups: number of cups in one serving
- rating: a rating of the cereals (Possibly from Consumer Reports)


## Modelling
We built different algorithms, such as

- Linear Regression
- Lasso Regression
- Ridge Regression
- And compared their metrics.

## Model selected for the project:
Ridge Regression


## Model Deployment:
Streamlit was used to deploy the model


## Model Development
https://github.com/Awanieva/Team-InsightHub/blob/main/Model%20Development.ipynb


## Exporatory Data Analysis



## Dashboard Link (POWER BI)


## Link to the documentation


## Link to Deployment Code
https://github.com/Awanieva/Team-InsightHub/blob/main/streamlitapp.py

## Link to the Presentation slide





