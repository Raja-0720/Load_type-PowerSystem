# Load_type-PowerSystem

In this project, a machine learning–based classification system was developed to predict the operating Load_Type of a power system using historical energy consumption, reactive power, environmental, and time-based features. The problem was formulated as a supervised multi-class classification task with three target categories: Light Load, Medium Load, and Maximum Load.

Comprehensive data preprocessing, exploratory data analysis, and feature engineering were performed to understand the underlying patterns and prepare the dataset for modeling. Time-based features such as Month and Hour were engineered to capture seasonal and daily variations in power usage, which significantly improved the learning capability of the models.

Two machine learning models were implemented: Logistic Regression as a baseline and Random Forest as the primary predictive model. Among them, the Random Forest classifier achieved superior performance due to its ability to model complex non-linear relationships present in power consumption data.

The developed model can assist power utility organizations in:
Optimizing energy generation and distribution,
Preventing system overload during peak demand,
Reducing energy wastage during low-demand periods,
Improving overall operational reliability.

Future Scope

The model can be further enhanced by:
Applying hyperparameter tuning,
Exploring advanced ensemble methods such as Gradient Boosting and XGBoost,
Integrating real-time sensor data for live load prediction.
