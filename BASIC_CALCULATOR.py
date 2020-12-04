import time
		

print("Welcome to the simple calculation")
time.sleep(1)

print("additon -- 1")
print("subration -- 2")
print("multiply -- 3")
print("division -- 4")
time.sleep(2)

def main():

        Selection = input("Select any number for your calculation:")

        number_1 = int(input("Enter First number:"))
        number_2 = int(input("Enter Second number:"))


        if Selection == '1':
                print("Addition of your two number is ",number_1+number_2)

        elif Selection == '2':
                print("subration of your two number is ",number_1-number_2)

        elif Selection == '3':
                print("Multiply of your two number is ",number_1*number_2)
                
        elif Selection == '4':
                print("division of your two number is ",number_1/number_2)
         
        recalculation = input("Do You want to calculate Again ??? (yes/no) ").lower()
        if recalculation == "yes":
        	main()
        else:
        	print("bye")
        	exit()
        	time.sleep(5)
main()			
