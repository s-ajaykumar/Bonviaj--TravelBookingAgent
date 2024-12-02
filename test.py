from amadeus import Client, ResponseError

amadeus = Client(
    client_id = "OUWCIfM9fgIAF8h43Gd5FCogZ2Xd5Nht",
    client_secret = "dCcFWliLTZPae6du"
)


'''def get_flight_details(origin, destination, departureDate):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocation = origin,
            destinationLocation = destination,
            departureDate = departureDate
        )
        return response.data
    except ResponseError as error:
        print(error)

output = get_flight_details('SEN', 'FLL', "2024-12-09")
print(output)'''

try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode = 'IXM',
        destinationLocationCode = 'MAA',
        departureDate = '2024-12-09',
        adults = 1,
        currency = "INR"
        
    )
    print(response.data)
    print(len(response.data))
except ResponseError as error:
        print(error)



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