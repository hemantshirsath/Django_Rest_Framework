from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit=2
    max_limit=5
    limit_query_param='l'
    offset_query_param='o'