import requests

#  https://restcountries.eu/
# Find by Name https://restcountries.eu/rest/v2/name/{name}
# Filter via Fields https://restcountries.eu/rest/v2/name/{name}?fields=name

url = 'https://restcountries.eu/rest/v2/'



# a = requests.get(url)
# json_result = a.json()

# print(json_result[84]['name'], json_result[84]['topLevelDomain'])


# r = requests.get(url + 'name/canada?fields=name')
# print(r.json())

# fields = {'fields' : 'name;currencies;alpha2Code'}
# z = requests.get(url + 'name/sin', params=fields)
# print(z.json())

# Great API

print('Country API - get information for a country')
print('What info do you want about a country')
print('1.Population')
print('2.Languages')
print('3.Timezone')
option = input('')
print('I pick: {}'.format(option))


country = input('What country do you want that info for? ')


params = {'fields': 'name;population;languages;timezones', 'fullText' : 'true'}

r = requests.get(url + 'name/{}'.format(country), params=params)

json_response = r.json()

country = None
try:
    country = json_response[0]
except KeyError:
    print('Country is not found')


# Note you need to sanitise data working with web systems
if country:
    if option == '1':
        print('{} has a population of {} people'.format(country['name'], country['population']))

    elif option == '2':
        langs = []
        for language in country['languages']:
            langs.append(language['name'])
        print('{} spoke the following languages: {}.'.format(country['name'], ', '.join(langs)))

    else:
        print('{}\'s Timezone: {}.'.format(country['name'], ', '.join(country['timezones'])))


