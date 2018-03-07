# Twitter Stream Filter API(TweetBot)

APIs has been created to store twitter streaming data and retrieve data based on applied filters. It is a set of 3 APIs-
1. API to trigger Twitter Stream
2. API to filter/search stored tweets
3. API to export filtered data in CSV

Technologies used:
  - Python
  - Flask framework
  - ElasticSearch 
  - Twitter Streaming API
  
## To setup project (Installation Instructions)
  1. clone the project
  2. cd to project folder `cd twitterapibackend` and create virtual environment
  `virtualenv venv`
  3. activate virtual environment
  `source venv/bin/activate`
  4. install requirements after activating virtual environment
  `pip install -r requirements.txt`
  5. Change the twitter stream Api credentials in configure.py file.

## To setup elasticsearch (Installation Instructions)
  To install and configure follow the given link of where all steps are clearly given.
  `https://www.tutorialspoint.com/articles/ install-and-configure-elasticsearch-in-ubuntu-14-04-3`

## To runserver (Installation Instructions)
Run the `python runserver.py` (try to avoid running at 9200 port because elastic default port is also 9200 )
  
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
  ***Default time for streaming is 30 seconds


## 2. API to filter/search stored tweets (/api2)
This API fetches the data stored by the [first api](#1-api-to-trigger-twitter-stream) based on the filters and search keywords provided and sorts them as required.
## Operators

**Operators**: Following operators are available in order to filter/query data/tweets -

* _```equals```_ : Facilitates exact match, or **=** operator for numeric/datetime values.

* _```contains```_ : Facilitates full-text search.

* _```wildcard```_ : 

  * ```startswith``` : _*ind_ (Starts with *ind*), 
  
  * ```endswith``` : _ind*_ (Ends with *ind*), 
  
  * ```wildcard``` : _\*ind\*_ (searches *ind* anywhere in string)

* _```gte```_ : **>=** operator for numeric/datetime values.

* _```gt```_ : **>** operator for numeric/datetime values.

* _```lte```_ : **<=** operator for numeric/datetime values.

* _```lt```_ : **<** operator for numeric/datetime values.


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
## Response
 You'll get the filtered tweets response 

 *** AND represents must, OR repesents should and NOT repesents must_not, as matched according to elasticsearch query attributes.
 *** Response may result to empty in case if it'll not find any relevant result according to provided query.

Example:
Body Json:

```{
  "sort":["created_at"],              
  "criteria": {
    
    "OR": [{
      "fields": ["tweet_text"],
      "operator": "contains",
      "query": "modi"
        }
    ]
  }
}```

Response:
  {
    "count": {
        "total": 16,
        "fetched": 16
    },
    "results": [
        {
            "sort": [
                1520414046000
            ],
            "_type": "tweet",
            "_source": {
                "lang": "und",
                "is_retweeted": false,
                "retweet_count": 0,
                "screen_name": "jova_novic",
                "country": "",
                "created_at": "2018-03-07T09:14:06",
                "hashtags": [],
                "tweet_text": "@pravoverna Kamenjarke nisu u modi vise,sad su trotoarke i zovu sebe starletama!",
                "source_device": "Twitter for Android",
                "reply_count": 0,
                "location": "Kragujevac, Srbija",
                "country_code": "",
                "timestamp_ms": "1520414046040",
                "user_name": "Jova Novic",
                "favorite_count": 0
            },
            "_score": null,
            "_index": "tweets_index",
            "_id": "AWH_vTXoVKT_vQpI5__3"
        },
        {.....}
        {.....}
        {.....}
        {.....}
    ]
}

 

## 3. API to export filtered data in CSV (/api3)

API 3 : `http://0.0.0.0:8080/api3`
(methods supported - GET, POST)

This API returns the data in CSV. Input should be given in same format as in api2 as json payload but here no need for providing pagination details.
Csv will be downloaded when puts request on browser and When posted in postman csv data will be reflected in response body and you can find attachment in header.

