#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


df = pd.read_csv(r"D:\jupyter projects\world pop tutorial\world_population.csv") #import dataset
df


# In[5]:


df.info() #Overview of dataset


# In[8]:


pd.set_option('display.float_format', lambda x: '%.1f' % x)
df


# In[9]:


df.describe()


# In[10]:


df.sort_values(by="2022 Population", ascending=False).head(10) #Show top 10 most populus countries, decensing order


# In[35]:


sns.barplot(df.nlargest(10, '2022 Population'), x="Country", y="2022 Population", legend=True) #Creating a bar graph of top 10 countries by 2022 pop. 
plt.show()


# In[39]:


df[df['Continent'].str.contains('Oceania')]


# In[44]:


df.boxplot()


# In[ ]:




