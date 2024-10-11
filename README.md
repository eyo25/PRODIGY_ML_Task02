# Customer Segmentation Dashboard with K-Means Clustering

This project provides an interactive **Streamlit dashboard** for customer segmentation using **K-Means Clustering**. The app allows you to perform **Exploratory Data Analysis (EDA)** and segment customers based on their **Annual Income** and **Spending Score**.

## Features

- **Interactive EDA**: Visualize customer demographics like age, gender, income, and spending score.
- **K-Means Clustering**: Segment customers based on their purchasing behavior.
- **Elbow Method**: Choose the optimal number of clusters using the Elbow Method.
- **Easy Deployment**: The app can be deployed directly on **Streamlit Cloud**.

---

## Running the App Locally

To run the app on your local machine, follow the steps below:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/my-streamlit-app.git
cd my-streamlit-app
```
### 2. Install the Required Dependencies
```bash
   pip install -r requirements.txt
```
###  3. Run the Streamlit App
 ```bash
streamlit run streamlit_app_dashboard.py
```
 ## Dataset
The app uses the Mall_Customers.csv dataset, which contains basic customer information. The following fields are included:

CustomerID: Unique ID for each customer.
Gender: Gender of the customer (Male/Female).
Age: Age of the customer.
Annual Income (k$): Annual income of the customer in thousands of dollars.
Spending Score (1-100): A score assigned to customers based on their purchasing behavior.
Exploratory Data Analysis (EDA)
The app provides several visualizations to explore customer demographics:

 ## Elbow Method
To determine the optimal number of clusters (K), the Elbow Method is used. The inertia (sum of squared distances) is plotted for different values of K, and the "elbow" in the plot indicates the optimal K.
How to Deploy on Streamlit Cloud
To deploy the app on Streamlit Cloud, follow these steps:

## 1. Fork the Repository
Fork this repository to your GitHub account.

## 2. Go to Streamlit Cloud
Go to Streamlit Cloud and log in using your GitHub account.

## 3. Create a New App
Click on New App, select your forked repository, and set streamlit_app_dashboard.py as the main file.

# 4. Deploy
Click Deploy, and Streamlit Cloud will launch your app with a public URL.
```bash
Technologies Used
Python: Main programming language.
Streamlit: For creating the web dashboard.
Plotly: For interactive visualizations.
Scikit-learn: Used for K-Means clustering.
Pandas: For data manipulation and analysis.
License
This project is licensed under the MIT License.
```
### Contact
If you have any questions or suggestions, please contact me at eyosias.teffera@gmail.com.
