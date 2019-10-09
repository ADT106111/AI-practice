
# coding: utf-8

# In[4]:


sum = 0
n = int (input("請輸入正整數："))


# In[5]:


for i in range(1, n+1):
    sum =  sum + i


# In[6]:


print("1到 %d 的整數合為 %d " % (n, sum))

