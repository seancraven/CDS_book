#!/usr/bin/env python
# coding: utf-8

# # Hide cell contents
# 
# You can use Jupyter Notebook **cell tags** to control some of the behavior of
# the rendered notebook. This uses the [**`sphinx-togglebutton`**](https://sphinx-togglebutton.readthedocs.io/en/latest/)
# package to add a little button that toggles the visibility of content.[^download]
# 
# [^download]: This notebook can be downloaded as
#             **{nb-download}`hiding.ipynb`** and {download}`hiding.md`
# 
# (use/hiding/code)=
# 
# ## Hide code cells
# 
# You can use **cell tags** to control the content hidden with code cells at the cell level.
# Add the following tags to a cell's metadata to control
# what to hide in code cells:
# 
# * **`hide-input`** tag to hide the cell inputs
# * **`hide-output`** to hide the cell outputs
# * **`hide-cell`** to hide the entire cell
# 
# For example, we'll show cells with each below.

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
data = np.random.rand(2, 100) * 100


# Here is a cell with a `hide-input` tag. Click the "toggle" button to the
# right to show it.

# In[2]:


# This cell has a hide-input tag
fig, ax = plt.subplots()
points =ax.scatter(*data, c=data[0], s=data[0])


# Here's a cell with a `hide-output` tag:

# In[3]:


# This cell has a hide-output tag
fig, ax = plt.subplots()
points =ax.scatter(*data, c=data[0], s=data[0])


# And the following cell has a `hide-cell` tag:

# In[4]:


# This cell has a hide-cell tag
fig, ax = plt.subplots()
points =ax.scatter(*data, c=data[0], s=data[0])


# (use/hiding/markdown)=
# 
# ## Hide markdown cells
# 
# You cannot hide an entire markdown cell, but you can hide sections of markdown **content** by using roles and directives.
# 
# For information on how to hide / toggle markdown content in Sphinx, see either [the `sphinx-togglebutton` documentation](https://sphinx-togglebutton.readthedocs.io/en/latest/) or the [`sphinx-design` dropdowns documentation](https://sphinx-design.readthedocs.io/en/latest/dropdowns.html).
# 
# (use/removing)=
# 
# ## Remove parts of cells
# 
# Sometimes, you want to entirely remove parts of a cell so that it doesn't make it into the output at all.
# 
# To do this at the global level, use the `nb_remove_code_source` or `nb_remove_code_outputs` configuration options, or at a per-file level, e.g.
# 
# ```yaml
# ---
# mystnb:
#   remove_code_source: true
#   remove_code_outputs: true
# ---
# ```
# 
# See the [configuration section](config/intro) for more details.
# 
# At a per-cell level you can use the same tag pattern described above,
# but with the word `remove_` instead of `hide_`. Use the following tags:
# 
# * **`remove-input`** tag to remove the cell inputs
# * **`remove-output`** to remove the cell outputs
# * **`remove-cell`** to remove the entire cell

# Here is a cell with a `remove-input` tag. The inputs will not make it into
# the page at all.

# In[5]:


# This cell has a remove-input tag
fig, ax = plt.subplots()
points =ax.scatter(*data, c=data[0], s=data[0])


# Here's a cell with a `remove-output` tag:

# In[6]:


# This cell has a remove-output tag
fig, ax = plt.subplots()
points = ax.scatter(*data, c=data[0], s=data[0])


# And the following cell has a `remove-cell` tag (there should be nothing
# below, since the cell will be gone).

# In[7]:


# This cell has a remove-cell tag
fig, ax = plt.subplots()
points = ax.scatter(*data, c=data[0], s=data[0])

