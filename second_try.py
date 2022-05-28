#!/usr/bin/env python
# coding: utf-8

# In[1]:

#wget https://download.geonames.org/export/zip/UA.zip

# In[2]:

import pandas as pd


# In[41]:


col = ['c_code', 'p_code','name', 'obl', 'un_num','region', 'rand col1', 'col2', 'col3', 'lat', 'lon', 'sm']
df = pd.read_csv('E:\\map\\UA\\UA.txt', sep='\t', names = col)
df.head()

df = df.drop(["c_code", "un_num", "sm","rand col1", "col2", "col3"], axis=1) 
df.head()


# In[42]:


df.head()


# In[152]:


df.to_csv("E:\\map\\changed.csv")


import folium


# In[55]:


m = folium.Map(location=[49.013, 31.285], zoom_start=6, min_zoom=6, max_zoom = 11)
m


# In[56]:


import requests


# In[83]:


res = requests.get('https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D1%87%D1%82%D0%BE%D0%B2%D0%BE%D0%B5_%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D1%8B')
print(res.text)


# In[71]:


from bs4 import BeautifulSoup


# In[86]:


soup = BeautifulSoup(res.text, 'html.parser')
table1 = soup.find('table')
table1


# In[91]:


headers = []
for i in table1.find_all('th'):
 title = i.text
 headers.append(title)


# In[92]:


i_range = pd.DataFrame(columns=headers)


# In[95]:


for j in table1.find_all('tr')[1:]:
 row_data = j.find_all('td')
 row = [i.text for i in row_data]
 length = len(i_range)
 i_range.loc[length] = row


# In[101]:


i_range = i_range.replace('\n', '', regex=True)


# In[102]:


i_range.to_csv('E:\\map\\index_range.csv')


# In[156]:


list(i_range.iloc[0, 1].split(', '))


# In[130]:


t = i_range.shape[0]


# In[235]:


i_start = []
for i in range(t):
    i_start.append(list(i_range.iloc[i, 1].split(', ')))
i_start[22] = ['83', '84', '85', '86', '87']
i_start


# In[139]:


obl_path = {}


# In[144]:


df.head()
    


# In[151]:

df = df.astype({"p_code":str})


tp = {'p_code' : str}


col = ['c_code', 'p_code','name', 'obl', 'un_num','region', 'rand col1', 'col2', 'col3', 'lat', 'lon', 'sm']
tp = {'p_code':str}
df = pd.read_csv('E:\\map\\UA\\UA.txt', sep='\t', names = col, dtype = tp)
df.head()

df = df.drop(["c_code", "un_num", "sm","rand col1", "col2", "col3"], axis=1) 
df.head()


# In[159]:


t = len(i_start)
t


# In[192]:


test = df[df['p_code'].str.startswith(tuple(i_start[3]))]
test


# In[165]:


test_list = []


# In[174]:


for i in range(245, 250):
    test_list.append(list(test.iloc[i, 4:6]))
test_list


# In[172]:


print(list(test.iloc[i, 4:6]))


# In[295]:


for i in range(t):
    test = df[df['p_code'].str.startswith(tuple(i_start[i]))]
    obl_path[i] = []
    for j in range(test.shape[0]):
        obl_path[i].append(tuple(test.iloc[j, 4:6])) 
    


# In[229]:
"""

m = folium.Map(location=[49.013, 31.285], zoom_start=6, min_zoom=6, max_zoom = 11)
m


# In[231]:


colors = ['gray', 'blue', 'yellow', 'green', 'pink', 'red', 'orange', 'purple']
for i in range(t):
    if obl_path[i]:
        
        folium.PolyLine(obl_path[i], color = colors[i%8], weight=1).add_to(m)
m


# In[294]:


marik = df[df['p_code'].str.startswith(tuple(i_start[22]))]
t_tuple = ('875', '876', '877')
marik_city = df[df['p_code'].str.startswith(t_tuple)]
marik_city.head()
marik_dot = []
for i in range(marik_city.shape[0]):
    
    marik_dot.append(tuple(marik_city.iloc[i, 4:6]))
m_dot = marik_city.shape[0]
print(marik_dot[0:5] in obl_path[22])
#print(marik_dot[0:5])


# In[297]:


m1 = folium.Map(location=[49.013, 31.285], zoom_start=6, min_zoom=6, max_zoom = 11)
#folium.PolyLine(marik_dot, color = colors[7], weight=1).add_to(m1)
folium.PolyLine(obl_path[22], color = colors[3], weight=1).add_to(m1)
folium.Marker(marik_dot[0]).add_to(m1)
m1
"""

# In[310]:


m4 = folium.Map(location=[49.013, 31.285], zoom_start=6, min_zoom=6, max_zoom = 11)

colors = ['gray', 'blue', 'yellow', 'green', 'pink', 'red', 'orange', 'purple', 'black', 'cadetblue']#, 'beige']
for i in range(t):
    if obl_path[i]:
        
        folium.PolyLine(obl_path[i], color = colors[i%9], weight=1).add_to(m4)
m4


# In[ ]:




