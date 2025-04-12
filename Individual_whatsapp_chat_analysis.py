#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import pandas as pd


# In[4]:


f=open(r'C:\Users\WINDOWS\Downloads\WhatsApp Chat with BOKU BAVA\WhatsApp Chat with BOKU BAVA.txt','r',encoding='utf-8')
data=f.read()
print(data)


# In[5]:


pattern='\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
messages=re.split(pattern,data)[1:]
(messages)
dates= re.findall(pattern, data)
dates


# In[8]:


df=pd.DataFrame({'user_message':messages,'message_date':dates})
#convert message_datetype
df['message_date']=pd.to_datetime(df['message_date'], format='%m/%d/%y, %H:%M - ')
df.rename(columns={'message_date': 'date'}, inplace=True)
df.head()
df.shape


# In[21]:


#separate users and messages
users = []
messages = []
for message in df['user_message']:
    entry = re.split('([\w\w]+?):\s',message)
if entry[1:]:#user name
    users.append(entry[1])
    messages.append(entry[2])
else:
    users.append('group_notification')
    messages.append(entry[0])
 


# In[22]:


df['user']= users
df['message'] = messages
df.drop(columns=['user_message'], inplace=True)
df.head()
df['date'].dt.year
df.head()
df['month']=df['date'].dt.month_name()
df['year']=df['date'].dt.year
df['day']=df['date'].dt.day
df['hour']=df['date'].dt.hour
df['minute']=df['date'].dt.minute
df.head(10)
df[df['user']=='MOHAN'].shape


# In[23]:


#Anlyzing number of words
words=[]



for message in df['message']:
 print(message.split())
words=[]
for message in df['message']:
 words.extend(message.split())
words
len(words)
from collections import Counter
pd.DataFrame(Counter(words).most_common(20))
temp=df[df['user'] !='121']
temp
df['month_num']=df['date'].dt.month
timeline=df.groupby(['year','month_num','month']).count()['message'].reset_index()
timeline
time=[]
for i in range(timeline.shape[0]):
 time.append(timeline['month'][i]+"-"+str(timeline['year'][i]))
timeline['time']=time
timeline
import matplotlib.pyplot as plt
plt.plot(timeline['time'],timeline['message'])
plt.xticks(rotation='vertical')
plt.show()



df['only_date']=df['date'].dt.date
daily_timeline=df.groupby('only_date').count()['message'].reset_index
daily_timeline
plt.figure(figsize=(18,10))
plt.plot(daily_timeline['only_date'],daily_timeline['message'])
df.head(30)
df['day_name']=df['date'].dt.day_name()
df['day_name'].value_counts()
df['month'].value_counts()
period=[]
for hour in df[['day_name','hour']]['hour']:
 if hour==23:
period.append(str(hour) + "-" +str('00'))
 elif hour==0:
 period.append(str('00') + "-" +str(hour+1))
 else:
 period.append(str(hour) + "-" +str(hour+1))
df['period']=period
df.sample(5)
import seaborn as sns
plt.figure(figsize=(20,6))



sns.heatmap(df.pivot_table(index='day_name',columns='period',values='message',agg
func='count').fillna(0))
plt.yticks(rotation='horizontal')
plt.show()
import matplotlib.pyplot as plt


# In[24]:


# Grouping data by 'user' and counting the number of messages
user_message_counts = df['user'].value_counts()


# In[25]:


# Plotting a pie chart
plt.figure(figsize=(8, 8))
plt.pie(user_message_counts, labels=user_message_counts.index, 
autopct='%1.1f%%', startangle=140)
plt.title('Message Distribution by User')
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
import re
import pandas as pd
from collections import Counter


# In[26]:


# Open and read the WhatsApp chat text file
with open('whatsapp_chat_with_Tej_kumar_122.txt', 'r', encoding='utf-8') as f:
 data = f.read()


# In[27]:


# Define a regular expression pattern to match emojis
emoji_pattern = r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-
\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-
\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-
\U0001FAFF\U00002702-\U000027B0\U000024C2-
\U0001F251\U0001F004\U0001F0CF\U0001F170-\U0001F251\U0001F300-
\U0001F5FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U0001F700-
\U0001F773\U0001F780-\U0001F7D8\U0001F7E0-\U0001F7EB\U0001F90D-
\U0001F93A\U0001F93C-\U0001F945\U0001F947-\U0001F971\U0001F973-
\U0001F976\U0001F97A\U0001F97C-\U0001F9A2\U0001F9B0-
\U0001F9B9\U0001F9C0-\U0001F9C2\U0001F9D0-\U0001F9FF\U0001FA70-
\U0001FA74\U0001FA78-\U0001FA7A\U0001FA80-\U0001FA86\U0001FA90-
\U0001FAA8\U0001FAB0-\U0001FAB6\U0001FAC0-\U0001FAC2\U0001FAD0-
\U0001FAD6]+'


# In[28]:


# Extract emojis from each message using regular expressions
emojis = re.findall(emoji_pattern, data)
# Count the frequency of each emoji
emoji_freq = Counter(emojis)
# Display the most common emojis and their frequencies
print("Top 10 Most Common Emojis:")
print(pd.DataFrame(emoji_freq.most_common(10), columns=['Emoji', 'Frequency']))






