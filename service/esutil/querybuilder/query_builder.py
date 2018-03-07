from service.esutil import dsl_search
from elasticsearch_dsl import Q
from service.esutil.querybuilder.query.query import Query

class Operator(object):
    # equals, contains, wildcard, gt, gte, lt, lte
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.operator = kwargs.get('operator')

    __equals__ = "equals"
    __contains__ = "contains"
    __wildcard__ = "wildcard"
    __gt__ = "gt"
    __gte__ = "gte"
    __lt__ = "lt"
    __lte__ = "lte"

    def get_query_type_instance(self):
        if self.operator == self.__equals__:
            return Query.instantiate(Query.TERM, **self.kwargs)
        elif self.operator == self.__contains__:
                return Query.instantiate(Query.MULTIMATCH, **self.kwargs)
        elif self.operator in [self.__wildcard__]:
                return Query.instantiate(Query.WILDCARD, **self.kwargs)
        elif self.operator in [self.__gt__, self.__gte__, self.__lt__, self.__lte__]:
                return Query.instantiate(Query.RANGE, **self.kwargs)


class QueryBuilder(object):
    def __init__(self, criteria):
        self.criteria = criteria

    def _get_fragments(self):
        bool_query_fragments = {
            "AND": [],  # must
            "OR": [],   # should
            "NOT": []   # must_not
        }

        for operator_type, operator_type_criteria in self.criteria.items():
            for operator_type_criterion in operator_type_criteria:
                query_type_obj = Operator(**operator_type_criterion).get_query_type_instance()
                q = query_type_obj.build()
                bool_query_fragments[operator_type].append(q)

        return bool_query_fragments

    def _combine_query(self):
        processed_fragments = dict()
        fragments = self._get_fragments()
        print fragments.items()
        for op, queries in fragments.items():
            if len(queries) > 0:
                if op == "AND":
                    processed_fragments["must"] = queries
                elif op == "OR":
                    processed_fragments["should"] = queries
                elif op == "NOT":
                    processed_fragments["must_not"] = queries

        combined_q = Q('bool', **processed_fragments)
        return combined_q

    def search(self, index=None, doc_type=None):
        q = self._combine_query()
        s = dsl_search.index(index).doc_type(doc_type).query(q)
        return s

    @classmethod
    def get_raw_query(cls, s):
        return s.to_dict()

    @classmethod
    def execute(cls, s):
        return s.execute()