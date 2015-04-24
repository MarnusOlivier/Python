from datetime import datetime
def StringToDateTime(StringDates, TypeIndex = 0):
    Types = ['%Y-%m-%d %H:%M:%S',       # 2013-01-01 15:24:00
             '%Y/%m/%d %I:%M:%S %p',     # ?
             '%Y-%m-%d %H:%M:%S.%f',
             '%Y-%m-%d']       
    DateTime = []
    for el in StringDates:
        DateTime.append(datetime.strptime(el, Types[TypeIndex]))
    return DateTime