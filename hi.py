class Customers:
    greeting = "Welcome to the coffee Palace!"
    def __init__(self, name, beverage, Food, Total):
        self.name = name
        self.beverage = beverage
        self.Food = Food
        self.Total = Total

customer01 = Customers("Nate", "Espresso", "Pastrami on rye", 220)
customer02 = Customers("Elaine", "Straberry frappuccino", "Tuna wrap", 270)
customer03 = Customers("Samirah", "Iced caffe latte", "Cinnamon roll", 225)
customer04 = Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
customer05 = Customers("Paz", "Iced tea", "Blueberry pancakes", 315)

def get_sum(x,y):
    return (x + y)