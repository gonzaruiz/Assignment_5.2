
# coding: utf-8

# In[1]:


subjects=["Americans", "Indians"]
verbs=["play", "watch"]
objects=["Baseball","Cricket"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print (sentence)
        

