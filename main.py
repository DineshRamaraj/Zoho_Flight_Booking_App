class Flight:
    uniqueId = 0
    def __init__(self):
        Flight.uniqueId += 1
        self.tickets = 50
        self.price = 5000
        self.id = Flight.uniqueId
        self.flightID = self.id
        passengerDetails = []
        passengerIDs = []
        bookedTicketsPerPassenger = []
        passengerCost = []
        
    def addPassengerDetails(self, passengerDetail,  numberOfTickets, passengerID):
        passengerDetails.append(passengerDetail)
        passengerIDs.append(passengerID)
        passengerCost.append(self.price, numberOfTickets)
        
        self.price += 200 * numberOfTickets
        self.tickets -= numberOfTickets
        
        
        bookedTicketsPerPassenger.append(numberOfTickets)
        print("Booked Successfully!")
        
    def cancelTicket(self, passengerID):
       indexToRemove = passengerIDs.index(passengerID)
       if(indexToRemove < 0):
           print("Passenger ID not found!")
           return
       
       ticketsToCancel = bookedTicketsPerPassenger[indexToRemove]
       
       self.tickets+=ticketsToCancel
       
       self.price-= 200 * ticketsToCancel
       
       print("Refund Amount after cancel : " , passengerCost[indexToRemove]);
       
       bookedTicketsPerPassenger.pop(indexToRemove)
       passengerIDs.remove(passengerID)
       passengerDetails.pop(indexToRemove)
       passengerCost.pop(indexToRemove)
       
       print("Cancelled Booked Tickets Successfully!")
       
       
       def flightSummary(self):
           print("Flight ID ", self.flightID, " --- ", "Remaining Tickets  ", self.tickets , "  ---  ", "Current Ticket Price ", self.price)
           
       def printDetails(self):
           print("Flight ID ", self.flightID, "-->")
           for i in self.passengerDetails:
               print(i)
            
            
def book(currentFlight,  tickets, passengerID):
       passengerDetail = "";
       
       passengerDetail = "Passenger ID " , passengerID ,  " -- " , " Number of Tickets Booked " , tickets , " -- " , "Total cost " , currentFlight.price * tickets
       currentFlight.addPassengerDetails(passengerDetail,tickets,passengerID)

       currentFlight.flightSummary()
       currentFlight.printDetails()

def cancel(currentFlight, passengerID):
        currentFlight.cancelTicket(passengerID)
        currentFlight.flightSummary()
        currentFlight.printDetails()
        
def print(f):
    f.printDetails()
    
def main():
        flights = []
        for i in range(2):
            flights.append(Flight())

        passengerID = 1

        
        while(True):
            print("1. Book 2. Cancel 3. Print")
            choice = int(input("Enter Your choice"))
        
            if choice == 1:
                    fid = int(input("Enter Flight ID"))
        
                    if fid > len(flights):
                        print("Invalid flight ID")
                        break
                    
                    currentFlight = null;
                    for f in flights:
                        if f.flightID == fid:
                            currentFlight = f
                            f.flightSummary()
                            break
                    
                    t = int(input("Enter number of tickets"))
        
                    if t > currentFlight.tickets:
                        print("Not Enough Tckets")
                        break
                    
                    book(currentFlight,t,passengerID)
        
                    passengerID = passengerID + 1
                    break
            
                
            elif choice == 2:
                fid = int(input("Enter flight ID: "))
    
                if fid > len(flights):
                    print("Invalid flight ID")
                    break
                
                currentFlight = null;
                for f in flights:
                    if f.flightID == fid:
                        currentFlight = f
                        break
                id = int(input("Passenger ID to cancel booking"))
                
                cancel(currentFlight,id)
                break
            
            elif choice == 3:
                for f in flights:
                    if len(f.passengerDetails) == 0:
                        println("No passenger Details for  - Flight " , f.flightID)
                    else:
                     print(f)
                     break
            else:
                break
