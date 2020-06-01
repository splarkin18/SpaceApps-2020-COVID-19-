#COVID-19 Prgram Draft 1
#This survey is meant to be taken by people who have all this information readily available such as a government official
def covid_impacts():
    counter = 0.0
    prompt = "This is a survey testing to see if your city is at risk of a COVID-19 outbreak. Please answer the questions as directed.\n"
    print(prompt)

    intl_travel = input("Does your city have an international airport?\nYes or no? ")
    #type convert the response to an int just in case
    #intl_travel = int(intl_travel)
    if intl_travel.lower().strip() == 'yes':
        counter += 5.0
    print(counter)
    print('\n')

    population = input("What is the population of your metropolitan area? ")
    population = int(population)
    if (population < 1500000):
        counter += 2.0
    elif (population >= 1500000) and (population <= 3000000):
        counter += 3.0
    elif (population > 3000000):
        counter += 4.0
    print(counter)
    print('\n')

    pop_dens = input("What is the population density of your city/town in people/sq. mile? ")
    #type convert the response to an float just in case
    pop_dens = float(pop_dens)
    if (pop_dens > 0.0) and (pop_dens <= 1.0):
        counter += 0.0
    elif (pop_dens > 1.0) and (pop_dens <= 5.0):
        counter += 1.0
    elif (pop_dens > 5.0) and (pop_dens <= 25.0):
        counter += 2.0
    elif (pop_dens > 25.0) and (pop_dens <= 250.0):
        counter += 3.0
    elif (pop_dens > 250.0) and (pop_dens <= 1000.0):
        counter += 4.0
    elif (pop_dens > 1000.0):
        counter += 5.0
    print(counter)
    print('\n')

    pub_transport = input("What percent of the population relies on public transportation as their primary form of transportation? ")
    #public_transportation = int(public_transportation)
    pub_transport = float(pub_transport)
    if (pub_transport > 0.0) and (pub_transport <= 10.0):
        counter += 0.5
    elif (pub_transport > 10.0) and (pub_transport <= 20.0):
        counter += 1.0
    elif (pub_transport > 20.0) and (pub_transport <= 25.0):
        counter += 2.0
    elif (pub_transport > 25.0) and (pub_transport <= 30.0):
        counter += 3.0
    elif (pub_transport > 30.0) and (pub_transport <= 40.0):
        counter += 4.0
    elif (pub_transport > 40.0):
        counter += 5.0
    print(counter)
    print('\n')

    major_highways = input("Is your city within close proximity of any major highways, interstates, or freeways? ")
    if major_highways.lower().strip() == 'yes':
        counter+= 5.0
    print(counter)
    print('\n')

    political_affiliation = input("Has your state voted Republican or Democratic for the past four elections? ")
    if political_affiliation.lower().strip() == 'republican':
        counter += 1.0
    print(counter)
    print('\n')

    pov_rates = input("Please enter the poverty rates of your city as a percentage. \n")
    pov_rates = float(pov_rates)
    if (pov_rates > 0.0) and (pov_rates <= 10.0):
        counter += 0.5
    elif (pov_rates > 10.0) and (pov_rates <= 20.0):
        counter += 1.0
    elif (pov_rates > 20.0) and (pov_rates <= 25.0):
        counter += 2.0
    elif (pov_rates > 25.0) and (pov_rates <= 30.0):
        counter += 3.0
    elif (pov_rates > 30.0) and (pov_rates <= 40.0):
        counter += 4.0
    elif (pov_rates > 40.0):
        counter += 5.0

    hotspot_potential = (counter / 30.0) * 100.0
    print('Potential for COVID-19 Hotspot: ' + str(hotspot_potential) + '%\n')

def devastating_impacts():
    counter = 0.0
    resp_illness = input("Does your city have a large population of people with respiratory illnesses. ")
    if resp_illness.lower().strip() == 'yes':
        counter += 5.0
    print(counter)
    print('\n')

    elder_population = input("What percentage of your population is above the age of 65? ")
    elder_population = float(elder_population)
    if (elder_population >= 0.0) and (elder_population < 10.0):
        counter += 1.0
    elif (elder_population >= 10.0) and (elder_population < 15.0):
        counter += 2.0
    elif (elder_population >= 15.0) and (elder_population < 20.0):
        counter += 3.0
    elif (elder_population >= 20.0) and (elder_population < 25.0):
        counter += 4.0
    elif (elder_population >= 25.0):
        counter += 5.0
    print(counter)
    print('\n')
    devastation_potential = (counter / 10.0) * 100.0
    print('Given the vulnerability of people with respiratory illenesses and those over the age of 65,\nthe risk for a higher mortality rate in your city is: ' + str(devastation_potential) + '%\n')

covid_impacts()
devastating_impacts()
