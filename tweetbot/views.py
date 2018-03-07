from tweetbot.application import app
from service.esutil import es
from configure import es_mappings
from flask import Flask
from flask import request
from flask import abort
from datetime import date
from operator import itemgetter
import json, csv
from service.esutil.querybuilder.query_builder import QueryBuilder
from service.commons import json_response,json_to_csv

@app.route('/')
def index():
    return '<h1>Welcome to TweetBot</h1>'

@app.route('/api1')
def stream():
    res = dict()
    try:
        keywords = request.args.get('keywords')
        runtime = request.args.get('runtime')
        if keywords:
            keywords = keywords.split(",")
        else:
            res = {
                "status": "error",
                "message": "Please provide a few keyword(s) (comma-separated)",
                "example": "/api1?keywords=kw1,kw2,abc,xyz"
            }
            return json_response(res)
        from twitter_api import Tweety
        Tweety().filter(keywords=keywords,runtime = runtime)
        res['status'] = "success"
        res['message'] = "Started streaming tweets with keywords {}".format(keywords)

    except Exception as exc:
        res['status'] = "error"
        res['message'] = exc.message
        res['args'] = exc.args
    return json_response(res)


@app.route('/api2', methods=["GET","POST"])
def search_handler():
    es_size = int(request.args.get('size', 100))
    es_from = int(request.args.get('from', 0))
    data = json.loads(request.data)
    criteria = data.get('criteria')
    sort = data.get('sort')
    s = QueryBuilder(criteria).search(index='tweets_index', doc_type='tweet')
    if sort:
        s = s.sort(*sort)
    s = s[es_from:es_size]
    print "[QUERY]", QueryBuilder.get_raw_query(s)

    try:
        es_res = QueryBuilder.execute(s)
    except Exception as ex:
        res = {
            "status": "error",
            "message": ex.message,
            "args": ex.args
        }
        return json_response(res)
    res = dict()
    if es_res is not None:
        hits = es_res.hits
        res["count"] = {"total": hits.total, "fetched": len(hits.hits) }
        res["results"] = hits.hits
    return json_response(res)


@app.route('/api3', methods=["GET","POST"])
def jsontocsv():
    data = json.loads(request.data)
    criteria = data.get('criteria')
    sort = data.get('sort')
    s = QueryBuilder(criteria).search(index='tweets_index', doc_type='tweet')
    if sort:
        s = s.sort(*sort)
    print "[QUERY]", QueryBuilder.get_raw_query(s)

    try:
        es_res = QueryBuilder.execute(s)
    except Exception as ex:
        res = {
            "status": "error",
            "message": ex.message,
            "args": ex.args
        }
        return json_response(res)
    res = dict()
    if es_res is not None:
        hits = es_res.hits
        res["count"] = {"total": hits.total, "fetched": len(hits.hits) }
        res["results"] = hits.hits

    json_to_csv(res)
    res = {
            "status": "success",
        }
    return json_response(res)
   
    




           