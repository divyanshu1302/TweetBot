import json
from flask import Response
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def jsonify(data=None):
    """
    Converts data to it's corresponding JSON format. If data is string then return data as it is.
    If data is `None` return empty json as '{}'.
    :param data: str or dictionary/list/array
    :return: Jsonified version of data.
    """
    json_res = None
    if not data:
        json_res = '{}'
    if type(data) != str:
        data = {} if not data else data
        json_res = json.dumps(data)
    return json_res

def json_response(res=None):
    """
    Converts dictionary/array/list to corresponding JSON structure.
    :param res: dictionary/array/list or a valid json string
    :return: JSON
    """
    json_res = jsonify(res)
    return Response(json_res, mimetype="application/json")


def json_to_csv(res):
    """
    Converts Json to csv 

    """
    d = []
    l  = len(res["results"])
    for i in range(l):
        d.append(res["results"][i]["_source"])

    # open a file for writing
    data = open('tweet.csv', 'w++')
    # create the csv writer object
    csvwriter = csv.writer(data)
    count = 0
    for t in d:
          if count == 0:
                 header = t.keys()
                 csvwriter.writerow(header)
                 count += 1
          csvwriter.writerow(t.values())
    data.close()

    return True