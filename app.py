# streamlit_app.py

# streamlit_app_dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1: Load the data
@st.cache
def load_data():
    data = pd.read_csv('./data/Mall_Customers.csv')
    return data

# Step 2: Preprocess and scale the features
def preprocess_data(data):
    X = data[['Annual Income (k$)', 'Spending Score (1-100)']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled

# Step 3: Elbow Method to determine the optimal number of clusters
def find_optimal_clusters(X_scaled, max_k=10):
    inertia = []
    for k in range(1, max_k+1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        inertia.append(kmeans.inertia_)
    return inertia

# Step 4: Run KMeans Clustering
def run_kmeans(X_scaled, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    return labels, kmeans.cluster_centers_

# Step 5: Plot clusters with Plotly
def plot_clusters(data, labels, centers):
    data['Cluster'] = labels
    fig = px.scatter(data, x='Annual Income (k$)', y='Spending Score (1-100)', color='Cluster',
                     title='Customer Segments', hover_data=['CustomerID', 'Age', 'Gender'],
                     color_continuous_scale=px.colors.qualitative.Set1)
    # Add centroids to the plot
    centers_scaled = pd.DataFrame(centers, columns=['Annual Income (scaled)', 'Spending Score (scaled)'])
    fig.add_scatter(x=centers_scaled.iloc[:, 0], y=centers_scaled.iloc[:, 1],
                    mode='markers', marker=dict(color='yellow', size=15, symbol='x'),
                    name='Centroids')
    return fig

# Step 6: Plot EDA (Exploratory Data Analysis)
def plot_eda(data):
    # Age distribution
    fig_age = px.histogram(data, x='Age', nbins=20, title='Age Distribution', color_discrete_sequence=['blue'])
    
    # Gender distribution
    fig_gender = px.pie(data, names='Gender', title='Gender Distribution')
    
    # Annual Income distribution
    fig_income = px.histogram(data, x='Annual Income (k$)', nbins=20, title='Annual Income Distribution', color_discrete_sequence=['green'])
    
    # Spending Score distribution
    fig_score = px.histogram(data, x='Spending Score (1-100)', nbins=20, title='Spending Score Distribution', color_discrete_sequence=['orange'])

    return fig_age, fig_gender, fig_income, fig_score

# Streamlit interface
st.title("Customer Segmentation Dashboard")
st.write("This dashboard provides insights into customer data and allows you to perform K-Means clustering for customer segmentation.")

# Load the data
data = load_data()

# Display the data in an expandable section
with st.expander('Show raw data'):
    st.write(data)

# Sidebar for dashboard controls
st.sidebar.title("Dashboard Settings")
analysis_type = st.sidebar.radio("Select Analysis Type", ["EDA", "K-Means Clustering"])

# EDA Section
if analysis_type == "EDA":
    st.subheader("Exploratory Data Analysis (EDA)")
    
    # Display visualizations for EDA
    fig_age, fig_gender, fig_income, fig_score = plot_eda(data)
    
    st.plotly_chart(fig_age)
    st.plotly_chart(fig_gender)
    st.plotly_chart(fig_income)
    st.plotly_chart(fig_score)

# K-Means Clustering Section
elif analysis_type == "K-Means Clustering":
    st.subheader("K-Means Clustering")
    
    # Select the number of clusters
    num_clusters = st.sidebar.slider('Select Number of Clusters (K)', 2, 10, 5)
    
    # Preprocess the data
    X_scaled = preprocess_data(data)
    
    # Run KMeans
    labels, centers = run_kmeans(X_scaled, num_clusters)
    
    # Plot the clusters
    st.plotly_chart(plot_clusters(data, labels, centers))
    
    # Optionally, show the elbow plot
    if st.sidebar.checkbox('Show Elbow Method Plot'):
        inertia = find_optimal_clusters(X_scaled)
        elbow_fig = px.line(x=range(1, 11), y=inertia, title='Elbow Method', labels={'x': 'Number of Clusters (K)', 'y': 'Inertia'})
        st.plotly_chart(elbow_fig)

st.write("Use the sidebar to navigate between EDA and K-Means Clustering sections.")
