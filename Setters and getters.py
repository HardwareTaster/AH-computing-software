
class ticket:


    def __init__(self):
        self.movie_name = ""
        self.date = "01/01/2021"
        self.time = "12.00"
        self.sceen_no = 1
        self.seat_no = "A1"

    def setTicket(self, thisMovieName, thisdate): #setter
        self.movie_name = thisMovieName
        self.date = thisdate
    def getTicket(self):    #getter
        return self.movie_name, self.date


bookings = [ticket() for i in range (5)]

bookings[0].setTicket ("grokdessey" , "2024")


print (bookings[0].getTicket())
