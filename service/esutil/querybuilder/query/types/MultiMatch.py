from service.esutil.querybuilder.query.query import Query
from elasticsearch_dsl import Q

# For contains
class MultiMatch(Query):
    def __init__(self, query, fields):
        self.query = query
        fields = fields or "_all"
        self.fields = fields if type(fields) == list else [fields]

    def build(self):
        q = Q("multi_match", query=self.query, fields=self.fields)
        return q

    @classmethod
    def instantiate(cls, **kwargs):
        return cls(kwargs.get('query'), kwargs.get('fields'))