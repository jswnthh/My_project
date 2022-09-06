# WELCOME TO THE NOTEBOOK
---

In this project, I am going to demonstrate about two important data analysis methods **EDA** (Exploratory Data Analysis) and **CDA** (Confirmatory Data Analysis).


### Task 1: What Is Exploratory Data Analysis (EDA)?

Exploratory Data Analysis (EDA) is an approach to analyzing data. It's where the researcher takes a bird's eye view of the data and tries to make some sense of it. It's often the first step in data analysis, implemented before any formal statistical techniques are applied.

Importing Modules


```python
# Pandas Module
import pandas as pd

import datetime

# Data Visualization Module
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo

```

# Let's load our canons


```python
data = pd.read_csv('dataset.csv', header= 0,
                        encoding= 'unicode_escape')
data.head()              
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order Date</th>
      <th>Customer Name</th>
      <th>State</th>
      <th>Category</th>
      <th>Sub-Category</th>
      <th>Product Name</th>
      <th>Sales</th>
      <th>Quantity</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11/8/2016</td>
      <td>Claire Gute</td>
      <td>Kentucky</td>
      <td>Furniture</td>
      <td>Bookcases</td>
      <td>Bush Somerset Collection Bookcase</td>
      <td>261.9600</td>
      <td>2</td>
      <td>41.9136</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11/8/2016</td>
      <td>Claire Gute</td>
      <td>Kentucky</td>
      <td>Furniture</td>
      <td>Chairs</td>
      <td>Hon Deluxe Fabric Upholstered Stacking Chairs,...</td>
      <td>731.9400</td>
      <td>3</td>
      <td>219.5820</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6/12/2016</td>
      <td>Darrin Van Huff</td>
      <td>California</td>
      <td>Office Supplies</td>
      <td>Labels</td>
      <td>Self-Adhesive Address Labels for Typewriters b...</td>
      <td>14.6200</td>
      <td>2</td>
      <td>6.8714</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10/11/2015</td>
      <td>Sean O'Donnell</td>
      <td>Florida</td>
      <td>Furniture</td>
      <td>Tables</td>
      <td>Bretford CR4500 Series Slim Rectangular Table</td>
      <td>957.5775</td>
      <td>5</td>
      <td>-383.0310</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10/11/2015</td>
      <td>Sean O'Donnell</td>
      <td>Florida</td>
      <td>Office Supplies</td>
      <td>Storage</td>
      <td>Eldon Fold 'N Roll Cart System</td>
      <td>22.3680</td>
      <td>2</td>
      <td>2.5164</td>
    </tr>
  </tbody>
</table>
</div>



# Checking the data size


```python
data.shape
```




    (9994, 9)



# Checking the data


```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 9994 entries, 0 to 9993
    Data columns (total 9 columns):
     #   Column         Non-Null Count  Dtype  
    ---  ------         --------------  -----  
     0   Order Date     9994 non-null   object 
     1   Customer Name  9994 non-null   object 
     2   State          9994 non-null   object 
     3   Category       9994 non-null   object 
     4   Sub-Category   9994 non-null   object 
     5   Product Name   9994 non-null   object 
     6   Sales          9994 non-null   float64
     7   Quantity       9994 non-null   int64  
     8   Profit         9994 non-null   float64
    dtypes: float64(2), int64(1), object(6)
    memory usage: 702.8+ KB
    

# #2: EDA 

Understanding the big picture
	This involves various methods to understand the dataset(without going into deatails)
	"We try to understand the problem we want to solve, thinking about the entire dataset and the meaning of the variables."

- Variable: name of the variable
- Type: this type or format of the variable. This can be categorical, numerical, boolean and so on.
- Context: useful information to understand the semantic space of the variable.
- `Expectations`(most important): how relevant is this variable with respect to our task ? We can use a scale of 10.
- Comments: whether or not we have any comments to make on the variable.


# In our data, we have the following information:
    
    Time Information (Order Data)
    Customer Information (Customer Name)
    Place Information (State name)
    Hierarchical Information about the products (Category, Sub-category, Product Name)
    Sale Information (sales, profit, quantity)


now let's start our exploration

# #3: Data Exploration: Time Information 


```python
data["Order Date"] = pd.to_datetime(data["Order Date"])
```


```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 9994 entries, 0 to 9993
    Data columns (total 9 columns):
     #   Column         Non-Null Count  Dtype         
    ---  ------         --------------  -----         
     0   Order Date     9994 non-null   datetime64[ns]
     1   Customer Name  9994 non-null   object        
     2   State          9994 non-null   object        
     3   Category       9994 non-null   object        
     4   Sub-Category   9994 non-null   object        
     5   Product Name   9994 non-null   object        
     6   Sales          9994 non-null   float64       
     7   Quantity       9994 non-null   int64         
     8   Profit         9994 non-null   float64       
    dtypes: datetime64[ns](1), float64(2), int64(1), object(5)
    memory usage: 702.8+ KB
    


```python
from_ = data["Order Date"].min()
to_ = data["Order Date"].max()
```

# What is the timespan of our data?


```python
print("We have the sales information from", from_ , "to", to_)
```

    We have the sales information from 2014-01-03 00:00:00 to 2017-12-30 00:00:00
    

# Now let's sort our data by the date


```python
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order Date</th>
      <th>Customer Name</th>
      <th>State</th>
      <th>Category</th>
      <th>Sub-Category</th>
      <th>Product Name</th>
      <th>Sales</th>
      <th>Quantity</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-11-08</td>
      <td>Claire Gute</td>
      <td>Kentucky</td>
      <td>Furniture</td>
      <td>Bookcases</td>
      <td>Bush Somerset Collection Bookcase</td>
      <td>261.9600</td>
      <td>2</td>
      <td>41.9136</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-11-08</td>
      <td>Claire Gute</td>
      <td>Kentucky</td>
      <td>Furniture</td>
      <td>Chairs</td>
      <td>Hon Deluxe Fabric Upholstered Stacking Chairs,...</td>
      <td>731.9400</td>
      <td>3</td>
      <td>219.5820</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-06-12</td>
      <td>Darrin Van Huff</td>
      <td>California</td>
      <td>Office Supplies</td>
      <td>Labels</td>
      <td>Self-Adhesive Address Labels for Typewriters b...</td>
      <td>14.6200</td>
      <td>2</td>
      <td>6.8714</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015-10-11</td>
      <td>Sean O'Donnell</td>
      <td>Florida</td>
      <td>Furniture</td>
      <td>Tables</td>
      <td>Bretford CR4500 Series Slim Rectangular Table</td>
      <td>957.5775</td>
      <td>5</td>
      <td>-383.0310</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015-10-11</td>
      <td>Sean O'Donnell</td>
      <td>Florida</td>
      <td>Office Supplies</td>
      <td>Storage</td>
      <td>Eldon Fold 'N Roll Cart System</td>
      <td>22.3680</td>
      <td>2</td>
      <td>2.5164</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9989</th>
      <td>2014-01-21</td>
      <td>Tom Boeckenhauer</td>
      <td>Florida</td>
      <td>Furniture</td>
      <td>Furnishings</td>
      <td>Ultra Door Pull Handle</td>
      <td>25.2480</td>
      <td>3</td>
      <td>4.1028</td>
    </tr>
    <tr>
      <th>9990</th>
      <td>2017-02-26</td>
      <td>Dave Brooks</td>
      <td>California</td>
      <td>Furniture</td>
      <td>Furnishings</td>
      <td>Tenex B1-RE Series Chair Mats for Low Pile Car...</td>
      <td>91.9600</td>
      <td>2</td>
      <td>15.6332</td>
    </tr>
    <tr>
      <th>9991</th>
      <td>2017-02-26</td>
      <td>Dave Brooks</td>
      <td>California</td>
      <td>Technology</td>
      <td>Phones</td>
      <td>Aastra 57i VoIP phone</td>
      <td>258.5760</td>
      <td>2</td>
      <td>19.3932</td>
    </tr>
    <tr>
      <th>9992</th>
      <td>2017-02-26</td>
      <td>Dave Brooks</td>
      <td>California</td>
      <td>Office Supplies</td>
      <td>Paper</td>
      <td>It's Hot Message Books with Stickers, 2 3/4" x 5"</td>
      <td>29.6000</td>
      <td>4</td>
      <td>13.3200</td>
    </tr>
    <tr>
      <th>9993</th>
      <td>2017-05-04</td>
      <td>Chris Cortes</td>
      <td>California</td>
      <td>Office Supplies</td>
      <td>Appliances</td>
      <td>Acco 7-Outlet Masterpiece Power Center, Wihtou...</td>
      <td>243.1600</td>
      <td>2</td>
      <td>72.9480</td>
    </tr>
  </tbody>
</table>
<p>9994 rows × 9 columns</p>
</div>




```python
pd.to_datetime(data["Order Date"])
```




    0      2016-11-08
    1      2016-11-08
    2      2016-06-12
    3      2015-10-11
    4      2015-10-11
              ...    
    9989   2014-01-21
    9990   2017-02-26
    9991   2017-02-26
    9992   2017-02-26
    9993   2017-05-04
    Name: Order Date, Length: 9994, dtype: datetime64[ns]



**`important method`**

    pd.to_datetime()

Converts argument to datetime.


```python
data = data.sort_values("Order Date")
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order Date</th>
      <th>Customer Name</th>
      <th>State</th>
      <th>Category</th>
      <th>Sub-Category</th>
      <th>Product Name</th>
      <th>Sales</th>
      <th>Quantity</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7980</th>
      <td>2014-01-03</td>
      <td>Darren Powers</td>
      <td>Texas</td>
      <td>Office Supplies</td>
      <td>Paper</td>
      <td>Message Book, Wirebound, Four 5 1/2" X 4" Form...</td>
      <td>16.448</td>
      <td>2</td>
      <td>5.5512</td>
    </tr>
    <tr>
      <th>739</th>
      <td>2014-01-04</td>
      <td>Phillina Ober</td>
      <td>Illinois</td>
      <td>Office Supplies</td>
      <td>Labels</td>
      <td>Avery 508</td>
      <td>11.784</td>
      <td>3</td>
      <td>4.2717</td>
    </tr>
    <tr>
      <th>740</th>
      <td>2014-01-04</td>
      <td>Phillina Ober</td>
      <td>Illinois</td>
      <td>Office Supplies</td>
      <td>Storage</td>
      <td>SAFCO Boltless Steel Shelving</td>
      <td>272.736</td>
      <td>3</td>
      <td>-64.7748</td>
    </tr>
    <tr>
      <th>741</th>
      <td>2014-01-04</td>
      <td>Phillina Ober</td>
      <td>Illinois</td>
      <td>Office Supplies</td>
      <td>Binders</td>
      <td>GBC Standard Plastic Binding Systems Combs</td>
      <td>3.540</td>
      <td>2</td>
      <td>-5.4870</td>
    </tr>
    <tr>
      <th>1759</th>
      <td>2014-01-05</td>
      <td>Mick Brown</td>
      <td>Pennsylvania</td>
      <td>Office Supplies</td>
      <td>Art</td>
      <td>Avery Hi-Liter EverBold Pen Style Fluorescent ...</td>
      <td>19.536</td>
      <td>3</td>
      <td>4.8840</td>
    </tr>
  </tbody>
</table>
</div>



# Some data preparation: let's extract year, month, and day from the Order Date column


```python
data["Year"] = pd.DatetimeIndex(data["Order Date"]).year
```


```python
data["Month"] = pd.DatetimeIndex(data["Order Date"]).month
```


```python
data["Day"] = pd.DatetimeIndex(data["Order Date"]).day
```

Profit gained over time by different product categories


```python
# i have sliced and combined year and category columns using groupby and used aggregate method to add up profit using sum operation.
profit_data = data.groupby(["Year","Category"]).agg({"Profit":sum}).reset_index()

```


```python
profit_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Category</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014</td>
      <td>Furniture</td>
      <td>5457.7255</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014</td>
      <td>Office Supplies</td>
      <td>22593.4161</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014</td>
      <td>Technology</td>
      <td>21492.8325</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>Furniture</td>
      <td>3015.2029</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015</td>
      <td>Office Supplies</td>
      <td>25099.5338</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2015</td>
      <td>Technology</td>
      <td>33503.8670</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>Furniture</td>
      <td>6959.9531</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016</td>
      <td>Office Supplies</td>
      <td>35061.2292</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016</td>
      <td>Technology</td>
      <td>39773.9920</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2017</td>
      <td>Furniture</td>
      <td>3018.3913</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2017</td>
      <td>Office Supplies</td>
      <td>39736.6217</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2017</td>
      <td>Technology</td>
      <td>50684.2566</td>
    </tr>
  </tbody>
</table>
</div>



# Visualizing the results using a line chart


```python
px.line(profit_data, x = "Year", y = "Profit", color = "Category")
```


<div>                            <div id="cd881d01-64b8-480e-9eb5-875fac12ac2a" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("cd881d01-64b8-480e-9eb5-875fac12ac2a")) {                    Plotly.newPlot(                        "cd881d01-64b8-480e-9eb5-875fac12ac2a",                        [{"hovertemplate":"Category=Furniture<br>Year=%{x}<br>Profit=%{y}<extra></extra>","legendgroup":"Furniture","line":{"color":"#636efa","dash":"solid"},"marker":{"symbol":"circle"},"mode":"lines","name":"Furniture","orientation":"v","showlegend":true,"x":[2014,2015,2016,2017],"xaxis":"x","y":[5457.7255000000005,3015.2029,6959.9531,3018.3913000000002],"yaxis":"y","type":"scatter"},{"hovertemplate":"Category=Office Supplies<br>Year=%{x}<br>Profit=%{y}<extra></extra>","legendgroup":"Office Supplies","line":{"color":"#EF553B","dash":"solid"},"marker":{"symbol":"circle"},"mode":"lines","name":"Office Supplies","orientation":"v","showlegend":true,"x":[2014,2015,2016,2017],"xaxis":"x","y":[22593.4161,25099.5338,35061.2292,39736.6217],"yaxis":"y","type":"scatter"},{"hovertemplate":"Category=Technology<br>Year=%{x}<br>Profit=%{y}<extra></extra>","legendgroup":"Technology","line":{"color":"#00cc96","dash":"solid"},"marker":{"symbol":"circle"},"mode":"lines","name":"Technology","orientation":"v","showlegend":true,"x":[2014,2015,2016,2017],"xaxis":"x","y":[21492.8325,33503.867,39773.992,50684.2566],"yaxis":"y","type":"scatter"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Year"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"Profit"}},"legend":{"title":{"text":"Category"},"tracegroupgap":0},"margin":{"t":60}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('cd881d01-64b8-480e-9eb5-875fac12ac2a');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python

```

# #4 Data Exploration: Customer Aspect


# let's see how many unique costumers do we have


```python
len(data["Customer Name"].unique())
```




    793



# let's see the yearly change in number of unique customers


```python
customer_data = data.groupby("Year").agg({"Customer Name":"nunique"}).reset_index()
customer_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Customer Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014</td>
      <td>595</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015</td>
      <td>573</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>638</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017</td>
      <td>693</td>
    </tr>
  </tbody>
</table>
</div>



# visualizing the result


```python
px.bar(customer_data, x = "Year", y = "Customer Name")
```


<div>                            <div id="97303a09-83d3-4e2a-9f15-b2602dbb35c8" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("97303a09-83d3-4e2a-9f15-b2602dbb35c8")) {                    Plotly.newPlot(                        "97303a09-83d3-4e2a-9f15-b2602dbb35c8",                        [{"alignmentgroup":"True","hovertemplate":"Year=%{x}<br>Customer Name=%{y}<extra></extra>","legendgroup":"","marker":{"color":"#636efa","pattern":{"shape":""}},"name":"","offsetgroup":"","orientation":"v","showlegend":false,"textposition":"auto","x":[2014,2015,2016,2017],"xaxis":"x","y":[595,573,638,693],"yaxis":"y","type":"bar"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Year"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"Customer Name"}},"legend":{"tracegroupgap":0},"margin":{"t":60},"barmode":"relative"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('97303a09-83d3-4e2a-9f15-b2602dbb35c8');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


# Top 10 customers who brought the highest profit 


```python
top10_profit = data.groupby("Customer Name").agg({"Profit" : "sum"}).reset_index().sort_values("Profit", ascending = False).head(10)
```


```python
top10_profit["Customer Name"].duplicated()
```




    730    False
    622    False
    671    False
    334    False
    6      False
    757    False
    157    False
    431    False
    35     False
    194    False
    Name: Customer Name, dtype: bool




```python
#28.656896
px.bar(top10_profit, x = "Customer Name", y = "Profit")
```


<div>                            <div id="1f33bb5a-7b00-4140-ae65-45cb4c36a8b1" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("1f33bb5a-7b00-4140-ae65-45cb4c36a8b1")) {                    Plotly.newPlot(                        "1f33bb5a-7b00-4140-ae65-45cb4c36a8b1",                        [{"alignmentgroup":"True","hovertemplate":"Customer Name=%{x}<br>Profit=%{y}<extra></extra>","legendgroup":"","marker":{"color":"#636efa","pattern":{"shape":""}},"name":"","offsetgroup":"","orientation":"v","showlegend":false,"textposition":"auto","x":["Tamara Chand","Raymond Buch","Sanjit Chand","Hunter Lopez","Adrian Barton","Tom Ashbrook","Christopher Martinez","Keith Dawkins","Andy Reiter","Daniel Raglin"],"xaxis":"x","y":[8981.323900000001,6976.0959,5757.411899999999,5622.4292,5444.8054999999995,4703.7883,3899.8903999999998,3038.6254000000004,2884.6208,2869.0759999999996],"yaxis":"y","type":"bar"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Customer Name"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"Profit"}},"legend":{"tracegroupgap":0},"margin":{"t":60},"barmode":"relative"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('1f33bb5a-7b00-4140-ae65-45cb4c36a8b1');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python

```

# #5 Data Exploration: Place (location) Aspect

Let's analyze the profits gained in different states in the US


```python
geo_data = data.groupby("State").agg({"Profit":"sum"}).reset_index()
geo_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alabama</td>
      <td>5786.8253</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arizona</td>
      <td>-3427.9246</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arkansas</td>
      <td>4008.6871</td>
    </tr>
    <tr>
      <th>3</th>
      <td>California</td>
      <td>76381.3871</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Colorado</td>
      <td>-6527.8579</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Connecticut</td>
      <td>3511.4918</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Delaware</td>
      <td>9977.3748</td>
    </tr>
    <tr>
      <th>7</th>
      <td>District of Columbia</td>
      <td>1059.5893</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Florida</td>
      <td>-3399.3017</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Georgia</td>
      <td>16250.0433</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Idaho</td>
      <td>826.7231</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Illinois</td>
      <td>-12607.8870</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Indiana</td>
      <td>18382.9363</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Iowa</td>
      <td>1183.8119</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Kansas</td>
      <td>836.4435</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Kentucky</td>
      <td>11199.6966</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Louisiana</td>
      <td>2196.1023</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Maine</td>
      <td>454.4862</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Maryland</td>
      <td>7031.1788</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Massachusetts</td>
      <td>6785.5016</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Michigan</td>
      <td>24463.1876</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Minnesota</td>
      <td>10823.1874</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Mississippi</td>
      <td>3172.9762</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Missouri</td>
      <td>6436.2105</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Montana</td>
      <td>1833.3285</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Nebraska</td>
      <td>2037.0942</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Nevada</td>
      <td>3316.7659</td>
    </tr>
    <tr>
      <th>27</th>
      <td>New Hampshire</td>
      <td>1706.5028</td>
    </tr>
    <tr>
      <th>28</th>
      <td>New Jersey</td>
      <td>9772.9138</td>
    </tr>
    <tr>
      <th>29</th>
      <td>New Mexico</td>
      <td>1157.1161</td>
    </tr>
    <tr>
      <th>30</th>
      <td>New York</td>
      <td>74038.5486</td>
    </tr>
    <tr>
      <th>31</th>
      <td>North Carolina</td>
      <td>-7490.9122</td>
    </tr>
    <tr>
      <th>32</th>
      <td>North Dakota</td>
      <td>230.1497</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Ohio</td>
      <td>-16971.3766</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Oklahoma</td>
      <td>4853.9560</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Oregon</td>
      <td>-1190.4705</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Pennsylvania</td>
      <td>-15559.9603</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Rhode Island</td>
      <td>7285.6293</td>
    </tr>
    <tr>
      <th>38</th>
      <td>South Carolina</td>
      <td>1769.0566</td>
    </tr>
    <tr>
      <th>39</th>
      <td>South Dakota</td>
      <td>394.8283</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Tennessee</td>
      <td>-5341.6936</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Texas</td>
      <td>-25729.3563</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Utah</td>
      <td>2546.5335</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Vermont</td>
      <td>2244.9783</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Virginia</td>
      <td>18597.9504</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Washington</td>
      <td>33402.6517</td>
    </tr>
    <tr>
      <th>46</th>
      <td>West Virginia</td>
      <td>185.9216</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Wisconsin</td>
      <td>8401.8004</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Wyoming</td>
      <td>100.1960</td>
    </tr>
  </tbody>
</table>
</div>



### Let's create a choropleth map 
Plotly uses abbreviated two-letter postal codes for state locations so it will be necessary to create a dictionary that contains conversions of the full names of states into abbreviations.


```python
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
```

# let's map the abbreviated two-letter postal codes to the State column


```python
geo_data.State = geo_data.State.map(state_codes)
```


```python
px.choropleth(geo_data,
              locations = "State",
              color = "Profit",
              locationmode = "USA-states",
              scope = "usa",
              title = "Profit gained in each state"
              
)
```


<div>                            <div id="7f2777cd-aa9e-403a-a2ef-dfcd7a220d98" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("7f2777cd-aa9e-403a-a2ef-dfcd7a220d98")) {                    Plotly.newPlot(                        "7f2777cd-aa9e-403a-a2ef-dfcd7a220d98",                        [{"coloraxis":"coloraxis","geo":"geo","hovertemplate":"State=%{location}<br>Profit=%{z}<extra></extra>","locationmode":"USA-states","locations":["AL","AZ","AR","CA","CO","CT","DE","DC","FL","GA","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"],"name":"","z":[5786.8253,-3427.9246000000003,4008.6871,76381.3871,-6527.8579,3511.4918,9977.3748,1059.5892999999999,-3399.3017000000004,16250.0433,826.7231,-12607.887,18382.9363,1183.8119,836.4435,11199.6966,2196.1023,454.4862,7031.1788,6785.5016,24463.1876,10823.187399999999,3172.9762,6436.2105,1833.3285,2037.0942,3316.7659,1706.5028,9772.9138,1157.1161,74038.5486,-7490.9122,230.14969999999997,-16971.3766,4853.956,-1190.4705000000001,-15559.9603,7285.6293,1769.0566,394.82829999999996,-5341.6936,-25729.3563,2546.5335,2244.9782999999998,18597.9504,33402.6517,185.9216,8401.8004,100.196],"type":"choropleth"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"geo":{"domain":{"x":[0.0,1.0],"y":[0.0,1.0]},"center":{},"scope":"usa"},"coloraxis":{"colorbar":{"title":{"text":"Profit"}},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]},"legend":{"tracegroupgap":0},"title":{"text":"Profit gained in each state"}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('7f2777cd-aa9e-403a-a2ef-dfcd7a220d98');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>





```python
ex_data = data[data.Category == "Technology"].groupby("State").agg({"Profit" : "sum"}).reset_index()

px.choropleth(ex_data,
             locations = ex_data.State.map(state_codes),
             color = "Profit",
             locationmode = "USA-states",
             scope = "usa",
             title = "Profit Gained In different states",
             color_continuous_scale = "Pubu")
```


<div>                            <div id="4264b5ec-7b27-450b-bcb7-344cfeeca9f1" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("4264b5ec-7b27-450b-bcb7-344cfeeca9f1")) {                    Plotly.newPlot(                        "4264b5ec-7b27-450b-bcb7-344cfeeca9f1",                        [{"coloraxis":"coloraxis","geo":"geo","hovertemplate":"locations=%{location}<br>Profit=%{z}<extra></extra>","locationmode":"USA-states","locations":["AL","AZ","AR","CA","CO","CT","DE","DC","FL","GA","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WI"],"name":"","z":[3297.8029,112.50119999999991,1261.4384,29470.0368,-3471.5845,780.9336,6239.0508,648.5624,530.8047999999998,4399.6597,92.09729999999999,4822.5592,11000.8773,318.3682,174.9866,4156.636399999999,1015.0152,251.0328,1322.8776,1755.7501,4782.3025,1018.8008,986.4024,3014.7267999999995,1523.0354000000002,961.5150000000001,512.8456,902.7073,4170.198,337.2828,42186.7856,-3583.304,-12649.9401,1580.9003,126.35640000000001,-3191.2216000000003,4598.012299999999,453.5875,133.8966,66.03370000000004,3291.429,581.7351,447.2863,7407.7544,15019.3435,2597.0697],"type":"choropleth"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"geo":{"domain":{"x":[0.0,1.0],"y":[0.0,1.0]},"center":{},"scope":"usa"},"coloraxis":{"colorbar":{"title":{"text":"Profit"}},"colorscale":[[0.0,"rgb(255,247,251)"],[0.125,"rgb(236,231,242)"],[0.25,"rgb(208,209,230)"],[0.375,"rgb(166,189,219)"],[0.5,"rgb(116,169,207)"],[0.625,"rgb(54,144,192)"],[0.75,"rgb(5,112,176)"],[0.875,"rgb(4,90,141)"],[1.0,"rgb(2,56,88)"]]},"legend":{"tracegroupgap":0},"title":{"text":"Profit Gained In different states"}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('4264b5ec-7b27-450b-bcb7-344cfeeca9f1');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


# #6 Data Exploration - Hierarchical Information about the products


```python
product_data = data.groupby(["Category", "Sub-Category"]).agg({"Profit":"sum"}).reset_index()
product_data = product_data[product_data.Profit > 0]
product_data["Sales"] = "Any"
product_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Category</th>
      <th>Sub-Category</th>
      <th>Profit</th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Furniture</td>
      <td>Chairs</td>
      <td>26590.1663</td>
      <td>Any</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Furniture</td>
      <td>Furnishings</td>
      <td>13059.1436</td>
      <td>Any</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Office Supplies</td>
      <td>Appliances</td>
      <td>18138.0054</td>
      <td>Any</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Office Supplies</td>
      <td>Art</td>
      <td>6527.7870</td>
      <td>Any</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Office Supplies</td>
      <td>Binders</td>
      <td>30221.7633</td>
      <td>Any</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Office Supplies</td>
      <td>Envelopes</td>
      <td>6964.1767</td>
      <td>Any</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Office Supplies</td>
      <td>Fasteners</td>
      <td>949.5182</td>
      <td>Any</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Office Supplies</td>
      <td>Labels</td>
      <td>5546.2540</td>
      <td>Any</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Office Supplies</td>
      <td>Paper</td>
      <td>34053.5693</td>
      <td>Any</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Office Supplies</td>
      <td>Storage</td>
      <td>21278.8264</td>
      <td>Any</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Technology</td>
      <td>Accessories</td>
      <td>41936.6357</td>
      <td>Any</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Technology</td>
      <td>Copiers</td>
      <td>55617.8249</td>
      <td>Any</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Technology</td>
      <td>Machines</td>
      <td>3384.7569</td>
      <td>Any</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Technology</td>
      <td>Phones</td>
      <td>44515.7306</td>
      <td>Any</td>
    </tr>
  </tbody>
</table>
</div>




```python
px.sunburst(product_data, path = ["Sales", "Category", "Sub-Category"], values = "Profit")
```


<div>                            <div id="42d4e888-7fd1-44c6-b131-3a96502107c2" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("42d4e888-7fd1-44c6-b131-3a96502107c2")) {                    Plotly.newPlot(                        "42d4e888-7fd1-44c6-b131-3a96502107c2",                        [{"branchvalues":"total","domain":{"x":[0.0,1.0],"y":[0.0,1.0]},"hovertemplate":"labels=%{label}<br>Profit=%{value}<br>parent=%{parent}<br>id=%{id}<extra></extra>","ids":["Any/Technology/Accessories","Any/Office Supplies/Appliances","Any/Office Supplies/Art","Any/Office Supplies/Binders","Any/Furniture/Chairs","Any/Technology/Copiers","Any/Office Supplies/Envelopes","Any/Office Supplies/Fasteners","Any/Furniture/Furnishings","Any/Office Supplies/Labels","Any/Technology/Machines","Any/Office Supplies/Paper","Any/Technology/Phones","Any/Office Supplies/Storage","Any/Furniture","Any/Office Supplies","Any/Technology","Any"],"labels":["Accessories","Appliances","Art","Binders","Chairs","Copiers","Envelopes","Fasteners","Furnishings","Labels","Machines","Paper","Phones","Storage","Furniture","Office Supplies","Technology","Any"],"name":"","parents":["Any/Technology","Any/Office Supplies","Any/Office Supplies","Any/Office Supplies","Any/Furniture","Any/Technology","Any/Office Supplies","Any/Office Supplies","Any/Furniture","Any/Office Supplies","Any/Technology","Any/Office Supplies","Any/Technology","Any/Office Supplies","Any","Any","Any",""],"values":[41936.6357,18138.005400000002,6527.787,30221.7633,26590.1663,55617.8249,6964.1767,949.5182,13059.1436,5546.254,3384.7569,34053.5693,44515.7306,21278.8264,39649.3099,123679.90030000001,145454.9481,308784.1583],"type":"sunburst"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"legend":{"tracegroupgap":0},"margin":{"t":60}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('42d4e888-7fd1-44c6-b131-3a96502107c2');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
px.treemap(product_data,
          path = ["Sales","Category","Sub-Category"],
          values = "Profit")
```


<div>                            <div id="a6c5f01e-3eb1-49d7-91a5-8ac8c526c5fc" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("a6c5f01e-3eb1-49d7-91a5-8ac8c526c5fc")) {                    Plotly.newPlot(                        "a6c5f01e-3eb1-49d7-91a5-8ac8c526c5fc",                        [{"branchvalues":"total","domain":{"x":[0.0,1.0],"y":[0.0,1.0]},"hovertemplate":"labels=%{label}<br>Profit=%{value}<br>parent=%{parent}<br>id=%{id}<extra></extra>","ids":["Any/Technology/Accessories","Any/Office Supplies/Appliances","Any/Office Supplies/Art","Any/Office Supplies/Binders","Any/Furniture/Chairs","Any/Technology/Copiers","Any/Office Supplies/Envelopes","Any/Office Supplies/Fasteners","Any/Furniture/Furnishings","Any/Office Supplies/Labels","Any/Technology/Machines","Any/Office Supplies/Paper","Any/Technology/Phones","Any/Office Supplies/Storage","Any/Furniture","Any/Office Supplies","Any/Technology","Any"],"labels":["Accessories","Appliances","Art","Binders","Chairs","Copiers","Envelopes","Fasteners","Furnishings","Labels","Machines","Paper","Phones","Storage","Furniture","Office Supplies","Technology","Any"],"name":"","parents":["Any/Technology","Any/Office Supplies","Any/Office Supplies","Any/Office Supplies","Any/Furniture","Any/Technology","Any/Office Supplies","Any/Office Supplies","Any/Furniture","Any/Office Supplies","Any/Technology","Any/Office Supplies","Any/Technology","Any/Office Supplies","Any","Any","Any",""],"values":[41936.6357,18138.005400000002,6527.787,30221.7633,26590.1663,55617.8249,6964.1767,949.5182,13059.1436,5546.254,3384.7569,34053.5693,44515.7306,21278.8264,39649.3099,123679.90030000001,145454.9481,308784.1583],"type":"treemap"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"legend":{"tracegroupgap":0},"margin":{"t":60}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('a6c5f01e-3eb1-49d7-91a5-8ac8c526c5fc');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


# #7 Data Exploration: Product Sales information (Sales, Quantity, Profit)


```python

```

Distribution Analysis on **Quantity** column 

Let's check the statistical summary of the column


```python
data.Quantity.describe()
```




    count    9994.000000
    mean        3.789574
    std         2.225110
    min         1.000000
    25%         2.000000
    50%         3.000000
    75%         5.000000
    max        14.000000
    Name: Quantity, dtype: float64




```python
px.histogram(data, x = "Quantity")
```


<div>                            <div id="96309a54-6bee-4e7b-996a-24215a9dd4be" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("96309a54-6bee-4e7b-996a-24215a9dd4be")) {                    Plotly.newPlot(                        "96309a54-6bee-4e7b-996a-24215a9dd4be",                        [{"alignmentgroup":"True","bingroup":"x","hovertemplate":"Quantity=%{x}<br>count=%{y}<extra></extra>","legendgroup":"","marker":{"color":"#636efa","pattern":{"shape":""}},"name":"","offsetgroup":"","orientation":"v","showlegend":false,"x":[2,3,3,2,3,2,9,2,3,2,4,4,1,3,3,7,3,2,1,1,2,5,6,3,5,2,7,2,6,3,3,6,4,5,3,2,3,6,4,10,4,5,5,7,4,2,7,1,3,5,3,3,3,4,3,1,2,5,3,2,3,3,6,2,3,8,3,2,3,2,2,13,4,1,3,1,2,2,2,6,2,5,5,2,3,3,4,2,5,1,4,2,7,4,2,2,1,3,2,3,2,3,6,3,2,2,2,3,3,5,3,2,14,5,2,3,4,2,5,3,3,3,4,3,4,6,3,3,3,3,5,6,2,6,3,5,2,3,1,5,8,3,3,5,3,3,4,1,3,5,2,3,6,2,3,2,6,5,5,1,2,3,3,3,2,4,3,3,5,6,2,3,14,3,2,2,2,1,2,6,1,4,12,2,4,3,3,3,4,1,2,4,2,1,3,4,7,7,3,2,2,6,10,6,7,3,6,2,3,4,4,10,3,2,3,2,7,6,3,4,4,3,5,3,4,3,2,3,3,1,2,5,7,3,3,4,3,3,5,2,3,4,3,5,3,6,2,2,5,6,4,2,7,2,5,3,2,4,2,4,3,1,3,3,5,2,5,3,5,7,7,3,2,7,2,2,2,1,7,2,5,1,4,2,2,4,7,5,7,5,2,3,2,2,3,2,5,6,2,1,4,3,2,3,7,2,5,6,1,4,5,4,7,1,2,7,2,2,3,3,3,3,6,2,2,1,3,1,7,5,9,3,2,3,2,1,8,3,4,1,8,1,3,3,7,2,6,2,7,6,14,5,3,2,7,4,3,4,12,10,13,4,2,6,2,2,3,3,3,4,4,5,11,3,3,5,2,4,5,6,5,3,8,1,3,2,2,8,4,3,3,5,5,2,3,5,6,2,3,3,2,2,2,5,9,2,1,3,2,2,2,3,5,2,3,5,5,3,2,3,3,7,2,2,6,4,7,4,3,2,2,2,1,2,3,2,8,6,2,3,3,4,5,3,5,3,4,7,3,2,7,5,1,3,6,5,5,8,2,3,9,1,4,3,2,3,7,6,8,3,2,2,2,2,3,5,3,1,4,3,2,9,5,9,4,2,5,2,3,7,2,8,6,6,1,3,3,7,7,3,1,2,2,9,5,2,2,1,2,3,2,2,2,5,3,2,2,2,2,2,3,10,6,12,4,1,4,4,6,2,3,4,3,3,5,4,3,3,3,7,2,6,6,5,4,7,4,5,6,3,2,3,6,3,2,7,3,6,4,2,2,2,4,2,2,9,2,2,10,2,3,3,1,2,3,3,2,3,3,6,3,7,4,2,3,7,2,2,2,7,6,5,1,4,2,9,5,3,3,2,2,4,3,5,3,4,8,3,3,5,2,3,5,4,4,7,2,2,6,2,3,2,5,1,3,3,3,3,1,3,2,3,7,4,7,2,2,1,4,2,3,3,5,6,3,3,3,3,9,1,2,5,11,1,5,5,4,1,1,4,8,3,5,3,7,3,6,4,1,7,7,5,5,3,2,5,6,1,2,4,2,3,5,3,3,3,2,2,5,6,3,3,11,2,1,2,2,1,3,6,4,6,3,2,6,5,2,1,1,3,3,9,3,4,2,5,4,5,5,4,3,3,4,9,4,2,7,3,2,9,8,3,1,3,7,2,5,1,2,2,4,3,3,4,2,2,1,2,1,2,3,2,2,4,3,3,2,4,3,6,2,1,3,1,5,2,1,5,2,3,5,5,1,4,2,3,10,2,6,1,3,5,6,3,3,10,1,5,8,2,8,4,5,1,4,7,2,2,9,5,3,3,3,2,3,4,8,9,3,13,11,2,2,7,6,5,8,2,2,1,4,3,3,5,2,2,10,2,3,2,2,1,5,5,8,1,9,3,2,5,13,2,7,5,2,3,2,2,1,3,7,2,1,2,3,8,4,2,5,3,3,4,2,11,1,3,3,6,3,3,8,7,4,5,2,2,1,1,2,1,1,3,7,7,13,6,8,2,3,6,5,1,4,3,5,5,3,8,3,3,4,6,7,4,4,5,3,3,9,2,2,4,7,2,1,2,2,13,1,2,3,3,3,9,2,4,1,6,9,3,4,3,2,2,3,6,3,8,14,3,4,4,2,1,5,3,4,7,3,4,3,3,1,3,8,2,2,5,4,3,4,3,2,3,4,2,2,3,5,9,3,6,3,3,2,2,1,7,3,3,3,3,5,1,5,5,2,2,8,6,3,2,1,5,4,4,4,5,1,2,2,3,5,2,3,6,3,3,3,2,5,3,2,2,3,2,2,8,2,2,9,3,3,3,5,2,2,6,4,3,1,5,9,3,5,2,8,6,6,5,4,2,2,3,2,1,6,6,9,6,3,3,7,3,5,5,5,7,4,2,3,7,5,2,5,1,2,5,2,6,1,3,2,7,2,1,3,3,4,5,3,5,2,3,5,2,6,2,4,5,3,5,3,2,5,1,2,5,4,3,9,9,4,7,2,2,2,4,3,1,5,6,3,3,5,1,2,10,2,5,2,2,3,4,3,1,2,3,3,6,7,6,7,2,3,4,5,6,2,2,4,3,2,5,6,9,2,1,3,2,2,2,3,2,5,3,3,9,3,3,3,2,3,2,2,1,9,2,1,4,3,3,5,4,2,3,5,5,2,9,5,4,3,2,3,4,3,4,2,2,2,8,2,2,6,2,6,4,1,2,3,3,11,5,1,3,2,3,5,8,3,2,4,1,5,6,4,11,2,2,3,2,1,1,2,2,2,9,4,3,9,4,6,6,1,3,3,7,1,3,2,1,2,2,2,6,3,5,3,1,2,3,3,4,2,3,3,2,3,2,5,4,5,5,2,5,2,2,3,5,10,4,3,2,1,3,2,2,3,7,7,1,6,5,7,2,2,2,4,1,11,4,1,3,5,1,5,2,2,5,3,5,4,2,3,2,4,4,1,4,7,4,4,5,3,13,3,9,5,1,2,2,3,3,5,3,2,3,4,1,6,6,6,5,2,6,3,1,3,5,3,6,6,4,4,3,1,1,1,3,3,1,4,3,5,3,4,4,4,3,2,3,3,3,4,5,4,2,3,2,2,5,6,2,2,2,2,6,5,4,8,3,2,13,2,3,9,8,5,3,2,2,2,5,3,3,1,2,5,3,3,4,3,9,3,2,2,5,12,3,6,3,2,3,3,5,3,10,2,2,7,1,6,6,7,3,3,2,2,2,4,3,2,2,6,9,3,7,3,3,2,4,4,4,1,1,2,7,3,6,4,5,3,4,1,2,3,2,2,2,6,5,6,5,3,6,7,3,4,3,3,5,4,3,3,7,6,3,2,4,3,7,6,9,2,4,3,5,1,8,8,8,3,5,3,3,2,3,2,3,1,1,2,2,2,6,5,2,3,1,5,7,8,4,3,4,2,5,5,3,9,2,1,4,2,4,4,7,3,1,1,2,3,6,3,2,3,2,3,7,5,2,4,4,10,3,9,4,3,2,3,3,2,5,3,4,3,2,6,2,2,4,5,2,7,7,3,5,3,3,5,10,2,5,3,3,2,3,3,7,4,1,5,2,6,4,3,3,5,4,8,6,2,1,2,5,1,6,3,3,2,7,6,4,2,5,1,7,4,3,4,6,3,1,5,2,3,2,1,3,1,6,5,2,1,9,5,2,3,3,1,3,3,7,2,5,2,3,3,3,2,2,7,4,4,7,6,2,5,3,4,2,1,5,4,1,5,3,7,3,2,4,3,6,2,5,4,3,3,2,5,4,3,1,3,7,3,3,4,4,5,4,1,9,3,3,3,5,2,4,2,5,2,7,5,4,3,6,4,3,2,4,7,3,5,2,2,2,2,2,5,4,7,9,4,6,2,2,2,3,4,8,2,4,3,7,3,1,7,5,6,3,5,5,8,3,8,4,5,3,1,4,4,2,4,7,3,3,1,2,2,4,7,4,4,9,6,2,3,8,4,2,4,5,3,3,3,7,2,2,1,4,3,7,3,2,2,4,3,3,5,10,7,2,5,5,3,2,2,6,2,2,3,3,6,4,3,4,2,7,4,3,3,1,3,2,3,6,3,12,3,2,3,1,6,3,3,1,4,1,1,2,3,4,4,2,3,5,7,2,9,2,6,7,5,2,2,2,4,5,5,1,4,7,2,3,4,3,3,3,5,14,5,5,6,1,2,2,4,1,3,2,3,3,2,2,5,2,7,2,2,3,7,5,3,5,3,7,2,3,5,1,3,6,6,3,2,1,4,6,4,4,13,11,1,3,5,2,1,1,2,3,1,3,1,7,1,2,3,5,2,1,6,2,2,4,5,3,3,3,3,3,3,3,5,6,8,2,4,5,1,3,3,4,3,6,3,3,4,6,3,14,2,1,6,9,4,4,5,5,9,2,6,4,3,3,5,4,6,3,3,6,3,4,5,1,6,2,3,3,2,3,3,2,3,7,3,1,5,3,4,4,6,2,3,3,7,7,5,3,7,7,2,9,2,2,3,5,2,3,3,2,5,3,9,5,3,14,2,2,1,6,6,3,5,2,5,3,3,2,4,4,2,3,2,3,2,9,2,4,3,8,2,7,4,1,2,3,5,8,5,2,4,1,13,6,3,7,3,2,2,3,4,3,2,9,1,3,2,3,3,2,4,5,3,9,2,5,1,2,3,2,2,2,4,6,5,5,9,3,3,1,3,2,2,5,5,3,2,5,6,3,2,6,3,7,2,1,3,7,1,4,2,4,6,2,4,1,7,2,9,6,3,8,2,2,2,2,6,4,4,3,3,6,1,7,4,2,7,7,2,5,2,2,6,1,2,3,3,2,2,2,7,3,2,3,2,5,6,1,3,3,1,7,3,3,5,2,6,2,3,4,2,3,8,4,2,3,3,4,3,2,5,2,2,1,3,5,3,3,1,2,1,3,4,2,2,2,3,7,4,6,3,2,5,2,2,8,9,4,3,8,3,1,2,3,14,4,2,2,3,2,1,7,9,4,9,4,4,2,4,4,3,11,2,5,3,3,3,6,8,3,7,5,3,3,1,5,1,6,5,3,3,3,4,4,2,4,5,5,5,3,3,3,3,5,2,7,3,2,4,3,1,2,2,2,2,2,1,6,7,4,5,4,2,5,1,6,8,3,4,2,3,6,2,9,3,2,4,6,8,3,3,3,3,3,4,2,3,1,5,2,4,2,3,3,3,2,2,6,3,2,1,1,4,4,2,2,2,3,3,1,5,1,3,4,7,3,2,9,7,1,3,3,2,4,3,13,1,5,3,2,5,2,3,6,6,1,2,1,2,3,3,6,3,2,2,4,1,7,3,2,2,4,2,6,3,3,2,5,2,3,3,3,3,1,2,3,5,5,2,3,3,1,1,8,2,3,3,3,1,2,3,2,3,5,3,8,3,1,3,4,3,2,10,5,1,5,1,3,5,5,5,3,3,1,2,6,3,3,3,3,3,6,2,2,3,3,2,2,2,4,3,6,7,7,2,7,7,2,4,2,6,2,2,7,3,2,3,3,2,3,3,3,2,4,5,7,3,7,3,3,6,6,4,2,4,2,4,1,3,5,4,3,7,4,8,2,3,2,2,3,4,10,5,4,3,2,4,4,8,4,2,7,7,2,6,3,4,7,5,3,9,6,7,3,2,2,3,7,13,4,2,7,2,4,5,1,1,1,2,3,3,2,5,5,1,1,3,7,3,3,5,3,3,4,5,5,3,3,4,2,5,3,3,7,6,6,8,2,4,5,7,2,7,2,6,2,1,6,8,7,2,2,2,10,2,4,3,2,2,3,9,2,5,4,5,3,3,7,2,10,4,7,2,2,3,5,3,4,5,3,2,3,5,7,6,2,2,2,4,3,5,2,5,2,2,4,2,2,2,5,6,2,3,1,3,2,1,5,3,2,6,2,2,4,1,6,3,2,2,3,3,2,3,4,4,3,2,4,3,3,7,5,2,3,2,2,2,2,3,5,1,2,2,2,3,6,7,3,2,4,7,1,3,2,4,3,3,3,2,2,2,9,3,2,5,6,3,3,3,4,3,9,8,2,1,5,2,2,4,6,3,4,2,1,1,3,2,2,3,4,10,3,1,3,2,5,6,2,3,1,2,9,2,4,3,2,3,2,5,3,3,5,2,2,4,3,3,5,2,5,5,6,9,4,3,3,2,3,3,2,2,3,4,7,3,3,2,3,7,3,5,8,6,4,3,4,2,7,2,4,7,9,2,4,3,1,2,2,6,6,9,6,2,4,3,6,3,1,10,3,4,9,3,4,5,2,1,4,2,1,2,1,1,7,5,4,5,5,2,5,5,2,3,3,3,6,14,9,3,2,4,9,5,2,2,5,2,5,2,6,3,3,3,2,3,3,3,6,4,7,3,6,7,7,3,4,6,3,2,4,1,2,2,2,1,5,7,3,3,2,3,5,3,3,1,3,3,9,2,10,4,2,1,2,1,2,2,7,3,1,2,2,5,2,3,5,5,2,9,3,4,3,2,3,1,4,4,3,4,1,7,5,2,2,3,3,5,3,7,4,3,2,3,7,5,3,2,2,8,3,3,7,1,4,3,2,3,2,4,9,7,3,3,2,1,3,2,1,3,12,4,4,2,3,6,1,6,2,6,4,2,3,9,4,2,3,5,2,3,8,5,5,4,3,3,2,3,7,7,3,3,3,2,3,14,1,5,2,4,1,3,1,3,1,5,11,9,2,5,5,5,3,2,1,5,7,2,7,5,3,1,9,5,4,4,1,2,6,1,5,2,1,2,7,1,3,5,6,1,2,2,3,3,2,2,5,5,2,2,4,2,3,4,9,5,6,3,3,2,4,3,1,3,4,1,9,1,2,2,5,2,1,3,7,4,4,3,2,5,2,2,2,7,6,3,6,5,8,3,9,4,2,2,2,6,6,1,4,4,4,2,6,7,1,1,3,4,9,3,4,2,1,2,2,5,1,2,2,4,7,4,5,1,4,2,4,3,3,7,7,3,1,3,6,3,9,5,5,3,2,2,3,4,3,7,1,4,8,2,3,2,2,2,1,4,4,5,6,3,3,4,2,2,7,2,2,7,5,2,3,5,3,2,6,6,3,2,2,2,2,1,7,4,2,14,9,4,2,4,2,2,7,14,3,5,2,2,4,2,3,6,11,6,5,4,3,4,2,4,1,5,4,6,7,2,4,8,4,7,2,2,3,2,2,3,3,5,2,3,2,5,4,1,2,2,4,10,6,3,4,3,2,1,4,2,5,2,2,2,7,2,1,2,6,6,9,2,1,2,3,4,2,3,2,1,1,1,3,4,2,2,2,2,2,7,4,3,9,2,1,6,6,5,4,5,7,9,2,2,7,5,2,3,6,5,4,5,4,5,5,12,1,2,2,3,3,3,3,3,3,2,2,2,6,1,6,2,5,2,4,4,4,2,1,3,6,5,3,5,5,1,4,1,2,5,3,4,14,2,2,2,1,5,2,3,4,3,2,4,4,5,1,4,3,2,2,5,3,8,2,3,7,4,5,5,2,3,2,3,4,3,6,3,7,3,1,5,2,4,3,3,5,2,1,4,6,2,2,8,7,3,1,2,1,5,10,3,5,6,3,2,6,3,2,3,3,3,5,3,6,5,1,7,3,6,2,3,1,4,7,7,2,2,1,8,2,9,3,4,2,1,1,7,3,3,2,8,7,4,8,4,3,1,5,3,5,6,2,3,2,7,10,2,3,5,1,7,4,5,2,1,3,4,2,4,5,5,4,2,1,4,4,5,3,14,1,5,3,7,2,2,2,3,4,1,4,5,7,2,1,2,2,2,1,4,7,3,2,5,7,6,11,2,9,4,3,3,7,10,2,3,3,3,4,3,4,6,6,4,3,3,2,3,7,3,2,2,10,3,1,2,2,5,9,5,4,5,3,1,3,3,5,7,1,3,11,5,6,3,2,3,2,7,1,5,2,4,3,5,3,11,5,2,3,2,3,3,7,6,5,3,3,2,5,3,3,1,3,2,2,5,3,6,2,7,2,7,3,5,1,2,3,5,5,1,3,7,7,4,2,3,5,7,6,9,3,3,5,6,3,7,6,3,3,2,2,3,2,3,2,5,5,3,2,2,2,4,3,3,4,3,6,6,9,3,2,13,5,3,4,3,9,3,3,5,2,2,6,3,2,5,2,4,7,4,5,3,5,3,4,5,4,2,4,2,6,3,4,2,2,6,4,4,5,6,3,3,4,7,3,2,3,3,7,9,2,4,4,3,3,1,2,1,2,6,6,2,2,3,5,2,8,2,2,5,4,3,7,5,5,5,2,3,2,6,4,3,10,3,2,5,4,3,2,3,2,4,2,6,3,6,4,2,2,8,7,3,6,3,2,4,9,2,8,5,5,11,4,3,5,3,1,5,4,3,3,3,8,3,3,2,1,6,2,5,3,3,3,3,4,6,5,2,9,5,2,3,8,3,4,5,2,1,9,4,9,4,2,3,2,4,5,7,4,2,3,3,12,3,2,2,4,7,3,4,2,7,3,5,3,4,2,4,2,4,5,5,9,9,2,5,2,6,4,3,1,2,3,5,2,7,2,4,6,5,5,2,7,4,4,7,5,3,3,5,3,3,7,3,2,4,2,5,2,2,2,5,3,6,3,2,6,8,2,6,2,6,8,7,2,3,4,5,6,1,1,9,2,3,5,2,5,1,7,9,2,4,4,3,1,2,6,5,2,6,2,5,3,11,4,3,2,9,2,5,5,1,2,1,2,3,2,6,7,7,1,4,1,6,2,2,3,5,1,2,2,4,2,3,11,5,3,3,5,3,2,9,4,4,2,5,1,3,2,2,4,3,4,2,7,4,2,6,5,5,2,3,3,1,2,4,2,2,4,3,2,3,2,1,2,2,2,2,3,2,7,3,2,6,4,9,3,1,1,5,3,9,2,5,2,4,1,2,2,3,5,1,5,8,8,9,4,2,4,3,2,3,4,5,3,4,3,9,2,2,5,3,4,3,3,4,2,2,4,1,2,1,2,6,3,8,7,13,2,2,2,3,2,1,7,4,2,4,4,2,4,7,4,2,3,7,7,7,2,7,2,4,2,4,6,2,4,5,4,2,2,2,3,2,3,3,1,6,2,1,2,4,5,1,6,3,5,2,5,2,2,3,2,9,8,3,3,3,3,4,2,3,9,9,7,4,7,2,3,2,2,2,6,3,3,3,3,8,5,3,2,5,12,2,4,4,2,2,3,2,5,7,3,2,2,2,1,4,6,6,2,2,1,3,5,3,2,7,6,7,5,2,9,4,2,5,14,3,3,2,8,2,4,2,2,1,3,2,3,9,3,2,4,3,3,1,7,2,5,5,4,8,2,4,6,3,4,3,4,6,2,13,7,4,5,3,5,3,1,7,2,4,9,2,9,4,3,1,4,2,3,3,5,1,8,2,1,4,5,7,2,8,5,2,4,2,2,2,3,1,9,5,3,4,2,3,3,3,3,7,3,4,2,4,4,3,5,2,4,3,2,3,7,4,6,3,1,7,3,6,3,3,4,2,4,1,1,4,3,6,3,3,2,3,3,2,3,2,1,5,3,2,4,3,7,2,3,7,5,1,3,5,9,3,5,3,2,3,6,7,2,1,7,2,8,3,5,1,3,3,7,3,3,3,3,3,7,5,3,7,2,3,1,4,3,1,4,2,1,3,3,2,5,3,4,3,3,5,2,5,2,3,2,3,5,8,9,3,4,1,5,5,1,5,1,3,3,1,8,4,4,2,2,4,2,5,3,4,5,2,2,3,7,2,3,1,5,5,5,2,5,3,5,2,2,2,4,5,2,3,5,2,2,1,6,7,5,2,5,7,2,2,14,4,3,5,5,2,2,3,2,5,2,3,3,1,4,3,1,2,1,4,2,4,7,3,3,1,5,2,2,7,2,4,3,2,1,3,5,3,5,3,3,5,1,4,2,4,1,2,7,8,5,3,8,6,4,5,2,1,3,2,6,3,4,3,1,6,3,5,1,2,8,6,3,3,4,4,2,3,5,3,4,9,4,2,3,2,3,3,2,3,7,4,5,3,3,2,3,2,3,9,4,4,4,5,6,1,4,5,6,5,4,2,3,2,2,6,4,9,2,2,5,4,2,3,3,4,2,5,9,7,1,3,3,1,3,3,4,5,3,1,3,5,4,2,5,4,7,5,3,2,2,5,7,2,3,4,5,7,2,7,3,5,3,1,8,5,3,2,5,4,4,4,3,1,3,2,2,4,1,5,2,4,2,2,2,3,5,3,5,5,5,3,8,3,4,8,3,9,5,1,6,2,2,2,5,2,5,5,2,7,6,3,1,6,2,3,6,1,3,3,2,2,3,3,2,4,3,2,3,7,2,2,3,3,2,1,2,3,3,2,9,3,2,3,2,4,3,5,3,2,3,3,5,2,1,7,5,3,3,2,3,2,6,1,4,5,3,3,5,3,1,2,7,2,2,2,4,3,8,7,5,5,4,3,2,3,2,2,2,2,2,7,2,1,4,6,6,5,2,5,4,4,2,2,2,1,2,3,4,1,6,4,5,3,6,7,2,3,5,1,2,8,3,8,4,4,3,4,4,3,9,4,7,6,2,2,8,3,1,3,4,3,3,1,5,8,2,5,5,4,8,4,2,4,7,5,5,9,2,2,3,2,3,10,2,6,2,3,4,2,5,5,2,1,1,9,4,3,3,5,4,3,2,4,9,4,6,2,1,3,5,2,1,3,2,3,2,6,3,7,3,3,2,3,2,5,3,2,9,3,6,5,2,8,8,2,13,4,1,7,3,2,3,5,5,5,1,5,7,6,5,5,5,6,2,2,8,4,2,3,1,6,6,10,2,2,2,9,2,3,3,4,2,3,3,6,3,12,3,1,2,2,2,3,5,3,5,3,1,4,5,3,2,4,2,2,6,3,4,6,3,6,3,3,3,2,3,3,9,2,3,5,7,4,3,4,2,5,6,5,1,1,3,3,2,3,5,4,2,8,7,3,4,3,14,2,3,4,3,2,6,3,2,3,3,4,4,7,1,2,7,9,2,6,3,2,3,8,9,5,3,3,2,7,4,3,5,1,2,4,2,3,7,7,5,3,1,2,2,3,3,2,4,5,1,4,6,3,2,3,4,2,3,6,5,2,3,2,2,2,2,3,4,2,3,3,7,1,2,2,3,6,2,2,6,3,8,2,1,5,6,7,4,3,7,5,5,4,3,1,2,7,2,3,4,4,1,9,4,3,6,2,2,3,3,5,2,9,1,4,3,1,2,5,3,2,5,5,3,4,3,2,7,2,2,2,3,2,2,4,3,6,3,7,7,2,9,1,1,3,2,5,2,8,1,2,5,7,2,5,2,5,2,4,3,5,3,5,1,5,1,2,1,5,5,2,7,2,2,8,9,5,4,3,2,2,5,1,9,4,3,7,2,3,4,2,6,4,3,3,2,6,7,1,5,4,2,2,8,7,4,3,1,9,3,7,7,2,2,5,5,3,5,5,5,3,3,9,2,2,2,4,3,3,3,2,3,3,2,2,3,3,2,8,1,5,1,3,1,3,2,7,3,2,3,3,4,1,8,3,5,3,1,10,1,6,4,3,2,2,6,5,5,5,5,1,2,1,1,2,7,3,2,1,2,8,5,3,2,3,2,5,5,5,2,8,4,2,1,5,4,2,1,2,2,5,5,7,5,4,1,5,4,2,4,6,5,1,9,9,1,8,4,2,8,3,5,5,5,2,7,6,3,3,5,3,2,3,2,4,2,3,4,1,4,7,2,2,2,2,2,3,2,3,12,2,9,2,5,2,3,3,1,7,4,9,2,3,4,6,3,2,3,5,2,2,4,3,5,9,7,5,2,7,1,6,4,2,7,2,7,4,3,3,2,2,1,2,2,8,3,6,2,3,5,2,2,3,3,3,4,3,3,1,3,7,3,5,2,4,9,3,1,4,1,8,6,5,2,2,3,4,9,2,9,5,9,2,10,7,2,2,2,2,2,3,2,3,2,8,6,5,5,8,3,7,3,1,2,5,3,5,6,6,4,4,1,6,5,2,3,3,3,8,6,4,2,5,3,1,2,3,3,3,4,2,1,4,5,1,5,1,4,3,3,5,1,4,9,2,8,3,3,9,4,4,3,4,3,3,7,2,7,4,2,10,4,3,4,5,6,2,7,2,6,2,4,2,3,2,4,4,1,2,5,1,1,1,5,3,6,4,4,3,3,3,1,5,3,8,9,3,3,5,2,7,2,4,2,5,9,7,3,1,2,2,3,2,7,4,3,6,2,3,8,2,3,3,5,5,8,5,1,1,3,3,2,5,4,3,5,4,3,5,2,6,2,3,3,2,3,3,9,3,5,8,3,2,2,4,2,2,7,1,3,2,6,3,2,2,3,4,7,2,3,8,3,3,7,5,4,2,2,3,3,9,3,2,6,1,4,2,3,2,3,3,3,4,7,3,2,1,2,1,4,2,1,2,5,2,4,4,3,2,8,4,4,2,4,7,2,2,3,2,1,3,5,3,2,5,2,5,2,4,9,2,3,1,2,2,5,3,13,2,8,1,3,4,4,3,5,3,4,3,3,1,3,3,3,4,2,2,3,3,3,6,2,5,2,3,14,5,4,3,2,4,5,2,7,3,1,5,2,2,4,2,3,4,3,5,2,2,2,4,2,3,5,5,3,1,2,3,2,1,2,4,9,1,9,2,1,4,1,3,2,3,3,2,3,2,2,5,6,3,2,7,4,3,3,9,2,5,9,2,2,1,2,5,2,4,2,7,2,6,2,9,5,3,2,2,2,3,7,6,8,2,7,3,5,3,2,4,6,4,3,2,7,3,5,1,2,5,3,9,7,5,2,5,2,1,4,1,2,2,3,8,5,9,2,3,1,4,11,4,5,1,3,1,2,2,5,2,3,5,3,3,2,3,5,1,4,2,5,5,2,2,6,3,7,2,3,3,4,4,1,5,4,3,3,7,1,9,3,2,5,1,1,5,4,2,4,3,8,6,2,3,7,5,2,2,6,4,2,2,2,2,5,7,3,2,1,9,3,3,4,5,6,4,5,3,2,12,2,2,2,8,6,5,4,1,2,4,4,1,1,3,2,4,2,3,3,2,3,5,3,1,5,5,3,2,5,7,1,2,3,4,2,3,6,14,3,2,1,1,1,3,2,3,7,5,4,7,5,9,2,8,3,1,2,6,3,6,7,4,1,2,3,7,1,5,1,5,6,3,3,4,1,5,7,7,4,2,7,3,3,6,2,6,3,4,3,3,3,4,4,8,2,3,8,2,2,9,6,1,4,3,5,3,3,7,5,10,5,4,1,3,2,3,5,14,4,1,3,4,7,3,2,2,3,5,3,1,4,5,4,2,7,3,5,8,6,5,3,3,3,3,3,1,5,5,2,2,3,6,5,2,3,7,3,3,5,2,3,9,3,7,2,5,4,7,1,3,2,3,7,3,12,2,7,3,1,5,3,4,3,2,6,3,2,3,4,6,7,1,2,10,2,7,4,3,2,1,8,3,3,3,1,2,6,4,3,3,2,7,5,3,5,1,5,5,4,2,2,2,3,5,8,2,3,2,2,2,3,2,2,3,2,2,3,4,4,2,3,4,5,2,2,3,3,2,2,4,3,4,2,3,3,1,7,2,3,2,5,4,4,7,6,2,3,7,3,7,5,1,7,1,4,4,5,3,3,5,9,7,4,7,1,3,2,2,1,7,3,6,4,2,3,2,4,2,3,3,2,3,11,3,3,6,1,2,3,9,3,2,2,2,8,6,3,7,2,7,2,5,6,7,2,4,3,4,1,2,2,7,7,5,2,5,3,2,1,5,2,3,2,3,2,4,3,2,3,2,2,3,4,1,1,7,3,2,4,5,5,5,3,4,3,4,1,5,1,2,2,6,2,6,4,5,2,4,5,2,2,5,5,6,3,2,2,2,2,3,12,3,6,2,3,2,8,5,3,1,7,2,4,5,3,2,3,2,2,3,7,1,3,7,2,12,3,3,7,3,3,5,2,2,2,1,3,4,7,4,2,8,3,3,1,6,9,2,6,7,5,2,5,3,5,2,3,2,4,1,4,5,4,6,2,1,3,2,3,8,2,3,3,4,6,5,2,3,3,7,8,5,3,1,2,2,8,1,4,3,9,4,3,2,3,4,8,2,5,7,2,8,3,9,9,6,2,2,4,3,1,6,4,5,7,3,5,1,5,5,6,2,6,2,2,6,3,8,7,6,3,3,4,2,2,1,4,3,7,2,3,5,6,5,7,3,2,4,2,5,9,3,3,2,3,8,2,4,4,1,3,3,3,3,3,3,3,3,1,3,2,5,7,4,6,10,9,8,5,3,4,2,3,1,2,2,8,3,2,8,6,5,4,4,3,3,6,1,2,1,1,4,3,3,2,3,3,3,3,11,9,8,1,3,5,7,1,2,8,1,14,3,7,13,2,4,7,3,7,1,7,1,2,5,3,5,7,2,3,3,5,3,6,7,2,2,7,7,7,5,2,3,3,2,7,3,3,2,2,1,1,7,1,4,1,4,8,7,3,2,9,4,6,3,5,2,12,3,3,2,1,5,4,5,2,3,3,3,3,7,1,2,4,2,5,9,5,2,5,5,4,7,5,5,4,4,5,4,4,3,3,3,7,2,6,4,5,6,4,3,4,3,7,5,5,3,2,4,4,4,2,2,6,2,10,6,2,1,3,3,3,2,3,2,3,5,3,3,2,7,13,10,2,3,1,6,3,7,5,2,5,2,3,6,8,3,2,3,4,2,3,3,4,4,5,4,7,4,2,6,5,6,3,5,2,2,4,5,3,10,1,2,2,8,1,4,4,3,3,2,2,4,5,7,2,3,3,9,2,2,2,3,1,2,4,3,6,5,7,7,3,8,9,3,3,2,7,3,3,8,7,7,4,3,2,2,2,3,5,1,9,2,2,5,3,2,2,2,2,3,2,5,3,1,3,3,3,4,2,8,2,1,6,7,5,3,4,3,2,6,2,3,6,1,6,7,6,1,1,5,4,4,2,2,3,2,3,3,4,7,5,2,4,11,4,4,5,2,14,5,5,6,2,5,2,1,5,2,3,6,8,3,7,2,3,7,1,11,3,2,3,2,6,1,5,5,6,3,5,2,4,9,7,5,3,2,5,5,4,7,2,5,2,2,4,1,1,1,5,4,2,8,8,2,1,7,4,3,4,7,3,2,2,4,1,4,1,3,2,2,3,3,5,5,3,4,3,5,1,7,3,5,7,6,4,4,1,5,3,5,3,3,2,3,5,2,6,1,2,4,2,5,3,3,3,2,7,2,8,4,2,7,3,3,3,3,3,5,3,9,2,1,1,4,3,8,2,2,5,3,1,5,2,4,7,2,7,3,1,2,4,1,3,4,4,2,2,2,9,2,4,2,4,5,2,3,1,3,2,2,5,2,1,3,5,5,5,4,6,5,1,3,4,2,5,4,4,2,2,2,4,2,3,7,4,2,4,3,8,3,3,3,1,1,2,6,3,2,3,3,1,5,5,3,3,4,5,1,1,2,1,5,2,6,3,3,2,3,3,3,7,2,2,1,2,2,9,1,3,3,3,5,1,5,6,5,4,5,5,3,5,2,7,4,4,3,8,4,2,4,2,2,1,4,7,7,4,1,2,6,2,3,6,3,2,8,5,7,3,8,1,5,2,1,1,1,4,2,3,4,4,2,3,2,2,6,9,4,2,1,3,6,4,7,2,2,3,3,6,2,2,5,8,5,2,2,1,2,4,2,1,4,3,4,3,5,4,4,1,1,3,1,3,9,7,2,5,1,3,4,2,1,8,1,5,6,2,2,3,4,2,3,2,7,8,2,2,5,3,1,8,3,6,6,2,2,2,3,1,8,3,8,5,6,2,2,6,1,3,3,3,6,3,5,5,3,7,3,7,4,3,3,7,2,5,7,7,3,6,6,2,4,1,2,2,2,7,7,1,5,1,4,2,6,1,3,7,6,3,3,4,5,6,2,8,4,2,3,3,2,4,2,3,1,2,3,4,5,9,4,2,4,2,3,3,7,1,2,1,3,2,3,3,2,8,3,5,5,4,3,2,2,2,2,2,3,2,4,5,3,1,2,5,1,7,7,9,4,2,2,3,5,5,1,2,1,5,2,3,2,8,2,5,4,5,3,5,1,5,7,13,9,8,2,5,3,2,3,3,13,3,3,6,3,2,4,4,3,3,4,4,1,1,2,4,1,3,5,3,2,2,3,3,2,2,5,4,5,6,3,3,2,4,3,3,8,2,3,1,3,3,4,4,2,2,3,2,5,1,4,3,1,2,3,5,3,1,7,2,5,2,8,4,5,1,6,5,5,5,2,8,3,3,3,3,3,1,3,5,3,3,4,5,3,2,1,4,2,4,3,5,1,4,5,5,4,11,3,6,5,8,2,3,3,2,2,5,3,3,3,4,5,4,2,2,1,3,7,3,4,3,9,3,4,1,3,2,3,3,3,2,6,7,7,2,2,1,6,5,4,2,1,3,5,2,2,1,2,5,10,2,2,1,7,2,3,9,4,3,3,5,3,8,1,3,2,4,7,4,4,1,2,3,2,5,1,3,3,3,2,3,7,2,2,4,2,5,6,4,2,4,3,8,5,2,5,2,4,5,3,3,5,5,4,3,2,2,7,2,4,5,5,4,8,1,1,3,3,5,4,1,5,2,2,1,3,8,2,1,3,9,10,7,5,4,7,3,4,6,11,4,5,3,4,5,2,1,2,7,1,3,4,6,8,2,3,3,2,3,1,5,4,3,3,1,2,2,6,2,7,2,2,5,2,2,5,3,2,5,4,5,1,4,5,8,5,2,3,3,9,3,2,2,5,1,3,5,9,9,2,2,5,5,2,3,1,5,5,2,3,2,5,7,2,2,2,2,2,1,1,2,3,2,1,1,2,3,6,7,5,5,3,3,2,2,2,7,2,1,7,3,7,6,5,1,4,3,2,9,7,6,1,1,2,3,4,12,2,4,4,2,4,1,9,5,1,3,10,2,4,3,8,5,3,2,2,3,7,1,7,3,1,3,5,2,3,3,3,2,5,8,1,2,3,2,2,6,5,5,3,3,2,5,3,5,3,4,2,3,8,3,3,4,3,4,2,4,3,5,5,4,3,1,1,2,3,5,1,2,6,1,2,1,4,1,3,3,3,5,4,5,2,2,6,8,1,6,2,1,2,4,5,6,1,2,2,6,7,2,2,4,5,3,3,5,9,10,1,7,2,2,2,7,2,3,6,7,3,4,3,5,1,3,2,2,2,7,4,2,3,3,2,2,5,4,3,8,1,2,5,4,6,3,1,8,5,3,5,7,5,4,4,3,5,6,2,3,3,1,4,3,2,1,5,2,3,4,4,2,3,3,3,2,3,3,3,7,4,2,4,7,1,3,3,2,3,5,1,5,4,3,1,8,8,5,3,2,6,2,7,1,2,2,3,7,5,4,2,3,3,4,2,3,3,4,1,3,5,3,9,6,3,2,9,1,3,3,8,1,6,3,2,4,3,8,2,2,1,2,3,6,2,4,5,3,1,5,2,8,5,6,5,3,3,2,2,5,3,1,9,8,3,3,3,3,2,3,8,6,2,1,2,4,3,3,5,2,6,3,3,14,9,1,4,8,5,4,3,3,12,3,5,3,3,3,2,9,3,3,2,2,2,3,1,2,3,3,9,5,3,1,2,7,2,5,7,5,2,3,3,3,4,1,4,4,5,4,7,1,2,6,2,2,6,4,3,3,3,1,4,1,3,10,2,9,4,9,9,1,4,3,6,3,3,1,2,2,3,3,3,3,2,4,3,3,7,4,5,3,3,2,5,2,4,2,8,2,2,2,2,3,6,3,5,6,5,9,2,5,4,2,5,5,3,3,6,4,5,6,5,3,5,6,1,1,2,9,2,2,7,4,5,3,3,4,3,2,3,9,5,5,2,3,2,3,6,2,3,3,3,2,2,2,3,2,4,5,2,2,5,2,5,5,5,2,5,4,2,2,4,3,2,2,2,4,5,3,2,2,1,3,2,7,4,3,7,6,2,4,1,9,2,3,6,3,2,4,5,1,2,7,9,3,6,4,2,4,3,2,4,5,5,4,3,9,3,3,3,5,6,4,4,1,7,1,5,3,5,3,4,4,3,1,8,5,3,2,1,4,4,5,3,3,2,3,1,2,2,9,2,2,3,4,5,7,2,4,7,3,1,3,2,1,2,4,6,5,3,2,5,2,7,3,5,3,3,2,5,3,1,3,2,1,6,2,9,2,9,4,8,3,3,5,6,5,3,10,2,1,4,3,2,1,2,4,3,3,5,1,5,2,5,9,5,2,6,11,4,4,2,8,7,5,4,4,5,5,3,3,6,4,1,8,3,3,2,5,6,3,7,7,3,5,4,2,3,1,6,2,3,6,8,2,4,3,3,3,2,3,9,6,9,3,4,2,3,4,2,2,2,8,5,2,3,2,7,3,4,9,3,9,2,5,3,3,1,9,2,2,3,1,3,2,6,5,3,3,4,1,3,6,6,7,4,2,2,4,3,4,3,4,4,3,7,6,5,4,1,2,5,1,3,9,1,2,13,2,5,2,6,1,2,4,8,2,1,2,5,2,4,2,5,6,2,2,4,1,4,2,5,1,3,3,8,3,3,1,14,8,5,7,4,5,6,5,2,3,5,5,3,4,2,9,7,2,7,2,3,3,1,3,7,9,4,2,5,1,4,7,5,1,4,3,3,2,2,2,3,3,4,7,3,2,4,5,3,4,5,1,2,8,1,5,2,5,1,3,5,3,5,5,4,2,5,3,6,3,2,5,2,1,4,4,2,2,5,3,7,2,2,3,1,5,3,2,4,4,5,4,6,8,6,2,7,4,4,7,2,1,9,5,3,3,3,2,3,2,2,1,3,5,1,2,4,1,2,4,2,3,4,3,3,2,3,5,1,5,8,7,5,2,4,2,3,4,3,9,3,4,6,7,5,1,2,7,2,4,4,2,5,5,3,7,4,9,3,2,4,2,5,6,5,1,1,2,1,3,2,2,2,2,3,2,2,4,3,5,3,7,6,3,3,3,4,2,4,3,2,2,3,1,2,3,3,6,5,2,5,4,6,2,7,5,4,5,4,3,5,8,1,4,2,2,3,3,6,11,5,2,5,2,3,3,5,7,5,7,5,3,3,2,1,4,2,4,2,1,5,2,2,5,7,9,3,3,8,3,1,3,2,1,2,7,2,5,7,3,3,5,8,6,9,4,2,3,10,7,7,1,2,5,2,2,3,1,4,5,2,2,2,3,1,1,6,2,3,5,5,6,3,3,3,3,3,2,3,2,4,2,4,5,3,2,3,3,3,4,7,3,4,2,4,4,7,2,2,2,5,3,8,2,3,5,3,2,5,2,8,2,2,4,5,2,2,3,3,3,3,9,2,2,11,3,3,4,2,1,2,3,5,2,1,1,2,7,1,2,2,7,2,3,5,4,2,2,2,7,3,9,1,4,7,5,2,3,8,1,9,3,6,3,2,6,4,3,3,2,1,3,2,2,3,2,2,4,3,2,5,8,2,6,5,4,1,10,2,5,3,4,4,3,2,3,3,5,3,3,3,6,3,3,2,3,2,7,3,5,2,3,2,5,5,6,8,2,4,5,3,2,6,1,3,3,6,4,3,2,4,2,2,3,3,1,1,2,1,2,1,3,2,5,1,3,3,5,2,2,5,2,4,3,7,2,3,7,1,4,1,7,2,9,3,3,2,1,3,11,3,4,6,7,2,5,13,8,1,3,1,7,6,2,11,4,1,4,3,2,7,2,7,6,2,11,7,3,6,4,5,2,2,1,7,3,3,5,3,3,5,2,2,4,1,3,2,4,3,2,4,2,5,5,4,7,5,1,4,4,3,2,4,2,2,2,1,2,4,3,1,3,5,2,2,3,6,3,9,7,4,10,2,2,1,2,1,2,4,3,2,6,3,5,7,4,5,3,4,3,3,2,7,3,3,3,5,2,5,2,2,5,1,2,12,3,14,2,5,6,4,3,3,5,8,6,4,2,4,3,3,2,5,4,1,9,7,2,4,5,2,5,4,1,3,3,5,7,2,7,13,5,5,2,1,2,4,2,3,4,2,10,4,2,2,4,3,1,3,3,3,7,4,2,4,2,5,1,4,5,3,3,2,4,2,2,1,2,8,1,3,3,6,2,8,2,3,2,2,1,5,1,4,4,1,2,5,1,5,8,4,5,4,4,4,4,2,3,4,1,2,4,3,1,3,3,5,1,5,11,3,3,3,8,4,2,4,5,5,5,7,7,2,1,2,3,5,1,1,5,2,2,3,4,7,5,2,1,3,3,3,2,3,3,2,2,3,2,8,7,5,14,1,3,2,8,4,2,2,2,2,7,2,1,2,2,6,2,8,2,2,6,2,3,4,10,9,1,5,5,4,4,3,6,7,2,3,4,7,3,3,9,2,2,2,4,3,6,1,3,5,2,10,5,2,3,4,7,2,3,6,1,5,3,5,5,2,2,2,3,3,12,3,3,4,4,2,2,4,2,3,9,2,6,2,3,2,4,3,4,2,3,5,2,1,5,3,1,5,2,2,1,7,6,2,2,2,10,4,2,2,5,3,4,4,3,1,1,3,2,2,4,5,2,5,3,1,9,6,8,7,5,2,2,1,1,2,3,2,7,3,4,3,4,9,5,4,7,4,10,5,4,3,7,2,1,3,3,3,8,3,9,2,3,3,7,5,4,2,1,6,5,5,2,14,2,3,2,4,3,7,1,2,4,1,4,5,5,5,2,5,3,3,5,3,1,2,3,2,9,3,2,3,2,6,5,4,2,2,2,3,2,2,2,3,3,2,4,2,3,5,5,2,4,3,8,3,1,4,4,7,3,3,3,6,4,3,11,6,5,5,4,1,10,5,2,8,10,5,6,2,2,2,2,6,4,4,5,3,6,3,3,4,6,3,1,1,4,2,3,3,3,3,8,7,7,2,4,6,3,3,5,7,2,5,3,6,2,3,1,5,4,2,5,1,1,4,8,3,2,8,4,6,2,7,2,4,6,6,5,2,1,7,7,2,9,4,7,2,5,2,3,6,6,3,4,6,1,7,4,6,3,7,2,1,4,3,3,5,2,2,3,3,3,7,10,1,3,5,3,7,3,7,2,2,2,4,4,2,2,2,1,1,2,1,3,3,8,5,1,8,1,8,1,1,2,5,2,9,2,2,1,2,2,7,8,5,1,8,7,1,8,2,14,1,8,4,2,2,2,1,1,9,3,2,3,2,7,2,2,12,6,1,3,1,4,2,3,5,2,5,5,5,5,9,6,7,3,8,5,8,5,3,4,2,2,4,3,3,2,3,7,6,9,1,5,1,3,4,8,7,5,6,3,3,5,5,6,2,11,3,6,2,5,7,1,12,2,5,2,7,3,6,3,3,3,6,4,3,3,4,5,3,5,5,3,4,2,4,9,5,2,7,2,3,7,7,3,12,5,5,9,4,7,2,4,2,2,4,7,2,3,3,1,3,5,3,3,9,2,2,4,2,4,4,2,5,6,6,8,3,1,6,3,5,5,9,5,2,5,1,1,8,9,5,5,2,6,2,7,6,2,4,7,6,8,1,1,5,6,2,3,5,3,6,1,2,2,1,3,2,2,3,1,2,5,10,3,4,5,7,2,3,3,2,3,2,5,1,3,3,2,5,3,2,6,6,5,3,2,5,3,6,5,3,7,3,3,3,1,6,5,4,3,2,4,3,6,3,1,2,4,1,3,6,3,7,4,3,3,2,1,4,1,2,5,9,3,5,2,3,4,9,4,1,13,4,2,3,5,3,5,1,4,1,9,2,3,2,2,2,3,9,2,5,2,5,1,3,5,3,4,1,3,3,7,2,4,5,6,5,3,3,3,2,3,4,2,2,2,5,4,3,4,1,3,1,2,3,7,8,5,3,2,1,6,4,2,3,4,7,1,1,2,1,3,1,7,3,3,1,5,2,2,2,8,3,2,3,3,6,3,5,2,4,4,2,14,3,6,3,6,3,3,1,3,6,5,1,7,3,3,4,3,3,5,2,5,4,5,2,5,2,2,5,5,2,2,4,1,2,2,2,3,3,5,5,4,2,3,9,5,3,3,2,3,13,3,2,2,6,1,2,7,5,5,2,9,2,2,2,5,2,2,7,5,1,1,3,3,2,3,5,3,1,7,4,3,6,2,2,2,7,1,1,2,1,5,5,6,3,5,2,5,2,3,7,1,5,3,5,2,4,7,3,6,2,5,4,3,8,3,3,7,8,4,2,4,3,4,4,4,2,3,6,6,3,3,2,4,5,3,3,1,4,3,3,2,3,1,2,2,3,2,2,3,3,3,1,7,13,2,2,3,5,2,6,5,7,9,2,2,2,2,5,3,4,2,7,2,5,2,2,2,3,2,4,1,2,6,1,5,4,5,3,1,7,3,2,3,5,8,4,1,3,8,1,1,2,2,2,2,3,3,7,4],"xaxis":"x","yaxis":"y","type":"histogram"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Quantity"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"count"}},"legend":{"tracegroupgap":0},"margin":{"t":60},"barmode":"relative"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('96309a54-6bee-4e7b-996a-24215a9dd4be');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
px.box(data, y = "Quantity", x = "Year", color = "Category")
```


<div>                            <div id="53d5b431-1b7a-4b10-b574-18e240e7e64e" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("53d5b431-1b7a-4b10-b574-18e240e7e64e")) {                    Plotly.newPlot(                        "53d5b431-1b7a-4b10-b574-18e240e7e64e",                        [{"alignmentgroup":"True","hovertemplate":"Category=Office Supplies<br>Year=%{x}<br>Quantity=%{y}<extra></extra>","legendgroup":"Office Supplies","marker":{"color":"#636efa"},"name":"Office Supplies","notched":false,"offsetgroup":"Office Supplies","orientation":"v","showlegend":true,"x":[2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017],"x0":" ","xaxis":"x","y":[2,3,3,2,3,2,2,3,4,1,3,7,2,1,5,6,3,5,2,7,2,3,2,3,4,10,4,5,4,7,1,5,3,3,3,1,2,5,2,3,6,2,8,3,2,4,1,1,2,2,2,5,2,3,3,4,2,4,2,4,2,3,2,2,3,2,2,3,5,3,2,14,2,2,5,3,3,3,4,3,4,3,3,3,5,5,2,1,5,8,3,3,3,4,3,5,2,6,2,3,5,5,2,3,3,3,2,4,3,3,6,3,14,2,2,1,2,6,1,4,2,3,3,4,1,2,1,3,4,7,3,2,2,6,10,6,7,6,2,3,4,3,3,7,4,5,3,4,3,1,2,5,3,4,3,5,2,3,4,5,3,2,5,6,2,2,5,2,4,3,5,5,3,5,3,2,7,2,2,1,2,5,1,4,2,2,4,5,7,5,3,2,5,6,2,4,3,2,3,7,2,5,6,1,4,5,4,7,2,7,2,3,6,1,3,1,9,3,2,8,3,1,3,2,7,5,2,7,3,4,10,13,2,6,2,2,3,4,5,11,3,5,6,5,3,8,1,3,8,3,2,3,5,6,2,3,2,2,9,2,1,3,3,5,5,5,3,3,3,7,2,6,4,4,3,2,2,2,1,2,2,8,6,3,3,3,5,3,7,2,3,6,5,3,9,3,8,2,2,2,3,1,4,9,5,9,4,2,5,8,6,6,1,3,7,7,3,2,9,5,2,2,1,3,2,2,5,3,3,6,4,4,2,3,4,3,4,2,6,6,5,4,4,5,3,2,3,2,3,4,2,2,4,9,2,2,10,2,3,1,2,3,2,6,3,4,2,3,7,2,2,5,5,3,2,3,5,3,4,3,5,2,4,7,2,6,3,2,5,3,3,3,2,7,2,2,4,2,3,3,3,9,1,11,1,5,1,4,8,3,3,7,3,6,4,1,7,7,5,5,3,5,6,1,4,2,3,5,3,3,2,5,6,3,11,6,4,6,3,2,6,5,2,1,4,2,5,5,5,4,9,2,7,3,2,9,3,7,2,5,1,3,2,2,2,1,3,2,4,3,4,3,6,2,1,3,1,5,3,5,1,4,2,10,6,1,5,1,5,4,5,1,4,2,5,3,4,8,13,11,2,7,5,2,2,1,3,3,5,2,10,2,3,2,1,5,8,1,3,2,5,13,2,7,2,3,2,3,2,2,11,3,3,3,3,8,7,5,1,1,2,1,3,7,6,2,6,5,1,4,3,5,5,3,8,3,3,7,4,5,3,3,2,2,4,2,1,2,1,2,3,3,3,2,4,1,6,9,4,3,2,3,6,3,8,14,3,4,4,2,3,4,3,3,1,3,2,2,4,2,4,2,2,3,5,3,6,3,2,2,1,3,3,5,5,5,2,8,1,4,5,2,2,3,5,2,3,2,5,3,2,2,2,2,9,3,3,5,2,2,6,4,1,5,2,8,6,6,2,3,9,3,3,7,5,7,4,2,7,5,2,5,2,3,2,7,1,3,5,3,3,5,2,2,4,5,3,2,5,2,9,4,7,2,2,3,1,6,3,3,5,1,5,2,2,3,4,2,3,6,6,2,3,4,6,4,2,1,2,3,5,3,3,9,3,3,2,3,2,1,9,2,1,4,3,5,2,3,5,5,2,9,5,4,3,3,4,4,2,2,8,2,6,6,4,1,2,3,5,3,2,8,3,2,1,5,6,4,11,2,3,1,2,9,3,4,6,6,1,3,7,1,2,2,2,6,5,2,3,4,2,3,2,3,2,4,5,5,5,2,2,10,4,2,3,2,2,7,1,5,2,4,1,1,3,1,5,2,5,3,4,3,4,4,1,4,7,4,4,3,13,5,2,3,5,3,4,1,6,2,6,1,3,5,3,6,4,3,1,1,1,3,1,4,3,5,3,2,3,3,4,2,3,2,2,5,2,2,5,4,3,13,2,3,2,2,5,3,2,5,3,3,3,3,2,2,5,12,3,3,3,5,3,2,7,3,2,2,4,3,2,2,9,7,3,2,1,1,3,5,3,4,3,2,6,6,7,3,4,3,3,5,3,3,7,6,3,2,4,7,6,3,5,8,8,3,3,2,3,3,1,6,5,2,1,5,8,4,3,4,5,3,2,1,2,4,7,1,2,3,6,3,5,2,4,4,10,9,4,3,2,3,2,5,3,2,6,4,5,7,7,3,5,3,3,2,3,3,7,1,5,3,5,4,8,1,5,1,6,3,2,7,4,3,4,3,1,2,3,2,3,6,5,2,1,9,5,2,3,3,3,3,3,3,3,2,4,7,6,2,3,2,1,5,4,3,2,4,6,3,2,4,1,7,3,3,4,1,9,3,3,3,5,2,4,2,2,7,3,6,4,3,2,4,3,2,2,2,2,5,4,7,9,4,7,7,6,3,8,3,1,4,4,3,3,2,2,4,7,4,9,6,3,8,2,4,3,7,2,2,4,3,7,3,2,4,3,5,7,2,5,2,2,6,2,2,3,3,6,4,2,7,4,2,3,3,3,2,1,6,3,1,2,4,5,1,7,2,3,4,3,3,5,6,1,2,2,1,2,3,3,2,2,2,2,3,7,5,5,5,1,6,2,1,4,6,4,4,13,11,1,3,5,2,1,3,1,1,1,2,2,2,2,4,5,3,3,3,3,5,6,4,1,3,3,4,3,6,3,4,2,1,6,9,4,4,5,5,9,2,6,5,4,3,1,3,3,3,3,7,1,5,3,4,3,7,2,2,3,2,3,2,3,5,3,2,2,6,6,3,5,2,5,3,3,2,3,2,2,3,8,2,2,3,5,8,6,2,2,3,9,3,2,3,3,5,3,2,5,1,2,2,4,5,9,3,2,2,5,5,6,3,2,6,3,7,2,3,7,4,2,4,6,2,4,1,6,3,2,2,4,6,1,4,7,5,2,2,6,3,3,2,2,1,3,1,3,2,6,2,3,2,3,3,4,5,2,1,3,5,3,3,2,2,2,2,3,4,6,3,2,5,2,2,8,9,4,3,8,3,1,3,14,4,2,9,4,9,4,4,4,4,11,2,3,3,6,7,5,3,3,1,5,6,3,4,4,2,5,3,3,2,2,4,3,2,2,2,6,7,4,1,8,4,2,3,6,9,3,2,4,8,3,3,3,3,4,2,5,2,3,3,2,6,3,1,1,1,5,1,4,7,1,3,3,3,13,5,2,2,3,6,6,2,3,3,3,1,7,3,2,2,4,2,3,2,3,3,1,2,3,5,5,2,3,1,3,3,1,2,5,3,3,1,3,4,3,2,1,3,1,2,6,3,3,3,3,2,2,3,2,2,2,3,7,7,2,4,2,2,3,2,3,3,2,5,3,7,3,3,6,4,4,1,3,4,7,4,8,2,2,3,10,5,4,3,2,4,8,4,2,7,2,3,4,7,5,3,6,3,2,2,7,13,2,4,1,3,3,2,5,5,1,3,7,3,3,5,3,5,5,2,5,3,3,7,6,6,4,5,2,7,2,1,6,8,7,2,10,4,2,2,2,5,4,5,3,3,2,10,4,7,2,2,5,3,2,3,5,7,2,2,4,5,2,2,4,2,5,6,2,1,3,2,1,5,3,2,2,3,3,2,3,4,3,2,4,3,7,2,2,2,2,2,3,5,1,2,2,4,1,3,2,2,2,3,2,6,3,3,4,9,8,1,5,2,2,3,4,3,2,2,3,4,3,3,5,2,3,2,3,2,3,5,3,5,4,5,5,6,9,4,3,3,2,3,3,2,4,7,3,2,3,3,5,4,3,7,2,3,2,2,6,6,4,3,3,4,9,3,4,2,2,1,1,7,5,2,5,5,3,3,6,9,2,4,9,2,5,2,6,3,2,3,4,3,3,4,2,2,1,7,3,3,2,3,5,3,1,9,2,10,4,2,2,2,2,7,1,2,2,3,3,3,2,1,4,3,4,1,5,2,3,5,7,4,3,2,3,3,2,2,8,7,1,2,3,9,7,3,2,2,1,3,12,4,2,3,1,6,2,6,4,2,3,4,2,3,5,2,3,8,5,3,3,3,7,3,14,4,1,3,1,3,1,5,11,9,5,5,5,9,4,4,1,6,5,1,2,7,1,3,6,2,2,3,5,2,2,4,2,9,5,6,3,3,1,1,9,2,5,1,4,4,3,2,2,7,3,6,5,3,9,4,2,2,6,4,6,7,1,3,4,9,3,4,1,2,2,5,1,2,4,4,1,2,3,7,1,6,9,5,3,4,3,8,2,3,2,2,2,4,3,4,2,7,5,2,5,3,2,6,6,2,2,2,4,14,4,2,4,2,2,7,5,2,2,3,6,11,6,5,4,1,6,7,2,8,4,2,2,2,5,3,5,4,1,2,2,4,6,3,4,1,4,2,5,2,2,2,7,1,2,2,1,2,3,3,2,1,1,2,2,2,2,7,4,3,9,6,6,5,4,9,2,2,5,2,3,6,4,5,4,5,5,1,2,2,3,3,3,3,3,2,2,6,1,6,5,4,4,1,3,6,5,5,5,4,2,3,4,14,2,5,4,2,4,5,2,2,8,2,3,7,4,5,2,2,3,6,7,3,2,5,2,2,8,1,1,10,2,6,3,5,3,6,1,2,1,4,7,2,1,8,4,2,1,3,2,4,4,3,5,6,3,7,10,2,3,1,4,5,3,5,2,4,5,3,14,1,5,3,7,2,2,2,3,4,2,1,7,7,4,3,2,3,4,3,4,6,6,4,3,3,2,7,3,2,2,10,2,2,9,5,7,1,3,11,5,6,3,3,7,1,5,5,3,11,5,3,3,3,6,3,3,2,5,3,3,3,2,5,6,2,7,2,7,3,5,1,2,5,3,7,2,7,6,3,6,7,2,3,2,5,5,2,3,3,6,6,9,3,13,5,9,3,5,2,5,4,7,5,3,5,4,2,6,3,4,2,6,4,5,3,7,9,4,4,3,3,2,6,6,2,3,5,2,5,4,5,5,2,3,2,6,4,10,3,2,5,3,3,4,2,6,3,6,4,2,2,8,7,3,6,3,2,9,8,5,5,4,3,5,3,3,3,3,6,2,5,4,5,2,2,8,4,2,1,9,4,4,2,4,5,7,4,2,3,3,2,7,3,7,3,5,3,4,2,4,2,5,2,5,6,4,2,5,7,2,7,4,5,3,3,7,3,4,5,2,2,5,6,2,6,8,6,8,7,2,3,5,1,9,3,5,2,5,1,7,2,3,1,2,5,2,2,3,11,3,9,2,5,5,1,2,6,7,7,1,4,1,2,3,5,2,4,2,3,3,3,3,2,2,5,1,2,2,4,3,2,7,4,5,2,3,2,4,2,2,3,1,2,2,2,4,3,1,1,5,2,5,4,1,5,8,8,9,4,2,4,2,3,5,3,4,2,3,4,3,4,2,1,1,7,2,2,2,4,2,4,4,2,4,7,3,7,7,2,2,4,6,5,4,2,2,2,3,3,3,1,6,5,5,2,2,3,9,3,4,2,3,7,2,2,2,3,3,3,8,5,3,2,12,2,4,4,2,2,2,2,1,6,2,1,5,3,7,7,3,3,2,4,2,2,2,3,9,2,5,2,4,6,3,4,6,13,4,5,3,5,7,2,4,9,2,9,2,3,3,5,8,2,1,4,5,2,8,2,3,1,9,5,3,3,7,3,2,3,2,4,6,3,1,7,3,3,4,4,1,1,6,2,3,3,3,2,3,2,4,3,7,3,5,3,9,3,5,3,3,6,7,2,1,3,1,3,7,3,3,7,3,1,4,3,1,4,1,3,3,3,5,2,2,3,2,9,3,4,1,1,5,2,4,5,4,5,2,2,3,7,1,5,5,5,2,2,4,5,2,3,5,1,6,7,7,2,2,14,2,3,5,2,3,3,4,2,3,3,1,2,2,1,3,5,3,3,5,2,4,1,2,7,5,3,2,1,3,3,6,3,5,1,2,8,3,3,4,2,3,3,9,2,3,2,7,4,3,2,2,3,4,4,5,6,1,4,6,4,2,3,2,2,9,2,4,2,3,3,4,2,5,9,1,3,3,1,3,5,3,1,3,4,2,5,7,5,3,2,2,3,5,7,3,5,3,2,4,3,1,3,2,2,4,1,5,2,4,2,3,3,5,5,5,3,8,3,4,8,9,1,2,2,5,2,5,5,2,7,6,3,6,2,3,1,3,2,4,3,2,2,3,2,1,2,3,3,2,3,3,2,3,3,5,2,1,7,3,3,3,2,1,4,5,1,2,2,2,3,7,3,2,3,2,2,7,2,1,4,6,6,5,5,4,4,2,2,1,2,4,1,5,6,2,3,2,8,3,8,4,4,3,4,4,3,9,7,6,2,2,8,3,1,3,3,1,5,8,5,5,4,2,4,7,9,2,2,3,6,3,4,2,1,1,5,4,3,2,9,2,1,3,2,3,2,6,7,3,2,3,2,9,3,6,5,2,8,13,4,2,3,5,5,7,6,5,6,2,2,4,2,3,1,6,2,9,3,4,2,3,3,12,3,1,2,2,5,3,4,2,2,6,3,4,6,3,3,3,2,3,5,7,4,5,6,5,1,1,5,2,8,4,14,2,4,3,2,6,2,3,4,4,7,1,2,9,6,3,3,8,9,5,3,2,4,4,3,7,5,3,2,3,2,4,1,6,2,3,4,6,5,2,3,2,2,2,2,3,7,2,2,3,6,2,6,3,8,1,5,6,7,4,3,5,5,4,3,1,2,7,2,3,1,4,6,3,5,2,9,1,5,2,5,5,3,4,7,2,2,3,2,2,4,6,3,2,9,1,1,2,2,8,2,7,2,5,2,2,4,1,2,1,5,2,7,2,9,5,3,2,2,4,7,2,3,6,4,3,2,1,5,2,2,7,9,3,7,7,2,5,5,5,5,5,3,9,2,2,3,3,3,2,2,3,2,8,1,1,3,1,2,7,2,3,3,4,8,5,10,1,6,4,2,5,1,2,1,1,2,7,3,2,8,5,3,2,2,5,5,5,2,4,2,5,4,2,1,2,5,1,5,4,2,6,5,1,9,1,8,3,2,7,6,3,3,5,3,2,3,2,4,2,4,2,2,2,3,2,5,2,3,3,1,7,9,2,4,6,3,2,3,5,4,3,5,9,7,5,2,1,6,4,7,4,3,3,1,2,2,8,3,3,3,4,3,1,3,3,5,4,9,1,8,6,5,2,4,9,2,10,2,2,2,2,2,3,2,2,8,6,5,5,8,1,5,3,5,6,4,4,1,3,8,5,3,1,2,3,2,1,4,5,1,5,1,4,3,5,4,9,8,3,9,4,3,3,7,2,7,2,10,6,2,7,2,6,2,4,4,4,1,2,5,1,5,3,4,4,1,5,3,8,3,3,5,7,2,2,9,7,1,2,7,3,6,2,8,5,5,8,5,1,3,3,2,4,3,5,4,3,2,6,2,2,3,3,5,8,2,2,4,2,3,2,6,2,3,7,3,3,3,7,5,4,2,3,9,6,1,4,3,2,3,3,7,1,2,4,2,2,4,4,2,8,4,2,2,2,3,2,1,3,3,2,2,2,4,2,3,1,2,2,5,3,2,1,3,4,3,5,3,3,3,3,3,3,6,2,2,3,5,4,2,4,5,2,7,1,5,2,4,3,5,4,5,5,1,2,4,1,9,1,1,3,3,2,2,2,6,3,2,7,3,3,9,5,9,2,2,5,4,2,7,6,9,5,3,2,2,3,6,2,7,3,5,2,4,2,7,3,1,2,5,9,7,5,1,1,2,2,5,9,2,1,4,4,1,3,1,5,2,5,3,3,2,5,1,2,2,2,6,3,3,3,4,4,5,4,3,7,1,9,2,1,4,8,6,2,3,7,2,2,2,2,2,2,7,3,1,4,4,5,2,12,2,2,2,6,5,1,4,2,2,3,3,2,1,5,3,2,5,7,1,2,3,4,2,3,6,2,1,2,3,4,7,5,9,2,8,3,2,6,3,6,7,4,7,5,1,3,3,7,7,4,7,3,3,6,3,3,3,4,4,3,8,2,9,1,3,3,5,10,3,4,3,4,7,2,2,3,1,5,4,7,5,8,6,5,3,3,3,3,1,5,2,2,3,6,2,7,3,3,3,9,7,4,7,2,3,3,12,2,7,1,3,4,3,2,6,3,2,4,6,1,2,2,7,2,1,8,3,3,3,3,2,3,5,1,5,5,2,3,2,2,2,2,4,4,2,3,4,2,2,3,2,2,1,7,3,2,5,4,4,6,2,3,3,5,1,4,4,5,3,3,5,7,4,7,1,3,1,3,6,3,3,11,3,1,2,3,2,2,2,8,2,7,5,6,7,3,2,7,7,5,2,5,3,2,1,5,2,2,3,2,3,1,1,7,5,5,5,4,3,4,1,2,6,2,5,2,4,5,2,2,5,6,3,2,2,3,12,3,6,2,3,8,5,3,1,2,3,2,7,3,2,12,3,5,2,2,1,7,4,8,3,3,1,6,9,6,5,3,5,3,1,5,4,2,1,3,3,4,2,3,3,7,1,2,1,4,4,3,2,4,5,7,2,9,9,2,2,4,3,4,5,5,5,6,2,6,2,2,6,3,8,2,4,7,6,5,7,4,3,3,2,3,8,4,1,3,3,3,3,1,3,2,5,7,4,9,8,3,4,2,8,3,8,4,4,3,6,1,2,1,4,3,3,3,9,8,3,5,7,1,2,14,3,7,13,4,7,7,1,7,2,5,3,7,3,2,7,7,2,3,2,2,2,1,7,1,4,1,8,7,3,9,4,6,3,2,12,3,3,1,5,4,2,3,3,3,1,2,2,5,9,2,5,4,7,4,3,3,7,2,4,5,3,4,3,3,2,2,2,6,2,10,1,3,3,2,3,3,3,2,13,10,2,3,1,7,5,2,2,6,2,4,4,5,4,4,2,5,6,3,2,2,5,10,2,4,3,2,7,2,3,9,2,2,1,2,4,5,7,3,3,3,7,2,9,2,2,2,3,2,5,3,1,4,2,1,6,7,3,4,3,2,2,3,6,1,6,7,6,1,5,4,4,2,2,3,2,3,4,7,5,2,4,2,14,5,5,6,5,2,2,3,6,8,3,7,3,7,1,11,3,3,6,1,5,5,6,5,2,9,5,3,5,7,5,2,2,1,1,1,5,4,8,2,1,4,7,4,1,4,1,3,2,2,5,5,4,3,7,5,7,6,4,4,5,3,3,2,3,5,2,1,4,5,3,3,2,2,8,2,7,3,5,2,1,1,4,8,2,2,5,3,1,5,2,7,2,2,3,4,2,9,2,4,2,4,3,3,2,2,5,2,1,3,5,5,4,5,4,5,4,2,4,7,2,3,8,3,3,3,2,6,3,2,3,5,5,2,6,2,3,3,7,2,2,3,3,5,5,6,4,5,3,7,4,4,4,4,2,1,4,7,7,4,1,6,2,3,8,5,2,1,1,1,4,2,4,4,2,3,2,2,6,9,4,2,1,6,4,7,2,3,6,2,2,5,8,5,2,4,1,4,1,1,3,9,3,4,2,8,5,6,2,3,4,3,2,7,2,5,3,1,3,6,2,1,8,3,5,6,2,2,6,1,3,3,3,5,5,3,7,4,3,7,2,7,7,3,6,2,2,7,5,1,4,2,1,7,6,3,3,4,5,6,2,2,3,3,2,4,3,5,9,4,2,4,2,1,2,3,8,3,3,2,2,2,2,3,4,7,9,4,2,3,5,5,1,2,2,8,4,3,5,1,13,9,5,3,2,13,3,6,3,4,3,1,4,1,3,5,2,2,5,4,5,3,4,3,3,8,2,3,1,3,3,4,4,2,2,2,5,4,1,2,3,3,1,7,2,8,4,5,1,5,5,2,3,3,3,3,1,3,3,3,4,5,3,2,4,4,3,5,1,4,5,4,6,5,8,2,3,2,2,5,3,4,4,1,7,3,4,4,3,3,2,6,7,2,1,5,1,5,2,1,2,5,2,2,1,2,3,9,4,3,5,3,8,3,2,4,4,1,2,3,1,3,3,3,2,3,7,2,2,4,2,4,4,5,2,2,5,5,3,2,7,2,4,5,4,8,1,3,3,5,4,1,2,2,1,8,2,1,3,9,10,5,4,3,6,11,5,3,4,2,4,8,3,3,5,4,3,3,2,2,6,2,2,2,2,2,5,3,2,4,1,4,5,8,2,3,3,9,2,2,1,5,9,9,2,5,5,2,3,5,5,2,5,2,2,2,3,2,1,6,7,2,2,7,1,7,7,6,5,4,2,7,6,1,2,4,4,2,4,5,3,10,2,4,3,3,2,3,7,1,3,1,5,2,3,3,2,5,1,2,3,2,5,5,2,5,3,3,3,3,3,5,3,1,1,2,5,6,1,4,3,5,5,2,2,8,6,2,2,4,5,6,7,2,4,3,3,9,1,2,2,7,3,7,3,4,5,2,2,4,2,3,3,2,5,4,8,2,4,6,3,1,8,5,7,5,4,6,2,3,3,4,3,2,1,5,2,3,4,3,3,3,7,4,3,3,5,1,5,1,8,5,2,3,7,5,4,2,3,3,4,2,3,4,1,3,6,3,2,1,8,1,3,2,3,2,2,1,2,3,6,2,1,5,2,8,6,5,3,3,2,5,3,1,9,8,3,3,3,3,8,6,2,3,3,5,2,6,1,4,4,3,12,3,3,2,3,3,2,2,1,2,9,5,3,7,7,5,3,4,1,4,4,5,4,7,6,3,2,4,9,1,3,6,3,2,3,3,3,3,7,3,2,4,8,2,2,2,3,6,3,5,6,9,2,5,4,5,5,3,6,4,5,5,3,1,2,2,2,7,4,5,4,2,5,3,2,3,2,3,2,2,2,5,5,5,2,2,4,2,2,5,2,2,2,7,4,3,7,2,1,2,3,6,2,4,1,2,7,3,6,2,4,4,3,9,3,3,3,4,7,1,5,3,4,2,1,4,2,2,9,2,2,3,4,7,2,3,3,2,1,4,6,5,2,7,3,5,3,5,1,3,2,1,6,9,2,9,4,8,3,6,10,2,2,2,3,3,5,2,5,5,6,11,4,4,8,7,4,5,3,3,6,4,3,3,5,6,3,7,7,3,5,4,3,6,2,6,8,2,4,3,3,2,3,9,3,2,3,4,2,8,5,3,7,4,9,3,9,5,3,2,3,1,3,2,6,5,3,4,3,6,7,4,2,4,3,7,6,5,1,5,1,3,9,5,2,6,1,2,4,8,1,2,5,2,4,6,2,4,1,4,5,1,3,3,1,8,5,5,6,2,3,5,5,4,2,9,7,7,3,3,1,3,7,9,2,5,1,4,2,3,4,2,4,5,3,4,5,2,8,1,5,5,1,3,5,3,5,2,3,6,2,4,4,5,7,2,3,5,3,2,4,5,4,6,6,2,7,4,7,2,1,5,3,3,2,2,1,3,5,1,2,1,2,3,3,3,5,8,5,2,3,3,9,4,5,7,4,5,3,7,4,9,2,5,6,5,1,1,2,1,2,2,2,2,4,3,3,6,3,3,3,3,2,2,3,1,2,3,2,5,4,6,2,7,5,5,4,3,4,2,3,3,11,2,5,3,3,5,7,5,7,5,3,3,2,1,4,2,4,5,2,9,3,3,2,2,2,7,5,8,9,2,10,7,1,2,2,4,5,2,2,2,1,6,3,5,3,3,3,3,2,2,2,5,3,3,3,3,4,7,3,2,4,4,7,2,2,5,3,2,5,2,2,4,5,2,3,3,3,9,2,4,2,3,1,1,7,1,2,7,3,4,2,7,3,9,4,7,5,2,3,8,1,3,2,6,4,3,3,1,3,2,3,2,8,2,6,4,1,5,3,3,6,3,3,2,7,3,5,2,2,5,6,2,4,5,2,6,1,3,3,6,2,4,2,3,1,1,2,2,3,2,5,3,5,2,2,5,2,3,7,7,4,1,7,2,9,3,3,1,3,6,7,2,13,8,1,3,6,4,1,4,3,7,2,7,7,3,6,4,5,7,3,5,3,5,2,2,4,3,2,5,5,4,3,4,2,2,2,1,2,3,1,3,5,2,6,3,4,1,2,2,6,7,5,4,3,2,3,5,2,5,2,2,4,3,3,5,8,6,4,2,3,5,4,1,9,7,5,2,5,4,3,5,7,5,2,2,4,3,4,2,10,2,4,3,3,7,4,2,5,1,4,5,3,3,2,2,1,2,1,3,6,8,2,2,5,1,4,4,1,5,4,4,4,3,1,4,3,3,1,5,3,8,2,4,5,7,7,2,2,3,2,3,7,2,1,3,3,3,3,2,3,2,8,5,14,3,2,8,4,2,7,2,6,2,6,2,3,10,1,5,5,4,3,6,7,2,3,7,3,2,2,4,3,6,3,5,2,10,5,2,3,7,6,5,5,2,2,3,3,3,4,2,2,4,2,2,6,2,3,2,2,3,2,3,1,2,2,1,7,6,10,2,2,5,4,4,3,1,1,3,2,4,5,2,5,3,9,6,8,2,1,2,3,9,4,7,5,2,3,9,2,3,3,1,5,5,14,3,3,7,1,4,1,4,5,5,2,5,3,3,5,3,2,3,9,3,2,3,5,2,2,2,2,3,4,3,5,5,2,3,1,3,3,6,4,3,11,4,1,10,2,8,5,2,2,2,6,6,4,1,1,3,3,8,7,7,6,3,7,2,3,6,2,3,4,2,1,1,4,8,3,8,6,2,7,2,6,6,5,1,7,7,2,9,7,2,5,6,4,6,7,4,7,1,4,3,3,7,10,3,7,7,2,4,4,2,2,2,1,2,8,5,8,1,2,5,2,2,1,2,7,8,8,7,1,8,1,8,4,2,1,1,9,3,3,2,7,2,12,1,3,1,4,2,5,9,6,7,3,8,3,4,7,6,5,1,7,5,6,3,3,5,6,2,3,2,1,2,6,3,4,3,4,5,3,4,2,4,5,7,7,5,5,9,4,7,4,2,7,3,1,3,3,9,2,2,4,6,6,3,1,6,3,5,5,5,2,5,1,8,9,5,2,7,2,4,7,5,6,2,3,3,6,1,2,2,2,5,2,3,3,5,3,3,3,2,6,6,5,3,5,6,5,3,3,1,6,5,4,3,3,1,2,4,1,3,6,4,3,3,1,4,1,5,9,3,9,1,4,3,5,3,5,1,4,1,2,3,2,2,2,9,2,5,1,5,3,1,3,3,7,2,4,5,5,3,4,2,2,2,5,1,3,3,7,8,2,4,7,1,2,1,3,1,3,3,5,2,3,2,3,6,14,3,6,6,1,5,7,3,4,3,2,5,4,5,5,2,5,2,4,1,2,2,3,3,5,4,2,3,5,3,3,2,3,13,2,2,6,2,7,5,9,2,2,2,2,5,1,1,3,3,3,5,1,7,3,6,2,2,1,5,6,3,5,3,1,5,3,5,7,3,2,5,4,3,8,3,7,8,4,4,4,4,2,6,3,3,2,5,3,3,3,3,1,3,2,3,3,1,13,2,5,2,6,7,9,2,2,2,5,3,4,7,2,5,2,4,1,1,5,4,5,1,7,3,2,5,1,1,2,2,2,3,3],"y0":" ","yaxis":"y","type":"box"},{"alignmentgroup":"True","hovertemplate":"Category=Furniture<br>Year=%{x}<br>Quantity=%{y}<extra></extra>","legendgroup":"Furniture","marker":{"color":"#EF553B"},"name":"Furniture","notched":false,"offsetgroup":"Furniture","orientation":"v","showlegend":true,"x":[2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017],"x0":" ","xaxis":"x","y":[9,3,1,2,6,3,4,6,5,2,3,3,4,3,3,3,3,2,3,2,2,1,3,6,2,5,4,6,3,6,2,6,5,3,2,6,1,5,4,3,4,7,3,10,2,2,3,3,3,3,3,3,2,7,4,1,3,2,7,7,2,1,3,3,2,7,2,1,1,8,3,4,3,3,2,4,5,2,2,4,5,5,3,2,2,2,2,7,3,2,4,7,1,8,4,3,7,6,2,5,3,3,7,2,2,2,2,2,10,3,7,6,6,7,6,2,2,2,3,3,3,3,7,2,7,9,3,2,4,8,3,4,1,1,3,5,2,5,1,5,2,3,2,2,2,1,3,1,3,9,3,3,4,3,2,4,1,3,2,5,1,2,5,3,3,8,2,9,3,3,3,6,8,4,2,5,2,7,8,4,4,6,1,3,4,6,9,7,2,13,3,2,1,4,4,3,3,1,2,6,2,5,1,6,2,3,9,5,5,2,6,6,3,5,5,3,2,6,3,6,5,3,5,9,2,4,2,1,7,2,3,5,6,3,2,2,3,4,3,2,2,3,1,3,5,4,2,2,1,2,4,9,3,3,3,1,3,5,5,3,7,2,11,4,5,2,9,1,2,2,6,6,3,3,4,4,4,4,6,8,5,3,2,3,1,6,2,6,6,3,4,2,1,2,6,5,4,9,2,5,3,2,1,2,2,5,4,4,3,1,3,2,3,3,2,5,10,5,3,2,3,4,2,4,3,6,2,6,2,5,2,2,7,5,4,1,3,2,4,3,5,3,3,5,5,5,4,6,2,2,3,8,3,3,5,3,5,8,5,5,3,3,1,2,5,3,3,3,3,1,3,6,12,3,3,1,4,2,5,7,2,9,6,7,5,2,2,2,14,3,7,2,3,2,3,3,6,3,1,2,5,1,6,3,3,3,8,2,3,6,3,14,3,6,3,5,3,6,2,7,5,5,9,14,1,4,9,4,7,4,1,5,2,13,7,3,4,2,1,4,9,2,5,1,7,8,2,6,3,3,7,2,2,2,7,6,3,7,4,3,8,4,2,2,1,4,2,2,5,3,8,5,3,4,3,2,1,4,5,3,3,3,2,2,4,2,2,3,2,9,7,1,2,1,6,2,3,3,1,8,2,3,2,3,5,1,5,5,3,6,6,2,7,2,6,3,2,3,7,4,5,3,2,3,4,9,7,3,5,1,1,3,4,8,2,7,2,6,3,9,7,4,2,3,5,2,6,4,6,2,4,3,5,2,6,7,3,9,5,3,4,6,1,1,10,2,6,1,2,9,2,2,2,3,3,2,2,7,8,6,4,9,1,9,6,2,6,1,3,5,2,1,4,5,3,3,2,2,5,3,3,3,6,7,6,4,1,5,3,3,1,3,5,5,2,9,3,3,3,7,3,3,3,1,3,6,5,2,3,1,5,2,2,2,1,7,1,2,3,2,4,3,2,4,3,1,2,3,2,2,8,2,6,1,4,4,2,7,5,4,3,7,3,3,3,5,2,7,1,4,1,5,6,2,2,7,3,2,2,3,2,4,2,4,4,4,3,2,2,10,3,6,1,3,4,3,1,2,1,3,3,4,1,5,3,3,3,5,4,3,1,3,2,5,6,3,7,6,3,3,1,7,8,7,8,5,3,5,7,4,1,4,5,2,2,4,3,5,6,11,2,10,3,3,3,1,5,5,3,1,3,2,3,7,3,3,5,7,4,3,9,3,3,3,3,4,2,3,3,2,6,2,2,4,5,3,2,4,6,3,4,3,2,3,3,1,2,2,8,7,2,4,11,5,4,1,3,3,9,5,3,3,5,9,2,12,2,4,2,4,5,9,9,3,1,3,6,5,2,7,3,5,2,2,3,4,6,1,4,4,2,2,3,5,5,9,4,3,2,3,2,2,3,7,3,9,2,2,3,5,4,3,2,3,13,7,4,2,7,4,2,2,6,1,4,1,3,2,3,3,9,3,5,3,7,3,6,2,4,5,14,8,1,3,7,2,5,8,4,7,3,1,3,1,4,7,2,4,2,3,2,4,4,4,3,6,2,4,3,3,2,5,7,2,8,3,5,3,2,5,3,8,5,1,4,4,2,3,2,5,2,2,2,5,2,5,4,5,5,3,1,4,1,4,7,5,2,7,3,1,4,8,6,5,6,6,4,5,4,2,3,4,5,5,6,4,5,7,3,4,5,4,2,2,3,8,5,5,4,2,3,5,6,2,6,3,2,2,3,7,3,9,2,4,5,2,2,6,5,3,7,4,8,4,2,3,3,1,4,3,4,2,4,8,5,2,3,4,6,5,3,3,3,2,5,8,3,5,8,10,2,3,3,2,3,5,3,1,4,5,3,2,3,3,4,7,3,3,2,2,7,3,5,2,7,5,4,3,2,3,3,2,2,3,2,2,3,3,3,2,7,1,5,5,5,5,5,2,8,4,3,4,2,4,4,1,3,3,3,5,3,3,1,6,5,5,2,3,2,5,4,9,4,2,8,5,5,5,3,7,2,2,9,2,2,7,2,2,2,3,2,3,4,9,9,7,3,3,6,3,6,4,4,1,2,4,4,4,4,3,3,3,9,2,3,2,4,3,2,3,1,3,3,3,9,2,7,1,3,2,2,3,3,3,3,2,1,1,3,4,4,5,4,4,1,4,2,2,14,3,2,2,2,2,3,3,3,2,1,9,2,4,3,2,3,4,2,2,1,2,2,2,7,3,4,6,3,5,3,5,2,2,4,3,11,2,2,3,5,5,7,5,1,5,4,6,4,5,2,3,8,2,4,1,3,4,5,3,5,14,3,1,1,2,1,5,4,1,5,2,3,4,2,2,4,3,5,7,14,1,3,3,5,4,2,3,5,5,3,5,2,7,3,5,3,7,10,4,3,3,1,6,7,2,2,5,8,3,2,2,2,5,3,4,2,3,2,7,1,9,2,4,2,3,2,3,6,9,3,6,7,2,4,1,2,3,3,2,4,4,2,6,2,2,5,3,2,3,3,3,2,4,2,7,2,5,2,4,6,3,3,9,2,8,6,7,3,7,3,4,3,2,5,3,2,2,5,2,4,3,3,6,10,2,3,1,2,2,6,3,3,3,1,8,1,6,7,5,3,7,3,2,5,3,7,5,5,5,4,6,4,5,4,4,6,2,3,2,3,5,6,5,8,3,3,4,6,5,4,1,2,8,4,2,2,3,6,7,9,2,8,4,3,3,5,1,2,5,3,3,3,8,5,6,1,4,11,4,5,5,2,2,3,2,7,3,4,3,2,3,1,2,4,3,3,7,1,4,1,2,2,1,1,3,4,2,2,2,4,1,3,1,5,3,5,1,2,3,1,2,9,5,2,3,2,2,7,3,1,5,3,1,2,4,3,1,1,6,3,5,1,1,6,3,8,2,3,3,7,1,3,2,2,2,5,3,2,1,7,5,2,2,5,8,3,3,2,3,4,3,3,2,6,3,2,3,5,6,5,8,3,5,1,3,3,3,5,2,2,3,3,9,2,3,3,7,2,4,3,7,1,7,4,5,6,2,8,4,5,3,3,2,5,1,3,7,5,1,2,3,2,3,1,1,7,5,5,5,5,2,2,2,2,1,1,3,3,2,3,9,12,1,8,5,2,3,3,5,4,2,8,3,4,2,4,3,2,1,1,3,6,2,2,7,2,6,1,2,3,1,5,3,1,4,2,3,3,4,7,2,4,3,2,7,2,3,9,3,3,6,4,5,2,2,3,1,4,3,5,3,3,9,2,3,3,1,2,5,2,3,3,1,2,3,1,9,9,3,1,3,4,3,5,2,2,5,3,9,3,3,5,6,3,3,2,3,4,5,2,2,5,4,3,2,4,3,1,4,3,5,2,4,6,4,1,3,4,3,1,3,3,2,7,2,3,3,5,1,1,2,4,5,2,1,3,9,4,2,2,2,2,3,3,6,3,4,3,4,4,2,1,2,2,2,5,2,3,8,7,5,3,2,4,7,5,2,3,3,1,5,5,2,5,1,2,2,8,9,3,2,2,3,4,5,2,4,7,2,5,2,2,2,3,5,3,4,5,8,1,2,2,2,5,8,1,7,5,3,3,4,3,5,3,5,3,4,2,4,8,2,11,3,1,5,2,1,2,2,3,10,4,3,2,3,8,3,4,3,3,1,1,1,4,2,1,3,4,7,2,11,2,6,2,2,1,3,4,1,3,2,5,4,2,2,3,2,3,3,5,4,3,3,2,5,3,14,4,3,2,1,3,7,13,2,2,1,3,4,2,4,3,3,2,1,5,4,2,4,2,11,3,4,5,5,1,5,3,1,2,2,1,2,2,2,8,2,9,4,3,2,1,4,1,3,12,4,3,5,2,2,2,1,7,5,2,2,3,4,10,3,7,3,8,5,4,2,4,5,2,3,2,3,3,6,2,4,4,3,3,3,2,2,4,2,4,2,2,3,6,3,1,6,3,2,3,5,2,2,5,3,3,2,2,1,1,1,9,2,1,2,2,2,6,2,3,5,5,5,2,3,3,3,1,3,5,6,5,7,12,2,5,7,3,6,5,9,2,3,12,2,2,3,5,4,2,5,8,9,6,1,5,2,3,2,3,1,10,3,7,3,2,2,5,2,3,6,7,2,2,2,4,4,13,9,3,3,3,2,3,4,2,5,1,6,1,1,2,8,3,2,4,3,3,6,1,3,2,2,2,2,5,9,1,5,2,5,7,2,2,7,1,2,2,2,6,2,4,3,4,3,1,4,2,2,2,3,5,2,2,2,2,2,6,3,8,4,1,3,8,2,4],"y0":" ","yaxis":"y","type":"box"},{"alignmentgroup":"True","hovertemplate":"Category=Technology<br>Year=%{x}<br>Quantity=%{y}<extra></extra>","legendgroup":"Technology","marker":{"color":"#00cc96"},"name":"Technology","notched":false,"offsetgroup":"Technology","orientation":"v","showlegend":true,"x":[2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017],"x0":" ","xaxis":"x","y":[2,4,3,6,5,3,7,2,13,6,5,5,1,7,3,3,3,3,3,1,3,2,3,2,12,2,4,6,4,3,2,7,6,4,3,2,3,7,2,7,2,3,2,1,2,3,2,5,3,4,3,7,6,2,6,14,4,12,3,4,3,2,5,2,3,2,5,4,3,5,5,2,1,2,3,3,2,2,3,1,2,2,2,2,12,1,4,6,5,3,3,3,7,3,6,1,4,2,3,5,2,2,1,3,3,3,7,4,3,6,3,5,4,2,2,3,1,3,3,4,4,8,1,2,4,3,2,2,2,2,6,3,3,10,8,2,7,3,2,9,2,2,5,9,1,1,2,3,5,3,3,2,1,4,2,2,7,13,8,4,9,5,7,3,8,5,3,9,3,7,3,3,3,4,4,3,3,3,8,2,3,3,3,4,2,1,6,1,5,1,2,4,5,2,1,4,3,5,2,10,3,3,7,5,2,2,9,2,3,2,2,2,11,2,3,1,2,3,2,3,3,1,6,7,2,5,2,2,5,3,3,3,5,3,6,4,3,5,2,2,6,2,9,8,4,9,3,10,2,1,6,7,3,2,3,4,4,7,6,4,2,2,5,3,3,4,1,8,2,3,7,2,9,2,3,7,3,4,2,2,6,2,3,7,4,2,5,1,6,5,1,1,1,7,4,5,7,3,5,4,4,7,5,2,4,2,4,2,1,5,4,4,2,7,1,4,2,4,3,10,4,4,1,3,3,2,4,5,4,3,5,5,4,5,3,7,3,7,3,5,4,3,3,6,4,6,2,2,2,3,4,3,7,3,7,9,2,3,5,4,2,2,3,4,1,3,3,2,3,2,6,3,3,1,5,3,2,1,2,9,2,4,2,7,1,2,2,3,3,5,3,5,3,2,1,3,7,2,3,2,1,7,3,3,1,3,5,5,3,5,7,3,1,2,5,2,6,2,6,1,4,3,2,4,2,3,3,3,2,4,1,3,5,6,2,2,4,3,5,3,3,8,10,5,5,3,3,3,4,7,7,3,4,6,2,2,4,7,6,4,2,7,2,1,3,3,4,2,2,2,3,3,5,3,6,2,2,3,2,1,3,2,3,2,3,7,3,3,2,4,3,3,2,2,1,4,3,5,3,3,2,4,7,2,4,10,1,4,5,2,14,5,3,7,6,7,3,2,2,3,1,5,2,4,4,7,2,5,3,4,2,4,4,9,4,7,3,3,2,5,3,5,7,2,3,1,5,2,5,1,2,5,3,4,2,7,5,6,1,2,2,4,2,3,4,3,2,3,1,7,9,14,4,3,5,7,2,3,3,2,2,6,9,4,2,2,2,1,5,7,7,5,12,2,2,2,4,2,3,1,5,2,2,4,3,5,3,4,1,3,4,6,2,7,5,3,3,3,2,3,5,3,7,2,2,9,3,1,2,2,2,1,4,2,5,4,4,1,7,1,2,2,9,3,7,3,4,3,5,2,2,4,2,2,5,1,2,1,5,5,3,6,3,2,2,2,2,4,3,3,4,3,4,4,2,7,2,1,2,2,3,5,3,4,2,2,1,3,3,8,2,3,3,6,3,3,4,2,2,4,5,4,3,2,3,2,6,2,2,9,6,6,5,4,1,2,6,2,1,2,11,4,4,6,5,3,1,4,2,2,3,2,6,9,2,1,3,3,9,2,5,4,2,2,6,8,3,2,1,2,7,4,2,2,5,2,8,3,9,4,7,2,6,3,2,5,3,2,4,6,2,2,5,9,2,2,3,3,4,3,1,4,3,2,4,1,5,2,4,3,3,4,5,3,2,3,7,3,1,2,1,5,7,2,5,3,3,3,7,2,2,3,3,4,5,5,5,3,3,1,8,2,3,5,3,2,3,2,2,2,1,2,4,5,3,8,4,3,2,4,1,4,3,3,3,5,3,9,2,5,7,4,7,1,4,2,5,1,3,2,3,3,3,5,3,3,2,5,5,2,2,2,2,6,4,7,5,5,2,3,10,2,2,5,5,9,4,3,4,1,2,3,2,1,7,5,1,5,5,6,2,2,6,3,2,6,3,9,3,3,4,2,3,2,3,3,3,7,3,1,2,1,2,3,4,2,3,1,7,4,4,9,1,4,3,2,2,3,7,3,5,3,3,1,5,5,1,9,3,6,7,8,3,2,2,4,3,2,3,3,3,1,3,2,5,1,8,1,7,5,4,4,1,2,3,12,2,4,3,2,7,2,6,2,5,2,3,3,7,1,2,3,2,5,7,3,2,6,5,2,3,2,3,3,3,3,3,4,3,5,2,2,1,1,6,3,4,5,3,2,3,5,5,3,4,2,8,2,2,4,2,5,7,5,5,9,13,8,3,3,3,5,3,3,4,2,2,2,5,2,8,3,8,5,3,4,2,1,3,3,2,3,5,9,3,5,6,3,4,1,3,1,3,7,5,1,3,6,2,6,8,6,5,4,1,2,3,5,3,2,3,5,1,3,2,4,5,4,2,3,3,3,3,4,3,7,7,7,2,7,2,4,2,3,3,2,4,4,2,2,3,3,2,3,5,1,4,5,2,7,4,2,1,7,3,7,3,2,2,4,2,8,2,3,6,5,8,5,3,2,8,3,8,3,1,6,1,5,6,3,2,1,3,9,3,3,5,5,1,2,3,11,2,3,1,5,2,3,3,5,2,7,3,1,4,2,5,4,5,4,5,4,3,6,7,5,4,7,3,3,3,2,3,7,3,1,3,4,5,3,3,3,8,7,3,7,2,2,2,2,3,2,3,2,1,2,4,7,5,4,2,4,2,8,2,3,3,5,1,3,3,5,6,2,3,7,3,3,3,3,9,4,3,4,2,5,5,6,2,3,4,1,3,4,1,1,3,3,2,1,3,1,5,5,8,2,6,3,2,8,3,2,3,2,2,4,3,3,5,4,7,2,5,1,1,2,2,8,2,8,2,2,3,8,3,6,7,3,6,2,4,2,7,4,1,2,4,3,2,3,5,5,4,1,5,2,1,3,5,5,7,2,3,4,4,1,2,2,3,3,1,5,2,2,5,11,3,3,1,6,2,2,10,3,2,5,3,5,4,5,7,4,4,7,1,6,2,5,3,3,1,3,7,2,1,2,5,5,3,2,1,3,1,3,2,4,1,9,7,8,2,6,3,3,3,4,4,5,1,2,3,4,1,1,1,2,6,5,5,10,2,3,3,2,7,5,3,4,5,3,2,2,1,3,3,8,6,1,2,3,5,9,8,4,5,3,2,3,14,9,8,3,5,3,2,2,2,6,4,3,1,4,3,10,4,2,2,4,3,5,2,2,6,5,6,1,3,3,9,2,2,2,5,3,6,9,9,4,3,5,5,5,5,8,5,4,5,3,3,1,5,4,1,2,3,2,5,3,2,5,3,1,4,3,4,5,9,2,5,1,8,2,3,6,2,1,9,2,3,1,2,4,13,2,2,3,14,4,2,4,1,3,3,2,7,2,4,3,2,3,1,4,4,3,4,4,2,1,7,4,3,6,1,2,2,4,3,4,3,7,4,2,4,6,5,6,5,1,2,7,3,3,1,6,7,2,3,1,1,2,6,3,4,2,8,3,5,3,2,2,3,2,3,2,2,2,2,5,2,2,9,6,3,2,2,4,5,5,2,3,4,2,3,5,3,3,3,5,2,3,3,2,11,5,1,11,2,3,2,4,7,1,4,4,9,7,10,2,1,2,4,7,3,3,2,1,12,5,6,2,4,2,5,1,4,3,2,8,2,2,1,8,5,4,1,3,5,3,5,1,1,2,4,5,2,2,7,2,4,4,9,2,3,5,2,3,3,9,4,4,5,1,5,2,4,3,1,7,4,3,5,4,4,1,3,3,7,2,6,2,2,2,1,2,6,4,2,2,3,2,4,8,4,4,7,5,5,5,10,6,5,3,6,4,3,3,3,5,5,1,5,5,4,4,3,3,1,3,3,1,1,8,2,5,14,2,2,5,5,5,8,2,4,2,9,4,8,11,3,3,3,3,5,2,3,7,4,2,3,2,4,1,5,2,6,6,8,1,1,4,5,2,1,3,7,3,3,2,4,3,3,5,2,2,5,4,6,3,3,4,1,3,4,2,3,7,2,3,5,4,2,3,3,3,5,5,3,2,3,4,1,5,5,2,7,4,3,3,6,2,7,2,3,2,3,3,7],"y0":" ","yaxis":"y","type":"box"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Year"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"Quantity"}},"legend":{"title":{"text":"Category"},"tracegroupgap":0},"margin":{"t":60},"boxmode":"group"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('53d5b431-1b7a-4b10-b574-18e240e7e64e');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


 


```python
data.Profit.describe()
```




    count    9994.000000
    mean       28.656896
    std       234.260108
    min     -6599.978000
    25%         1.728750
    50%         8.666500
    75%        29.364000
    max      8399.976000
    Name: Profit, dtype: float64




```python
px.box(data, y = "Profit")
```


<div>                            <div id="20fcfb63-cc0a-4633-9f97-ad139fd7d10f" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("20fcfb63-cc0a-4633-9f97-ad139fd7d10f")) {                    Plotly.newPlot(                        "20fcfb63-cc0a-4633-9f97-ad139fd7d10f",                        [{"alignmentgroup":"True","hovertemplate":"Profit=%{y}<extra></extra>","legendgroup":"","marker":{"color":"#636efa"},"name":"","notched":false,"offsetgroup":"","orientation":"v","showlegend":false,"x0":" ","xaxis":"x","y":[5.5512,4.2717,-64.7748,-5.487,4.884,1.4796,746.4078,274.491,5.2398,113.6742,204.1092,0.3112,3.0084,9.3312,-53.7096,-18.2525,9.75,1.168,21.2954,1.3583,3.0814,238.653,34.3548,2.7072,6.567,-2.5212,13.0928,5.3392,87.3504,3.9294,25.47,258.696,-53.2856,65.978,-31.05,-13.6312,10.1493,28.5984,6.4864,-23.716,19.6224,36.693,-320.597,181.9818,93.5816,5.79,6.6584,4.0542,30.0234,8.9535,224.2674,10.9698,1.7901,11.58,12.7368,-51.5154,9.2928,13.365,4.8609,15.9792,4.1028,0.0,19.2384,5.0196,30.7818,0.0,9.3312,8.34,4.4712,52.6344,39.7488,0.0,12.0252,14.3075,-16.65,1.3257,6.8982,4.752,3.4196,206.316,-12.224,13.572,5.8045,27.248,4.3134,29.0136,16.0928,6.0368,42.0355,42.0186,7.2,-14.7708,49.6048,9.744,5.5328,2.5984,15.2225,6.8724,4.4344,53.2704,8.2062,24.393,75.3732,103.158,-24.294,4.7724,22.9488,86.3892,6.066,7.209,-1.728,-13.93,8.8088,-11.322,-2.5248,22.4316,6.9088,6.2208,-13.7175,9.3312,2.3409,-6.8634,11.1024,7.6869,3.4048,-34.9536,-22.6716,8.5845,-43.0296,5.6784,-3.5325,0.0,51.4764,-172.1172,1.6038,17.472,5.3392,32.13,1.07,9.1785,-10.0512,4.914,40.872,-199.617,-23.4882,-459.6072,3.4048,4.5954,2.3328,17.745,5.3998,177.5889,16.7508,45.9754,15.4752,54.1764,21.8352,0.0,9.499,5.4801,33.64,4.6644,4.8588,-15.9102,10.7424,9.3564,2.0748,38.1576,2.288,1.7004,14.1728,7.0218,49.014,164.6316,20.1656,2.64,156.047,1.2506,5.7672,31.8696,3.2392,11.1672,6.624,4.752,284.98,-5.5338,5.1408,47.8152,-31.6712,17.847,29.495,-553.6476,36.5742,1.8792,8.4942,7.68,-447.5947,23.59,5.4432,0.3336,14.9156,5.7072,25.098,17.2224,16.3842,-122.7816,41.1528,6.3504,5.3721,75.9696,415.9896,70.49,1.002,14.43,5.9175,8.0766,334.1142,-1811.0784,15.294,-16.426,7.4816,1.3728,-25.737,1.962,3.9852,28.3479,53.2,5.5044,1.5876,-3.8646,1.2038,6.624,909.9818,60.2553,6.5904,2.7028,-10.9188,59.0112,22.2,6.512,23.235,-5.8604,-35.3646,-39.4565,3.2214,37.797,85.904,14.5728,11.703,9.9216,15.918,1.9024,65.2064,3.72,9.0,8.619,0.84,9.4284,2.8784,106.6248,22.6782,-143.2548,2.8764,-152.7156,2.94,-12.098,113.3055,22.2,20.853,-9.093,88.1804,0.0,6.465,-13.8278,252.588,14.8344,13.9972,-0.5964,98.4802,1.0584,-10.116,-1.3083,5.5536,14.8,3.0576,2.6784,293.9804,40.274,10.465,9.352,46.1968,7.128,5.58,57.5928,22.4316,42.9914,9.302,9.072,2.245,2.3521,23.808,9.3312,6.3504,4.5837,6.6584,6.3504,83.281,20.6946,26.6304,3.7224,18.09,3.9072,56.5264,8.4071,7.476,7.5768,23.7684,2.034,18.447,131.9868,111.1035,-36.1116,-35.928,21.897,15.6332,-2.1896,9.3312,26.6304,12.9129,163.787,27.9936,60.2553,2.7776,50.2425,0.8288,-94.6605,-11.8256,6.8904,139.986,2.4898,316.1392,3.3544,2.3328,81.5949,41.993,3.6288,91.3248,9.2386,24.3824,265.4232,94.0702,15.552,-18.147,16.2688,6.5569,38.3572,3.6018,1.116,8.3916,-407.976,10.0724,76.9816,31.0184,9.768,3.6022,1.008,-18.1176,50.4063,28.497,97.1892,3.8048,3.5475,34.2144,26.649,26.703,5.605,-131.951,27.5632,-95.67,0.0,5.5755,3.3453,121.4416,22.9877,-1.7514,-12.0588,-12.0588,-5.2416,7.8176,37.797,78.5088,148.704,63.6825,3.6288,0.546,6.206,5.715,5.796,23.028,2.0322,57.5928,-37.7332,9.387,125.997,129.3786,1.4952,1.512,2.5056,12.99,5.9364,70.198,8.6112,-1.249,5.1948,16.2486,45.487,214.76,1.9602,89.997,14.5638,3.9498,10.3488,9.8856,2.838,1.8468,19.0344,3.8976,21.06,4.239,1.9024,11.5432,3.9592,16.6568,5.346,-9.1335,2.7166,52.776,30.2232,-38.85,2.5056,7.9086,244.2496,239.996,14.985,9.499,4.536,4.068,21.7728,40.3128,19.1808,-216.9783,125.3,32.098,77.4837,11.0808,4.36,5.301,-69.312,7.6154,9.6957,-172.557,6.2995,-84.2928,5.6784,7.264,-130.0104,10.7849,20.9592,-331.96,52.4895,2.3976,9.99,3.84,23.316,3.384,17.466,45.84,1.4442,5.7768,3.7308,-168.9558,26.4132,9.234,11.9412,9.3184,3.6288,-13.392,-3.6372,-5.9409,60.1398,-29.2524,10.5072,68.8464,21.024,1.6308,-31.008,173.0316,219.4514,1276.4871,8.7906,12.586,33.995,0.1512,2.3814,5.837,-2.6256,6.2208,56.2032,-10.1178,56.9772,-166.32,-24.189,6.7252,23.232,3.1806,22.5296,31.494,20.1584,27.3568,-5.1396,7.6968,-28.356,-30.555,125.2692,7.1864,37.9962,51.36,2.208,5.7408,8.9544,77.8635,26.388,-184.8366,6.129,134.56,17.982,134.9955,197.991,32.9817,229.3018,41.68,83.868,23.94,496.0725,12.4416,580.5394,66.5088,12.376,9.102,20.9208,2.6536,67.1916,21.996,19.4376,107.082,-40.0036,9.9522,113.4936,5.1792,7.4872,5.8812,21.0752,4.0456,-44.196,6.7008,50.4711,4.7196,4.9432,33.831,4.4564,-347.1174,-38.1114,-0.91,22.4808,-209.7693,-20.5623,25.68,73.194,10.647,83.844,36.4044,245.021,1.9656,10.626,5.7825,4.6956,6.1572,0.1472,14.212,14.1694,90.7152,34.47,0.5994,68.3568,10.3974,85.3092,240.8595,4.7916,57.4938,11.8768,-18.5562,-56.996,-14.5656,19.458,14.3376,10.5,32.392,1061.5722,31.0059,8.95,22.4808,2.6208,12.2325,-5.088,-19.8744,-127.372,-97.72,1.6896,155.727,20.1584,5.4432,4.0768,6.206,74.0532,160.6722,9.039,352.3065,26.865,14.5614,10.3152,3.8864,-172.4925,357.1911,28.7904,-8.1312,-7.2048,1.0904,0.6474,8.4024,-16.776,-4.8588,-15.1767,0.0,56.5662,0.0,-6.0324,9.7164,1.0797,1.7514,0.3492,0.9612,11.196,17.908,0.8162,19.797,0.0,53.7504,22.3548,3.04,117.432,14.5152,-2.4288,0.0,-22.7964,3.6855,4.872,7.1928,1.64,0.84,108.7996,108.7408,9.072,10.368,2.904,71.99,6.972,-3.6288,2.1762,19.9746,62.1376,3.2432,10.92,7.644,-44.1552,9.3312,163.1898,6.8714,5.368,-6.867,67.86,0.3822,15.9912,-35.178,47.848,174.9975,-46.7362,12.0764,10.647,-87.9354,68.8464,4.0664,14.1426,4.485,3.6288,4.6488,15.552,2.224,1.4112,7.049,213.735,47.8065,52.1262,57.4113,23.0864,3.6288,7.056,43.1976,6.398,83.284,3.8016,-14.6388,-17.4588,13.8528,44.955,3.278,0.5668,3.9004,5.6112,2.7956,12.9978,28.7928,4.3902,-2.249,4.485,-46.3946,4.6782,6.291,11.0544,1.1994,-13.993,3.8272,2.6814,1.3068,-25.9136,4.5188,9.6048,-4.032,2.2098,1.8288,93.5948,-21.888,15.0984,5.8604,3.8048,160.623,15.4872,-140.196,9.7608,10.7301,30.2778,3.1552,50.328,38.5722,-5.1968,-14.229,10.0744,27.2848,25.792,50.098,-12.9792,29.673,-93.99,-1.827,3.2256,1.6688,71.772,68.585,57.5928,6.4944,1.3316,19.1646,-5.712,60.4752,4.95,37.797,-29.94,0.924,11.803,179.1888,7.9984,34.2848,4.5008,327.506,3.1752,15.0416,34.6983,18.3276,-12.09,36.1827,-13.32,70.0977,-29.3436,-10.0602,113.998,-109.5822,-26.8544,-3701.8928,-26.946,9.2556,76.5583,32.2322,38.08,0.0,16.5186,12.9888,5.191,259.8896,29.364,1.917,10.2245,12.1352,6.9132,5.9211,12.549,9.116,226.3626,26.598,5.7672,33.7212,18.7812,-161.875,0.2925,7.945,34.9965,219.4416,4.7792,104.7222,305.13,27.5292,4.264,124.6752,12.8744,7.0224,294.671,0.6312,22.2516,41.934,2.0064,1.636,9.8418,21.259,53.2608,36.7173,83.9916,22.6476,91.7728,-3.0344,22.0748,55.745,-10.7973,434.9913,-7.7728,83.9944,110.0528,274.995,37.23,17.253,22.6296,5.4432,-0.9486,9.6048,643.9825,68.198,-6.5415,-43.8336,22.298,2.691,10.6522,10.7912,5.434,18.767,6.7392,98.105,41.7186,98.1396,15.8436,50.396,-1.041,31.6128,10.8864,4.1965,0.9963,6.2496,41.823,17.127,29.692,42.8148,-52.632,15.093,30.2112,-12.196,-227.4912,4.5612,8.2616,122.3856,52.532,5.4432,10.3473,172.4814,1.148,1.742,-58.8616,26.0316,22.5732,421.5853,-6.0196,9.2552,145.0696,1.0269,5.6644,-1.8126,9.5256,5.4432,10.773,17.3488,12.4416,0.51,10.8864,69.705,1.2672,22.5008,4.4352,2.6936,6.3744,6.63,44.0316,7.4925,-16.6848,14.5348,-2.2896,-4.5696,12.4416,1.652,2.6376,30.432,-39.804,13.1868,75.5958,-19.8144,4.0584,8.4966,52.4895,1.5548,2.5056,22.984,6.4128,2.4824,168.1855,7.384,16.011,12.5216,300.735,6.4128,-110.7645,-336.784,10.8054,53.8608,9.594,11.891,18.504,15.6426,10.8864,-6.0192,57.12,8.3104,843.1706,8.955,95.1888,7.0218,53.9946,8.0712,-121.2705,16.17,4.9497,-11.52,7.056,1.999,19.824,27.4856,12.1452,4.3176,8.4736,-14.5764,111.774,-2.918,7.3872,-559.356,31.47,-22.948,9.6632,-4.818,-6.5076,-533.7325,5.7594,14.7582,213.6888,20.1207,28.3095,109.6113,6.2208,4.1125,3.5529,15.3888,45.3488,23.6529,3.0128,4.195,-1359.992,1.9698,8.4966,21.6,2.7324,-58.6347,8.9985,-453.849,1.6896,6.2664,61.4628,-79.3352,12.8583,4.1916,24.3595,-24.858,90.2871,121.99,2.646,91.152,6.8136,19.4352,-13.81,30.1968,13.4372,12.838,79.8912,-571.9956,-31.6204,212.1876,12.8928,2.6964,-4.8528,5.4432,3.405,51.8,5.0232,238.653,148.704,76.47,7.6048,22.1184,4.7236,21.7515,-46.8776,18.7695,3.6288,-8.029,30.0957,149.382,10.906,12.9792,420.588,2.2824,7.1586,9.7438,-12.432,20.06,24.47,1.4742,5.5341,60.8832,2.679,5.4432,53.55,75.9924,-2.0016,5.955,2.19,-9.7176,198.429,-1.3608,1.3,5.0922,-6.723,3.7743,3.4368,8.983,4.4174,2.14,52.688,1371.9804,80.6316,-108.3348,21.0654,6.552,31.4916,-131.12,-13.6832,6.2608,16.8896,7.0218,12.582,-21.945,46.47,85.9818,4.782,13.078,1.6762,13.1956,16.776,13.4292,46.3185,1.2112,0.4592,16.2204,-4.1244,-509.997,-45.8273,3.58,-944.9946,0.1134,7.5762,177.4206,24.9804,-251.9958,4.5816,6.5754,11.8584,157.4875,35.3346,140.396,26.3912,10.6428,36.294,3.475,-70.49,-407.682,661.4559,3.852,8.0548,50.9082,-10.0196,0.9856,-7.476,-5.037,23.9984,36.8245,9.4815,15.4752,17.334,701.9883,4.1151,10.881,7.5284,17.1678,7.3132,27.7182,3.1104,7.0227,1.6704,1.3944,5.7376,35.0784,-82.884,42.3625,83.7096,0.4068,15.525,16.196,4630.4755,6.47,10.08,15.552,6.924,2.8536,31.494,47.061,5.4488,20.5176,8.4784,1.1016,-97.2312,-4.3584,10.56,2.3686,0.0,3.1032,0.4728,1.2528,11.1024,-1.4016,80.6312,14.3952,73.194,38.456,-4.577,4.7664,9.3312,40.1702,37.6422,45.294,31.2832,12.4902,3.7408,16.8544,16.7886,153.4725,-337.806,6.8016,18.018,3.14,-81.8544,1.4784,53.196,-20.1528,3.1104,223.054,2.9568,37.9848,362.8404,36.3816,8.694,399.2994,2.8776,59.6556,11.2476,24.47,5.4432,5.1816,13.4925,0.0,20.1579,1.46,-0.0895,-3.264,107.46,3.4104,4.6284,13.7646,4.887,-19.0656,3.5858,1.7248,0.8688,-3.5622,-3.768,4.6176,-3.0396,-70.1043,4.1988,0.4644,31.0856,-6.549,13.7428,6.7915,11.49,34.993,-13.637,54.0876,7.68,1.9089,21.112,10.744,55.764,4.9878,31.0688,-2.9985,41.934,-13.3936,7.4872,13.7646,3.5154,112.574,-1.5715,71.9952,-19.168,66.1451,-71.3958,10.5714,-65.0352,8.2992,3.4357,19.041,3.9248,3.7436,67.9833,58.65,6.2031,4.172,2.502,4.3624,17.472,2.8101,311.652,6.304,2.578,7.1346,27.0578,3.2256,62.0368,9.47,-8.532,22.246,11.0016,6.9368,624.9875,-4.8609,100.685,30.09,260.6112,16.194,4.0383,-7.8588,2.8884,86.3856,5.0232,-17.248,-17.9964,-1.5936,11.0388,3.14,0.4704,70.9644,-35.046,145.2816,362.687,27.882,19.692,11.7576,1.122,68.9631,9.0,6.5856,20.097,7.0224,71.9928,8.4784,-24.588,1.2376,-14.7594,7.9378,31.5825,-147.8655,0.8804,13.7016,12.2715,9.735,-122.877,112.3508,10.3936,12.9096,11.1384,3.6288,3.792,-9.5886,0.5097,18.528,38.396,3.196,3.6288,4.0338,2.245,14.4222,38.178,-36.294,0.0628,74.8142,35.6636,0.891,341.994,20.878,12.1692,-734.5264,5.2164,8.2782,30.4278,5.3892,3.717,47.8629,83.5128,481.47,7.7748,15.6768,4.2804,4.7752,18.715,-9.147,6.03,-60.6078,22.0748,-94.333,22.2,-17.9424,247.996,4.3176,110.1195,1.6356,-2.61,19.4656,9.63,15.5376,54.5916,9.8208,0.8988,16.3172,82.2906,154.8426,1.41,5.1012,239.976,5.2182,105.2468,16.0356,4.6193,-107.9928,24.1218,-10.0464,7.7679,-13.4694,15.0984,18.336,1.1772,3.36,3.3756,-1.624,2.8478,-299.2614,48.5514,18.8937,-10.4874,-51.294,-64.4274,2.8224,219.5088,-64.5444,129.6,13.071,0.7938,13.4292,66.6344,9.3312,80.0226,139.99,5.096,2.7222,18.8732,24.1568,1995.99,8.226,16.7946,-34.196,-8.796,-94.5084,-6.445,8.8176,40.473,16.2486,20.9664,46.179,-2.214,9.0576,-44.2782,26.9526,9.072,0.0,5.8233,13.8828,3.5623,68.8464,9.8901,5.8708,2.8416,25.0182,28.819,24.9804,21.4776,10.4784,87.996,3.4092,45.528,4.2861,60.1536,18.3264,28.008,160.623,14.896,112.788,7.128,1.521,5.778,11.1664,11.9586,11.2648,0.8056,-7.9634,16.704,7.7896,13.3176,21.7845,2.19,15.0735,6.894,-1480.0335,15.3195,95.0968,55.764,6.756,109.7208,55.9984,75.49,7.8735,7.9248,57.5928,2.0228,-1.9744,-250.5408,762.594,-56.996,4.9632,12.7008,31.4532,-12.9987,0.334,5.8604,0.8856,-3.123,-6.9102,25.5968,20.8719,14.6224,6.36,233.2204,15.552,5.2256,7.2576,5.6448,21.024,3.2352,204.0714,7.78,0.4752,29.1424,3.285,146.7693,5.3196,36.8245,25.1979,-17.9928,10.3473,2.4012,14.256,-1.0656,10.9584,14.2688,42.3625,7.9984,352.296,792.2691,72.432,26.565,726.5619,2.478,-93.99,-50.098,3.89,81.583,17.22,14.9292,55.016,5.2773,-4.9164,9.891,-175.26,-16.3183,-66.801,-99.2664,-107.9928,94.926,43.2234,-1.4256,-23.892,12.5328,-8.6592,-30.294,-2.0774,-40.7976,-7.476,16.7875,1.9845,10.8,78.9516,79.8912,4.5816,1228.1787,235.9524,131.0296,7.25,41.986,-1.1874,102.2784,57.5016,17.37,12.4416,216.8244,4.536,0.5508,16.7475,3.0268,1.4742,6.2208,28.497,9.6975,9.9873,301.968,-16.467,4.8804,-11.0848,24.219,156.751,5.3392,290.3016,7.9527,6.2979,10.4832,6.7482,1.6632,23.84,-67.941,-2.5472,8.802,-87.1488,21.1977,-35.5136,8.88,9.6712,45.576,-250.396,4.2336,9.7176,53.3466,48.906,-4.5936,27.3096,7.98,0.4264,-8.0775,12.4416,-18.1068,-209.994,-34.9176,43.5981,69.1776,96.3438,55.896,0.0,93.0552,20.1248,47.243,54.4008,2.604,-37.9434,1.9926,-121.8735,12.3096,10.5072,0.882,-3.9624,8.2901,5.1012,4.6806,5.7672,78.3888,-14.475,-87.6672,2.5592,44.712,7.0218,1.512,5.4432,-167.27,40.1702,5.6448,11.3512,39.98,1.316,40.4012,43.736,-4.8392,3.9609,29.4492,19.872,22.3734,0.1472,4.3296,34.9825,11.7936,-199.77,6.0368,11.7782,1.764,3.945,71.99,15.2,29.2716,3.5994,-4.428,-16.614,-51.984,78.851,1.4224,3.2406,28.518,9.5968,673.8816,109.998,12.5928,15.5856,12.7008,-19.2588,0.833,1.4406,-23.976,7.2036,23.6808,29.95,-24.803,64.7568,7.1628,15.768,52.7824,-110.49,73.41,-6.3441,134.3888,12.4416,62.3904,-23.952,76.6395,5.6784,35.6613,-9.1845,6.8768,1.8612,-30.2288,117.6147,62.988,23.0864,11.907,72.5754,-44.985,7.2,111.3024,-7.008,-8.05,-31.536,-120.372,-4.8492,-14.3856,4.6746,327.9458,-8.3524,13.7176,-170.8038,48.5392,80.7912,70.0336,2.4192,11.1664,21.0128,-4.5192,2.9304,19.755,-2.6025,-18.186,9.0636,3.6288,3.744,45.294,28.5984,6.0416,-53.0088,16.9932,3.7408,2.9568,20.7459,9.585,-1.2588,125.9972,4.2294,12.4416,5.2256,37.2204,42.0256,4.4352,4.5144,4.331,11.9988,-336.6272,0.6258,95.586,7.6284,135.4068,5.8233,-4.1712,-42.4926,0.365,41.5104,7.6965,-13.896,-52.3365,2239.9872,42.8935,0.2952,0.4706,-2.1885,13.9728,-8.6768,1.9712,-9.153,-21.808,-108.2662,-7.476,101.3832,7.9984,9.7218,-2.5872,70.196,18.1176,14.6718,-74.9526,70.5564,39.5,52.532,-0.8558,95.9904,12.7008,0.6696,11.214,-4.0216,-7.7406,5.4432,36.4473,8.7945,163.7874,72.975,-18.585,74.8524,1.9629,-3.6892,6.8714,15.8376,1.7343,74.574,-49.5516,29.2857,14.904,12.298,0.0,-8.18,2.64,493.7856,152.495,100.122,496.7865,3.8073,9.072,-42.4116,77.672,21.5928,89.5888,10.3936,36.3018,50.414,1.1564,-21.4704,7.9488,149.148,35.76,-14.592,9.912,56.264,-31.332,3.1752,44.9616,100.1403,58.0272,0.504,15.9348,-1.049,-10.6068,1.8144,6.4784,-19.5492,15.8256,0.2034,13.1985,41.4294,17.3656,3.6322,101.3488,51.1485,8.7285,3.4684,5.5177,18.267,5.6316,8.1552,-42.588,-14.773,-8.5794,1.1022,9.2988,6.1641,20.1558,0.1191,-24.5646,-62.88,19.188,78.8592,1.1136,11.7208,184.26,-8.4728,13.8915,13.896,5.4332,3.6156,-694.2936,23.028,5.778,3.0016,-19.7712,-18.2352,161.9674,-25.109,2.9646,503.7822,29.9646,66.6272,8.6744,84.51,13.299,126.3942,6.8768,44.4,47.92,-5.6943,-4.8048,6.045,9.504,23.9904,19.1976,4.6644,287.982,-50.6688,35.9964,8.217,7.9896,-50.3928,6.992,2.8536,-192.0468,14.3952,4.7067,30.735,19.0386,-3.6576,12.8499,28.7679,-8.8038,-459.9875,7.0218,91.9508,742.632,151.47,78.6508,27.3528,8.694,59.493,196.686,23.384,11.4741,11.5752,16.1602,17.9684,-950.4,22.2352,4.4792,9.6192,-244.323,8.88,-14.6958,2.6568,3.6288,84.66,0.7938,-437.5404,19.95,15.5232,69.1992,8.2156,4.6088,-6.9282,17.55,23.5872,15.4752,9.25,-1.3566,24.2285,45.7632,49.9704,11.1176,-373.3048,2.6376,-43.1178,120.9468,2.2066,-21.4236,1.5552,92.97,4.8118,38.024,24.5028,10.008,2.004,-312.0614,-8.5416,-13.1706,6.8714,13.9392,2.132,84.0512,0.0,-54.5958,-100.7944,-36.253,-1862.3124,5.0064,215.9973,81.8496,16.5354,16.1504,6.2208,4.0986,41.076,50.9898,11.076,35.0244,15.147,1.5312,1.7608,-125.766,-4.9878,4.4004,82.3368,13.455,2.9346,266.4522,6.3504,146.2405,1.8011,1.728,-26.9955,4.293,6.5,-30.588,13.5324,89.991,22.941,7.724,9.5787,0.8997,-80.9955,187.797,0.897,-11.9616,-1.6764,26.5905,13.0375,64.7856,195.9944,4.176,157.0176,9.3312,6.4128,16.146,17.3148,41.2237,28.0876,-0.8886,4.4352,74.5654,2.999,23.0864,1270.99,20.6336,6.72,3.8136,10.224,1.512,-28.224,1.0598,80.838,2.2044,-3.3879,43.8408,-28.2744,6.2244,0.444,1.1988,-36.1176,27.0112,34.742,-20.7846,165.3813,50.94,2.6416,63.9345,67.608,6.6976,-93.2316,16.3863,-5.4548,-470.548,-16.818,6.0416,2.4864,-1.289,-7.098,14.67,-1.7892,2.394,-1.8848,377.9946,95.7572,52.734,33.2544,170.5113,14.9156,223.2855,82.0776,4.494,9.3312,97.4586,0.8946,189.4046,-14.5656,22.4925,29.799,1.6704,25.1496,-1.8904,2.9322,3.86,1.764,1.4418,91.7728,102.9528,39.7488,9.3312,315.8118,7.5992,1.6776,2.577,3177.475,44.7096,3.3948,0.7398,6.3072,240.8595,2.1684,11.685,18.1146,9.1314,2.7036,39.6879,-67.6704,6.3684,100.656,23.7742,4.8924,1480.4671,8.6736,19.6686,349.3392,5.8604,3.597,6.8714,-4.396,24.8832,6.1308,20.1408,16.8237,353.5792,2.5641,11.995,53.9946,-9.8463,96.0232,156.338,-25.9136,15.6332,185.997,1.1988,5.2877,89.5888,-21.168,48.5392,-33.8418,5.4768,0.5584,-29.2524,14.202,16.68,86.3892,92.5056,0.5244,13.132,-35.9058,23.235,3.4086,12.51,610.8624,5.0328,282.2092,3.348,11.2308,5.4432,1.7004,16.032,24.936,99.9408,131.2785,20.7675,9.5616,4.5402,21.2512,8.1144,1.4456,-110.0232,8.526,13.572,27.986,35.6613,-7.833,24.2919,-13.734,32.925,-80.48,-0.6265,1.7991,2.628,3.2944,27.7911,0.438,209.993,5.8696,4.3524,22.764,107.346,2.37,7.7688,18.396,-68.392,-3.2175,21.1428,-9.7972,-211.47,-115.7156,26.3934,6.4368,89.2224,-6.952,2.8884,-12.075,-16.884,4.4604,5.256,16.1838,5.8708,12.4416,47.994,-1181.2824,1.0269,-13.8717,144.3546,3.0498,6.0147,38.3508,4.3308,14.3136,10.5552,113.848,10.104,215.9892,24.2696,34.9074,0.4074,17.8152,19.3932,29.5776,10.8864,8.0178,15.8256,0.3864,0.8058,69.986,-113.282,-15.098,41.993,-45.294,17.9982,-97.7394,2.6406,-46.225,0.2353,-27.7158,4.0872,-2.2134,-4.9005,2.8392,125.5824,119.686,4.57,1.2792,4.5216,148.1064,485.9892,2.7846,21.0249,36.852,419.8185,129.348,5.8604,68.5965,2.224,6.5058,17.9634,35.3346,-20.245,2.9568,17.0981,-6.8992,10.3071,0.8856,41.535,30.0144,8.2848,6.123,24.4768,-2.2878,9.4717,5.4432,27.882,-52.8336,-512.1468,6.2208,297.69,44.046,77.7519,81.432,131.586,51.8292,9.798,35.6796,7.7679,16.6764,7.5371,9.8164,4.5318,16.17,76.272,-55.256,90.8292,-23.7822,-76.6062,0.4264,-114.3912,1.213,15.4752,6.3936,17.6232,-18.196,-5.8346,38.997,0.73,316.8825,3.267,8.8686,648.5624,2.6811,41.496,1906.485,-18.8728,-20.3322,2.8884,58.66,13.188,3.792,1.7325,3.1104,9.702,-15.2225,-255.7425,10.449,14.2992,11.094,4.4138,10.518,10.794,4.6548,10.4496,2.9889,13.8579,5.193,106.5408,17.3488,14.2272,2.5578,-0.3444,6.5164,21.8736,2.8884,122.3856,-9.594,-36.1764,2.0475,118.293,12.864,-8.9152,35.2604,21.0128,5.3784,-31.3722,1.2528,21.99,0.5904,1014.9797,9.3312,18.2112,105.8316,30.1872,21.294,7.1586,11.1564,23.9169,3.6784,-2.918,-191.619,16.7972,5.778,41.5688,4.9248,9.8901,69.6546,11.556,-15.9268,20.1584,5.6,16.6788,55.896,0.8088,-3.4272,41.9965,31.7512,81.2646,62.8075,17.76,17.3488,-6.098,34.4148,-13.6312,-10.3936,8.7906,31.996,15.12,-49.92,16.124,4.9308,5.3214,20.392,-4.9128,-52.9584,8.7672,-18.0312,29.3412,334.4985,3.7996,58.1796,13.8915,13.7016,-12.796,245.7,87.7443,19.5858,-13.0152,-163.5767,8.0712,1.6776,60.1412,4.8609,11.7334,84.5728,58.38,36.3972,50.3832,4.4312,53.8048,-4.497,7.8936,5.9384,-28.6862,-79.908,14.346,1.7901,2.0574,6.003,21.714,2.436,13.3371,160.623,21.7728,5.6994,28.7064,15.552,140.5482,-86.0586,-4.1568,62.91,2.9145,3.8655,2.3997,36.4704,44.8896,7.56,-6.237,1.1556,26.271,21.0288,0.3024,770.352,2.9808,48.5392,134.652,140.686,1.9926,54.215,-61.872,9.102,61.389,16.7886,181.656,-9.1648,13.2986,11.732,83.9944,5.7624,13.2,35.994,14.3068,11.9952,3.4686,3.0558,395.988,169.182,4.752,2.632,-12.208,9.072,1.002,3.15,45.4671,0.3336,13.2,-6.462,54.215,-13.3936,-393.602,0.7425,-8.1675,8.7735,92.3936,-42.8,-26.964,6.2208,56.55,15.552,16.6796,10.203,15.764,10.7892,-3.14,21.1428,7.3008,-62.88,51.8312,-182.637,31.198,7.596,7.2576,4.1988,4.3296,6.8768,5.083,6.9384,13.428,314.9895,0.2996,13.734,3.8822,3.1104,15.552,8.8044,14.9556,5.1072,2.99,-19.5624,11.0704,-0.7295,-36.4704,22.5576,33.495,-25.3764,1143.891,9.8658,2.1728,9.3444,56.2744,7.2576,-4.4946,15.0742,3.5784,19.4688,4.3326,-3.3264,20.724,15.8496,140.391,16.608,58.5052,-6.104,-9.5568,87.7443,14.3075,3.1104,4.0192,1.9926,91.9954,47.241,100.4796,15.743,37.7916,456.588,2.3312,-525.6405,74.691,18.0,19.0386,22.6764,1.7919,8.9985,9.3228,-1.476,5.24,1.6704,-20.7306,27.735,-17.6076,57.358,10.8864,9.1269,16.1838,79.9056,69.1008,109.3365,15.6078,21.0896,8.799,4.1634,42.225,54.9976,1.9926,46.632,-376.6932,5.4432,11.232,72.8946,1.7591,1.3098,9.3312,3.2872,-2.3136,5.6376,-85.2384,45.954,4.0338,8.352,48.9942,-5.8346,6.0025,-92.7996,3.7692,144.5157,4.9686,-29.4812,56.5776,2.436,285.9896,4.4892,7.4256,4.2717,0.7392,8.93,-2.436,2.175,-5.784,0.7392,6.7008,2.8912,-17.0352,63.8862,2.499,60.392,156.429,6.6,21.4032,70.5456,32.5376,42.045,0.8385,3.0268,59.0112,5.6994,-121.58,20.0156,209.2365,5.056,28.4809,40.4973,-2.244,12.974,34.4232,36.225,-2.0016,0.834,-73.176,3.4848,-4.752,13.4865,-37.1124,193.32,103.8982,-2.9884,49.4376,53.7544,-5.4801,16.704,30.7168,0.6912,-2.134,4.2804,4.6812,-66.5088,18.6624,321.84,-191.646,49.716,6.7048,-64.7748,-219.1644,39.6312,43.7842,191.968,78.7671,5.4144,63.135,2.0358,3.4276,5.798,-13.7976,36.7173,176.7864,1.6128,2.1402,1.2064,-1.35,9.7328,49.105,-4.464,-126.4816,124.68,-52.196,45.9754,38.178,11.88,13.4386,20.682,3.6792,50.2398,41.4276,64.3678,62.1414,6.0726,0.471,-18.4624,49.23,38.9975,39.4438,28.0784,56.392,6.2208,25.792,3.6288,8.3868,-204.4458,13.3176,3.0861,78.8942,0.2997,4.095,2.3232,38.97,6.1792,92.3692,9.3312,105.468,762.1845,-290.8752,15.777,3.36,-175.8708,3.8655,2.1492,-188.7,15.5372,4.116,41.88,83.9916,-2.1792,-11.439,-1.2558,-4.896,9.8658,19.1376,13.32,-9.6565,-114.0174,6.4638,1.1151,148.491,34.0704,20.1708,11.7782,10.68,13.064,11.898,10.8588,2.73,28.7964,2.2302,33.0368,210.4942,4.4088,0.2198,2.9372,1.6704,274.386,89.3142,68.976,48.118,136.939,2.9568,-153.1224,5.0055,34.692,69.1776,456.588,18.3456,0.968,15.0156,38.3572,12.5118,19.872,1.8,-31.4874,29.1375,3.1096,34.5,12.1149,15.8571,13.208,10.4148,8.085,5.5664,2.7072,61.389,18.9702,28.1421,211.4955,-2.7588,-1.9068,3.6288,105.6456,-5.4558,0.0,3.3516,0.2592,-112.6216,-204.9996,1.764,3.21,-5.264,-31.6,23.49,12.7008,1.1556,40.8006,-0.6976,-3.8976,-42.747,-8.9796,1.926,8.2344,10.0128,11.7208,3.8024,-82.99,28.1718,34.494,3.2392,-165.768,15.49,16.2864,7.5992,3.6288,152.0232,47.8629,2.772,-13.5548,4.2336,9.63,48.94,6.7236,2.256,94.962,-118.1295,18.3908,-4.2222,2.5056,-75.8304,0.7152,124.929,1416.8,48.9942,170.5113,4.0473,11.7,4.6221,-135.765,4.5882,-3.94,-16.5858,29.6688,-6.0768,92.0835,1.6588,9.2232,1.4784,52.532,122.2936,29.1528,28.9568,267.705,13.959,874.9875,15.1116,1.7472,-16.2613,82.497,11.452,35.6346,200.9546,46.3185,80.9919,15.6993,27.9936,41.697,6.812,4.49,1.6038,335.9944,315.7404,15.185,51.57,27.3592,-149.9058,3.6,62.8075,31.2858,-7.2672,46.602,19.692,25.1225,60.5528,2.1492,8.4888,89.307,3.401,-12.9568,137.151,111.591,2.0492,-6.8334,-6.1248,7.4872,6.7188,-4.8392,-14.688,-25.2185,9.7038,-20.6964,17.3148,2.9568,12.2328,-7.8225,-2.5256,74.8098,18.0648,2.0975,21.4452,22.3548,2.1336,60.392,1.1765,101.394,-6.9828,-14.1639,167.979,2.3892,12.3144,18.9702,0.2792,16.2,2.0574,-120.294,-2.0364,20.1579,-131.994,-3.9384,0.8376,11.88,8.1168,7.0218,125.469,1.5456,83.2508,16.1096,2.0672,17.694,33.0708,-2.5698,29.9808,3.9248,4.004,50.5632,18.6624,79.758,1.576,6.7966,14.904,108.1752,48.9645,4.2336,96.416,8.5722,12.7746,3.0558,4.2392,14.161,0.5828,9.936,59.998,6.048,55.3896,-10.0372,24.882,2.934,-12.148,100.656,15.9968,12.993,7.8225,31.4685,394.212,12.0609,-2.01,71.772,257.712,-8.5068,4.536,12.691,118.6575,5.3898,329.994,200.49,0.0,-2.8608,5.4432,306.4894,-2.0988,2.5532,8.2688,2.1588,29.952,11.4516,6.2208,-29.4368,1.1596,14.6264,1.356,-25.049,158.5764,7.8225,10.896,27.434,8.8784,53.2608,41.2237,-103.266,217.767,-1665.0522,1.043,-7.0532,15.525,15.552,-10.2114,1.1016,9.7092,-5.715,58.7916,-10.4196,3.546,7.9724,8.7138,129.9974,327.5818,31.8892,10.248,78.7528,152.388,9.7608,5.4896,8.8784,2.19,5.07,0.0,134.3328,19.4688,2.184,11.2504,4.3372,23.226,8.8624,-4.4928,-913.176,16.5242,16.956,28.858,-58.8736,32.13,0.0,14.501,31.0912,7.5371,176.386,-1.4784,47.9376,24.0688,2.528,422.51,17.7568,11.7208,118.293,6.862,147.475,141.1644,57.3212,6.396,32.9817,-7.7247,6.255,11.0354,16.5888,53.196,15.552,-63.0056,-4.767,0.3168,-2.5632,4.2,394.268,-4.488,5.4201,335.8548,4.6221,13.17,17.991,6.858,2.3686,1.926,10.4284,1.6784,0.5992,1.8522,1.45,7.9378,5.544,213.7044,155.25,395.9604,5.796,2.211,5.1648,7.0854,19.8276,52.49,9.6192,8.2156,3.799,-1.8106,6.8388,240.2649,-11.5176,-2.2848,57.5928,21.0128,-2.0622,32.2514,12.8744,-4.6464,18.6093,-59.0571,12.0,-9.1788,10.8864,-100.92,47.844,-86.3664,47.96,376.11,28.6578,-48.392,14.4096,296.0671,-3.432,58.4962,16.1868,-1.4988,23.0965,31.2736,25.792,12.4416,4.756,69.705,561.564,4.3428,-22.62,6.2208,-12.7512,73.41,14.2758,0.846,13.6851,55.845,15.246,-0.792,-8.2764,26.5824,4.2309,76.3152,89.3142,10.327,93.594,2.7192,-4.488,17.428,50.12,3.6162,9.3312,20.1264,-5.412,-4.641,13.181,45.528,3.0338,23.004,32.4,0.9576,50.396,4.1328,19.4184,75.6952,1.5008,0.5998,18.4548,-15.6156,-22.449,-2.7,6.4944,7.2576,43.2234,7.0096,-14.5584,12.936,21.714,-103.8606,57.6,-4.641,9.5172,0.559,62.737,-70.9605,7.4752,8.3268,5.2272,27.2412,10.764,111.591,53.982,-1.3104,8.4564,-8.5974,35.0973,303.3408,14.904,-337.806,-54.3204,21.7728,1.002,2.2365,-383.031,2.5164,112.392,46.9764,35.2872,6.567,5.652,-13.978,71.2692,20.0928,0.0,3.401,24.8832,23.4416,77.7438,1.8704,6.1704,1.674,67.992,-6.93,42.8805,-350.49,-95.2476,214.4922,3.894,-186.5682,3.462,15.599,3.2352,8.7906,97.2,459.396,17.22,17.6088,44.985,-2.838,23.9232,86.3892,6.0876,11.5432,27.3582,0.9952,-7.764,12.7008,-13.2867,2.2712,1.0346,1.1225,20.4984,15.0384,63.7776,42.1176,5.664,5.6644,27.0882,-10.336,16.7972,161.9919,5.4432,3.6288,-73.8192,-69.4722,-6.286,-29.1168,23.808,16.3215,41.3374,75.686,-31.647,20.388,47.6268,9.2386,47.8152,-14.603,-10.4874,-161.694,2.6496,9.8901,9.158,4.9082,12.9129,103.3116,16.032,-45.9954,164.997,53.0439,269.308,74.975,3.6784,30.786,7.08,145.782,12.6468,20.0392,20.196,21.036,8.027,1.26,196.6132,9.3906,9.3125,8.019,6.7116,35.982,0.7228,3.2832,124.485,125.99,1.3365,6.2192,106.477,601.9699,13.6776,1.2885,-3.094,45.294,-0.7128,1.773,21.8376,-46.9952,-30.147,38.7792,51.942,41.1208,33.936,553.3902,8.5372,49.2723,55.3616,4.1832,37.7874,106.1242,209.274,2.1476,16.614,25.875,-5.5338,24.196,35.6526,15.7,8.8704,6.4428,2.04,-3.5208,2.478,26.824,33.5895,0.5236,5.319,3.431,7.93,-51.296,178.8,11.92,-16.9568,-28.8678,-84.448,-12.9168,-1031.5385,76.5484,1013.127,41.0388,1.4136,22.0077,66.9546,58.812,79.758,2.4,18.6606,17.6418,3.3785,-17.2854,8.073,43.164,41.823,142.9948,-29.2446,1.638,6.975,115.5528,2229.024,4.728,28.65,0.2016,11.814,16.7875,1114.512,4.1151,6.0114,3.0498,5.1552,215.1198,5.7528,53.997,8.4966,12.3234,1.1656,4.891,7.9212,34.3896,274.995,143.1918,178.91,35.156,207.147,12.8568,43.3188,46.7908,117.1296,7.3132,69.965,5.6376,7.065,-14.5764,-4.0158,16.4403,1.323,-72.039,10.0792,-3.7296,28.6965,21.7532,-40.196,3.4552,-18.0588,42.495,13.482,6.372,-7.4358,-3.8385,40.3536,-1.3995,-100.92,94.4925,19.8716,-26.8758,13.2522,56.9943,43.1904,46.1184,-25.8174,16.98,26.649,2.256,16.65,2.289,20.1558,23.96,-1.1996,9.3812,29.994,4.5588,322.1829,99.432,20.5755,11.7936,35.712,15.642,-17.046,14.3856,-116.844,-1.744,26.9973,229.9908,111.1035,84.5154,36.3987,8.694,141.2775,-15.5268,1.6116,76.0878,22.8582,160.1766,15.552,2.8196,5.4124,54.4047,29.1456,3.069,49.9704,383.931,15.372,51.996,6.098,8.3916,2.244,249.9104,22.7136,-7.3692,16.3215,3.3408,1.308,55.9986,30.9504,33.636,-93.4724,-5.784,-247.7988,8.01,-3.4272,9.3024,-15.4581,-36.294,9.5736,6.4206,35.76,5.0596,7.56,6.0114,23.5564,-50.304,-26.541,9.039,4.7712,-2.544,164.997,22.653,4.914,28.4928,41.1684,0.7348,-67.617,5.369,-76.0116,-480.2032,-1.459,3.9474,5.135,23.1168,165.2868,-11.3372,-3.7715,-13.167,-24.0435,18.2112,28.1718,-2.0622,18.5976,4.9648,-1.9791,19.26,7.0218,-9.288,-123.858,-1.3584,-3.816,-32.5226,10.089,89.3142,5.6416,2.3674,18.6624,4.485,20.727,117.432,-40.6504,7.7832,735.0336,54.5832,9.3312,9.3612,68.9631,0.99,22.3328,180.7659,6.1512,29.7024,6.615,1.476,190.4298,30.52,5.1465,25.176,6.9231,233.9961,17.745,0.0,22.6737,12.5118,7.3479,-162.2296,53.4954,28.1718,88.3932,32.4862,19.2384,3.0576,69.705,-1.0497,4.6764,23.5116,-157.0095,117.432,56.6916,4.044,-19.5624,-8.4924,9.779,0.564,27.9456,29.2528,64.518,15.3952,-182.352,3.4776,1.5602,46.9278,130.87,121.7601,9.3624,87.5684,-0.2685,15.764,-13.6152,178.901,10.8836,12.4416,32.346,-5.823,19.9665,42.588,-122.3928,25.1808,8.2156,15.82,-4.2336,9.8352,29.1456,1.068,-2.3814,9.3312,52.532,2.9346,30.7008,8.7138,16.6536,1.0192,-4.0128,15.552,125.245,267.6672,401.814,19.3984,5.56,10.5754,206.6232,3.36,12.6672,0.777,5.5512,-29.6058,-73.577,9.2386,84.9436,1.168,-337.638,9.0288,539.925,8.098,68.3332,-1065.372,12.012,10.3896,29.8802,6.253,11.376,8.2764,13.832,-6.0324,8.7906,40.4012,122.148,14.6718,6.048,0.5998,76.4,4.504,10.9602,4.4312,78.435,12.8058,-19.9824,17.55,11.1132,9.7092,4.672,-89.089,50.4426,449.991,-58.6872,61.96,-4.851,2.0228,-10.3824,42.1504,6.723,48.9516,-24.2352,3.1104,33.642,19.1786,6.8724,238.653,4.3904,15.065,3.1104,20.5114,97.1946,0.0,28.7712,70.98,41.2938,1.2006,6.2208,224.4426,7.209,2.3408,150.36,4.4392,11.996,5.1012,130.7581,40.12,16.6698,200.49,9.3024,2.8224,20.585,12.672,36.4473,4.4604,1.2006,32.6332,141.1644,15.764,18.9888,84.9436,-108.8304,0.4984,12.4416,3.4357,21.4074,249.995,1.521,4.6344,1.148,31.4975,35.9964,-8.9796,38.6848,96.3438,-7.5768,61.3305,10.984,9.6936,28.7064,-248.166,0.4752,10.35,15.0696,-6.534,-143.7904,93.6988,15.876,0.5967,21.645,3.6156,48.94,7.4496,2.2194,6.4308,8.8624,0.5152,16.398,34.8928,128.9742,27.3735,9.855,6.2208,49.4376,9.3312,15.2208,4.5816,34.9648,18.94,1.8048,35.9964,5.1816,10.5,11.5587,10.2588,3.1104,20.724,15.764,1.9712,2.7324,12.8568,-16.998,69.0018,21.5397,-2639.9912,607.608,36.372,377.9622,18.6006,1.4104,2.3406,7.052,14.8491,136.665,31.374,53.261,38.4372,14.4648,-15.7514,16.998,-19.7372,48.4704,1.476,24.936,3.556,18.8784,5.9904,-145.5246,7.2576,0.5992,7.7728,13.8579,0.444,43.4352,-105.3164,14.651,2.5056,0.2016,556.974,517.4793,3.3088,4.779,84.495,56.9772,-2.22,10.881,-71.8116,7.704,3.9512,3.9474,51.1936,2.772,21.42,26.6304,11.9988,14.628,-33.6414,135.456,4.5738,356.0414,0.3384,9.2178,14.2272,4.7976,137.264,36.852,0.0,4.9648,1.6784,56.3528,7.2268,2.7168,21.5824,63.7392,99.432,1.7352,1.5795,-786.744,37.1812,10.3488,11.1984,2302.9671,6.2208,19.0848,1.8148,-13.8432,8.2302,3.7752,-383.9904,74.213,3.3408,3.6288,4.8804,124.488,8.073,56.196,6.174,8.4966,0.9512,46.8996,19.9746,20.9274,371.316,-68.392,224.9925,-15.4764,99.9408,-90.3762,10.434,71.97,14.161,51.6558,103.2284,2.2512,8.194,35.415,3.4848,-46.9764,-3.168,16.0056,0.7092,91.9508,61.389,6.7068,75.168,-464.697,10.3488,41.7564,-12.7302,31.0184,-15.147,1.3596,1.551,0.0636,286.713,122.148,35.985,14.2386,31.5192,52.38,38.15,44.5278,-1.3248,-11.439,167.808,0.5668,-5.8496,27.8944,152.495,-26.7204,38.2668,67.2742,13.572,350.427,-6.21,28.615,-5.264,5.346,0.584,119.996,-80.178,40.6878,0.5904,5.1786,10.0282,-10.9611,9.072,5.952,10.8784,49.8435,407.1288,-24.6624,118.983,3.792,141.723,34.3656,13.2962,7.7035,8.9362,5.4432,20.5764,-9.8724,31.5776,32.4684,7.5992,40.1702,24.5998,-15.5826,91.7892,1.3514,17.3376,28.8576,11.7741,4.2224,31.6,64.518,66.9546,13.1956,76.0116,-5.7588,9.499,37.366,-20.2356,4.2816,6.2208,6.4864,0.3024,22.2,9.2176,15.8631,-67.6704,2.7336,42.9914,406.7154,21.5964,15.68,8.28,2.3025,15.092,-99.3453,7.8166,0.0,10.3168,52.8228,12.2247,17.7744,76.2525,143.9968,-538.446,7.7728,-59.8356,5.8914,-2.6784,5.4432,27.783,8.2194,58.9192,11.68,635.495,48.5392,14.677,7.1022,5.898,18.2,2799.984,-77.4732,225.264,23.5248,3.9512,3.7208,7.2177,1.6196,170.9316,0.189,7.1592,-31.9936,52.7956,60.2553,28.3095,126.0558,1.5444,160.9139,50.3658,6.9716,78.9412,-18.1808,21.0,3.6018,38.9975,10.6232,0.0,126.8973,11.151,39.5868,0.6993,7.4824,175.5156,73.41,2.1465,68.6868,-47.1798,4.6464,2.0748,124.485,3.5752,36.4736,1.8312,1.8144,2.61,34.9888,39.5868,-225.5568,39.9234,-2.6982,33.3136,6.6846,4.0749,14.6718,9.7176,5.5674,0.7794,28.959,80.0199,-26.726,6.496,-2.7588,10.9368,1.999,32.4342,66.542,8.983,15.2208,5.0055,55.745,137.2896,21.591,17.52,49.5552,-6.8816,28.41,18.24,8.3328,105.2468,12.1348,2400.9657,13.9986,-264.9208,7.605,129.5865,0.7776,32.3982,11.895,219.4514,33.5895,-786.0144,79.8912,-127.5792,37.758,15.5092,-56.343,11.9952,5.7365,57.5928,64.2,4.9271,3.528,50.4063,-0.812,-2.7648,-71.99,-1.4982,-6.3018,-12.5103,-99.2664,-194.824,1.5804,-25.3344,-7.1148,49.3938,3.753,22.5732,8.388,-1.3464,48.3336,6.3504,-3.8385,85.2475,44.304,-14.1696,8.7906,23.31,3.363,87.89,88.725,6.5435,7.152,-22.098,5.1015,377.73,7.4985,363.9048,31.5372,9.48,19.7714,8.2062,125.1432,-31.3722,40.274,77.0352,14.9744,6.7655,6.2208,8.991,13.4964,19.194,-5.524,-643.71,-41.5176,-138.14,13.9185,-15.44,-28.368,47.495,-116.9805,0.0,44.8896,40.9216,7.3528,20.7,17.766,-2.1624,196.5036,24.528,15.2388,-22.1382,1.8792,14.1426,16.3737,6.2905,4.3524,-14.196,-35.8176,21.0128,1.6472,147.0896,84.502,-13.6461,-143.431,252.59,-20.1362,10.3168,297.6435,62.3904,89.955,15.9446,-94.941,87.18,-98.8018,6.9088,-20.724,6.8908,-20.1362,0.8994,7.2576,3.6288,146.4036,38.038,-12.8961,1.5066,0.504,0.0,-1.4196,-4.752,14.6902,19.3314,25.198,-241.176,1.6324,10.3408,17.856,244.6155,-17.9964,5.9185,5.538,8.6436,18.398,8.7032,11.1776,15.9446,0.8792,2.9302,7.85,14.9814,124.2,9.3125,15.9348,60.9552,-36.1764,-36.9544,-167.986,6.74,5.5566,-60.8361,1.1994,54.666,2.8536,9.1312,7.9248,0.2598,71.2476,15.4752,9.8625,1.1225,3.0144,18.5136,292.776,3.285,4.6644,3.0976,22.8904,9.936,9.7164,378.274,3.21,124.7808,-83.205,22.0472,7.4376,5.9988,8.0652,37.7874,13.0707,183.995,-27.7158,13.8572,-163.4516,336.635,2.5146,374.9925,18.2112,146.388,0.9828,3.6744,64.7892,-4.1136,-1850.9464,6.9864,15.824,14.4,3.2161,8.6016,88.725,-100.92,10.374,12.7008,2.5984,9.6192,6.2208,3.7996,-4.8588,31.984,12.8151,134.654,2.4288,6.549,15.6104,-6.5296,81.1314,44.3664,3.2224,6.2208,8.12,6.0264,-31.9144,-5.1984,3.4668,9.3312,4.6228,13.734,-36.441,75.6624,28.755,-22.6716,20.0851,2.8764,38.38,4.2976,11.7782,12.18,105.0228,5.8604,2.9145,68.976,0.0,-0.7748,54.7425,76.6395,-145.3508,0.864,8.3524,11.891,40.0036,3.2868,2365.9818,3.7236,9.0055,24.2352,4.1391,6.2856,13.846,-48.9549,3.2616,-67.137,7.9812,-93.4724,55.0584,2.0271,1.8468,77.7468,3.248,2.2504,13.7964,1.971,21.228,17.99,10.224,1.476,0.7794,-58.1332,3.2676,12.987,1.5288,146.79,15.372,2.808,-126.8592,24.8832,4.4892,-12.792,-67.272,10.4148,8.3538,7.068,0.8064,-814.4832,-34.758,8.662,2.3952,-20.889,5.8704,11.325,6.291,29.364,6.5569,37.9176,35.985,34.9965,81.744,-2.1756,5.4432,149.148,1.3944,64.674,-3.4272,-20.7,-13.816,62.7822,41.5773,2.598,5.6956,9.9468,-31.8612,-10.1736,22.3776,2.7956,53.8608,-142.071,9.3312,4.3524,1.2948,-2.0108,-3.168,15.9516,1.764,11.691,12.5832,4.0192,5.397,6.0168,-110.0232,-3.7872,83.733,33.93,10.3936,-75.5958,-164.9538,-44.019,2.1,-3.6003,2.7384,34.7865,-71.2962,5.2026,-1.7772,36.4044,2.0048,320.3172,1.0166,31.4712,3.344,19.9665,7.4694,2.352,21.5397,15.2544,15.49,11.6263,1.7138,-3.272,-5.2932,14.144,22.2,28.0192,30.8966,1159.9855,21.9945,59.0352,8.073,3.7408,88.0299,7.264,1.57,3.6288,42.392,1.9136,9.1938,26.824,3.504,14.418,107.082,-27.792,9.92,13.1572,3.44,-20.4352,-131.7168,-123.998,5.8604,2.3868,2.691,-19.5624,4.4088,2.9592,2.3409,46.8,303.3408,26.901,8.3028,10.8864,48.7011,0.4172,-44.1462,4.36,29.769,-7.612,-9.8208,2.1684,240.5648,25.7488,-5.176,4.4772,5.5216,0.0,8.4966,13.3056,19.7988,18.8993,-21.6144,-2.1648,6.8714,9.54,2.4675,-4.7685,-10.1736,17.324,8.7906,26.07,3.3544,6.206,23.7168,179.7488,70.441,0.0,15.0864,12.3256,14.92,-2.245,5.0128,-32.508,272.792,85.2475,30.996,-3.2406,27.1666,-12.4146,54.8604,-5.8869,179.73,22.2384,12.9024,74.8142,7.2177,172.3384,-19.9184,30.432,86.25,3.6288,2.4402,-4.196,148.4946,1119.9968,16.302,-24.4764,20.155,91.968,3.3312,9.2928,6.24,152.118,23.7564,-84.8232,6.534,0.1692,5.2026,-88.784,3.6288,-7.1991,11.3148,11.98,0.0,5.842,13.8528,17.3754,21.7728,116.2425,9.3312,4.4344,-33.3582,-1.6752,700.98,69.1776,6.1548,97.3026,150.984,50.1876,15.372,78.672,-24.392,84.0512,41.88,19.435,7.384,25.06,7.896,14.547,0.3336,-8.6457,274.386,11.375,3.969,35.2772,11.198,21.7728,18.6624,9.294,21.33,7.996,301.968,-11.9616,-2.6256,11.7488,13.9328,-15.08,-1.9008,11.8871,653.301,29.808,386.835,1.4456,69.999,26.8752,12.744,50.098,109.422,-38.2158,6.7048,3.6288,-12.8256,2.3244,88.053,13.8828,18.7224,3.9312,-12.9568,-1.7772,35.6636,1.2038,-2.8308,-356.728,-4.6752,9.396,7.0218,5.1294,20.7808,-120.513,364.4595,11.1944,15.7248,93.6988,2.79,7.0044,6.8724,-23.364,15.9588,2.646,75.5748,30.7872,5.6016,34.974,6.2208,28.1718,129.348,226.7946,0.0,5.1015,207.147,10.584,48.5392,161.19,28.7196,3.7744,46.953,3.4974,15.552,1.5548,2.3177,13.7646,19.9665,-27.828,173.235,15.552,-217.048,9.936,7.9704,-9.0944,33.8517,-2.1504,132.5898,17.5448,6.8714,71.991,-13.6488,41.823,6.2208,83.646,43.1991,-2.667,18.396,18.3456,13.878,-160.96,113.6394,56.2032,6.8714,19.7316,6.7536,-4.5396,63.4368,8.0352,-119.2312,5.6376,3.9424,51.759,8.381,8.694,94.4925,11.7488,334.551,2.0416,4.1031,35.245,9.6657,2.308,-26.624,-118.0116,2.5056,80.843,54.215,21.7845,4.536,-1.8295,3.3,54.8604,153.0819,2.8536,6.9888,16.362,7.098,0.84,54.3528,52.14,-213.5574,3.7412,0.4074,107.7216,14.098,-13.3176,10.8,15.552,2.14,90.72,26.9024,-3.855,8.0464,33.5772,23.6529,26.3912,6.104,5.4432,4.95,22.4448,0.552,3.6288,1.3416,6.4206,18.6624,-8.0784,5.6628,-21.7932,9.7164,15.2064,-44.196,-1.3376,12.796,60.4968,12.1401,25.2936,10.3071,97.0137,8.6715,38.988,56.1752,68.9631,9.3906,1.4652,16.7034,-19.602,72.432,-9.56,503.64,50.328,123.4548,-27.9312,-18.0882,-50.8704,-26.1696,-6.089,17.0268,12.8316,8.95,11.586,180.7659,39.4255,9.7972,9.0171,3.7694,3.5742,84.51,6.4206,5.616,1.043,6.615,0.4641,44.4704,-7.7094,12.599,12.1758,27.882,2.2724,20.7332,2.8101,3.7412,11.7488,121.1056,35.9976,19.188,9.7119,291.3778,-0.6265,6.532,33.777,14.0438,0.9048,6.168,28.0032,449.985,6.2208,14.5152,19.5184,3.157,0.0,197.9208,0.0792,38.725,6.2208,225.735,20.6612,0.5584,19.9665,8.636,8.997,8.636,0.8225,73.321,-12.9987,3.276,24.47,944.9865,-4.7625,6.2208,5.1282,12.8744,-14.4784,-27.1296,7.6986,-7.85,-3.5996,6.03,4.995,6.2208,51.4975,9.4486,107.955,-6.1152,74.574,-1.2558,-13.312,3.5712,14.8752,72.5344,-35.8848,17.352,-33.804,-319.1916,1.4672,7.182,52.493,3.363,17.108,21.7176,2.8836,5.133,38.0864,50.0346,10.164,12.4173,15.525,13.3245,3.2004,6.8943,10.465,1.0178,7.25,79.692,34.294,23.028,12.432,11.086,4.794,-3.8208,6.255,28.8576,18.2352,0.73,3.1654,-115.3544,-28.7964,3.7224,5.58,-4.6764,89.964,4.8588,13.788,3.894,4.1652,4.4712,17.38,25.4016,26.6304,10.89,3.7436,10.0878,47.7306,280.59,45.5392,41.2237,3.3099,0.0,-33.804,-1.4352,6.7048,3.4995,1.2672,10.6794,4.225,40.8006,39.4268,24.857,4.042,120.5106,0.8792,132.5898,4.498,35.6776,76.0878,126.225,43.176,197.353,0.0,-1.294,8.7052,1.512,4.168,1.3992,-8.1312,2.0358,0.364,36.2835,3.3488,24.8832,135.219,2.592,3.024,9.3228,10.5504,15.552,24.998,10.512,6.5164,11.5136,-8.316,2.6412,-111.4995,15.393,-18.8364,0.3336,1.8144,1.0008,31.0156,21.228,27.608,48.4575,83.314,96.8544,0.3156,32.095,5.6956,9.6914,191.9968,10.74,27.4365,4.8024,11.151,22.869,7.0659,40.3704,81.8432,18.1176,388.8128,0.711,-378.4,-9.88,-78.078,53.8608,9.198,-913.176,8.694,-1.476,26.4285,-20.0904,-16.9568,-13.896,178.91,3.1212,51.8312,30.0234,165.3496,33.3172,72.358,-32.3673,3.1382,90.9762,6.6312,13.788,4.704,33.3576,15.3522,38.3238,23.4192,30.2384,46.116,4.8118,-6.567,10.518,3.9771,7.0713,1.8998,59.115,18.4772,15.7194,33.3136,86.3856,3.6296,136.6176,0.2334,4.752,17.5344,5.334,12.8256,4.4784,64.0728,-3.0366,-7.92,9.63,19.2556,15.552,35.6776,52.4979,3.1104,286.3836,2.7984,-66.2302,-255.5875,-8.098,51.8,10.7136,3.21,4.1748,24.196,15.1158,-153.2024,-34.758,4.6818,-8.2368,5.4432,35.6238,-49.4376,7.6146,48.993,-56.3108,22.5296,43.6842,3.0498,10.35,18.0096,12.2328,7.1976,1.512,-13.8468,70.5544,5.1042,15.552,12.096,5.6956,99.4896,-3.8208,-3.4122,-2.1376,11.5971,30.392,55.008,9.1785,89.9548,3.9906,91.7892,3.3408,-339.705,-7.996,180.441,-20.691,21.384,3.506,11.704,63.686,4.752,6.2208,-2.6544,8.5164,45.3222,9.3312,-6.8992,9.8328,1.6704,-18.4464,7.9218,281.016,8.733,-172.7328,-10.1736,-33.32,62.82,4.1916,0.891,11.206,17.6673,63.873,16.9932,-39.9528,0.1588,11.592,3.1104,8.25,87.4825,13.1956,1.6416,41.0388,14.8707,45.84,-29.2776,100.196,43.9956,69.705,4.9104,11.2404,5.6644,2.5056,163.1898,58.7916,98.5248,3.7996,1.1466,6.2064,-10.948,1.062,27.972,1.6762,3.3408,60.2553,28.7856,13.92,20.967,5.256,36.693,-52.8908,-12.288,5.6115,8.1432,-21.681,-16.5396,-81.94,-3.0396,-56.448,-10.7973,8.0997,22.6184,-2.7888,-2.3814,5.5,3.389,33.831,-258.5016,-67.8762,15.9936,42.495,-27.6936,2.3968,5.4236,10.94,9.906,2.99,71.162,-4.7976,61.3824,30.4416,1415.4296,14.4648,1.0668,11.5432,11.086,2.3086,5.751,2.2828,12.672,3.285,206.316,23.0864,3.4048,303.804,-149.6307,-2.6997,2.5592,9.8685,30.9918,-13.3424,31.2444,0.9468,12.0978,-12.628,9.995,5.2332,-8.3524,68.198,19.6248,33.9065,34.8138,-17.5651,28.4364,0.6516,3.8822,-75.8448,-19.47,449.991,22.1536,0.0,-14.9736,11.223,5.8696,-90.2484,27.4856,4.2804,31.0446,-46.797,-760.98,14.17,41.0216,114.96,24.9366,1.0269,7.0173,160.623,7.7832,67.188,5.1968,2.5344,20.4525,6.5888,4.1148,944.9865,8.7168,54.6912,8.3328,16.614,8.7372,-7.46,-166.3935,29.1528,11.6496,20.5755,9.072,5.3352,80.736,3.7584,3.3524,42.0256,10.35,46.1184,-24.843,3.666,23.3928,3.942,-6.4944,-11.6622,-1.2178,1.7876,26.985,12.208,-63.1092,6.799,3.21,29.0,7.6284,-17.523,10.584,-7.3255,92.2368,-19.3382,11.7782,314.0586,0.5904,4.266,-63.3765,11.151,22.5852,0.8088,15.196,37.0782,29.985,-2.4564,90.294,3.5952,23.4552,8.3524,14.2002,-300.735,-7.7748,62.244,65.435,-12.7785,23.4976,11.5584,14.6642,0.7198,21.7355,6.1572,-32.784,6.9372,13.9152,3.72,15.408,-317.1528,18.684,5.484,-12.0064,58.464,8.922,89.9548,13.8684,40.1702,3.0774,8.445,53.997,4.455,3.4686,-34.392,2.99,62.93,0.91,7.2576,-157.9383,2.64,6.6588,5.4341,33.6042,2.1,3.752,-17.9424,636.0003,12.9584,751.9624,3.5767,-3.2436,3.5948,7.764,5.2029,0.679,5.2164,307.1448,4.8162,1.656,1.7136,31.5192,2.0358,9.1845,5.196,14.5728,52.5114,8.6436,0.4074,0.2997,100.7316,136.08,41.986,5.07,8.4528,387.5676,7.056,12.4416,131.355,252.588,6.6352,13.452,294.5488,15.8158,259.5297,1.8704,10.058,6.3504,-12.8784,4.5448,30.445,131.355,190.08,6.633,78.435,9.9652,8.2782,7.9188,5.9136,33.9388,61.3824,12.358,-62.7725,6.2244,3.1104,23.9984,1.6056,-7.098,84.2352,6.0168,117.0104,-99.6219,0.3674,180.7659,50.098,1.731,-167.3184,1.05,26.1096,140.396,8.0997,4.1832,3.1248,3.8448,-3.462,0.1512,107.4785,12.72,1.872,17.38,73.5448,244.2496,23.7744,7.668,481.869,-50.098,41.013,30.2634,1.068,15.808,-11.0691,37.9848,129.7725,40.97,3.1752,88.3948,16.7132,27.4344,37.2186,7.584,-6.0048,5.369,4.5873,5.796,19.99,6.3744,0.8856,8.554,16.146,5.5944,1.9176,3.6848,8.694,34.2925,81.1734,0.307,7.7,-26.6352,4.4604,-20.7846,3.6936,-9.7608,4.0338,23.384,2.9348,2.9372,20.85,21.7515,-95.823,-729.9138,56.324,-13.3176,143.303,7.504,3.1104,60.392,2.2908,14.8,1.6704,161.9919,4.4736,5.123,22.518,-4.8448,-204.4458,1.0336,6.9552,17.16,5.1792,174.9825,-3.5154,-82.884,17.891,50.49,84.294,13.455,3.348,-96.1146,14.651,13.8915,3.6018,6.2208,-75.5958,13.452,4.4955,21.0,-24.9984,-136.4895,19.998,-251.1864,-11.5872,66.3264,4.5837,-225.0976,125.198,-2.0349,8.7906,30.98,1.1808,15.2208,9.534,5.1792,30.2112,71.3898,10.6288,9.1056,7.776,75.18,-3.2406,-26.196,9.5688,-115.7058,10.881,-4.49,18.873,12.178,20.8719,5.0336,-40.1808,4.872,16.5888,16.8413,8399.976,9.5088,331.191,93.2232,102.9528,5.0856,3.852,45.9754,2.9568,-29.512,19.4194,34.539,-23.9372,13.984,2591.9568,19.755,2.6028,-9.1816,0.8495,-938.28,-14.92,14.425,62.82,5.0688,0.9336,1.7248,8.8608,27.882,-32.32,20.2986,-67.851,-15.5844,0.1584,0.0,-24.9624,5.98,13.5882,-2.9985,-190.8522,-26.2272,-6.3,-4.3792,-2.73,3.465,0.668,23.997,-465.568,4.368,1.1904,-150.414,12.492,23.9688,18.2112,11.454,-11.0005,16.6568,3.0044,9.6192,3.456,1.9698,26.6616,18.4464,20.6976,33.7266,54.8604,10.2592,14.682,5.9598,30.09,1.4364,33.7212,272.9825,544.4175,13.128,116.48,13.0375,28.8576,21.0128,32.936,14.2758,1.375,6.2208,32.6046,251.8911,14.4354,9.8784,55.936,-37.9152,21.294,220.4853,751.7601,12.098,6.583,148.5106,-34.641,35.196,6.03,0.7152,4.8392,-14.5764,18.33,1.4602,15.9425,7.89,51.8346,29.3412,3.4092,29.4372,17.5812,5.5888,-9.282,12.1068,271.4192,11.2308,1644.2913,5.6994,10.44,3.564,-47.0304,-231.4116,1.5444,-21.0848,9.6832,0.1472,6.9795,9.816,3.2064,11.1776,30.582,10.048,2.2518,17.8152,-12.117,8.184,178.318,162.0,21.0,85.9957,5.4432,21.5988,17.9982,78.396,80.7772,25.176,75.6548,7.8225,11.8584,12.6077,19.296,3.2832,1.3392,41.262,75.68,5.2164,6.5688,38.024,-29.94,-14.0928,0.0,25.48,13.7862,-26.733,10.8248,26.0568,15.552,22.6782,27.3168,17.3376,0.4074,3.0342,3.8168,32.16,32.186,3.504,1.1946,10.0632,11.2224,-14.081,6.1488,81.1734,282.2092,3.4692,9.9882,70.196,6.104,118.3413,6.9795,17.8794,41.2237,-29.9178,29.0325,429.5772,-3.465,14.4,-251.9874,3.0212,9.3312,-13.433,56.9772,15.7992,22.788,5.0358,160.1586,2.625,9.158,2.0748,9.6,2.3814,3.3524,13.3476,150.984,14.2956,-5.688,55.912,18.6624,16.4647,1.305,-34.758,-292.1,3.9592,-4.1762,-84.2928,35.6796,2.7956,5.3116,228.0792,5.2626,-97.5528,16.7832,-14.4078,77.22,8.2056,52.7692,77.4837,-6.237,16.2688,-225.0976,45.1395,-20.1408,24.84,4.44,50.352,9.828,12.96,-15.992,9.9652,71.2296,18.8937,75.68,-160.2952,19.968,26.2416,-28.5978,-9.1602,5.7798,22.9068,12.6392,31.0688,163.1898,6.8714,6.321,100.7916,0.2992,11.7,6.2208,5.841,8.7672,-17.784,20.1544,3.2944,22.4955,19.6305,89.9548,9.688,71.2692,6.2244,100.196,41.9136,219.582,177.5889,1.6762,42.0714,17.158,24.5028,39.3408,-3.312,3.3408,29.302,-9.7902,10.8864,32.4684,7.5087,29.6576,1.8144,48.9902,3.969,4.461,-29.0745,2.7944,38.976,4.4604,15.552,-2.436,32.5008,28.858,191.6586,-46.592,187.3976,10.465,7.3834,16.8237,62.1544,54.7136,1.365,220.4825,17.19,1.2348,2.2272,10.9096,0.0,74.8142,1.1996,-2.0568,8.1882,50.3658,6.48,7.8792,11.0264,11.4504,14.9925,241.1046,20.84,-6.9216,25.0938,0.0,-8.4294,8.69,8.991,10.5504,129.384,-8.532,25.497,-21.0686,33.0288,5.5566,-12.8392,-4.598,5.4444,-3.3488,1.999,13.0548,6.8724,592.7896,1.5048,11.4452,7.2298,5.8653,78.6828,20.163,6.9664,39.41,9.8901,-4.704,2.376,7.567,-3.9032,9.7152,3.8822,2.8536,3.4686,179.9964,10.5144,3.9144,-21.7176,72.5344,114.9954,25.1916,6.5736,6.149,381.297,13.3476,40.7499,27.1032,-199.5076,13.348,2.808,13.365,6.7176,5.5216,3.3675,55.896,18.3168,95.2,6.1192,33.2156,1.0348,16.8948,6.6312,-18.222,527.984,22.156,15.8756,18.522,20.585,6.006,2.2724,25.186,-17.248,-16.3644,15.9384,2.5984,-2.0264,1.598,-0.7566,6.4206,21.888,13.8267,5.0112,3.6288,4.6644,3.9032,6.2424,4.4685,150.984,2.3077,46.095,4.086,24.4768,-77.333,-2.8272,10.8588,62.916,-1.9272,54.3966,-48.7032,6.6836,13.2293,-10.5798,236.2325,6.8714,11.31,5.1012,2.0394,-24.276,-9.111,15.5904,15.552,6.3504,12.7764,1.6176,13.4512,109.3338,-12.196,19.8254,4.1148,11.1664,46.9952,24.2256,7.4952,0.6786,-9.6348,2.6568,-0.6008,-6.732,12.3284,2.37,3.9512,8.498,1.6008,381.2375,3.0814,7.605,3.352,85.1816,3.1104,11.492,3.668,6.0256,210.594,4.2384,7.745,15.282,217.767,0.8688,190.3728,-2.3748,33.7266,-7.4394,3.4216,49.3164,-22.7435,5.6644,23.235,1.5795,19.8072,62.4,-6599.978,11.9952,8.304,-304.392,17.994,118.3704,1.651,67.608,19.4352,329.4081,4.2408,45.84,19.488,-115.4958,-2.6208,1459.2,-120.0508,16.875,34.7802,2.5592,160.3136,14.9925,-57.7566,10.4076,297.69,6.4128,-24.496,12.4416,9.702,23.7993,19.5,3.9808,100.4255,-114.3534,10.4148,38.376,14.595,15.378,69.92,29.7408,-5.0512,-5.6994,-7.7292,3.4368,315.825,56.301,2.6928,-24.843,6.102,52.9743,-73.7061,-302.72,16.7946,6.3296,2.7144,16.68,35.0973,24.843,-1.2178,35.8644,48.906,40.5168,11.803,694.5015,-47.0583,51.75,-30.8672,1.598,-17.745,86.3928,297.6435,222.588,0.4116,11.2308,6.912,4.3524,11.7208,150.384,22.992,44.9925,5.193,-6.21,134.9322,5.6628,11.4504,26.865,33.8598,26.9304,8.8062,9.264,582.232,19.8254,12.4416,23.8986,-137.976,9.63,54.4448,176.386,7.308,108.1752,-12.098,6.7176,8.0946,104.7528,3.024,5.9184,10.089,-153.3456,84.0512,51.474,659.98,93.7688,-14.5536,102.4998,5.823,0.0,50.328,11.6316,34.386,0.6048,19.8744,3.6588,20.4822,195.9944,74.8098,120.9468,132.5922,5.9988,103.8015,70.1784,13.2288,6.432,3.8844,80.6285,51.5543,2.3406,0.3094,585.552,20.485,153.1152,9.3312,314.8418,77.8232,89.997,4.6816,0.0,26.9985,116.5976,16.1505,15.3426,13.7193,6.4128,89.159,19.4376,27.196,5.2332,31.198,17.8794,-2.484,2.299,3.4398,-195.4788,32.4688,2.4824,31.198,-9.5018,21.7728,123.4737,-147.963,81.0474,9.534,176.8026,3.2872,158.529,-9.153,-29.3238,-2.0622,-11.7612,3.052,0.8162,5.0596,23.3954,56.1752,1.7343,-1.428,99.296,15.6884,1.5426,25.1916,29.5254,162.864,22.5624,22.869,8.5025,8.7138,36.9288,51.8238,12.285,28.1372,3.1104,220.987,55.764,356.225,1.69,7.4571,11.19,2.0088,-147.8655,111.517,13.941,2.1286,25.1916,6.0632,68.12,39.8736,25.245,24.1918,-4.06,-137.529,9.192,6.2566,298.6855,-31.843,24.196,31.6,29.95,30.0768,6.068,22.6782,1.668,-51.7191,4.816,6.715,122.7648,9.9456,3.614,76.7904,8.7048,-14.3313,23.0864,15.8256,184.2204,19.996,19.9155,3.2472,2.2098,41.7852,24.9132,198.46,2.8224,6.7252,10.5252,7.803,35.048,58.6872,-9.1602,4.6305,231.4116,-1.476,9.3312,4.2804,-304.6653,8.7168,80.0199,7.049,3.0576,-7.9002,1.8032,4.4541,4946.37,18.144,4.3836,13.0284,3.8529,-325.572,-6.21,-169.372,28.965,843.1706,-264.215,3.7856,-8.4582,18.6624,62.5056,112.788,24.316,146.7693,117.0104,21.792,6.0288,-7.17,11.1776,5.1792,-204.3145,2.336,6.6976,-30.16,-4.1712,-218.8656,-2.88,-7.656,11.5587,-30.392,1.0208,6.939,7.3788,15.594,8.619,-25.056,4.8416,8.9544,10.9096,202.2528,3.757,19.376,3.108,35.985,-4.0722,2.6892,-0.7566,899.982,-374.9925,11.6795,2.2728,39.6879,2.5578,14.742,18.2112,-14.1372,1.176,83.0502,22.992,30.3604,55.896,14.8365,166.1004,16.032,18.4632,18.6872,53.4519,76.704,207.8856,-20.4468,-47.2542,-120.0508,76.272,49.9704,-7.896,313.2624,21.7728,257.5944,6.5472,173.3292,-386.957,21.42,11.7488,52.3764,629.01,-24.1026,5.3703,171.9914,4.1972,137.54,-5.4882,3.51,2.054,4.9728,30.2384,15.1116,2.5488,15.594,1.6848,7.4172,18.8937,25.5528,33.8517,7.4,0.5,-12.0784,3.6288,1.2006,6.2292,9.8784,60.356,-1.9656,-27.9312,10.422,22.9488,23.9904,7.2696,3.9312,67.4424,4.0687,8.8704,13.0928,-10.386,2.1546,0.0,1.652,25.2784,125.1432,1.0284,1.9926,13.4316,1.638,22.6782,3.5712,-35.2152,53.9217,8.218,1.728,8.5568,199.2606,-26.6352,2.2288,-187.3815,-38.8212,-22.6842,-9.705,-107.958,-21.1596,-27.828,-12.528,3.968,5.8065,-169.637,-13.58,27.9108,18.6624,682.5168,3.1008,15.5204,679.996,0.6102,31.9319,3.5505,44.5962,-1.9656,80.3682,-228.7425,15.8256,19.2384,4.89,-1141.47,15.552,54.5844,53.235,83.281,0.1008,1.356,14.7546,-14.7931,69.705,6.6468,8.532,0.693,17.524,70.312,12.7008,6.999,-4.577,-1.8392,5.2528,2.5452,7.3386,5.5566,3.8682,6.206,-52.4544,14.3952,13.3008,312.676,5.842,-6.6278,-14.9877,2504.2216,72.6408,8.0968,25.2315,-63.3765,-93.08,6.3936,7.0512,0.9588,37.5624,5.7716,152.0232,2.1,1.0208,10.0485,130.4913,7.986,4.176,2.3094,42.0744,9.7176,111.591,49.497,30.4682,152.0883,7.056,-28.6272,33.6474,9.4284,90.6444,18.6956,6.552,86.3856,1379.977,0.8856,56.301,5.382,13.8915,4.914,-3.6212,8.6352,3.1104,11.998,12.4416,21.098,6.888,0.1134,6.7236,8.2764,89.9548,764.3818,1.816,5.6832,24.4608,3.4368,4.1769,-26.9955,1.752,-8.997,35.8644,26.3967,137.151,12.8316,157.4685,2.4012,2.2282,3.5048,-20.6176,4.6221,40.3704,0.4768,6.2208,45.528,2.1684,3.4695,16.175,10.881,60.4768,5.733,9.14,14.5236,51.75,-13.5882,6.465,-68.1096,-47.175,2.3814,250.396,2.772,3.1536,12.6348,38.9974,6.9732,10.062,16.38,29.364,38.9312,-11.994,29.3284,40.3536,-26.085,-4.1832,35.694,23.7742,146.79,-2.588,1.8144,8.4942,0.712,41.76,459.396,-426.986,65.9634,13.455,30.098,79.1934,15.606,15.998,17.745,-417.0936,6.5472,-32.48,-2.6892,16.7986,11.3288,-3.6892,7.7679,7.7343,108.3528,9.936,343.9828,1.7901,38.9752,2.7846,8.7906,6.5052,21.506,7.3451,18.2112,3.504,81.1314,6.1992,-8.5794,-8.1822,-3.6537,39.948,-106.393,8.4564,-269.3376,-87.6672,-12.849,10.9193,-17.0274,8.2896,-11.5188,-4.7625,5.7624,52.632,10.4985,47.0979,4.8118,12.0609,3.4668,0.2244,361.2994,-6.396,1.9024,7.3359,18.8972,16.3172,-185.7168,4.7988,25.0182,3.0654,3.4086,3.857,-2.994,0.336,16.848,25.186,-3.7996,38.725,214.4675,-3.0396,5.798,-22.1382,99.9012,11.3288,109.7208,89.2224,66.7152,22.1184,15.6332,13.32,19.3932,4.7232,3.501,-1.3952,-20.1663,27.2412,-12.352,-0.9452,101.6508,33.3396,33.64,15.4752,52.7934,14.7582,42.9914,9.744,19.656,-14.9877,-17.0352,440.7648,47.0548,-77.625,32.4684,7.015,0.8624,0.654,2.7028,78.672,125.9874,57.5016,19.6328,11.7782,9.1581,62.7004,2.528,112.4928,5.4288,4.7616,1.7248,12.1348,16.5531,8.1192,5.6448,140.5957,16.945,23.2182,42.1314,4.908,9.072,0.8736,9.936,64.2,168.4384,9.6375,59.998,69.993,0.5022,0.5904,-10.0372,11.5164,3.6588,21.2724,-8.379,-173.3472,-10.7964,-181.265,24.9132,421.0824,-8.6058,3.246,-46.4292,11.7568,9.7176,18.5886,32.1678,335.9944,88.1295,-2.5648,5.6376,12.4752,15.44,2.5974,25.424,-7.3015,1.86,138.3552,74.975,-299.8116,150.984,2.1888,8.9994,81.921,120.9416,21.7728,49.2576,4.9616,80.6312,6.888,54.8613,1.8604,-81.664,-3.462,22.9008,7.6896,-7.396,3.389,43.9956,49.4982,3.1104,27.9344,12.0978,13.604,9.0,-22.0416,1.6704,5.8914,22.458,3.4357,3.0861,18.2592,3.21,31.122,6.5538,3.753,9.312,-320.2395,26.3494,-41.262,47.0351,21.252,-7.392,4.5201,9.2799,5.1184,8.7145,13.2986,106.7808,2.4138,6.6906,-131.5008,10.9494,85.9828,12.6813,19.1376,38.08,27.882,63.8232,102.774,1.3677,133.152,8.048,210.4936,2.8836,523.7052,2.8322,6.4206,0.3906,10.3194,2.8782,3.9498,7.1864,11.297,11.556,4.872,76.2624,6719.9808,-32.3388,9.6192,17.379,0.9576,106.5216,60.392,22.0947,136.2971,11.7,2.3094,15.8376,2.9835,4.4856,62.748,2.14,45.7704,6.93,40.5867,47.0376,427.4368,14.5584,59.998,5.949,20.7675,1.316,23.235,23.1192,-28.9764,-226.6368,2.4174,1.7995,569.9905,33.5888,9.9882,53.2608,21.0128,1.5008,8.88,3.7996,5.97,58.42,8.1144,-30.098,-8.5794,6.9986,-66.3916,55.647,10.0624,6.8992,7.9548,-48.1194,12.8256,53.272,6.3504,9.6192,21.164,-4.7625,16.7328,149.8956,18.5391,39.564,2.0672,176.1708,-36.2352,36.0192,8.0406,22.087,30.7776,25.62,8.019,-90.774,17.27,1439.976,188.1404,-22.8956,19.3185,85.176,359.9988,13.348,2.0358,2.7166,-19.1058,-5.6943,38.025,21.7515,1.8207,23.55,6.8724,70.006,129.6,2.8912,6.5286,2.205,7.6416,47.98,11.1294,7.2111,33.3256,2.0416,8.49,49.9704,-5.94,0.0,1.2192,19.1786,-7.7247,-248.2458,-102.048,-3.552,10.4875,621.9744,114.9385,15.7584,79.794,1264.7559,71.2296,97.88,9.7119,4.914,219.9904,4.8118,4.2336,-13.363,88.074,0.0,91.968,-29.0536,6.2208,23.7742,20.3439,3.6288,71.5375,41.9958,21.9492,6.4176,3.5767,3.58,-3.0933,1.848,-17.046,0.1533,14.2324,1.4672,21.9945,-4.746,2.3616,17.982,13.365,2.376,-38.2116,302.373,1.683,20.1015,4.2048,-32.2192,21.3408,2.5536,3.5022,9.0882,5.0286,2.0049,-11.937,70.722,36.4044,5.4432,7.2576,2.065,-44.2782,-7.7292,-6.049,2.0592,1.5588,9.5448,12.222,-10.054,-4.7784,7.2576,-9.223,-3399.98,-43.9056,46.7313,-19.1058,-6.5736,3.597,11.2896,3.4686,5.2773,13.5072,-15.8356,3.546,-6.38,5.7753,-18.1176,-24.4764,-21.2136,-6.188,18.28,10.3936,-52.17,33.2704,9.5418,70.4928,-4.7145,-243.16,34.146,227.205,8.3958,7.2576,3.462,-4.9878,6.2152,87.7578,0.0,3.3534,7.008,30.186,36.813,26.544,7.9662,35.3626,1.8704,55.9224,15.372,-14.5176,11.9196,1.05,-11.6928,-7.84,-0.99,4.8986,0.6516,12.41,-18.2525,34.5,-21.294,-5.7638,-18.196,28.4102,4.5188,8.763,5.256,0.6672,27.504,22.6737,6.792,9.3564,19.2472,-1.4413,5.6994,12.298,33.4584,39.0824,11.592,-42.1096,0.7336,0.7704,5.265,84.5982,-69.89,2.4059,3.8844,-3.5508,4.8525,1.6704,-9.264,-69.3952,4.0098,2.8224,80.3404,3.6288,-158.102,-8.2764,28.332,21.4368,14.9744,0.7425,6.216,7.553,1.4976,18.093,0.416,-458.1468,0.0,-15.7176,12.993,7.065,15.824,59.0372,15.4752,2.8,7.3008,6.6584,19.4656,12.4416,-44.94,-112.041,-17.592,45.8064,-1.9275,11.2839,-7.5168,8.4528,15.552,165.7176,4.5657,20.6955,72.948,-1.5414,4.0995,-152.9847,-7.3232,11.58,3.2064,15.525,7.434,-18.802,-119.1918,-57.951,29.6,76.6395,41.2938,28.7952,18.0378,-52.5481,70.5564,39.689,0.6408,27.4352,423.0085,18.4604,7.4592,119.2,52.493,28.7964,-23.7822,22.7024,1049.985,14.5152,-2.0568,25.875,22.0158,87.9912,26.07,63.107,46.225,2.6784,12.7368,17.6673,-6.9965,2.14,-14.8832,16.848,0.5904,-356.9643,9.4366,4.42,15.426,1.9926,2.9568,42.048,1.1556,4.7724,34.96,6.4692,-10.7055,2.0979,-53.072,-15.99,27.4856,-124.431,2.3364,411.7365,7.3206,149.76,158.7519,95.4612,81.432,-12.849,7.745,134.9925,-46.536,23.8581,206.8893,1.764,6.2152,1.932,5.775,1.0904,16.1838,0.6993,6.615,9.3,26.9024,18.8937,23.5764,37.0,601.9699,5.8708,17.1828,4.2624,19.1376,3.475,24.858,2.5893,-3.168,5.6376,-55.256,-0.9933,-3.2934,15.6744,-10.1736,54.6912,197.9208,2.299,15.6375,-0.9012,75.735,4.4824,38.7792,0.6696,-10.6547,6.2608,1.0287,20.7312,-35.3646,140.5957,13.7808,49.92,9.5992,91.9508,113.9886,28.1764,374.6286,10.1094,109.7226,10.896,1.395,1.0208,98.2722,12.8184,42.588,89.3142,4.068,4.2952,19.8144,8.2944,38.61,70.1955,18.821,3.3504,35.6238,7.095,3.0044,162.0948,3.4827,-97.176,72.807,5.2113,-54.5958,-2.6268,2.5137,18.8328,0.7228,25.3302,2.8536,-1.9602,-6.4233,-46.716,0.6156,-11.5938,-11.2806,6.0288,13.428,207.475,13.2,1.4805,0.7728,62.532,6.924,6.2208,9.816,-10.05,9.072,134.9925,0.3399,28.0032,28.629,22.6782,138.417,7.86,14.7,33.2156,5.0286,101.4504,-29.0073,-6.237,-64.9376,36.2877,54.3936,9.8856,4.0776,5.4432,19.596,9.396,-52.3392,4.6746,3.99,19.9686,120.9416,2.6208,1.1775,17.6391,-3.094,10.179,1.8672,33.8744,-0.3398,18.0096,-6.0196,3.0438,15.9543,-77.1267,1.311,-34.3148,25.872,8.69,-2.6586,539.2464,793.716,14.7593,10.0572,3.7408,-0.6435,2.401,9.1872,15.921,7.92,-2.5749,-115.4304,-4.14,36.1836,1.8354,0.585,0.0,22.2264,50.396,-3.4914,5.4432,8.5025,5.4504,362.835,1.2714,9.6712,5.382,1.999,5.616,54.04,25.1944,4.3884,-17.4432,-9.555,2.5056,7.2576,52.9173,0.0,2.178,28.6182,-3.504,-48.392,-8.3524,12.3123,-18.8728,-4.466,2.079,28.7064,140.9568,5.0764,54.057,23.0864,-14.3856,11.36,-71.8905,14.8,-30.245,5.4332,15.012,0.7065,3.895,84.22,17.4975,7.7679,4.756,4.116,4.2,54.3332,7.7004,41.8608,130.2075,6.6294,18.2112,16.5888,60.2553,35.099,-3.81,-48.5082,1.0296,1.984,6.603,1.0904,4.2666,143.04,9.3296,1.068,41.952,8.997,9.3312,19.176,67.941,-6.8634,16.6764,50.9208,-25.4744,5.998,-39.1248,-87.3418,7.4975,8.7906,22.2,-3.8864,4.7976,29.692,17.847,22.8285,9.3504,26.9973,1.7466,6.7032,223.9936,1.7115,52.3764,-28.224,107.9892,8.7138,90.972,17.1574,90.588,51.8346,4.7304,-8.904,1.794,92.2368,4.3368,9.3312,50.5848,-16.38,4.4312,46.575,-32.9292,-3.5712,4.0687,8.1072,1668.205,17.9592,75.5937,19.0512,23.235,-32.6366,1.5291,0.8388,-84.9615,7.272,47.5072,-1.11,-43.4352,-11.0208,11.5432,21.1344,3.7596,10.312,45.9754,6.465,-5.2072,0.5904,18.6006,10.8864,4.8118,125.99,14.995,71.991,0.3348,15.552,3.0576,219.4416,2.464,-34.38,40.376,12.6927,-5.0094,146.388,0.6696,-23.8855,-7.5768,1.3536,11.8206,111.824,48.3771,3.21,6.795,-320.2395,32.6332,49.8042,25.8984,26.64,16.704,-5.0098,0.7348,148.138,-2.1195,0.0,8.236,37.1084,4.6818,-13.6776,41.79,72.7888,64.7892,2.043,214.164,135.98,31.587,5.4128,31.5192,67.1916,1.6752,9.2322,244.6155,9.3312,31.941,40.416,5.77,185.2578,7.9794,39.213,3.0368,310.9872,8.5544,22.4316,1.8144,-54.5496,-39.5118,-96.4704,101.5794,302.373,90.735,9.7812,125.198,67.1139,-10.3124,-295.9785,282.2092,100.4255,5.368,25.5798,5.1294,-178.8468,12.4416,78.1954,13.3176,-8.1096,59.4355,11.1024,92.4399,26.598,-2.7,11.223,-103.9882,26.3912,209.58,742.632,54.3438,49.761,1.5522,2.6973,62.988,5.5177,77.7519,93.204,11.5432,114.6285,0.8792,-17.6607,-348.6294,-10.4214,22.3888,5.6376,11.2752,-13.7403,5.8203,23.924,-2.2586,-113.998,1.0044,0.1188,6.3336,5.4432,85.787,93.24,-45.3492,4.8231,8.673,5.8744,58.179,30.2316,4.9104,24.2696,62.737,9.1954,4.3296,99.23,385.3752,7.8192,10.5,4.1472,11.5432,3.0996,35.3346,6.2016,45.487,48.8064,31.587,-146.16,-0.792,14.3075,3.9128,74.8142,134.652,2.9835,10.8966,7.9128,26.1156,11.8248,9.3125,17.238,43.706,4.0749,244.6155,5.3964,1.1925,-7.2589,6.2376,19.3392,93.6988,3.3524,17.9592,2.3312,2.132,52.9173,19.7358,20.8568,7.9128,1.4456,49.8042,-377.9892,4.653,148.845,8.799,3.6018,6.2208,50.3832,88.5528,1.9024,157.1292,-48.7839,13.0095,4.3904,0.91,-1.0196,15.147,0.0,14.4596,210.735,2.1736,67.495,15.552,89.997,47.952,28.95,69.9965,10.098,-448.896,-14.196,1.148,5.2312,-6.1248,-42.8967,112.4064,6.4128,25.4744,31.2664,20.21,27.441,8.714,6.8714,-5.7148,132.5898,331.191,30.415,4.5448,-22.62,25.011,-52.641,-3.3792,-21.3264,3.1752,6.2937,1.6896,17.6232,5.7072,69.6762,11.586,-4.5824,3.872,7.5371,7.6798,-164.836,121.9644,7.1712,29.5626,67.99,22.5296,-75.192,14.0859,5.4896,15.192,143.982,11.1825,19.872,4.2666,27.9936,5.5071,20.5764,4.35,839.986,-4.2588,3.0144,7.2576,-34.647,9.5081,1.0738,-25.992,4.2471,659.98,45.294,12.052,12.178,10.5072,4.0203,135.98,32.893,-2.2758,6.2208,4.1944,3.6192,100.24,1.375,72.6408,133.9713,6.534,11.7741,15.599,0.4706,25.5112,22.2444,16.4052,60.5528,0.3822,-53.7432,43.176,12.6,85.904,-57.1152,11.4576,17.8152,4.1391,5.3949,15.2712,5.5392,8.2848,8.4096,54.558,390.977,-263.9967,5.999,16.9975,18.5274,12.7008,50.3658,5.369,23.9688,7.4655,-36.6744,24.84,11.1564,4.1756,-5.6406,2.8884,3.1842,60.4224,29.5186,66.6,6.3296,7.5528,21.036,11.8272,40.3536,23.3184,7.392,68.364,247.485,44.2425,26.2,-25.109,21.9978,19.8276,-13.4379,5.4896,25.898,4.644,7.8064,11.673,4.1832,114.9385,15.525,17.9955,11.5432,412.468,378.1674,83.284,25.473,35.04,219.6546,10.0116,12.4416,13.4386,-22.512,2.87,12.2465,7.2576,19.7712,59.373,373.779,5.256,11.685,37.764,92.2368,89.997,27.2952,152.0232,5.9211,0.4752,9.12,-1237.8462,8.4888,22.6233,30.6054,15.4752,4.797,9.2568,47.6604,11.7078,0.0,4.3368,2.8224,5.2287,-337.806,23.184,25.4384,-0.8392,-11.19,48.3771,8.997,3.852,4.872,654.7554,9.816,-630.882,140.5482,-2.1312,11.68,1.002,-99.1032,-22.2388,-1.041,97.6524,77.3696,302.373,3.0814,1.239,15.7872,290.0058,22.4196,-11.4648,942.8157,-7.9068,33.57,371.316,-33.139,27.2862,12.504,10.9939,224.424,61.389,7.6494,37.236,182.3553,9.3312,-3.9032,63.4368,77.714,10.788,5.166,12.4416,3.596,10.4754,38.8704,34.3548,16.8,10.7996,7.4872,11.613,4.9648,7.11,225.264,28.4364,37.7972,31.2528,54.9504,11.2308,1453.1238,24.84,10.3936,2.085,8.5544,133.152,29.358,20.7459,42.4647,2.6251,-83.8752,327.5922,0.4176,2.943,15.49,12.1032,1.3104,3.7584,7.71,64.6272,-89.0664,1.07,1.7024,67.256,1.9272,13.9672,15.1158,-43.848,11.565,294.5488,99.23,0.896,1.8144,96.576,329.994,8.236,0.9774,3.96,23.028,33.1584,56.9772,100.9113,0.372,209.979,16.5984,17.745,-297.6848,11.4296,32.396,7.92,250.305,1.4456,5.8887,26.564,9.352,41.4456,17.76,2.401,-5.184,0.7056,7.1196,43.4217,217.767,2.7222,2.1684,0.8058,9.6975,83.2097,166.0698,77.5584,0.6984,8.022,2.9562,45.3696,134.5302,39.066,6.7966,103.818,40.3128,-7.119,38.08,3.9474,3.462,-2.6997,2.214,7.704,829.3754,4.1448,-15.0876,5.6,2.726,73.41,37.5624,-44.235,-93.3262,6.468,8.9208,3.7642,37.0,12.599,6.552,2.834,4.1148,46.225,1.7739,11.206,132.99,323.946,81.0474,213.735,757.4112,9.072,57.4113,-2.9566,-105.69,1.6688,14.1246,8.8624,201.312,21.42,-8.0784,28.896,85.491,-68.1856,2.224,14.098,3.339,1.7375,-20.448,4.1328,-3.0576,39.5428,0.6192,65.355,3.744,6.9654,92.392,4.3368,152.495,-58.716,-1.428,0.5432,3.185,3.6288,-0.2098,-117.882,3.772,-99.1764,5.55,0.864,6.074,15.1116,6.2208,105.275,3.798,5.4432,7.196,0.7228,-29.4368,-1.1196,7.2744,-28.2744,46.5432,7.1372,2.397,34.8128,1.6524,5.4432,34.1784,-6.0237,37.884,1.8872,9.8685,133.8624,80.4839,7.774,10.5672,47.46,18.7812,757.4112,8.2992,2.355,26.4654,13.8579,16.9312,20.235,-566.5625,5.397,1.7055,107.9946,-68.1856,-47.3968,33.5892,7.2576,-11.6512,15.498,-39.637,-3.564,12.5762,3.4496,22.8096,28.764,1.7024,51.1872,-2.3276,3.888,11.2752,14.677,0.8382,1.5768,1.9024,-3.6024,64.674,-9.0904,8.2156,-5.215,-48.4704,4.2408,-3.231,2.388,62.1376,23.9688,-15.245,-1.9872,-386.3916,5.9778,-1143.891,7.776,28.7064,8.8008,-56.3108,16.5564,17.1774,7.254,9.0048,6.5808,1.3622,2.245,27.1764,14.6157,6.768,53.433,3.72,11.703,3.29,6.42,10.8682,84.9436,459.9875,11.6496,113.848,50.8768,3.21,-65.853,256.784,6.0382,6.674,6.2208,8.8784,9.3312,9.3312,17.994,34.2144,-17.991,-4.2012,20.37,3.0096,79.8912,22.89,19.95,26.3494,45.528,21.7728,2.786,8.763,23.235,-2.588,3.549,-12.208,3.852,94.2784,-29.1528,-18.0385,8.6855,5.6644,-168.819,-6.549,190.3881,26.082,18.447,323.955,4.7976,20.2485,11.2839,5.2164,6.512,11.5971,10.8136,12.0904,8.3328,18.96,116.3904,203.5644,-20.7846,59.4355,11.5536,102.9444,106.9578,143.6288,0.0,0.0,41.706,32.3351,884.058,0.84,10.7964,105.98,30.5088,6.3684,19.7934,5.5992,7.2576,8.771,4.0572,-2.7552,-412.6154,2.2512,1.5548,3.24,6.42,14.3952,4.2717,-77.333,-10.15,88.485,77.5764,3.5022,3.2214,80.7912,9.534,65.435,37.7874,6.3504,225.6,8.9544,188.2192,7.056,49.9704,3.2406,68.976,5.1042,2.3814,35.89,24.4608,9.3312,6.9088,7.98,10.224,12.4416,3.528,-2.974,0.558,119.4742,114.9385,34.182,26.7904,9.9992,8.1072,31.4895,19.1976,29.495,15.552,6.0632,61.3824,-128.2388,9.5616,-13.938,13.452,-2.5248,4.4792,4.8546,-3.3894,6.5538,20.3898,18.1044,21.792,1.7876,609.7157,18.1764,28.3095,12.712,6.3296,8.0991,350.9082,3.9771,375.735,95.76,24.144,-8.6058,26.3934,9.8784,3.8775,-1.5264,15.1158,27.93,41.1332,14.5638,15.378,318.3016,113.6742,22.9954,6.2208,-18.5262,5.022,13.3056,3.9831,107.7216,-1049.3406,17.524,6.1488,12.231,15.5288,-4.2987,171.36,6.4584,9.816,25.2213,33.5888,-197.5752,7.2576,5.2026,88.074,-8.9964,2.322,8.4888,48.288,0.5998,23.712,-240.784,59.4816,102.186,3.666,6.2208,63.984,97.0784,3.3524,9.0384,275.478,3.7128,3.8775,71.928,109.7544,7.56,131.355,181.176,12.96,4.9608,25.172,85.5297,-253.4337,38.396,75.18,24.4758,2.4585,15.2292,177.198,10.0725,-14.8704,-11.418,2.19,17.8066,3.7128,-6.303,9.936,51.2943,3.8822,47.9385,35.988,0.9282,20.7328,-42.9516,8.8624,10.374,86.8704,1.4456,16.146,0.556,314.2719,5.538,33.0648,-57.6312,2.9568,26.224,-58.8616,-29.4368,1.3596,5.2026,4.4352,-1.8585,-0.3488,3.6288,3.2776,-6.396,0.0,10.9698,16.3352,24.2285,15.525,44.868,3.9102,-54.882,2.5896,25.4384,25.792,2.64,7.4368,5.4432,16.8,-189.321,65.9934,28.217,-15.4666,9.4392,1.0114,6.9741,5.7624,-17.469,80.7912,82.2906,47.994,50.328,9.3312,767.2005,0.0,9.5032,0.5004,27.3672,60.49,21.9975,20.8494,45.0016,0.504,4.1124,17.1574,-1002.7836,4.3956,3.4544,56.7864,-26.2476,1.4112,7.2576,26.703,1.3284,22.792,-38.8212,-16.6012,-384.7164,5.9364,32.3015,10.7037,-21.888,-56.0592,23.0864,42.045,-20.1362,5.928,1.5691,204.7682,66.9546,3.1161,1.12,-6.4233,5.4432,2.322,5.8708,843.1706,21.8192,8.5914,5.1588,13.5626,7.2268,25.5798,2.4598,1351.9896,27.882,13.473,26.973,-59.8356,3.2186,6.854,2.6973,4.108,43.9,68.976,2.9372,66.0736,1.197,18.2112,32.6628,3.1104,1.8688,115.1856,7.668,20.0851,10.3473,-6.36,22.2352,-14.4784,-36.1116,-33.636,5.9175,200.8638,-28.9674,65.3256,26.973,16.6788,3.2392,11.1176,0.4068,11.6091,6.48,115.1808,-32.6646,8.9206,6.156,-42.6528,-430.617,5.8751,9.1776,16.544,-15.7176,3.5152,4.3254,-47.8716,4.6812,27.7158,128.6805,4.95,29.952,8.771,17.4064,129.294,-1.4994,2.6892,36.917,0.4356,1.5876,130.752,-76.9536,-18.186,3.7584,95.2,39.8886,12.4416,8.694,20.5764,1906.485,104.568,5.9712,-145.176,4.0768,346.0396,5.2029,-6.8094,-7.996,253.372,5.9072,-23.548,-42.4638,18.4534,3.6894,15.2988,100.4255,4.2048,6.003,26.376,9.3152,7.2177,6.378,70.219,111.5688,4.4004,-968.8833,175.136,-479.988,57.385,6.2208,4.6193,9.4924,2.7664,-3.3506,13.8684,7.4,4.3008,15.12,-56.7556,10.3904,-3.5224,-1306.5504,8.502,-67.5435,5.2125,9.9468,-91.7586,9.2442,14.7056,1.3986,4.1416,18.7812,70.008,1.8,7.5864,12.0295,4.485,15.9348,-75.8304,6.0412,-0.7748,1.112,2.502,66.5408,374.3792,-6.5619,42.747,-4.461,19.41,-76.9972,9.0912,-62.3792,5.1408,47.848,16.1568,62.9064,10.512,1.3716,-4.9728,2.0088,1.8144,6.745,28.755,0.5299,-120.513,647.892,11.088,-6.54,-28.9568,-2.5344,12.0252,3919.9888,54.7756,23.3163,14.7,1.2005,50.5632,-58.3056,-15.1311,-2.07,10.0464,0.8988,51.4975,0.666,11.88,29.0136,-6.237,-127.5792,107.985,21.2856,-13.7568,5.6644,5.256,-81.3065,4.9815,19.775,-65.1504,113.211,5.5616,6.7966,2.9568,-27.735,60.6645,-13.3341,9.4788,6.549,2.64,2.0388,2.205,34.742,20.5842,7.196,5.544,16.2342,0.5754,-3.9249,10.3071,-3.272,15.5904,5.4432,-29.4368,-2.7,16.1838,23.99,22.5408,-55.3,6.567,510.636,-0.8999,27.735,3.71,14.4,7.2576,3.6632,0.9856,16.704,5.214,4.2392,-2.5128,9.1638,-6.098,-68.1302,4.0644,37.9962,-23.0352,-8.5008,10.518,20.6142,0.5904,3.2214,38.1576,91.056,239.9058,20.0851,7.85,4.224,-186.16,16.7776,0.1674,206.6232,22.6275,5.7624,2.8782,292.776,38.29,10.5084,9.3312,517.4793,-35.5136,-81.7258,2.6068,5.4336,9.12,9.1674,0.6624,1.2585,10.7325,1.4456,20.975,43.706,3.7408,6.8724,26.8744,65.7342,27.1032,0.5097,17.5812,0.9995,11.88,17.3754,14.148,87.89,311.9948,-2.9964,4.1988,-7.782,5.2884,20.9148,10.875,5.6994,36.4776,5.9696,3.852,1.7248,-6.4232,-2.3232,15.5961,-32.3838,-2.97,-13.188,14.651,-12.5286,8.88,-6.188,-192.0468,-3839.9904,3.2616,-43.7292,118.9965,1.419,54.3966,38.532,82.2906,2.0286,171.93,6.2208,6.2208,3.7128,30.499,55.5822,24.2012,-66.6,3.9992,31.188,55.4364,53.2608,-1.8308,-25.648,32.688,19.872,22.2264,28.1718,-3.788,2.8322,43.7136,1.816,-73.0548,-51.8272,3.614,1.7608,12.672,16.1838,2.9682,149.9112,10.8864,-10.6176,366.6348,-19.864,-1.9344,-30.9332,1.017,12.1348,7.4872,12.0276,6.3612,66.6351,43.6752,2.5216,13.7931,-140.1408,19.08,-71.994,7.6272,33.3102,145.134,112.422,32.97,31.198,52.3392,40.5426,3.178,43.9956,38.3952,-2.6997,355.4466,20.7328,157.8702,473.6106,4.4344,314.2719,2.106,43.5981,-427.45,-146.1096,124.9552,10.0772,-35.9928,112.224,-7.68,-63.996,-25.592,-36.2136,9.5526,15.1188,11.8728,8.5728,50.9208,2.8314,12.3144,-32.088,0.0,21.5824,3.393,39.52,14.4495,3.6288,130.2885,6.63,9.3312,-45.84,-15.5904,8.499,4.4312,-47.2542,-0.5598,69.705,2.3025,4.752,5.8203,9.9652,-10.9116,8.381,13.0,50.3988,22.0748,5.6644,-17.7072,-55.256,3.5256,3.0134,-92.6955,8.0997,-5.6784,4.9056,0.693,9.12,9.352,5.373,4.5816,12.208,-27.2646,23.992,-48.9549,3.363,70.5028,9.1296,-935.9595,30.99,4.2336,3.339,-24.7086,-63.0056,10.3473,190.0206,150.294,163.787,1.375,6.1792,0.1548,-7.48,29.0325,-2.7968,9.9296,15.992,-32.985,-27.2922,3.024,28.1372,7.4872,4.504,25.0536,0.0,55.016,-1.7495,215.9973,34.6296,4.4712,23.988,6.0736,5.997,5.193,7.9896,-1.3984,24.1224,23.7864,74.9985,5.397,73.41,10.788,24.3384,0.9772,93.884,-14.4588,76.9816,18.6624,349.3392,5039.9856,83.986,-3.465,4.5188,55.647,6.6177,20.586,12.264,14.2632,28.7964,107.79,48.632,3.4686,36.7255,-0.6624,15.5344,7.2576,14.5152,9.594,2.7354,-16.1856,8.2992,24.9804,2.9568,7.7728,1.4208,54.3332,45.8136,20.844,-19.323,-25.4772,10.5728,-45.9333,6.6584,6.4128,76.2525,2.3976,12.53,10.7604,3.912,-8.7232,-53.2704,-2287.782,213.6888,-46.3998,8.6744,13.932,7.106,626.185,8.7384,-71.8116,-131.445,18.2525,-13.993,0.5004,5.28,-29.3238,8.37,28.13,11.5836,1.5714,327.5922,1.3365,1.7955,2.6964,9.68,170.997,19.3116,-46.137,9.1746,22.4448,16.614,27.3182,-25.2956,-23.5764,3.5178,3.9296,3.1752,2.64,15.2712,1.4456,11.2422,2.2412,14.7668,20.5842,-12.4146,49.4982,24.8832,56.55,103.9992,2.232,2.0994,17.6016,-4.04,-5.9808,3.7408,4.176,-9.156,7.2144,16.6788,29.364,1.0738,0.1744,11.076,12.7008,138.2016,19.596,-31.0335,157.3632,24.318,7.9896,-41.5872,-16.0784,87.1962,3.501,-12.672,9.9936,39.55,78.9412,-1.7772,1.4112,2.8812,7.371,2.5707,-14.998,-7.782,-15.1976,83.2097,6.2208,9.102,375.4296,173.7408,-24.7716,0.0,2.8296,3.7376,168.4704,-29.6058,-24.398,1.3416,-81.441,3.4965,37.495,-179.776,23.9463,15.336,14.6825,3.7236,-53.7088,264.5865,-40.4712,37.884,9.801,32.6704,12.1728,9.8856,545.1884,240.294,40.416,43.1904,67.0644,23.9778,36.2556,56.0547,19.2454,0.7665,4.3584,6.0288,5.7568,59.8176,41.1208,114.9385,72.8088,224.073,2.0271,29.4455,272.792,7.92,35.982,494.9725,5.4432,75.5424,31.0688,7.524,-12.9122,0.738,-619.596,48.796,19.035,0.8288,-653.2834,9.5571,45.2226,81.5949,-10.7973,23.1093,-15.4188,82.992,5.3898,163.818,1.6712,262.39,8.997,43.45,24.7275,6.6465,5.4124,3.6714,5.1792,107.0388,6.132,-28.498,-5.6007,35.6346,6.9258,9.4437,21.7728,-18.1176,31.0992,5.373,35.3295,16.2099,7.4824,18.837,41.1684,5.8744,3.6288,1.7352,30.4776,-4.7481,9.2386,251.202,9.3312,3.6796,2.337,13.846,52.9173,3.5046,1.7262,22.5732,5.3214,-462.8624,-25.198,743.988,-3.7196,168.4704,68.001,5.04,-45.24,-363.528,10.395,2.4582,3.1584,22.2516,-766.012,44.975,43.4646,-33.484,0.1744,2.128,-7.9984,12.8574,-24.416,151.0974,284.1855,4.1965,4.9616,0.0,3.852,80.3208,-14.34,53.8608,8.8624,5.915,10.5534,14.0712,7.1988,4.6552,29.372,-21.1068,3.741,4.5216,3.344,79.8912,1.0008,1.512,88.7332,3.6288,36.9873,7.0128,5.1184,-14.2716,18.1764,1.5588,4.6176,8.671,-10.284,2.6961,-28.7964,143.982,-2.6936,5.7624,-4.455,45.555,-272.58,3.1806,6.846,2.552,29.988,23.235,41.823,10.9096,39.98,4.536,3.0212,60.4632,9.936,29.372,5.2029,18.1908,68.823,-7.0146,5.4288,17.505,8.3754,67.6599,40.7499,16.5888,6.0726,2.8836,25.02,-2929.4845,89.7792,46.797,25.5968,23.4,1.2432,25.5378,5.4432,20.844,28.0876,40.4432,4.6464,305.13,160.0398,32.0598,-112.9527,8.2992,9.3312,0.0,33.9388,8.409,12.6592,11.1176,-18.4548,13.3035,28.8576,434.9913,37.7895,15.468,33.93,41.3928,13.608,-58.5048,27.4302,31.4548,3.6432,-20.997,8.6391,62.321,-9.9705,146.79,0.4264,15.5112,68.04,22.4082,4.995,7.0218,19.5238,2.6496,13.5056,226.9644,48.5514,2.79,12.492,629.991,48.3285,0.6056,15.6978,26.901,2.724,44.4768,-7.4416,-1.9344,21.591,-8.1312,6.2208,7.4824,5.096,41.952,15.387,-5.8248,5.2896,4.908,23.316,257.9871,7.2268,22.9488,3.6288,6.2208,38.988,34.742,5.7312,116.872,-2.5093,5.1042,3.3725,4.2804,15.525,123.7691,22.0032,15.386,0.7794,-3.7584,-12.147,-420.0,-16.5528,13.5932,3.8655,7.884,6.5975,1.3584,-66.062,3.6288,5.0463,2.592,3.4944,23.2624,8.073,2.1582,-9.098,18.09,-14.8704,29.245,331.191,54.2808,4.2336,6.3504,7.1994,8.4888,18.6624,28.497,8.5025,-52.6582,70.312,-97.4988,467.9922,22.736,6.6846,8.1216,-26.7558,24.9984,19.755,-4.908,2.2155,11.025,-292.9872,20.539,-1.3208,1.0192,10.7301,9.7911,16.296,14.7582,22.2,31.4895,6.4128,7.945,10.43,5.184,9.1764,8.208,2.244,6.074,45.588,8.6855,7.584,-178.9668,125.1432,3.6348,41.68,27.3592,4.2804,8.3754,6.0858,5.1435,80.784,13.2352,8.4656,157.8702,139.5702,15.552,-6.03,1.7487,6.2208,1.7901,511.368,10.8558,1.376,13.0112,17.469,-12.6882,16.3352,2.338,29.692,22.9885,8.532,1.4256,1.6704,57.5904,33.3124,4.008,11.46,-17.6076,-183.6324,137.151,3.1104,2.3571,17.6232,16.6698,7.0048,79.8912,20.155,78.9516,18.767,290.0058,27.69,1.7901,11.2236,33.5772,1.7052,35.49,412.5394,50.8254,30.5964,70.006,2.934,-9.8115,142.485,34.758,218.2518,26.558,-135.087,63.984,7.6154,1.0842,94.4937,-1.3128,9.072,10.4496,8.6715,97.2032,6.704,2.891,1.962,-249.3216,7.79,16.291,14.7184,85.9818,-74.7456,148.491,-54.588,1.0731,10.3936,17.3712,9.8856,19.0848,38.2095,5.9312,-22.144,63.7536,20.6816,239.985,0.0,1007.9832,33.93,9.6957,19.824,60.5488,6.15,105.297,5.5875,6.8274,1.9224,7.992,4.8519,48.3136,9.3312,-10.4184,-104.673,10.9096,51.8238,2.7062,-7.2,5.775,9.594,-5.0688,1.3978,41.7186,12.7764,1.1946,23.5248,13.674,-65.568,2.3808,301.968,76.1125,5.0274,-59.373,4.7996,46.1184,-2.61,37.534,20.585,5.6112,3.6432,-35.6174,11.2266,-0.99,12.691,2.7168,-11.596,-1.406,4.0095,-3.2392,6.4216,-12.9568,3.034,-34.0704,1.926,34.2925,210.4936,-2.688,-2.3904,0.868,34.776,2.9547,100.656,22.6782,9.604,37.4144,-44.2764,87.2842,77.625,314.0384,5.8891,10.0282,20.538,4.5188,6.475,56.511,-0.6048,19.791,2.7279,12.1176],"y0":" ","yaxis":"y","type":"box"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0]},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"Profit"}},"legend":{"tracegroupgap":0},"margin":{"t":60},"boxmode":"group"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('20fcfb63-cc0a-4633-9f97-ad139fd7d10f');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


# #8 What Is Confirmatory Data Analysis (CDA)? 

Confirmatory Data Analysis is the part where you evaluate your evidence using traditional statistical tools such as significance, inference, and confidence.

    Assumption 1 - Every summer technology products have the highest sale quantity compared to other product categories.
    Assumption 2- In New York, there are many big companies, therefore, office supplies product has 
    the highest sale quantity compared to other big states such as Texas, Illinois, and California. 


# `Assumption 1 - Every summer technology products have the highest sale quantity compared to other product categories.`


```python
seasons = {
    1 : "Winter",
    2 : "Spring",
    3 : "Summer",
    4 : "Fall"
}
```

# Creating **Season** column


```python
data["Season"] = data.Month.astype(int) % 12 // 3 + 1
data.Season = data.Season.map(seasons)
data.sample(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order Date</th>
      <th>Customer Name</th>
      <th>State</th>
      <th>Category</th>
      <th>Sub-Category</th>
      <th>Product Name</th>
      <th>Sales</th>
      <th>Quantity</th>
      <th>Profit</th>
      <th>Year</th>
      <th>Month</th>
      <th>Day</th>
      <th>Season</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3193</th>
      <td>2014-09-01</td>
      <td>Jack Lebron</td>
      <td>Texas</td>
      <td>Office Supplies</td>
      <td>Binders</td>
      <td>Prestige Round Ring Binders</td>
      <td>3.6480</td>
      <td>3</td>
      <td>-6.0192</td>
      <td>2014</td>
      <td>9</td>
      <td>1</td>
      <td>Fall</td>
    </tr>
    <tr>
      <th>4484</th>
      <td>2016-11-03</td>
      <td>Xylona Preis</td>
      <td>California</td>
      <td>Office Supplies</td>
      <td>Binders</td>
      <td>Fellowes Black Plastic Comb Bindings</td>
      <td>9.2960</td>
      <td>2</td>
      <td>3.0212</td>
      <td>2016</td>
      <td>11</td>
      <td>3</td>
      <td>Fall</td>
    </tr>
    <tr>
      <th>2430</th>
      <td>2017-05-13</td>
      <td>Ross Baird</td>
      <td>California</td>
      <td>Office Supplies</td>
      <td>Labels</td>
      <td>Self-Adhesive Address Labels for Typewriters b...</td>
      <td>58.4800</td>
      <td>8</td>
      <td>27.4856</td>
      <td>2017</td>
      <td>5</td>
      <td>13</td>
      <td>Spring</td>
    </tr>
    <tr>
      <th>9062</th>
      <td>2016-02-28</td>
      <td>Rick Reed</td>
      <td>New York</td>
      <td>Office Supplies</td>
      <td>Fasteners</td>
      <td>Staples</td>
      <td>36.4800</td>
      <td>6</td>
      <td>18.2400</td>
      <td>2016</td>
      <td>2</td>
      <td>28</td>
      <td>Winter</td>
    </tr>
    <tr>
      <th>8454</th>
      <td>2016-04-18</td>
      <td>Thea Hudgings</td>
      <td>Texas</td>
      <td>Furniture</td>
      <td>Furnishings</td>
      <td>Howard Miller 16" Diameter Gallery Wall Clock</td>
      <td>127.8800</td>
      <td>5</td>
      <td>-67.1370</td>
      <td>2016</td>
      <td>4</td>
      <td>18</td>
      <td>Spring</td>
    </tr>
    <tr>
      <th>266</th>
      <td>2017-06-16</td>
      <td>Claudia Bergmann</td>
      <td>North Carolina</td>
      <td>Office Supplies</td>
      <td>Art</td>
      <td>Quartet Omega Colored Chalk, 12/Pack</td>
      <td>14.0160</td>
      <td>3</td>
      <td>4.7304</td>
      <td>2017</td>
      <td>6</td>
      <td>16</td>
      <td>Summer</td>
    </tr>
    <tr>
      <th>8709</th>
      <td>2014-11-16</td>
      <td>Justin Deggeller</td>
      <td>California</td>
      <td>Furniture</td>
      <td>Bookcases</td>
      <td>Bush Andora Bookcase, Maple/Graphite Gray Finish</td>
      <td>305.9745</td>
      <td>3</td>
      <td>25.1979</td>
      <td>2014</td>
      <td>11</td>
      <td>16</td>
      <td>Fall</td>
    </tr>
    <tr>
      <th>6927</th>
      <td>2016-06-23</td>
      <td>Ruben Dartt</td>
      <td>California</td>
      <td>Office Supplies</td>
      <td>Storage</td>
      <td>Mobile Personal File Cube</td>
      <td>93.6800</td>
      <td>4</td>
      <td>25.2936</td>
      <td>2016</td>
      <td>6</td>
      <td>23</td>
      <td>Summer</td>
    </tr>
    <tr>
      <th>7025</th>
      <td>2017-02-06</td>
      <td>Sibella Parks</td>
      <td>New York</td>
      <td>Technology</td>
      <td>Phones</td>
      <td>Grandstream GXP1160 VoIP phone</td>
      <td>227.4600</td>
      <td>6</td>
      <td>65.9634</td>
      <td>2017</td>
      <td>2</td>
      <td>6</td>
      <td>Winter</td>
    </tr>
    <tr>
      <th>5073</th>
      <td>2015-11-05</td>
      <td>Justin MacKendrick</td>
      <td>California</td>
      <td>Office Supplies</td>
      <td>Storage</td>
      <td>Hanging Personal Folder File</td>
      <td>62.8000</td>
      <td>4</td>
      <td>15.7000</td>
      <td>2015</td>
      <td>11</td>
      <td>5</td>
      <td>Fall</td>
    </tr>
    <tr>
      <th>8067</th>
      <td>2015-10-20</td>
      <td>Noel Staavos</td>
      <td>California</td>
      <td>Technology</td>
      <td>Accessories</td>
      <td>Logitech G602 Wireless Gaming Mouse</td>
      <td>239.9700</td>
      <td>3</td>
      <td>86.3892</td>
      <td>2015</td>
      <td>10</td>
      <td>20</td>
      <td>Fall</td>
    </tr>
    <tr>
      <th>8315</th>
      <td>2014-07-12</td>
      <td>Paul Van Hugh</td>
      <td>Texas</td>
      <td>Office Supplies</td>
      <td>Art</td>
      <td>Fluorescent Highlighters by Dixon</td>
      <td>22.2880</td>
      <td>7</td>
      <td>3.9004</td>
      <td>2014</td>
      <td>7</td>
      <td>12</td>
      <td>Summer</td>
    </tr>
    <tr>
      <th>2440</th>
      <td>2016-05-22</td>
      <td>Art Ferguson</td>
      <td>New Jersey</td>
      <td>Technology</td>
      <td>Phones</td>
      <td>AT&amp;T 841000 Phone</td>
      <td>345.0000</td>
      <td>5</td>
      <td>86.2500</td>
      <td>2016</td>
      <td>5</td>
      <td>22</td>
      <td>Spring</td>
    </tr>
    <tr>
      <th>1689</th>
      <td>2014-08-16</td>
      <td>Troy Staebel</td>
      <td>Pennsylvania</td>
      <td>Furniture</td>
      <td>Tables</td>
      <td>Chromcraft Rectangular Conference Tables</td>
      <td>853.0920</td>
      <td>6</td>
      <td>-227.4912</td>
      <td>2014</td>
      <td>8</td>
      <td>16</td>
      <td>Summer</td>
    </tr>
    <tr>
      <th>2291</th>
      <td>2015-04-20</td>
      <td>Theresa Swint</td>
      <td>Georgia</td>
      <td>Furniture</td>
      <td>Furnishings</td>
      <td>GE 48" Fluorescent Tube, Cool White Energy Sav...</td>
      <td>595.3800</td>
      <td>6</td>
      <td>297.6900</td>
      <td>2015</td>
      <td>4</td>
      <td>20</td>
      <td>Spring</td>
    </tr>
    <tr>
      <th>2946</th>
      <td>2017-12-14</td>
      <td>Mike Pelletier</td>
      <td>California</td>
      <td>Furniture</td>
      <td>Furnishings</td>
      <td>Eldon 400 Class Desk Accessories, Black Carbon</td>
      <td>26.2500</td>
      <td>3</td>
      <td>11.0250</td>
      <td>2017</td>
      <td>12</td>
      <td>14</td>
      <td>Winter</td>
    </tr>
    <tr>
      <th>8129</th>
      <td>2014-07-20</td>
      <td>Jonathan Doherty</td>
      <td>California</td>
      <td>Technology</td>
      <td>Accessories</td>
      <td>Maxell 74 Minute CD-R Spindle, 50/Pack</td>
      <td>41.9400</td>
      <td>2</td>
      <td>15.0984</td>
      <td>2014</td>
      <td>7</td>
      <td>20</td>
      <td>Summer</td>
    </tr>
    <tr>
      <th>408</th>
      <td>2017-12-08</td>
      <td>Keith Herrera</td>
      <td>California</td>
      <td>Furniture</td>
      <td>Tables</td>
      <td>Bevis Round Conference Table Top, X-Base</td>
      <td>1004.0240</td>
      <td>7</td>
      <td>-112.9527</td>
      <td>2017</td>
      <td>12</td>
      <td>8</td>
      <td>Winter</td>
    </tr>
    <tr>
      <th>7574</th>
      <td>2015-12-08</td>
      <td>Yana Sorensen</td>
      <td>California</td>
      <td>Office Supplies</td>
      <td>Storage</td>
      <td>Stur-D-Stor Shelving, Vertical 5-Shelf: 72"H x...</td>
      <td>221.9600</td>
      <td>2</td>
      <td>4.4392</td>
      <td>2015</td>
      <td>12</td>
      <td>8</td>
      <td>Winter</td>
    </tr>
    <tr>
      <th>1067</th>
      <td>2016-10-01</td>
      <td>Brian DeCherney</td>
      <td>California</td>
      <td>Furniture</td>
      <td>Chairs</td>
      <td>Global Value Mid-Back Manager's Chair, Gray</td>
      <td>194.8480</td>
      <td>4</td>
      <td>12.1780</td>
      <td>2016</td>
      <td>10</td>
      <td>1</td>
      <td>Fall</td>
    </tr>
  </tbody>
</table>
</div>



# Extracting data related to summer every year


```python
summer_data = data[data.Season == "Summer"]
summer_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order Date</th>
      <th>Customer Name</th>
      <th>State</th>
      <th>Category</th>
      <th>Sub-Category</th>
      <th>Product Name</th>
      <th>Sales</th>
      <th>Quantity</th>
      <th>Profit</th>
      <th>Year</th>
      <th>Month</th>
      <th>Day</th>
      <th>Season</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2201</th>
      <td>2014-06-01</td>
      <td>Liz Thompson</td>
      <td>Arkansas</td>
      <td>Technology</td>
      <td>Phones</td>
      <td>Adtran 1202752G1</td>
      <td>881.930</td>
      <td>7</td>
      <td>229.3018</td>
      <td>2014</td>
      <td>6</td>
      <td>1</td>
      <td>Summer</td>
    </tr>
    <tr>
      <th>245</th>
      <td>2014-06-01</td>
      <td>Dianna Wilson</td>
      <td>Minnesota</td>
      <td>Office Supplies</td>
      <td>Storage</td>
      <td>Safco Steel Mobile File Cart</td>
      <td>166.720</td>
      <td>2</td>
      <td>41.6800</td>
      <td>2014</td>
      <td>6</td>
      <td>1</td>
      <td>Summer</td>
    </tr>
    <tr>
      <th>307</th>
      <td>2014-06-01</td>
      <td>Corey Roper</td>
      <td>New Jersey</td>
      <td>Office Supplies</td>
      <td>Art</td>
      <td>Boston Heavy-Duty Trimline Electric Pencil Sha...</td>
      <td>289.200</td>
      <td>6</td>
      <td>83.8680</td>
      <td>2014</td>
      <td>6</td>
      <td>1</td>
      <td>Summer</td>
    </tr>
    <tr>
      <th>246</th>
      <td>2014-06-01</td>
      <td>Dianna Wilson</td>
      <td>Minnesota</td>
      <td>Office Supplies</td>
      <td>Paper</td>
      <td>Adams Telephone Message Book w/Frequently-Call...</td>
      <td>47.880</td>
      <td>6</td>
      <td>23.9400</td>
      <td>2014</td>
      <td>6</td>
      <td>1</td>
      <td>Summer</td>
    </tr>
    <tr>
      <th>247</th>
      <td>2014-06-01</td>
      <td>Dianna Wilson</td>
      <td>Minnesota</td>
      <td>Office Supplies</td>
      <td>Appliances</td>
      <td>Honeywell Enviracaire Portable HEPA Air Cleane...</td>
      <td>1503.250</td>
      <td>5</td>
      <td>496.0725</td>
      <td>2014</td>
      <td>6</td>
      <td>1</td>
      <td>Summer</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9663</th>
      <td>2017-08-31</td>
      <td>Maxwell Schwartz</td>
      <td>California</td>
      <td>Office Supplies</td>
      <td>Storage</td>
      <td>Space Solutions Commercial Steel Shelving</td>
      <td>193.950</td>
      <td>3</td>
      <td>9.6975</td>
      <td>2017</td>
      <td>8</td>
      <td>31</td>
      <td>Summer</td>
    </tr>
    <tr>
      <th>2841</th>
      <td>2017-08-31</td>
      <td>Rob Lucas</td>
      <td>North Carolina</td>
      <td>Office Supplies</td>
      <td>Paper</td>
      <td>Xerox 1945</td>
      <td>229.544</td>
      <td>7</td>
      <td>83.2097</td>
      <td>2017</td>
      <td>8</td>
      <td>31</td>
      <td>Summer</td>
    </tr>
    <tr>
      <th>3654</th>
      <td>2017-08-31</td>
      <td>Ashley Jarboe</td>
      <td>Indiana</td>
      <td>Office Supplies</td>
      <td>Appliances</td>
      <td>Tripp Lite Isotel 8 Ultra 8 Outlet Metal Surge</td>
      <td>638.730</td>
      <td>9</td>
      <td>166.0698</td>
      <td>2017</td>
      <td>8</td>
      <td>31</td>
      <td>Summer</td>
    </tr>
    <tr>
      <th>4990</th>
      <td>2017-08-31</td>
      <td>Arthur Wiediger</td>
      <td>California</td>
      <td>Technology</td>
      <td>Phones</td>
      <td>Aastra 6757i CT Wireless VoIP phone</td>
      <td>689.408</td>
      <td>4</td>
      <td>77.5584</td>
      <td>2017</td>
      <td>8</td>
      <td>31</td>
      <td>Summer</td>
    </tr>
    <tr>
      <th>7063</th>
      <td>2017-08-31</td>
      <td>Michael Granlund</td>
      <td>Oregon</td>
      <td>Office Supplies</td>
      <td>Supplies</td>
      <td>Acme Kleen Earth Office Shears</td>
      <td>6.208</td>
      <td>2</td>
      <td>0.6984</td>
      <td>2017</td>
      <td>8</td>
      <td>31</td>
      <td>Summer</td>
    </tr>
  </tbody>
</table>
<p>2133 rows × 13 columns</p>
</div>



Aggregating data based on Year, Category, and Season columns and summing up the Quantity


```python
summer_data_agg = summer_data.groupby(["Category","Year","Season"]).agg({"Quantity":"sum"}).reset_index()
summer_data_agg
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Category</th>
      <th>Year</th>
      <th>Season</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Furniture</td>
      <td>2014</td>
      <td>Summer</td>
      <td>343</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Furniture</td>
      <td>2015</td>
      <td>Summer</td>
      <td>386</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Furniture</td>
      <td>2016</td>
      <td>Summer</td>
      <td>402</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Furniture</td>
      <td>2017</td>
      <td>Summer</td>
      <td>486</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Office Supplies</td>
      <td>2014</td>
      <td>Summer</td>
      <td>1031</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Office Supplies</td>
      <td>2015</td>
      <td>Summer</td>
      <td>959</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Office Supplies</td>
      <td>2016</td>
      <td>Summer</td>
      <td>1406</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Office Supplies</td>
      <td>2017</td>
      <td>Summer</td>
      <td>1638</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Technology</td>
      <td>2014</td>
      <td>Summer</td>
      <td>306</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Technology</td>
      <td>2015</td>
      <td>Summer</td>
      <td>296</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Technology</td>
      <td>2016</td>
      <td>Summer</td>
      <td>385</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Technology</td>
      <td>2017</td>
      <td>Summer</td>
      <td>531</td>
    </tr>
  </tbody>
</table>
</div>



# Let's visualize our result using a grouped bar chart


```python
px.bar(summer_data_agg,
      x = "Year",
      y = "Quantity",
      color = "Category",
      barmode = "group")
```


<div>                            <div id="62743e7f-9b10-419f-a1dd-5cbf19486806" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("62743e7f-9b10-419f-a1dd-5cbf19486806")) {                    Plotly.newPlot(                        "62743e7f-9b10-419f-a1dd-5cbf19486806",                        [{"alignmentgroup":"True","hovertemplate":"Category=Furniture<br>Year=%{x}<br>Quantity=%{y}<extra></extra>","legendgroup":"Furniture","marker":{"color":"#636efa","pattern":{"shape":""}},"name":"Furniture","offsetgroup":"Furniture","orientation":"v","showlegend":true,"textposition":"auto","x":[2014,2015,2016,2017],"xaxis":"x","y":[343,386,402,486],"yaxis":"y","type":"bar"},{"alignmentgroup":"True","hovertemplate":"Category=Office Supplies<br>Year=%{x}<br>Quantity=%{y}<extra></extra>","legendgroup":"Office Supplies","marker":{"color":"#EF553B","pattern":{"shape":""}},"name":"Office Supplies","offsetgroup":"Office Supplies","orientation":"v","showlegend":true,"textposition":"auto","x":[2014,2015,2016,2017],"xaxis":"x","y":[1031,959,1406,1638],"yaxis":"y","type":"bar"},{"alignmentgroup":"True","hovertemplate":"Category=Technology<br>Year=%{x}<br>Quantity=%{y}<extra></extra>","legendgroup":"Technology","marker":{"color":"#00cc96","pattern":{"shape":""}},"name":"Technology","offsetgroup":"Technology","orientation":"v","showlegend":true,"textposition":"auto","x":[2014,2015,2016,2017],"xaxis":"x","y":[306,296,385,531],"yaxis":"y","type":"bar"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"Year"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"Quantity"}},"legend":{"title":{"text":"Category"},"tracegroupgap":0},"margin":{"t":60},"barmode":"group"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('62743e7f-9b10-419f-a1dd-5cbf19486806');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


## Assumption proved wrong: The graph says that, the quantities of office supplies are higher than the technology


        
# `Assumption 2- In New York, there are many big companies, therefore, office supplies product has the highest sale quantity compared to other big states such as Texas, Illinois, and California.` 

## Deriving unique details in the column State to locate the required States to confirm our Assumption


```python
data["State"].unique()
```




    array(['Texas', 'Illinois', 'Pennsylvania', 'Kentucky', 'Georgia',
           'California', 'Virginia', 'Delaware', 'Louisiana', 'Ohio',
           'South Carolina', 'Oregon', 'Arizona', 'Arkansas', 'Michigan',
           'Tennessee', 'Florida', 'Indiana', 'Nevada', 'South Dakota',
           'New York', 'Wisconsin', 'Washington', 'New Jersey', 'Missouri',
           'North Carolina', 'Colorado', 'Utah', 'Minnesota', 'Mississippi',
           'Iowa', 'New Mexico', 'Massachusetts', 'Alabama', 'Idaho',
           'Montana', 'Maryland', 'Connecticut', 'New Hampshire', 'Oklahoma',
           'Nebraska', 'Maine', 'Kansas', 'Rhode Island',
           'District of Columbia', 'Vermont', 'Wyoming', 'North Dakota',
           'West Virginia'], dtype=object)




```python
state_supply = data.loc[data['State'].isin(["New York", "Texas", "Illinois", "California"])]
```


```python
max_supplies = state_supply.groupby(["State","Category"]).agg({"Quantity":"sum"}).reset_index()
max_supplies

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Category</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>California</td>
      <td>Furniture</td>
      <td>1696</td>
    </tr>
    <tr>
      <th>1</th>
      <td>California</td>
      <td>Office Supplies</td>
      <td>4566</td>
    </tr>
    <tr>
      <th>2</th>
      <td>California</td>
      <td>Technology</td>
      <td>1405</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Illinois</td>
      <td>Furniture</td>
      <td>448</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Illinois</td>
      <td>Office Supplies</td>
      <td>1095</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Illinois</td>
      <td>Technology</td>
      <td>302</td>
    </tr>
    <tr>
      <th>6</th>
      <td>New York</td>
      <td>Furniture</td>
      <td>877</td>
    </tr>
    <tr>
      <th>7</th>
      <td>New York</td>
      <td>Office Supplies</td>
      <td>2585</td>
    </tr>
    <tr>
      <th>8</th>
      <td>New York</td>
      <td>Technology</td>
      <td>762</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Texas</td>
      <td>Furniture</td>
      <td>766</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Texas</td>
      <td>Office Supplies</td>
      <td>2299</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Texas</td>
      <td>Technology</td>
      <td>659</td>
    </tr>
  </tbody>
</table>
</div>



# Let's Visualize the data frame


```python
px.bar(max_supplies,
      x = "State",
      y = "Quantity",
      color = "Category",
      barmode = "group")
```


<div>                            <div id="e0358040-2716-4384-a8c0-78342806c958" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("e0358040-2716-4384-a8c0-78342806c958")) {                    Plotly.newPlot(                        "e0358040-2716-4384-a8c0-78342806c958",                        [{"alignmentgroup":"True","hovertemplate":"Category=Furniture<br>State=%{x}<br>Quantity=%{y}<extra></extra>","legendgroup":"Furniture","marker":{"color":"#636efa","pattern":{"shape":""}},"name":"Furniture","offsetgroup":"Furniture","orientation":"v","showlegend":true,"textposition":"auto","x":["California","Illinois","New York","Texas"],"xaxis":"x","y":[1696,448,877,766],"yaxis":"y","type":"bar"},{"alignmentgroup":"True","hovertemplate":"Category=Office Supplies<br>State=%{x}<br>Quantity=%{y}<extra></extra>","legendgroup":"Office Supplies","marker":{"color":"#EF553B","pattern":{"shape":""}},"name":"Office Supplies","offsetgroup":"Office Supplies","orientation":"v","showlegend":true,"textposition":"auto","x":["California","Illinois","New York","Texas"],"xaxis":"x","y":[4566,1095,2585,2299],"yaxis":"y","type":"bar"},{"alignmentgroup":"True","hovertemplate":"Category=Technology<br>State=%{x}<br>Quantity=%{y}<extra></extra>","legendgroup":"Technology","marker":{"color":"#00cc96","pattern":{"shape":""}},"name":"Technology","offsetgroup":"Technology","orientation":"v","showlegend":true,"textposition":"auto","x":["California","Illinois","New York","Texas"],"xaxis":"x","y":[1405,302,762,659],"yaxis":"y","type":"bar"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"State"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"Quantity"}},"legend":{"title":{"text":"Category"},"tracegroupgap":0},"margin":{"t":60},"barmode":"group"},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('e0358040-2716-4384-a8c0-78342806c958');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


## Assumption proved correct: The graph says that, the quantities of office supplies are relatively higher in NY than the other cities.


```python

```


```python
import jovian
```


```python
jovian.commit()
```


    <IPython.core.display.Javascript object>


    [jovian] Committed successfully! https://jovian.ai/kjswnth/the-notebook[0m
    




    'https://jovian.ai/kjswnth/the-notebook'




```python

```
