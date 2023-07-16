# sub problem 1
def get_farmers_information():
  farmersName = input("Please enter your name: ")
  categoryOfFarms = ["Rice Farming", "Poultry farming", "Cattle Keeping"]

def show_demonstration_farms():
  demonstrationFarms = [["rice farm 1", "rice farm 2"], ["poultry farm1", "poultry farm 2"], ["Cattle farm 1","Cattle farm 2"]]
  farmersChoice = int(input("What type of farm do you have? (1 for Rice Farming, 2 for Poultry Farming or 3 for Cattle Keeping): "))
  print(demonstrationFarms[farmersChoice - 1])

# sub problem 2
def get_farmers_crop_information():
  cropsList = ["Rice", "Maize", "Coffee"]

def show_best_harvesting_methods():
  farmersChoice = int(input("What crop do you harvest? (1 for Rice, 2 for Maize, 3 for Coffee): "))
  cropHarvest = [["Harvesting method for rice"], ["Harvesting method for Maize"], ["Harvesting method for Coffee"]]
  print(cropHarvest[farmersChoice - 1])

# sub problem 3
def get_farmers_budget_information():
  farmersBudget = input("Enter your monthly budget: ")
  farmersExpenses = input("Enter your monthly expenses: ")

def show_best_practices():
  best_practices = ["best practice 1", "best practice 2", "best practice 3"]
  print(best_practices)

if __name__ == "__main__":
  print("Sub Problem 1")
  get_farmers_information()
  show_demonstration_farms()
  print("Sub Problem 2")
  get_farmers_crop_information()
  show_best_harvesting_methods()
  print("Sub Problem 3")
  get_farmers_budget_information()
  show_best_practices()
