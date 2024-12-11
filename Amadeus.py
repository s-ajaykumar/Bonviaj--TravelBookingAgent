from amadeus import Client, ResponseError

amadeus = Client(
    client_id = "OUWCIfM9fgIAF8h43Gd5FCogZ2Xd5Nht",
    client_secret = "dCcFWliLTZPae6du"
)

def direct_flight(cheapest_flight):
    origin = cheapest_flight['itineraries'][0]['segments'][0]['departure']['iataCode']
    destination = cheapest_flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
    departureDateTime = cheapest_flight['itineraries'][0]['segments'][0]['departure']['at']
    arrivalDateTime = cheapest_flight['itineraries'][0]['segments'][0]['arrival']['at']
    flightNameCode = cheapest_flight['itineraries'][0]['segments'][0]['carrierCode']
    duration = cheapest_flight['itineraries'][0]['segments'][0]['duration']
    fare = cheapest_flight['price']['total']
    numberOfBookableSeats = cheapest_flight['numberOfBookableSeats']
    print(f"""flightNameCode: {flightNameCode}\norigin: {origin}\nduration: {duration[2:]}
destination: {destination}\ndepartureDateTime: {departureDateTime}\narrivalDateTime: {arrivalDateTime}
numberOfBookableSeats: {numberOfBookableSeats}\nfare: {fare}""")
                  
def StopsInBetween(cheapest_flight):
        segments = cheapest_flight['itineraries'][0]['segments']
        connecting_flight = 0
        for j in segments:
            if connecting_flight > 0:
                print(f"Connecting Flight {connecting_flight}")
            else:
                print("Origin Flight")
            print("-----------------------")
            connecting_flight += 1
            origin = j['departure']['iataCode']
            destination = j['arrival']['iataCode']
            departureDateTime = j['departure']['at']
            arrivalDateTime = j['arrival']['at']
            flightNameCode = j['carrierCode']
            duration = j['duration']
            print(f"""flightNameCode: {flightNameCode}\nduration: {duration[2:]}\norigin: {origin}
destination: {destination}\ndepartureDateTime: {departureDateTime}
arrivalDateTime: {arrivalDateTime}\n""")
        numberOfBookableSeats = cheapest_flight['numberOfBookableSeats']
        fare = cheapest_flight['price']['total']
        print(f"numberOfBookableSeats: {numberOfBookableSeats}\nTotal Fare: {fare}\n")
        
def get_cheapest_flights(response):
    option = 1
    for cheapest_flight in response.data:
        print("--------------------------------------")
        print(f"option {option}")
        print("--------------------------------------")
        option += 1
        if len(cheapest_flight['itineraries'][0]['segments']) == 1: 
            direct_flight(cheapest_flight)
        else:
            StopsInBetween(cheapest_flight)
        
try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode = 'LAS',
        destinationLocationCode = 'LAX',
        departureDate = '2024-12-30',
        adults = 1,
        children = 0,
        currencyCode = "INR",
        travelClass = "ECONOMY"
    )
    if len(response.data) == 0:
        print("No available flights")
    else:
        get_cheapest_flights(response)
except ResponseError as error:
        print(error)


'''def StopsInBetween(response):
    print(response.data)
    print("--------------------------------------------------------")
    print(f"Number of flights available: {len(response.data)}")
    print("--------------------------------------------------------")
    Option = 1
    for i in response.data:
        print(f"Option {Option}")
        print("--------------------------------------------------------")
        Option += 1
        segments = i['itineraries'][0]['segments']
        connecting_flight = 0
        for j in segments:
            if connecting_flight > 0:
                print(f"Connecting Flight {connecting_flight}")
            else:
                print("Origin Flight")
            print("-----------------------")
            connecting_flight += 1
            origin = j['departure']['iataCode']
            destination = j['arrival']['iataCode']
            departureDateTime = j['departure']['at']
            arrivalDateTime = j['arrival']['at']
            flightNameCode = j['carrierCode']
            duration = j['duration']
            print(f"flightNameCode: {flightNameCode}\n")
            print(f"duration: {duration[2:]}\n")
            print(f"origin: {origin}\n")
            print(f"destination: {destination}\n")
            print(f"departureDateTime: {departureDateTime}\n")
            print(f"arrivalDateTime: {arrivalDateTime}\n")
            
        numberOfBookableSeats = i['numberOfBookableSeats']
        fare = i['price']['total']
        print(f"numberOfBookableSeats: {numberOfBookableSeats}\n")
        print(f"Total Fare: {fare}\n")
        print("---------------------------------------------------")'''
        
'''try:   
    body = {
    "originDestinations": [
        {
            "id" : "1",
            "originLocationCode" : "IXM",
            "departureLocationCode" : "MAA",
            "departureDateTime" : {
                "date" : "2024-12-09"
            }
        }
    ],
    "travelers" : [
        {
            "id" : "1",
            "travelerType" : "ADULT"
        }
    ],
    "sources" : [
        "GDS"
    ]
    }  
    response = amadeus.shopping.availability.flight_availabilities.post(body)
    print(response.data)
except ResponseError as error:
    raise error'''