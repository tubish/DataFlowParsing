# Zangetsu
First Project

This project will be my first python project after completing Python Boot Camp, 
The objective is to create a custom data parser for Energy Industry Data Flow files in order to turn them to a format that is loadable to any relational database even readible from the files itself.

What is done --> 
"""
1. get the file names and counts from the source and its subfolders
2. first level file validations
    2.2. Header ID = Tail ID
    2.3. row_count = tail row count value
    2.4. file name pattern check D[0-9][0-9][0-9][0-9][0-9][0-9][0-9]
3. create the dflow folder under target
3. move the files that passes the validations to the target folder
4. move the files that fail the validations to the bad folder
5. report back total counts. dflow group by counts
6. create a full report as a pickle file for later use in jupyter
"""

watch this space !!!
