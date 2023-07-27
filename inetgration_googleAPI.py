import requests

def get_geocode(address, api_key):
    # URL для запроса к Google Maps API
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'

    # Отправляем GET-запрос к API
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        data = response.json()

        # Проверяем, что API вернул результаты геокодирования
        if data['status'] == 'OK':
            # Получаем координаты из ответа API
            location = data['results'][0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']

            print(f'Широта: {latitude}, Долгота: {longitude}')
        else:
            print('Ошибка геокодирования:', data['status'])
    else:
        print('Ошибка при запросе к API:', response.status_code)

if __name__ == "__main__":
    # Замените 'YOUR_API_KEY' на свой ключ API Google Maps
    api_key = 'AIzaSyBrarqLgaofy3crNi9GHSIccI4QdZizHIE'

    address = '1600 Amphitheatre Parkway, Mountain View, CA'


    get_geocode(address, api_key)
