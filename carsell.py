# Your class should be named `CarSell`.
# Your method should be named `getPromisingCustomers`
# Your method should return the indices of customers who are willing to pay greater than or equal to 90% of the car value
# Your class should be named `CarSell`.
# Your method should be named `getPromisingCustomers`
# Your method should return the indices of customers who are willing to pay greater than or equal to 90% of the car value
class CarSell:
    def __init__(self,proposals):
        self.proposals=proposals
    def getPromisingCustomers(self):
        goodpro=[]
        for i in range(len(self.proposals)):  
            if self.proposals[i]>=900000:
              goodpro.append(i)
        if len(goodpro)>0:
            return goodpro
        else:
            return [-1]    
if __name__ == "__main__":
    num_customers = int(input())
    customer_proposals = []
    for i in range(num_customers):
        customer_proposals.append(int(input()))
    car_sell = CarSell(customer_proposals)
    for j in car_sell.getPromisingCustomers():
        print(j)   