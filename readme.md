# Simple Reflex Agent for Current AQI Classification with Rule-Based Next-Day AQI Prediction

**Project Domain:** Artificial Intelligence
**Technology Used:** Python, Pandas, Streamlit
**Dataset:** Indian Climate Dataset (2024–2025)

## 2. Introduction

Air Quality Index (AQI) is used to show how clean or polluted the air is and its possible effect on human health.

In this project, a **Simple Reflex Agent** is used to monitor and classify air quality based on the current environmental conditions. The agent uses predefined rules and considers factors such as **temperature, humidity, rainfall, wind speed, and AQI**.

The system also includes a simple rule-based method to predict whether the **next day's AQI may increase or decrease**. For example, low wind speed and high humidity may increase AQI, while rainfall may help reduce it.

The project is developed using **Python, Pandas, and Streamlit**, allowing users to select a location and date and view the current conditions, AQI category, temperature classification, and predicted AQI.

# 3. Problem Statement

The problem addressed in this project is to develop an **AI-based Simple Reflex Agent** that can observe the current environmental conditions and apply predefined rules to classify the current AQI and temperature. The system should provide an understandable output based on the selected **state, city, and date**.

In addition, the system is extended with a **simple rule-based prediction module** that uses the current environmental conditions to estimate the possible AQI for the following day. Factors such as wind speed, humidity, and rainfall are considered in this prediction.

The proposed system therefore aims to provide an interactive and easy-to-understand solution for **current AQI monitoring, environmental condition classification, and basic next-day AQI prediction** using predefined rules.

## 4. Objectives

The main objectives of this project are:

1. To develop a Simple Reflex Agent** that makes decisions using predefined condition-action rules based on the current environmental data.

2. To classify the current AQI** into categories such as Good, Satisfactory, Moderate, Poor, Very Poor, and Severe.

3. To classify temperature** as Cool, Mild, or Hot using predefined temperature conditions.

4. To use environmental factors** such as humidity, rainfall, and wind speed as inputs for the agent's decision-making.

5. To predict the next day's AQI** using a simple rule-based approach based on the current AQI and environmental conditions.

6. To demonstrate how a Simple Reflex Agent can be applied to a real-world environmental monitoring problem.

## 5. Simple Reflex Agent

A imple Reflex Agent is an Artificial Intelligence agent that makes decisions based only on the current information it receives from the environment. It uses predefined **IF–THEN condition-action rules and does not use memory of previous states.

### General Structure


Environment
     ↓
  Current Data
     ↓
 Current Percept
     ↓
 IF–THEN Rules
     ↓
    Decision

### Simple Reflex Agent in This Project

In this project, the Indian Climate Dataset (2024–2025) acts as the environment. When the user selects a state, city, and date, the system retrieves the corresponding environmental data.

The current percept includes:

* Temperature
* Humidity
* Rainfall
* Wind Speed
* AQI

The agent uses these current values to make decisions through predefined rules.

### AQI Classification Rules

The current AQI is classified as follows:


IF AQI ≤ 50
THEN Good

IF AQI ≤ 100
THEN Satisfactory

IF AQI ≤ 200
THEN Moderate

IF AQI ≤ 300
THEN Poor

IF AQI ≤ 400
THEN Very Poor

IF AQI > 400
THEN Severe


### Temperature Classification Rules

The temperature is classified using these rules:


IF Temperature ≥ 37°C
THEN Hot

IF 30°C ≤ Temperature < 37°C
THEN Mild

IF Temperature < 30°C
THEN Cool


### Next-Day AQI Prediction Rules

The project also uses simple rules to estimate tomorrow's AQI. The prediction starts with the current AQI and adjusts it according to the current environmental conditions.


IF Wind Speed < 5 km/h
THEN Increase AQI by 15

IF Humidity > 70%
THEN Increase AQI by 10

IF Rainfall > 0 mm
THEN Decrease AQI by 20


If more than one condition is satisfied, all applicable rules are applied. The final predicted AQI is limited to a range of 0 to 500

### Overall Working

For example, if the selected day's AQI is 12, wind speed is 3 km/h, humidity is 75% and rainfall is 0 mm:


Current AQI = 120

Low wind speed  → +15
High humidity   → +10
Rainfall        → No change

Predicted AQI = 120 + 15 + 10
              = 145

The system then classifies 145 as "Moderate".

Therefore, the project demonstrates a Simple Reflex Agent by taking the current environmental data as its percept, applying predefined rules, and producing AQI classification, temperature classification, and a simple rule-based AQI prediction.

# 8. PEAS Description

PEAS stands for Performance Measure, Environment, Actuators, and Sensors. It is a framework used to describe the task environment of an intelligent agent.

### 1. Performance Measure

The performance measure describes how well the agent performs its task.

In our AQI system, the agent should:

* Correctly classify the current AQI.
* Correctly classify the temperature as Hot, Mild, or Cool.
* Provide clear and understandable results to the user.
* Give a reasonable rule-based prediction of the next day's AQI.

### 2. Environment

The environment is the **surrounding situation in which the agent operates**.

In this project, the environment consists of different Indian cities and their environmental conditions available in the Indian Climate Dataset (2024–2025).

The dataset contains information such as:

* State
* City
* Date
* Temperature
* Humidity
* Rainfall
* Wind Speed
* AQI

### 3. Actuators

Actuators are the components through which an agent produces an action or output.

In our project, the Streamlit application acts as the output interface. It displays:

* Current AQI
* AQI category
* Temperature category
* Predicted next-day AQI
* Predicted AQI category
* Rules that were triggered

### 4. Sensors

Sensors are used by an agent to obtain information from the environment.

In our project, the agent obtains the following environmental information from the dataset:

* Temperature
* Humidity
* Rainfall
* Wind Speed
* AQI

These values form the current percept of the Simple Reflex Agent. The agent then applies predefined IF–THEN rules to these values and produces the appropriate output.
