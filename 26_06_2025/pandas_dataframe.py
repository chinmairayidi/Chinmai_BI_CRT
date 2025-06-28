#dataframe
import pandas as pd
data={
    'std1':
    {'name':'jyothi',
    'branch':'bioinformatics',
    'skills':['python','c++','sql']

    },
    'std2':
    {
    'name':'chinmai',
    'branch':'bio-informatics',
    'skills':['python','c++','sql']
    }
    }
data = pd.DataFrame(data)
print(data)
print(type(data))