import json
import requests
from django.shortcuts import render

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "116fc2ce6cmsha455515b888a436p1ecb0djsnc40314a88b1d"
    }

response = requests.request("GET", url, headers=headers).json()

def home(request):
    mylist = []
    noofresults = int(response['results'])
    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])
    if request.method=='POST':
        selectedcountry = request.POST['selectedcountry']
        noofresults = int(response['results'])
        for x in range(0, noofresults):
            if selectedcountry==response['response'][x]['country']:
                population = response['response'][x]['population']
                new_cases = response['response'][x]['cases']['new']
                active_cases = response['response'][x]['cases']['active']
                critical_cases = response['response'][x]['cases']['critical']
                recovered_cases = response['response'][x]['cases']['recovered']
                total_cases = response['response'][x]['cases']['total']
                death_total = response['response'][x]['deaths']['total']
                new_death = response['response'][x]['deaths']['new']
                test= response['response'][x]['tests']['total']
                time = response['response'][x]['time']
                continent = response['response'][x]['continent']
                print(continent)
        context = { 'selectedcountry':selectedcountry, 
                    'mylist': mylist,
                    'population':population, 
                    'new_cases':new_cases, 
                    'active_cases':active_cases, 
                    'critical_cases':critical_cases, 
                    'recovered_cases':recovered_cases, 
                    'total_cases':total_cases, 
                    'death_total':death_total,
                    'new_death':new_death,
                    'test':test,
                    'time':time,
                    'continent':continent,
                     }
        return render(request, 'home.html', context)
    
    content = {'mylist':mylist}
    return render(request, 'home.html', content)
