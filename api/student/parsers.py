from student.models import Student
def parse_query(query):
    arg = {}
    l = query.split()

    field_values = [f.name for f in Student._meta.get_fields()]
    field_keys = ['USN', 'SAP', 'userid',
                  'Name', 'Phone', 'Email', 'RVEmail', 'Branch', 'joined']
    d = dict(zip(field_keys, field_values))

    cdict = {'after': 'gt', 'before': 'lt',
             'startswith': 'startswith', 'endswith': 'endswith'}
    
    while l:
        try:
            token = l.pop(0)
            if token == 'all':
                return {}
            if token == 'and' or token == '=' or token == 'is':
                continue
            elif token == 'joined':
                key = d[token] + '__year'
                c = l.pop(0)
                if c in cdict.keys():
                    key += ('__' + cdict[token])
                arg[key] = int(l.pop(0))
            elif token in field_keys:
                key = d[token]
            elif token in cdict.keys():
                key += ('__' + cdict[token])
            else:
                arg[key] = token
        except:
            return {}
    print(arg)
    return arg
