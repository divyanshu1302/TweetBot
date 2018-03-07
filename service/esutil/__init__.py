from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

es = Elasticsearch()
dsl_search = Search(using=es)
