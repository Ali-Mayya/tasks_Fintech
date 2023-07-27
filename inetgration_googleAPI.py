import requests

def get_geocode(address, api_key):
    # URL for the Google Maps API request
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Check if the API returned geocoding results
        if data['status'] == 'OK':
            # Extract coordinates from the API response
            location = data['results'][0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']

            print(f'Latitude: {latitude}, Longitude: {longitude}')
        else:
            print('Geocoding error:', data['status'])
    else:
        print('Error in API request:', response.status_code)

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your own Google Maps API key
    api_key = 'AIzaSyBrarqLgaofy3crNi9GHSIccI4QdZizHIE'

    address = 'Red Square, Moscow, Russia'

    # Call the function to get the geocode for the given address
    get_geocode(address, api_key)










