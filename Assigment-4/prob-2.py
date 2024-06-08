def calculate_final_price(original_price):
    # Check if the original price is a negative number
    if original_price < 0:
        print("Invalid input, the price must be a non-negative number.")
    # Apply a 10% discount if the price is greater than $20
    elif original_price > 20:
        final_price = original_price * 0.9  # Applying 10% discount
        final_price
    #elif original_price == 20:
        #print("No Discount applied")
        #print("The final price of the item is:20")
    else:  
        print("No Discount applied")  
        # No discount applied if price is $20 or less
        original_price

# Prompt the user to input the original price of the item
original_price = float(input("Enter the original price of the item: "))

# Calculate the final price of the item
final_price = calculate_final_price(original_price)

if final_price is not None:
    # Print the result in a formatted string
    print(f"The final price of the item is: {final_price}")