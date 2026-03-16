
🌸 **Iris Species Prediction Web App**



This project is a Machine Learning web application built with Streamlit that predicts the species of an Iris flower based on its sepal and petal measurements.



The app uses a trained machine learning model to classify the flower into one of the following species:



Iris-setosa



Iris-versicolor



Iris-virginica



**Features**



Interactive Streamlit web interface



User input for:



Petal Length



Petal Width



Sepal Length



Sepal Width



Predicts the Iris flower species



Displays an image of the predicted flower



Uses a trained machine learning model



🧠 **Machine Learning Model**



The application loads a pre-trained model (model\_final.pkl) that was trained on the Iris dataset, one of the most famous datasets in machine learning.



The model predicts the species based on four features:



Feature	Description

Sepal Length	Length of the sepal

Sepal Width	Width of the sepal

Petal Length	Length of the petal

Petal Width	Width of the petal



🛠 **Technologies Used**



Python



Streamlit



Scikit-learn



Pandas



NumPy



Pickle (for loading the trained model)



📂 **Project Structure**



IrisStreamlitApp

│

├── iris.py            # Streamlit application

├── requirements.txt   # Required Python libraries

├── model/

│   └── model\_final.pkl

└── README.md



▶️ **How to Run the Project**

* Clone the repository



git clone https://github.com/your-username/IrisStreamlitApp.git



* Navigate to the project folder



cd IrisStreamlitApp



* Install dependencies



pip install -r requirements.txt



* Run the Streamlit app



streamlit run iris.py



💻 **Application Interface**



The user enters the flower measurements and the model predicts the species of the Iris flower.



The application also displays a sample image of the predicted species.



📊 **Dataset**



This project uses the Iris dataset, a classic dataset used for machine learning classification problems.



Dataset features:



Sepal length



Sepal width



Petal length



Petal width



Target classes:



Setosa



Versicolor



Virginica



🎯 **Learning Outcomes**



Through this project I learned:



Building Machine Learning models



Creating interactive web apps using Streamlit



Deploying ML models in a user-friendly interface



Handling model predictions in real-time



