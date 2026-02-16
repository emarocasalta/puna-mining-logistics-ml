Mining Logistics Perfomance: Puna Region Optimization.

This project implements a comprehensive Machine Learning and Business Intelligence solutions to predict arrival times
and optimize logistics dispatches in the Puna region (Salta, Argentina), a high mountain enviroment with extreme weather
conditions.

Link to dashboard in Tableau Public:

https://public.tableau.com/views/MiningLogisticsPerformance-PunaRegion/MiningLogisticsPerformance-PunaRegion?:language=es-ES&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

Context of the Problem.

Mining logistics in the Puna faces unique challenges: altitudes above 4000 meters above sea level, unpaved routes and climatic
phenomena such as the "White Wind". A delay not only impacts the supply chain, but results in an estimated operating cost of
$500 per hour.

This project seeks:
Predict the ETA (Estimated Time of Arrival) with high precisión using hybrid models.
Quantify the economic risk of each office.
Visualize geographic and climatic bottlenecks.

Technologies Used.

Language: Python (Pandas, NumPy).
Machine Learning: Scikit-Learn (Stacking Regressor), XGBoost, RandomForest.
Data Visualization: Seaborn, Matplotlib.
App/Deployment: Streamlit.
BI: Tableau Public.

Analysis and Key Results.

Climate Impact.

The analysis revealed that weather is the determining factor in delays. While in clear conditions the weather is stable,
the White Wind increases the variance and actual travel time by more than 150%.

2. The Effect of Altitude and Load.

A direct correlation was identified between destination altitude and fuel consumption, intensified by cargo tonnage. Mines
above 3500 meters above sea level present the greatest risks of "Critical Delay".

3. Feature Importance.

Using the coefficients of the XGBoost model, we determined that the weather state (weather_clear, weather_white_wind) and
distance are the variables with the greatest predictive weight, displacing the driver's experience of the type of unit.

Machine Learning Model.

A Stacking Regressor was implemented to maximize precisión:
Base Models: RandomForestRegressor and XGBoostRegressor.
Meta-Model: RidgeCV.
Perfomance: The model manages to capture the non-linear complexity of weather and altitude delays.

App: Mining Dispatch Optimizer.

An interactive app was developed with Streamlit that works as a decisión-making tool for logistics coordinators.

Functionalities:
ETA calculation in real time according to route and weather.
Estimation of risk cost in USD.
Traffic light system to authorize or delay dispatches.

Repository Structure.

"dataset_artificial_data.ipynb": Synthetic dataset generation script (20000 records).
"project_logistics_mining.ipynb": Exploratory analysis and model training.
"app.py": Streamlit application code.
"mining_logistics_model.joblib": Trained model in .joblib format.
"coordinate.csv", "data_tableau.csv", "mining_logistics.csv": Datasets generated for training and Tableau.

Execution Instructions.

Clone the repository.
install dependencies: pip install -r requirements.txt.
Run the Streamlit app: 
	python -m streamlit run app.py

Author: Emanuel Roca
LinkedIn: www.linkedin.com/in/emanuel-roca-2bb525159 