#!/usr/bin/env python
# coding: utf-8

# # WELCOME TO THE NOTEBOOK
# ---
# 
# In this project, I am going to demonstrate about two important data analysis methods **EDA** (Exploratory Data Analysis) and **CDA** (Confirmatory Data Analysis).
# 

# ### Task 1: What Is Exploratory Data Analysis (EDA)?
# 
# Exploratory Data Analysis (EDA) is an approach to analyzing data. It's where the researcher takes a bird's eye view of the data and tries to make some sense of it. It's often the first step in data analysis, implemented before any formal statistical techniques are applied.

# Importing Modules

# In[75]:


# Pandas Module
import pandas as pd

import datetime

# Data Visualization Module
import plotly.express as px
from plotly.offline import plot, iplot, init_notebook_mode
import plotly.graph_objs as go
init_notebook_mode(connected=True)


# # Let's load our canons

# In[76]:


data = pd.read_csv('dataset.csv', header= 0,
                        encoding= 'unicode_escape')
data.head()              


# # Checking the data size

# In[77]:


data.shape


# # Checking the data

# In[78]:


data.info()


# # #2: EDA 
# 
# Understanding the big picture
# 	This involves various methods to understand the dataset(without going into deatails)
# 	"We try to understand the problem we want to solve, thinking about the entire dataset and the meaning of the variables."
# 
# - Variable: name of the variable
# - Type: this type or format of the variable. This can be categorical, numerical, boolean and so on.
# - Context: useful information to understand the semantic space of the variable.
# - `Expectations`(most important): how relevant is this variable with respect to our task ? We can use a scale of 10.
# - Comments: whether or not we have any comments to make on the variable.
# 

# # In our data, we have the following information:
#     
#     Time Information (Order Data)
#     Customer Information (Customer Name)
#     Place Information (State name)
#     Hierarchical Information about the products (Category, Sub-category, Product Name)
#     Sale Information (sales, profit, quantity)
# 
# 
# now let's start our exploration

# # #3: Data Exploration: Time Information 

# In[79]:


data["Order Date"] = pd.to_datetime(data["Order Date"])


# In[80]:


data.info()


# In[81]:


from_ = data["Order Date"].min()
to_ = data["Order Date"].max()


# # What is the timespan of our data?

# In[82]:


print("We have the sales information from", from_ , "to", to_)


# # Now let's sort our data by the date

# In[83]:


data


# In[84]:


pd.to_datetime(data["Order Date"])


# **`important method`**
# 
#     pd.to_datetime()
# 
# Converts argument to datetime.

# In[85]:


data = data.sort_values("Order Date")
data.head()


# # Some data preparation: let's extract year, month, and day from the Order Date column

# In[86]:


data["Year"] = pd.DatetimeIndex(data["Order Date"]).year


# In[87]:


data["Month"] = pd.DatetimeIndex(data["Order Date"]).month


# In[88]:


data["Day"] = pd.DatetimeIndex(data["Order Date"]).day


# Profit gained over time by different product categories

# In[89]:


# i have sliced and combined year and category columns using groupby and used aggregate method to add up profit using sum operation.
profit_data = data.groupby(["Year","Category"]).agg({"Profit":sum}).reset_index()


# In[90]:


profit_data


# # Visualizing the results using a line chart

# In[91]:


px.line(profit_data, x = "Year", y = "Profit", color = "Category")


# In[ ]:





# # #4 Data Exploration: Customer Aspect

# 
# # let's see how many unique costumers do we have

# In[92]:


len(data["Customer Name"].unique())


# # let's see the yearly change in number of unique customers

# In[93]:


customer_data = data.groupby("Year").agg({"Customer Name":"nunique"}).reset_index()
customer_data


# # visualizing the result

# In[94]:


px.bar(customer_data, x = "Year", y = "Customer Name")


# # Top 10 customers who brought the highest profit 

# In[95]:


top10_profit = data.groupby("Customer Name").agg({"Profit" : "sum"}).reset_index().sort_values("Profit", ascending = False).head(10)


# In[96]:


top10_profit["Customer Name"].duplicated()


# In[97]:


#28.656896
px.bar(top10_profit, x = "Customer Name", y = "Profit")


# In[ ]:





# # #5 Data Exploration: Place (location) Aspect

# Let's analyze the profits gained in different states in the US

# In[98]:


geo_data = data.groupby("State").agg({"Profit":"sum"}).reset_index()
geo_data


# ### Let's create a choropleth map 
# Plotly uses abbreviated two-letter postal codes for state locations so it will be necessary to create a dictionary that contains conversions of the full names of states into abbreviations.

# In[99]:


state_codes = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
}


# # let's map the abbreviated two-letter postal codes to the State column

# In[100]:


geo_data.State = geo_data.State.map(state_codes)


# In[101]:


px.choropleth(geo_data,
              locations = "State",
              color = "Profit",
              locationmode = "USA-states",
              scope = "usa",
              title = "Profit gained in each state"
              
)


# 

# In[102]:


ex_data = data[data.Category == "Technology"].groupby("State").agg({"Profit" : "sum"}).reset_index()

px.choropleth(ex_data,
             locations = ex_data.State.map(state_codes),
             color = "Profit",
             locationmode = "USA-states",
             scope = "usa",
             title = "Profit Gained In different states",
             color_continuous_scale = "Pubu")


# # #6 Data Exploration - Hierarchical Information about the products

# In[103]:


product_data = data.groupby(["Category", "Sub-Category"]).agg({"Profit":"sum"}).reset_index()
product_data = product_data[product_data.Profit > 0]
product_data["Sales"] = "Any"
product_data


# In[104]:


px.sunburst(product_data, path = ["Sales", "Category", "Sub-Category"], values = "Profit")


# In[105]:


px.treemap(product_data,
          path = ["Sales","Category","Sub-Category"],
          values = "Profit")


# # #7 Data Exploration: Product Sales information (Sales, Quantity, Profit)

# In[ ]:





# Distribution Analysis on **Quantity** column 

# Let's check the statistical summary of the column

# In[106]:


data.Quantity.describe()


# In[107]:


px.histogram(data, x = "Quantity")


# In[108]:


px.box(data, y = "Quantity", x = "Year", color = "Category")


#  

# In[109]:


data.Profit.describe()


# In[110]:


px.box(data, y = "Profit")


# # #8 What Is Confirmatory Data Analysis (CDA)? 

# Confirmatory Data Analysis is the part where you evaluate your evidence using traditional statistical tools such as significance, inference, and confidence.
# 
#     Assumption 1 - Every summer technology products have the highest sale quantity compared to other product categories.
#     Assumption 2- In New York, there are many big companies, therefore, office supplies product has 
#     the highest sale quantity compared to other big states such as Texas, Illinois, and California. 
# 

# # `Assumption 1 - Every summer technology products have the highest sale quantity compared to other product categories.`

# In[111]:


seasons = {
    1 : "Winter",
    2 : "Spring",
    3 : "Summer",
    4 : "Fall"
}


# # Creating **Season** column

# In[112]:


data["Season"] = data.Month.astype(int) % 12 // 3 + 1
data.Season = data.Season.map(seasons)
data.sample(20)


# # Extracting data related to summer every year

# In[113]:


summer_data = data[data.Season == "Summer"]
summer_data


# Aggregating data based on Year, Category, and Season columns and summing up the Quantity

# In[114]:


summer_data_agg = summer_data.groupby(["Category","Year","Season"]).agg({"Quantity":"sum"}).reset_index()
summer_data_agg


# # Let's visualize our result using a grouped bar chart

# In[115]:


px.bar(summer_data_agg,
      x = "Year",
      y = "Quantity",
      color = "Category",
      barmode = "group")


# ## Assumption proved wrong: The graph says that, the quantities of office supplies are higher than the technology

# 
#         
# # `Assumption 2- In New York, there are many big companies, therefore, office supplies product has the highest sale quantity compared to other big states such as Texas, Illinois, and California.` 

# ## Deriving unique details in the column State to locate the required States to confirm our Assumption

# In[116]:


data["State"].unique()


# In[117]:


state_supply = data.loc[data['State'].isin(["New York", "Texas", "Illinois", "California"])]


# In[118]:


max_supplies = state_supply.groupby(["State","Category"]).agg({"Quantity":"sum"}).reset_index()
max_supplies


# # Let's Visualize the data frame

# In[119]:


px.bar(max_supplies,
      x = "State",
      y = "Quantity",
      color = "Category",
      barmode = "group")


# ## Assumption proved correct: The graph says that, the quantities of office supplies are relatively higher in NY than the other cities.

# In[ ]:





# In[120]:


import jovian


# In[121]:


jovian.commit()


# In[ ]:





# In[ ]:




