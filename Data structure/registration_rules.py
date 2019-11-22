def check_registration_rules(**kwargs):
    removing= set()
    for key,value in kwargs.items():
        # print(key)
        if key == 'quera' or key == 'codecup':
            removing.add(key)
        if len(key) < 4:
            removing.add(key)
        if len(value) < 6 or value.isdigit():
            removing.add(key)
        pass
    # print("#")
    for item in removing:
        kwargs.pop(item)
        # print(item)
        pass
    out = []
    for key,value in kwargs.items():
        out.append(key)
    # print(out)
    return out
    pass
check_registration_rules(username='password', sadegh='He3@lsa', quera='kLS45@l$' , saeed='1234567', ab='afj$L12')