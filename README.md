# DataExtraction - Data export tool for MySQL & MongoDB

## What is DataExtraction 

DataExtraction is an unfinished data extraction tool for you to export your specified: 

1. Data columns (for MySQL), or 
2. Fields (for MongoDB), 
  
and save them as csv or json.

Besides, DataExtraction support:

1. Data format transform: convert Json object to DataFrame for MySQL. You may not need this since usually we don't store json object or dict in Mysql, and this function is project-oriented since we happened have some json-like or dict data stored in relational database. 

2. Query with list type of condition [Not a join operation, the conditon list should be specified in advance]: You can use this package to specified a (list) of condition you may need to filter your query.

## What dependencies you need to install

1. pandas (0.19.2)
2. MySQLdb (1.2.3c1)
3. json (2.0.9)

## How to install it

`pip install DataExtraction`

## Function description


## Demo for basic SQL Query

## Demo for basic Mongo Query


## License

MIT


You are welcome to pull request to upload your own implement function, improve and modified my current design.



