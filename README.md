# About

Small python App with tkinter GUI to search for specific string(s) in exported .dsx file and saving list of job names, where the string was found, into separate files.

## Basic logic

- User is requested to insert following 2 values via tkinter GUI:

  1. browse for exported file
  2. enter search string(s), which have to be comma delimited

- Exported ".dsx" file is split into list of 'jobs' based on "BEGIN DSJOB" string
- Script loops per search string all the jobs (within the created list) and creates new files (one per search string) within newly created folder "/SearchResults". The new files are named per search strings with ".txt" extension.
- Search is not case sensitive
- Files are saved into newly created subfolder "/SearchResults" - subfolder is created in the same folder as the selected export file

## Requirements

- Search strings must be comma delimited
- The search logic is not case sensitive

### Run the app

`python main.py`
