## Fitrack
 FitTrack is an advanced mobile application based on React Native platform and uses Expo, SQL and Node.js services. It uses accelerometer data to track user activities and predict them using a random forest machine learning model trained on the MotionSense dataset. The app collects data, pre-processes it, and using the ML model, provides accurate insights into fitness levels and daily activities. FitTrack focuses on health monitoring and personalized activity analysis through its innovative technology stack and machine learning capabilities.
![image](https://github.com/CoolProgrammerAK/Fittrack/assets/68710643/dd05fbb5-f00d-401c-9781-b177aa77b346)

### Stack
FitTrack has been developed entirely from scratch without relying on any online database or processing services, ensuring full control and customization of the app's functionalities.
The technology stack includes React Native for cross-platform development, Expo for streamlined app development and deployment, SQL for managing the app's database locally, Node.js for powering server-side functionalities autonomously, and a Random Forest machine learning model for accurate activity predictions. 
This comprehensive approach not only keeps the app free from external dependencies but also allows for a tailored and efficient user experience.


### Data Collection
When the user wants to start the tracking activity function, they can do this by clicking on the Enable Tracking button (here in picture it is called Collect Acc. Data as our app is still in development phase). FitTrack app then  starts collects accelerometer data from the phone's sensor and saves it in the database. The app then further saves this data in a CSV file in a directory in phone every 15 minutes. This is done to ensure that database doesn’t overload while usage.
![image](https://github.com/CoolProgrammerAK/Fittrack/assets/68710643/9554d7a8-5007-45ca-87f8-974ceb5ccafb)

#### About our dataset
The MotionSense dataset used in the FitTrack app contains time series data from accelerometer and captures activities such as downward stairs, stair climbing, walking, jogging, sitting and standing. 
The data was collected with an iPhone 6s using SensingKit and includes 24 participants who performed these activities in 15 trials each. On each trial, participants carried the phone in their front pocket and performed the specified activity naturally. 
The dataset contains demographic information (age, gender) and sensor values ​​such as posture, gravity, rotation rate and user acceleration. 
For our FitTrack app, we specifically utilized user acceleration data from the MotionSense dataset. This data, collected from the accelerometer sensor, captures the acceleration imparted to the device by the user. Our Random Forest machine learning model was trained exclusively on this user acceleration data to accurately predict user activities based on their movement patterns.
![image](https://github.com/CoolProgrammerAK/Fittrack/assets/68710643/ad9f1dc3-07f9-4c61-8853-3c0ef4686222)

#### Machine Learning Model
FitTrack employs a Random Forest machine learning model trained on the MotionSense dataset. 
The dataset is loaded and preprocessed to prepare features (X) and target labels (y) for training.
The data is split into training and testing sets to evaluate the model's performance.
The Random Forest Classifier is trained using the training data with 100 estimators to learn patterns and make accurate predictions.
This trained model is then used within FitTrack to predict user activities based on real-time accelerometer data from the app.
![image](https://github.com/CoolProgrammerAK/Fittrack/assets/68710643/d055d673-c42e-4f0c-a9c3-30c8a027265f)

####  Model Performance
FitTrack's Random Forest machine learning model exhibits strong performance metrics, showcasing its effectiveness in predicting user activities based on accelerometer data. 
Overall Accuracy: 72% F-1 Score
The F1-score is a harmonic mean of precision and recall, providing a balanced measure of the model's performance. 
FitTrack's machine learning model achieves consistent and reliable performance across various activity categories, contributing to an enhanced user experience and accurate activity tracking within the app!
[image](https://github.com/CoolProgrammerAK/Fittrack/assets/68710643/be7e152a-8daa-4074-9618-52411dcb64bd)



