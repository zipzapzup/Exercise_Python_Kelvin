import datetime


print('Hello')

result = []

# datetime.date(year, month, dates) 
# convert to a date time object
# print(i) will print the date
for i in range(1, 31 + 1):
    result.append(datetime.date(2000,1,i))

# for i in result:
#     print(i.strftime('%d-%B-%Y'))
# In here, we can use date.strftime(FORMAT) 
# to print the date

start_date = "1-March-2000"
end_date = "30-March-2000"
def search_date(start_date, end_date):
    result = []
    start = start_date.split('-')[0]
    end = end_date.split('-')[0]
    
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    newDict ={} # holds all the months 1: "January" mappings
    counter = 1
    for i in months:
        newDict[counter] = i
        counter += 1

    for i in range( int(start), int(end)):
        result.append(datetime.date( int(start[-1]), 3, i))
    return result

a = search_date(start_date, end_date)
f'---------- lines'

for i in a:
    print(i.strftime("%d-%B-%Y"))



# Define the Search Function using built-in date object

start = datetime.date(1999, 1, 1)
end = datetime.date(2000, 1, 8)

def search_range(start, end):
    result = []
    diff = end - start
    for i in range(diff.days):
        result.append(start + datetime.timedelta(i))
    return result

result2 = search_range(start, end)

f'-------- Search Range ------'
for i in result2:
    print(i, end='\t')