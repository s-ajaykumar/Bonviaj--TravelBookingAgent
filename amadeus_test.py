import json
import boto3
from botocore.exceptions import ClientError
from amadeus import Client, ResponseError
import config
amadeus = Client(
    client_id = "OUWCIfM9fgIAF8h43Gd5FCogZ2Xd5Nht",
    client_secret = "dCcFWliLTZPae6du"
)
prompt_client = boto3.client("bedrock-runtime", region_name = "us-east-1", aws_access_key_id = config.ACCESS_KEY, aws_secret_access_key = config.SECRET_KEY)

def lambda_handler(event):
    #modelResponse = event.get('node').get('inputs')[0].get('value')

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
        #json_output = json.loads(modelResponse)
        json_output = json.loads(event)
        print(type(json_output))
        originLocationCode = json_output["origin"],
        destinationLocationCode = json_output["destination"],
        departureDate = json_output["departureDate"],
        adults = json_output["adults"],
        children = json_output["children"],
        currencyCode = "INR",
        travelClass = json_output["travelClass"]

        print(originLocationCode)
        
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode = "IXM",
            destinationLocationCode = "MAA",
            departureDate = "2024-12-20",
            adults = 1,
            children = 1,
            currencyCode = "INR",
            travelClass = "FIRST"
        )
        if len(response.data) == 0:
            print("No available flights from the given locations on the given date.")
            return "No available flights from the given locations on the given date."
        else:
            get_cheapest_flights(response)
            print(f"Amadeus Response: {response.data}")
            return response.data

    except ResponseError as error:
        print(f"Amadeus error: {error}")
        
lambda_handler(
json.dumps({"origin": "IXM",
"destination": "MAA",
"departureDate": "2023-12-30",
"adults": 1,
"children": 1,
"currencyCode": "INR",
"travelClass": "FIRST"}))
    
    
