"""
    Creational :
        Prototype
"""

class Cinema:
    pass


class Movie:
    pass


class Time:
    pass


class Hall:
    def __init__(self, name, cinema, capacity):
        self.name = name
        self.cinema = cinema
        self.capacity = capacity


class Seat:
    def __init__(self, number):
        self.number = number
        self.status = None
        self.customer = None


class Sens:
    def __init__(self, cinema, movie, time, hall):
        self.cinema = cinema
        self.movie = movie
        self.time = time
        self.hall = hall
        self.seats = list()
        self.prototype_seats()

    def prototype_seats(self):
        """Prototype all seat of selected hall"""
        for item in range(self.hall.capacity):
            self.seats.append(Seat(item))


if __name__ == '__main__':
    cinema_instance = Cinema()
    movie_instance = Movie()
    time_instance = Time()
    hall_instance = Hall('hall name', cinema_instance, 60)
    sens = Sens(cinema_instance, movie_instance, time_instance, hall_instance)
    print(len(sens.seats))
    print(type(sens.seats[0]))
