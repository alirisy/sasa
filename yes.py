#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
st. header('''voting''')
st.write('''checking your voting eligibility''')
age = st.number_input('enter your age: ')
if age > 17:
    st.write("you can vote")
else:
    st.write("you cannot vote")


# In[ ]:




