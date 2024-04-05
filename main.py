#this program is named CraFinder for a company named AutoCountry.
#the program enables users to navigate through the menu options.

def CarFinder():

  print("AutoCountry")

 #recall the fuction  
CarFinder()

# display the list of cars 
AllowedVehiclesList= [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

#start your loop 
while True:
   print()
   print("*******************************")

   print("AutoCountry Vehicle Finder v0.1")
   print("*******************************")
# declare/assign your variables choice-num1, choice-num2, choice-num3.
   choice_num1=("1. PRINT all Authorized Vehicles") 
   
   choice_num2=("2. SEARCH for Authorized Vehicle")
   
   choice_num3=("3. Exit")
   

  #allow the user to choose/inter a number from the menue after the menu loads.  
   user_input=input("Please Enter the following number below from the following menu:" 
 +"                                "+ "    "+
   choice_num1 + "     " + choice_num2+ "  "+ "     "+ "       "+ choice_num3 + "      "+  "             ")
  #declare the variable nameVehich and enable the user to input the name of the vehicle.
   nameVehich=input("Please Enter the full Vehicle name:")

  
# start your if statement to direct the user to the correct path after the user chooses a number from the menu.

#note must indent the codes below the while loop.
  

   if user_input == "2" and nameVehich=="Ford F-150":
     
      print()
     
      print("Ford F-150 is an authorized vehicle")
     
   print()

   if user_input == "2" and nameVehich=="Tesla":
     print()
    
     print("Tesla is not an authorized vehicle, if you received this in error please check the spelling and try again")

#initilize continue statement to end the current iteration and start from the top of the program.
  
   continue