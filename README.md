# Crop Recommendation System

## Project Overview
The Crop Recommendation System is a machine learning-based application that assists farmers by suggesting the most suitable crops to grow based on various factors like soil type, weather conditions, geographical location, and other environmental factors. This system aims to help farmers improve their crop yield by making data-driven decisions.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Model](#model)
- [Data](#data)
- [Contributing](#contributing)

## Technologies Used
- **Programming Language**: Python
- **Libraries/Frameworks**:
  - Pandas
  - Scikit-learn
  - NumPy
  - Flask (for the web application)
  - Matplotlib/Seaborn (for data visualization)
  - Jupyter Notebook (for prototyping and development)


## Features
- **Crop Recommendations**: Suggests the best crops to plant based on user input..
- **User-Friendly Interface**: (If applicable) An easy-to-use front-end that allows farmers to input data and receive crop suggestions.
- **Data Visualization**: Visualizes key data and recommendations using charts/graphs (optional).

## Model
- The system uses Random Forest, which is trained on a dataset containing ratio of Nitrogen content in soil,ratio of Phosphorous content in soil, ratio of Potassium content in soil,temperature,humidity,pH and rainfall
- The model is trained to predict the most suitable crops based on input features like soil quality, location, and weather.

## Data
The dataset used for training the model can be found in the repository. The dataset includes the following features:

- **N**: Ratio of Nitrogen content in soil
- **P**: Ratio of Phosphorous content in soil
- **K**: Ratio of Potassium content in soil
- **Temperature**: Temperature in degrees Celsius
- **Humidity**: Relative humidity in percentage (%)
- **pH**: pH value of the soil
- **Rainfall**: Rainfall in millimeters (mm)

You can also upload your custom dataset for more personalized recommendations.

## Contributing
I welcome contributions to improve the crop recommendation system. If you would like to contribute, please fork the repository and submit a pull request with your proposed changes.

### Steps for contributing:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add feature'`).
5. Push your changes to your forked repository (`git push origin feature-name`).
6. Open a pull request.
