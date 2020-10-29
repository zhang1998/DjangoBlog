
def search(query, fields, terms):
    """ Performs a search based on a list of search terms. Returns a new
            query filtered with the search. """

    if len(terms) > 0:

        search_list = []

        for term in terms:
            field_list = []
            for field in fields:
                field_list.append(Q(**{field + '__icontains':term}))
            search_list.append(reduce(operator.or_, field_list))#逐个进行operator

        return query.filter(reduce(operator.and_, search_list))

    else:
        return query
