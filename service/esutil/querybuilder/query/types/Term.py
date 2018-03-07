from service.esutil.querybuilder.query.query import Query
from elasticsearch_dsl import Q

# For equals
class Term(Query):
    def __init__(self, query, fields):
        self.query = query
        self.fields = fields if type(fields)==list else [fields]

    def build(self):
        criterion = {self.fields[0]+".raw": self.query}
        #Q('term', category='meetup')
        q = Q("term", **criterion)
        return q

    @classmethod
    def instantiate(cls, **kwargs):
        return cls(kwargs.get('query'), kwargs.get('fields'))