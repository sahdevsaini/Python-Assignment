#!/usr/bin/env python
# coding: utf-8

# ## Q 1. To what does a relative path refer?

# In[4]:


# A relative path is a path with respect my current working DIrectory(PWD). 


# ## Q 2. Where \ does an absolute path start with your operating system?

# **ANS:-** 
# ### In Linux based Operating System it starts with \.But in windows it starts with c:
# 
# **For ex:-**  If Absolute Path to a file called assingment.py is **C:\Users\Dell\Pictures\assingment.py** and my Pwd is **C:\Users\Dell**
# then relate path is Pictures\assingment.py.

# ## 3. What do the functions os.getcwd() and os.chdir() do?

# **Ans:-**
# os.getcwd() function tells the current working directory(pwd) whereas os.chdir() is used to 
#        to change the current working directory to a specific path.

# In[11]:


import os 
print("This is the default working directory :- ",os.getcwd())    # It will print the current working directory.
new_path = r'C:\Users\Dell\Documents'
os.chdir(new_path)            # it will change the current working directory from default to **new_path**
print(os.getcwd())


# ## 4. What are the . and .. folders?

# **Ans:-** . Represents the Current Working Directory and **..** represent the Parent directory of Current Working Directory
#     <br>**For Ex:-**
#     <br>Current Working Directory :-  **C:\Users\Dell\Downloads\Assingment 9.ipynb**<br>
#     Parent Directory :- **C:\Users\Dell**
#     

# ## 5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?

#    dir name :- **C:\bacon\eggs**<br>
#     base name :- **spam.txt** 

# In[15]:


import os
path = r'C:\bacon\eggs\spam.txt'
print(os.path.dirname(path))
print(os.path.basename(path))


# ## 6. What are the three “mode” arguments that can be passed to the open() function?

# **Ans:-**<br> 
# A file can be Accessed in python using open() function. open function takes two arguments filename and mode of operation (optional). if mode is not provided the default mode of opening is read mode
# So, the syntax being: open(filename, mode)<br>
# <br>
# **‘r’ – Read Mode:** This is the default mode for open(). The file is opened and a pointer is positioned at the beginning of the file’s content.<br>
# **‘w’ – Write Mode:** Using this mode will overwrite any existing content in a file. If the given file does not exist, a new one will be created.<br>
# **‘r+’ – Read/Write Mode:** Use this mode if you need to simultaneously read and write to a file.<br>
# **‘a’ – Append Mode:** With this mode the user can append the data without overwriting any already existing data in the file.<br>
# **‘a+’ – Append and Read Mode:** In this mode you can read and append the data without overwriting the original file.<br>
# **‘x’ – Exclusive Creating Mode:** This mode is for the sole purpose of creating new files. Use this mode if you know the file to be written doesn’t exist beforehand.

# ## 7. What happens if an existing file is opened in write mode?

# **Ans:-**<br>
#     Using this mode will overwrite any existing content in a file. If the given file does not exist, a new one will be created.

# ## 8. How do you tell the difference between read() and readlines()?

# In[ ]:


Ans: The main difference is that read() will read the whole file at once and then print out the first characters that take up as many bytes as you specify in the parenthesis

Whereas the readline() that will read and print out only the first characters that take up as many bytes as you specify in the parenthesis. You may want to use readline() when you're reading files that are too big for your RAM.
The read() would treat each character in the file separately, meaning that the iteration would happen for every character.
The readline() function, on the other hand, only reads a single line of the file. This means that if the first line of the file were three lines long, the readline() function would only parse (or iterate/operate) on the first line of the file.


# ## 9. What data structure does a shelf value resemble?

# **Ans:-**<br> 
#    It contains key and values it represents dictionary.

# In[ ]:




