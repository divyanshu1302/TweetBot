# Twitter Stream Filter API(TweetBot)

APIs has been created to store twitter streaming data and retrieve data based on applied filters. It is a set of 3 APIs-
1. [API to trigger Twitter Stream](#1-api-to-trigger-twitter-stream-stream)
2. [API to filter/search stored tweets](#2-api-to-filtersearch-stored-tweets-search)
3. [API to export filtered data in CSV](#3-api-to-export-filtered-data-in-csv-getcsv)

Technologies used:
  - Python
  - Flask framework
  - ElasticSearch 
  - Twitter Streaming API
  
## Jump To
- [Installation Guide](#installation-instructions)
- [API 1 - API to trigger Twitter Stream](#1-api-to-trigger-twitter-stream-stream)
- [API 2 - API to filter/search stored tweets](#2-api-to-filtersearch-stored-tweets-search)
- [API 3 - API to export filtered data in CSV](#3-api-to-export-filtered-data-in-csv-getcsv)
  
## To setup project (Installation Instructions)
  1. clone the project
  2. cd to project folder `cd twitter-streaming-filter-api` and create virtual environment
  `virtualenv venv`
  3. activate virtual environment
  `source venv/bin/activate`
  4. install requirements after acuvating virtual environment
  `pip install -r requirements.txt`
  5. Change the twitter stream Api credentials in configure.py file.

## To setup elasticsearch (Installation Instructions)
  To install and configure follow the given link of where all steps are clearly given.
  `https://www.tutorialspoint.com/articles/ install-and-configure-elasticsearch-in-ubuntu-14-04-3`

## To runserver (Installation Instructions)
  
## API's/Endpoints
## 1. API 1 to trigger Twitter Stream (/api1)
This API triggers twitter streaming and stores a curated version of the data returned by Twitter Streaming API. The streaming is done as per the given parameters.

API 1 - `http://0.0.0.0:8080/api1?keywords=modi,AbkiBarModiSarkar,ModiForPM`
(methods supported - GET, POST)

Where keywords can be any keyword for which streaming needs to be performed.
Successful response
```
  {
  "status": "success",
  "message": "Started streaming tweets with keywords [u'modi', u'AbkiBarModiSarkar', u'ModiForPM']"
  }
  ```


## 2. API to filter/search stored tweets (/api2)
This API fetches the data stored by the [first api](#1-api-to-trigger-twitter-stream) based on the filters and search keywords provided and sorts them as required.

API 2- `http://0.0.0.0:8080/api2?from=0&size=20`

Body in Raw form 
```
{
  "sort":["created_at"],              
  "criteria": {
    "AND": [{
      "fields": ["created_at"], 
      "operator": "gte",    
      "query": "2017-12-17T14:18:13"
        }, {
      "fields": ["location"],
      "operator": "wildcard",
      "query": "*ndia*"
        }
    ],
    "OR": [{
      "fields": ["hashtags"],
      "operator": "contains",
      "query": "" //anything that hastag contians ex-- "Modi"
        }, {
      "fields": ["hashtags"],
      "operator": "contains",
      "query": " "
        }
    ],
    "NOT": [{
      "fields": ["source_device"],
      "operator": "equals",
      "query": "Twitter for Android"
        }
    ]
      }
}
```
Response
 You'll get the filtered tweets response 


## 3. API to export filtered data in CSV (/api3)
This API returns the data in CSV. Input should be given in same format as in api2 as json payload but here no need for providing pagination details.

API : `http://0.0.0.0:8080/api3`
(methods supported - GET, POST)
