# Application description

# Version 1

- command-line tool. installed and accessible from command line
- allows to:
  1. Download all retrosheet data:
    1.a - All files downaloaded
      1.a.i - Stored in folders as csv files. CSV files would be pre-processed for easier access from pandas
      1.a.ii - Converted and uploaded to DB. Add support for Postgresql and SQLite
    1.b - Basic data summary is available. All files sizes, column names etc. 
  2. Download selected data only (on demand):
    2.a - Provides a few command-line options to download only selected files (year, team, gametype)
    2.b - Data is converted to CSV and stored in location specified by user
    2.c - Basic data summary is available
  3. Would contain a special 'help' function, that would provide information about data, fields, sources, fields descriptions etc.
