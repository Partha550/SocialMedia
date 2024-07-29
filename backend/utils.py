from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.lexers.sql import PostgresLexer
from sqlparse import format

def print_sql(queryset):
    query = format(str(queryset.query), reindent=True)
    print(highlight(query, PostgresLexer(), Terminal256Formatter()))

