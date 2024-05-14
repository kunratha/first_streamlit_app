import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import streamlit as st

st.title("CAR DATABASE")

data_url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"


@st.cache_data
def load_data():
    car_data = pd.read_csv(data_url)
    return car_data


data_load_state = st.text("Loading data ...")
data = load_data()
data_load_state.text("Data Upload Done!")

if st.checkbox("Show raw car data"):
    st.subheader("Raw Car Data")
    st.dataframe(data)


st.write("")
st.subheader("Correlation plot of the car data: ")
car_data_numeric = data.drop(columns=["continent"])
fig = plt.figure(figsize=(10, 10))
fig = sns.heatmap(car_data_numeric.corr(), annot=True, cmap="coolwarm")
st.pyplot(fig.figure)

st.markdown("Explanation: ")
st.write(
    "The correlation coefficient represents the strength and direction of the linear relationship between two variables. It ranges from -1 to +1, where +1 indicates a perfect positive correlation, -1 indicates a perfect negative correlation, and 0 indicates no correlation."
)

# Display a text list using Markdown syntax
st.markdown(
    """
- In the correlation plot, cells with correlation coefficients close to +1 or -1 indicate strong relationships between the corresponding variables. For example, a correlation coefficient of +0.95 suggests a strong positive relationship between the variables cubicinches and cylinders.
- Cells with correlation coefficients close to 0 indicate weak or no linear relationships between the corresponding variables. A correlation coefficient close to 0 suggests that changes in one variable do not significantly affect the other variable."

"""
)

st.subheader("Distribution Plots")
# Remove dot from values in the "continent" column
data["continent"] = data["continent"].str.replace(".", "")

# Remove leading and trailing whitespace from continent values
data["continent"] = data["continent"].str.strip()

# Sidebar widget to select region
selected_region = st.sidebar.selectbox("Select Region", ["US", "Europe", "Japan"])

# Debugging: Display the selected region
# st.write("Selected Region:", selected_region)

# Filter DataFrame based on selected region
filtered_df = data[data["continent"] == selected_region]

# Debugging: Display filtered DataFrame
# st.write("Filtered DataFrame:", filtered_df)

# Create subplots according to the mosaic pattern
fig, ax = plt.subplots(2, 3, figsize=(15, 10))

# Flatten the axis array for easy indexing
ax = ax.flatten()

# Plot each variable in its corresponding subplot
plot1 = sns.histplot(filtered_df["mpg"], bins=100, kde=True, ax=ax[0])
plot2 = sns.histplot(filtered_df["cylinders"], bins=100, kde=True, ax=ax[1])
plot3 = sns.histplot(filtered_df["cubicinches"], bins=100, kde=True, ax=ax[2])
plot4 = sns.histplot(filtered_df["hp"], bins=100, kde=True, ax=ax[3])
plot5 = sns.histplot(filtered_df["weightlbs"], bins=100, kde=True, ax=ax[4])
plot6 = sns.histplot(filtered_df["time-to-60"], bins=100, kde=True, ax=ax[5])

# Adjust layout to fit the mosaic pattern
plt.tight_layout()

# Show plot
st.pyplot(fig)
