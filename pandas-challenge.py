#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dependencies
import pandas as pd
import mumpy as np
import os


# In[ ]:


school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"


# In[ ]:


school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)


# In[ ]:


school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])

