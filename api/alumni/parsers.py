from alumni.models import Alumni


def parse_query(query):
    arg = {}
    l = query.split()

    field_values = [f.name for f in Alumni._meta.get_fields()]
    field_keys = ['post', 'internships', 'placements',
                  'higherstudies', 'USN', 'user', 'Name', 'Phone', 'Email', 'RV Email', 'Branch', 'joined', 'passed']
    d = dict(zip(field_keys, field_values))

    pfield_values = [f.name for f in Placements._meta.get_fields()]
    pfield_keys = ['_', '__', 'Company', 'Role', 'Category', 'CTC', 'Type']
    pd = dict(zip(pfield_keys, pfield_values))

    cdict = {'above': 'gt', 'below': 'lt',
             'startswith': 'startswith', 'endswith': 'endswith'}
    
    while l:
        try:
            token = l.pop(0)
            if token == 'all':
                return {}
            if token == 'and' or token == '=' or token == 'is':
                continue
            elif token == 'joined' or token == 'passed':
                key = d[token] + '__year'
                arg[key] = int(l.pop(0))
            elif token in field_keys:
                key = d[token]
            elif token in pfield_keys:
                key = 'placements__' + pd[token]
            elif token in cdict.keys():
                key += ('__' + cdict[token])
            else:
                arg[key] = token
        except:
            return {}
    print(arg)
    return arg
