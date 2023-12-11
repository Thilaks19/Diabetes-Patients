.. code:: ipython3

    import numpy as np # for linear algebra
    import pandas as pd # data processing, CSV file I/O, etc
    import seaborn as sns # for plots
    import plotly.graph_objects as go # for plots
    import plotly.express as px #for plots
    import matplotlib.pyplot as plt # for visualizations and plots
    import missingno as msno # for plotting missing data

.. code:: ipython3

    df = pd.read_csv("C:/Users/THILAK.S/Downloads/Project 2 MeriSKILL/diabetes.csv")
    df.head() # displays the top 5 values in the dataset




.. raw:: html

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
          <th>Pregnancies</th>
          <th>Glucose</th>
          <th>BloodPressure</th>
          <th>SkinThickness</th>
          <th>Insulin</th>
          <th>BMI</th>
          <th>DiabetesPedigreeFunction</th>
          <th>Age</th>
          <th>Outcome</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>6</td>
          <td>148</td>
          <td>72</td>
          <td>35</td>
          <td>0</td>
          <td>33.6</td>
          <td>0.627</td>
          <td>50</td>
          <td>1</td>
        </tr>
        <tr>
          <th>1</th>
          <td>1</td>
          <td>85</td>
          <td>66</td>
          <td>29</td>
          <td>0</td>
          <td>26.6</td>
          <td>0.351</td>
          <td>31</td>
          <td>0</td>
        </tr>
        <tr>
          <th>2</th>
          <td>8</td>
          <td>183</td>
          <td>64</td>
          <td>0</td>
          <td>0</td>
          <td>23.3</td>
          <td>0.672</td>
          <td>32</td>
          <td>1</td>
        </tr>
        <tr>
          <th>3</th>
          <td>1</td>
          <td>89</td>
          <td>66</td>
          <td>23</td>
          <td>94</td>
          <td>28.1</td>
          <td>0.167</td>
          <td>21</td>
          <td>0</td>
        </tr>
        <tr>
          <th>4</th>
          <td>0</td>
          <td>137</td>
          <td>40</td>
          <td>35</td>
          <td>168</td>
          <td>43.1</td>
          <td>2.288</td>
          <td>33</td>
          <td>1</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df.info()


.. parsed-literal::

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 768 entries, 0 to 767
    Data columns (total 9 columns):
     #   Column                    Non-Null Count  Dtype  
    ---  ------                    --------------  -----  
     0   Pregnancies               768 non-null    int64  
     1   Glucose                   768 non-null    int64  
     2   BloodPressure             768 non-null    int64  
     3   SkinThickness             768 non-null    int64  
     4   Insulin                   768 non-null    int64  
     5   BMI                       768 non-null    float64
     6   DiabetesPedigreeFunction  768 non-null    float64
     7   Age                       768 non-null    int64  
     8   Outcome                   768 non-null    int64  
    dtypes: float64(2), int64(7)
    memory usage: 54.1 KB
    

.. code:: ipython3

    df.describe()




.. raw:: html

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
          <th>Pregnancies</th>
          <th>Glucose</th>
          <th>BloodPressure</th>
          <th>SkinThickness</th>
          <th>Insulin</th>
          <th>BMI</th>
          <th>DiabetesPedigreeFunction</th>
          <th>Age</th>
          <th>Outcome</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>count</th>
          <td>768.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
        </tr>
        <tr>
          <th>mean</th>
          <td>3.845052</td>
          <td>120.894531</td>
          <td>69.105469</td>
          <td>20.536458</td>
          <td>79.799479</td>
          <td>31.992578</td>
          <td>0.471876</td>
          <td>33.240885</td>
          <td>0.348958</td>
        </tr>
        <tr>
          <th>std</th>
          <td>3.369578</td>
          <td>31.972618</td>
          <td>19.355807</td>
          <td>15.952218</td>
          <td>115.244002</td>
          <td>7.884160</td>
          <td>0.331329</td>
          <td>11.760232</td>
          <td>0.476951</td>
        </tr>
        <tr>
          <th>min</th>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.078000</td>
          <td>21.000000</td>
          <td>0.000000</td>
        </tr>
        <tr>
          <th>25%</th>
          <td>1.000000</td>
          <td>99.000000</td>
          <td>62.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>27.300000</td>
          <td>0.243750</td>
          <td>24.000000</td>
          <td>0.000000</td>
        </tr>
        <tr>
          <th>50%</th>
          <td>3.000000</td>
          <td>117.000000</td>
          <td>72.000000</td>
          <td>23.000000</td>
          <td>30.500000</td>
          <td>32.000000</td>
          <td>0.372500</td>
          <td>29.000000</td>
          <td>0.000000</td>
        </tr>
        <tr>
          <th>75%</th>
          <td>6.000000</td>
          <td>140.250000</td>
          <td>80.000000</td>
          <td>32.000000</td>
          <td>127.250000</td>
          <td>36.600000</td>
          <td>0.626250</td>
          <td>41.000000</td>
          <td>1.000000</td>
        </tr>
        <tr>
          <th>max</th>
          <td>17.000000</td>
          <td>199.000000</td>
          <td>122.000000</td>
          <td>99.000000</td>
          <td>846.000000</td>
          <td>67.100000</td>
          <td>2.420000</td>
          <td>81.000000</td>
          <td>1.000000</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df.isnull().sum()




.. parsed-literal::

    Pregnancies                 0
    Glucose                     0
    BloodPressure               0
    SkinThickness               0
    Insulin                     0
    BMI                         0
    DiabetesPedigreeFunction    0
    Age                         0
    Outcome                     0
    dtype: int64



.. code:: ipython3

    df["Glucose"] = df["Glucose"].apply(lambda x: np.nan if x == 0 else x)
    df["BloodPressure"] = df["BloodPressure"].apply(lambda x: np.nan if x == 0 else x)
    df["SkinThickness"] = df["SkinThickness"].apply(lambda x: np.nan if x == 0 else x)
    df["Insulin"] = df["Insulin"].apply(lambda x: np.nan if x == 0 else x)
    df["BMI"] = df["BMI"].apply(lambda x: np.nan if x == 0 else x)

.. code:: ipython3

    df.isnull().sum()




.. parsed-literal::

    Pregnancies                   0
    Glucose                       5
    BloodPressure                35
    SkinThickness               227
    Insulin                     374
    BMI                          11
    DiabetesPedigreeFunction      0
    Age                           0
    Outcome                       0
    dtype: int64



.. code:: ipython3

    px.pie(df, names="Outcome")



.. raw:: html

    <div>                            <div id="6f9f174b-ca32-4f80-883e-2f8dfeb3eee8" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("6f9f174b-ca32-4f80-883e-2f8dfeb3eee8")) {                    Plotly.newPlot(                        "6f9f174b-ca32-4f80-883e-2f8dfeb3eee8",                        [{"domain":{"x":[0.0,1.0],"y":[0.0,1.0]},"hovertemplate":"Outcome=%{label}<extra></extra>","labels":[1,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0,1,0,1,1,0,0,1,0,1,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,1,0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0],"legendgroup":"","name":"","showlegend":true,"type":"pie"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"legend":{"tracegroupgap":0},"margin":{"t":60}},                        {"responsive": true}                    ).then(function(){
    
    var gd = document.getElementById('6f9f174b-ca32-4f80-883e-2f8dfeb3eee8');
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


.. code:: ipython3

    sns.countplot(x="Outcome", data=df, palette=random.choice(pallete))




.. parsed-literal::

    <Axes: xlabel='Outcome', ylabel='count'>




.. image:: output_8_1.png


.. code:: ipython3

    sns.countplot(x="Pregnancies", hue = "Outcome", data=df, palette=random.choice(pallete))




.. parsed-literal::

    <Axes: xlabel='Pregnancies', ylabel='count'>




.. image:: output_9_1.png


.. code:: ipython3

    sns.histplot(x="Pregnancies", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))




.. parsed-literal::

    <Axes: xlabel='Pregnancies', ylabel='Count'>




.. image:: output_10_1.png


.. code:: ipython3

    sns.histplot(x="BloodPressure", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))




.. parsed-literal::

    <Axes: xlabel='BloodPressure', ylabel='Count'>




.. image:: output_11_1.png


.. code:: ipython3

    sns.histplot(x="Glucose", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))




.. parsed-literal::

    <Axes: xlabel='Glucose', ylabel='Count'>




.. image:: output_12_1.png


.. code:: ipython3

    sns.histplot(x="SkinThickness", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))




.. parsed-literal::

    <Axes: xlabel='SkinThickness', ylabel='Count'>




.. image:: output_13_1.png


.. code:: ipython3

    sns.histplot(x="Insulin", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))




.. parsed-literal::

    <Axes: xlabel='Insulin', ylabel='Count'>




.. image:: output_14_1.png


.. code:: ipython3

    sns.histplot(x="Age", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))




.. parsed-literal::

    <Axes: xlabel='Age', ylabel='Count'>




.. image:: output_15_1.png


.. code:: ipython3

    sns.histplot(x="BMI", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))




.. parsed-literal::

    <Axes: xlabel='BMI', ylabel='Count'>




.. image:: output_16_1.png


.. code:: ipython3

    sns.histplot(x="DiabetesPedigreeFunction", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))




.. parsed-literal::

    <Axes: xlabel='DiabetesPedigreeFunction', ylabel='Count'>




.. image:: output_17_1.png


.. code:: ipython3

    sns.pairplot(df, hue='Outcome',palette=random.choice(pallete))




.. parsed-literal::

    <seaborn.axisgrid.PairGrid at 0x20232405290>




.. image:: output_18_1.png


.. code:: ipython3

    fig, axs = plt.subplots(4, 2, figsize=(20,20))
    axs = axs.flatten()
    for i in range(len(df.columns)-1):
        sns.boxplot(data=df, x=df.columns[i], ax=axs[i], palette=random.choice(pallete))



.. image:: output_19_0.png


.. code:: ipython3

    sns.heatmap(df.corr(), linewidths=0.1, vmax=1.0, square=True, cmap='coolwarm', linecolor='white', annot=True).set_title("Correlation Map")




.. parsed-literal::

    Text(0.5, 1.0, 'Correlation Map')




.. image:: output_20_1.png


.. code:: ipython3

    df.isnull().sum()




.. parsed-literal::

    Pregnancies                   0
    Glucose                       5
    BloodPressure                35
    SkinThickness               227
    Insulin                     374
    BMI                          11
    DiabetesPedigreeFunction      0
    Age                           0
    Outcome                       0
    dtype: int64



.. code:: ipython3

    msno.bar(df)




.. parsed-literal::

    <Axes: >




.. image:: output_22_1.png


.. code:: ipython3

    msno.matrix(df, figsize=(20,35))




.. parsed-literal::

    <Axes: >




.. image:: output_23_1.png


.. code:: ipython3

    msno.heatmap(df, cmap=random.choice(pallete))




.. parsed-literal::

    <Axes: >




.. image:: output_24_1.png


.. code:: ipython3

    msno.dendrogram(df)




.. parsed-literal::

    <Axes: >




.. image:: output_25_1.png


.. code:: ipython3

    df.isnull().sum()/len(df)*100
    




.. parsed-literal::

    Pregnancies                  0.000000
    Glucose                      0.651042
    BloodPressure                4.557292
    SkinThickness               29.557292
    Insulin                     48.697917
    BMI                          1.432292
    DiabetesPedigreeFunction     0.000000
    Age                          0.000000
    Outcome                      0.000000
    dtype: float64



.. code:: ipython3

    df.drop(columns=["Insulin"], inplace=True)

.. code:: ipython3

    df.describe()




.. raw:: html

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
          <th>Pregnancies</th>
          <th>Glucose</th>
          <th>BloodPressure</th>
          <th>SkinThickness</th>
          <th>BMI</th>
          <th>DiabetesPedigreeFunction</th>
          <th>Age</th>
          <th>Outcome</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>count</th>
          <td>768.000000</td>
          <td>763.000000</td>
          <td>733.000000</td>
          <td>541.000000</td>
          <td>757.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
        </tr>
        <tr>
          <th>mean</th>
          <td>3.845052</td>
          <td>121.686763</td>
          <td>72.405184</td>
          <td>29.153420</td>
          <td>32.457464</td>
          <td>0.471876</td>
          <td>33.240885</td>
          <td>0.348958</td>
        </tr>
        <tr>
          <th>std</th>
          <td>3.369578</td>
          <td>30.535641</td>
          <td>12.382158</td>
          <td>10.476982</td>
          <td>6.924988</td>
          <td>0.331329</td>
          <td>11.760232</td>
          <td>0.476951</td>
        </tr>
        <tr>
          <th>min</th>
          <td>0.000000</td>
          <td>44.000000</td>
          <td>24.000000</td>
          <td>7.000000</td>
          <td>18.200000</td>
          <td>0.078000</td>
          <td>21.000000</td>
          <td>0.000000</td>
        </tr>
        <tr>
          <th>25%</th>
          <td>1.000000</td>
          <td>99.000000</td>
          <td>64.000000</td>
          <td>22.000000</td>
          <td>27.500000</td>
          <td>0.243750</td>
          <td>24.000000</td>
          <td>0.000000</td>
        </tr>
        <tr>
          <th>50%</th>
          <td>3.000000</td>
          <td>117.000000</td>
          <td>72.000000</td>
          <td>29.000000</td>
          <td>32.300000</td>
          <td>0.372500</td>
          <td>29.000000</td>
          <td>0.000000</td>
        </tr>
        <tr>
          <th>75%</th>
          <td>6.000000</td>
          <td>141.000000</td>
          <td>80.000000</td>
          <td>36.000000</td>
          <td>36.600000</td>
          <td>0.626250</td>
          <td>41.000000</td>
          <td>1.000000</td>
        </tr>
        <tr>
          <th>max</th>
          <td>17.000000</td>
          <td>199.000000</td>
          <td>122.000000</td>
          <td>99.000000</td>
          <td>67.100000</td>
          <td>2.420000</td>
          <td>81.000000</td>
          <td>1.000000</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df.skew()




.. parsed-literal::

    Pregnancies                 0.901674
    Glucose                     0.530989
    BloodPressure               0.134153
    SkinThickness               0.690619
    BMI                         0.593970
    DiabetesPedigreeFunction    1.919911
    Age                         1.129597
    Outcome                     0.635017
    dtype: float64



.. code:: ipython3

    # Highly skewed
    df["BMI"].replace(to_replace=np.nan,value=df["BMI"].median(), inplace=True)
    df["Pregnancies"].replace(to_replace=np.nan,value=df["Pregnancies"].median(), inplace=True)
    
    # Normal
    df["Glucose"].replace(to_replace=np.nan,value=df["Glucose"].mean(), inplace=True)
    df["BloodPressure"].replace(to_replace=np.nan,value=df["BloodPressure"].mean(), inplace=True)
    df["SkinThickness"].replace(to_replace=np.nan,value=df["SkinThickness"].mean(), inplace=True)

.. code:: ipython3

    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    print(IQR)


.. parsed-literal::

    Pregnancies                  5.0000
    Glucose                     40.5000
    BloodPressure               16.0000
    SkinThickness                7.0000
    BMI                          9.1000
    DiabetesPedigreeFunction     0.3825
    Age                         17.0000
    Outcome                      1.0000
    dtype: float64
    

.. code:: ipython3

    df_out = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
    print(f'Before: {df.shape}, After: {df_out.shape}')


.. parsed-literal::

    Before: (768, 8), After: (627, 8)
    

.. code:: ipython3

    for col in df.columns[:-1]:
        up_out = df[col].quantile(0.90)
        low_out = df[col].quantile(0.10)
        med = df[col].median()
    #     print(col, up_out, low_out, med)
        df[col] = np.where(df[col] > up_out, med, df[col])
        df[col] = np.where(df[col] < low_out, med, df[col])

.. code:: ipython3

    df.describe()




.. raw:: html

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
          <th>Pregnancies</th>
          <th>Glucose</th>
          <th>BloodPressure</th>
          <th>SkinThickness</th>
          <th>BMI</th>
          <th>DiabetesPedigreeFunction</th>
          <th>Age</th>
          <th>Outcome</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>count</th>
          <td>768.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
          <td>768.000000</td>
        </tr>
        <tr>
          <th>mean</th>
          <td>3.213542</td>
          <td>119.185461</td>
          <td>72.397794</td>
          <td>28.988775</td>
          <td>32.127083</td>
          <td>0.411184</td>
          <td>31.007812</td>
          <td>0.348958</td>
        </tr>
        <tr>
          <th>std</th>
          <td>2.561112</td>
          <td>18.584971</td>
          <td>7.302671</td>
          <td>4.533622</td>
          <td>4.047594</td>
          <td>0.171833</td>
          <td>7.469534</td>
          <td>0.476951</td>
        </tr>
        <tr>
          <th>min</th>
          <td>0.000000</td>
          <td>87.000000</td>
          <td>58.000000</td>
          <td>18.000000</td>
          <td>24.000000</td>
          <td>0.165000</td>
          <td>22.000000</td>
          <td>0.000000</td>
        </tr>
        <tr>
          <th>25%</th>
          <td>1.000000</td>
          <td>106.000000</td>
          <td>68.000000</td>
          <td>29.000000</td>
          <td>29.600000</td>
          <td>0.278000</td>
          <td>25.000000</td>
          <td>0.000000</td>
        </tr>
        <tr>
          <th>50%</th>
          <td>3.000000</td>
          <td>117.000000</td>
          <td>72.202592</td>
          <td>29.153420</td>
          <td>32.300000</td>
          <td>0.372500</td>
          <td>29.000000</td>
          <td>0.000000</td>
        </tr>
        <tr>
          <th>75%</th>
          <td>5.000000</td>
          <td>129.000000</td>
          <td>76.000000</td>
          <td>29.153420</td>
          <td>34.500000</td>
          <td>0.514000</td>
          <td>36.000000</td>
          <td>1.000000</td>
        </tr>
        <tr>
          <th>max</th>
          <td>9.000000</td>
          <td>167.000000</td>
          <td>88.000000</td>
          <td>40.000000</td>
          <td>41.500000</td>
          <td>0.878000</td>
          <td>51.000000</td>
          <td>1.000000</td>
        </tr>
      </tbody>
    </table>
    </div>


