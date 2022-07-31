# url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"
import requests

class Observer():
    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, observable, *args, **kwargs):
        print('Got', args, kwargs, 'From', observable)
        return ('Got', args, kwargs, 'From', observable)

class Observable():
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for i in self._observers:
            i.notify(self, *args, **kwargs)

    def unsubscribe(self, observer):
        self._observers.remove(observer)


class Weather():

    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude
        temperature = None

    def __str__(self):
        return f'latitude: {self.latitude}, longitude: {self.longitude}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.latitude}, {self.longitude})'

    @property
    def latitude(self):
        return self._latitude
    
    @property
    def longitude(self):
        return self._longitude

    @latitude.setter
    def latitude(self, other):
        self._latitude = other
    
    @longitude.setter
    def longitude(self, other):
        self._longitude = other

    def get_data(self):
        response = requests.get(
            'https://api.open-meteo.com/v1/forecast',
            params={'latitude': self.latitude, 'longitude': self.longitude, 'hourly': 'temperature_2m'},
        )
        if response.status_code == 200:
            res = response.json()
            time, temp, unit = res['hourly']['time'][0], res['hourly']['temperature_2m'][0], res['hourly_units']['temperature_2m']
            return [time, temp, unit]


weather = Weather('52.52', '13.41')

data = weather.get_data()

data_object = {'time': data[0], 'temp': data[1], 'unit': data[2]}

subject = Observable()

observer1 = Observer(subject)
observer2 = Observer(subject)

subject.notify_observers(data_object)
subject.unsubscribe(observer2)

subject.notify_observers(data_object)
