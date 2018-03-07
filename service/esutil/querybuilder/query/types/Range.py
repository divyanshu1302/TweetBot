from service.esutil.querybuilder.query.query import Query
from elasticsearch_dsl import Q

# For eq, gt, gte, lt, lte
class Range(Query):
    def __init__(self, query, fields, operator):
        self.operator = operator
        self.query = query
        self.fields = fields if type(fields)==list else [fields]

    def build(self):
        criterion = {
            self.fields[0]: {
                self.operator: self.query
            }
        }
        # Range(** {'@timestamp': {'lt': 'now'}})
        q = Q("range", **criterion)
        return q

    @classmethod
    def instantiate(cls, **kwargs):
        return cls(kwargs.get('query'), kwargs.get('fields'), kwargs.get('operator'))