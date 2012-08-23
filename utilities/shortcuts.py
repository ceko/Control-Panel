
#Property decorator that returns an array of Django field information from string representation
def django_meta(model_type):    
    
    def wrap(f):
        def new_function(*args, **kw):            
            meta = []
            for column in f(*args, **kw):
                meta.append(model_type._meta.get_field(column))
            
            return meta
        return new_function
    return wrap