from django.shortcuts import render
import json
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "116fc2ce6cmsha455515b888a436p1ecb0djsnc40314a88b1d"
    }

response = requests.request("GET", url, headers=headers).json()

# print(response.text)
# print(response.text)



def home(request):
    mylist = []
    noofresults = int(response['results'])
    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])
    if request.method=='POST':
        selectedcountry = request.POST['selectedcountry']
        # print(selectedcountry)
        noofresults = int(response['results'])
        for x in range(0, noofresults):
            if selectedcountry==response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                death = int(total)-int(active)-int(recovered)
        context = {'selectedcountry':selectedcountry, 'mylist': mylist, 'new':new, 'active':active, 'critical':critical, 'recovered':recovered, 'total':total, 'death':death }
        return render(request, 'home.html', context)
    
    content = {'mylist':mylist}
    return render(request, 'home.html', content)