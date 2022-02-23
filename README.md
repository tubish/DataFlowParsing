# __Zangetsu__

## First Project
### Renamed as DataFlowParsing

This project will be my first python project after completing Python Boot Camp, 
The objective is to create a custom data parser for Energy Industry Data Flow files in order to turn them to a format that is loadable to any relational database even readible from the files itself.

### What is done:

__1.__ get the file names and counts from the source and its subfolders
__2.__ first level file validations
  - 2.2. Header ID = Tail ID
  - 2.3. row_count = tail row count value
  - 2.4. file name pattern check D[0-9][0-9][0-9][0-9][0-9][0-9][0-9]
__3.__ create the dflow folder under target
__4.__ move the files that passes the validations to the target folder
__5.__ move the files that fail the validations to the bad folder
__6.__ report back total counts. dflow group by counts
__7.__ create a full report as a pickle file for later use in jupyter


# watch this space !!!
