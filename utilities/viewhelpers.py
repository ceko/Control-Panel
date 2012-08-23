from django.utils.datastructures import SortedDict

class DataSet(object):
            
    @property        
    def columns(self):
        return self._columns
    
    @property
    def rows(self):
        return self._rows        
            
    def __init__(self):
        self._columns = []    
        self._rows = []
    
    @staticmethod
    def from_model_query(modelquery, model_fields=[]):
        set = DataSet()
        lookup = {}
        for field in model_fields:
            col = DataSetColumn(field.name, field.verbose_name)
            set._columns.append(col)
            lookup[field.name] = col
                
        if modelquery.count() != 0:
            for row in modelquery:
                current_row = SortedDict()
                for field in model_fields:                                        
                    current_row[field.name] = DataSetValue(getattr(row,field.name), lookup[field.name])
                set._rows.append(current_row)
        
        return set 
    

class DataSetColumn(object):
    
    @property 
    def verbose_name(self):
        return self._verbose_name
    
    @property
    def name(self):
        return self._name
    
    def __init__(self, name, verbose_name):
        self._name = name
        self._verbose_name = verbose_name
    
    def __unicode__(self):
        return self.verbose_name

class DataSetValue(object):
    
    @property 
    def value(self):
        return self._value
        
    @property
    def column(self):
        return self._column
    
    def __init__(self, value, column):        
        self._value = value
        self._column = column
        
    def __unicode__(self):
        return unicode(self.value)