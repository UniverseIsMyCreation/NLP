import re

"""
check filename for only one template (word with spaces and _ symbol).(only symbols of alphabet)
"""
def regex_for_filename(filename: str):
    list_of_matches = re.fullmatch(r'^[A-Za-z0-9_\s]{1,8}\.[A-Za-z]{1,4}$', filename)
    if list_of_matches is None:
        return 'Uncorrect'
    else:
        return 'Correct'

"""
check correctness of auto number
"""
def regex_for_auto(auto_number: str):
    list_of_matches = re.fullmatch(r'^([A-Z]{1}\d{3}[A-Z]{2}\d{2,3}){1}', auto_number)
    if list_of_matches is None:
        return 'Uncorrect'
    else:
        return 'Correct'

"""
check correctness of numerical number
"""
def regex_for_number(number: str):
    list_of_matches = re.fullmatch(r'^[-+]?(0|[1-9]+)([.,]{1}\d+([eE]{1}[+-]{1}\d+)?)?$', number)
    if list_of_matches is None:
        return 'Uncorrect'
    else:
        return 'Correct'


print(*[regex_for_filename(expression) for expression in ['fi le_1.py', 'inasd1.inasd.inasd', 'asdasd.12', 'asdasdasdasd.py']])
print(*[regex_for_auto(expression) for expression in ['C105MK777', 'C105MK77', 'c105MK777', 'C105MKLL777', 'C10MK777']])
print(*[regex_for_number(expression) for expression in ['-87.21E-5', '87.21E-5', '-87.21', '87.']])
