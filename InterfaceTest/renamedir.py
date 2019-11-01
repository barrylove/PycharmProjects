import os
import re

path = "D:\\files"
for root, dirs, files in os.walk(path, topdown=False):
    print(root)
