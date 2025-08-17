def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
    
    Returns:
        float: The final price after discount (if 20% or higher), 
               otherwise the original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


def main():
    try:
        original_price = float(input("Enter the original price of the item: $"))
        discount_percentage = float(input("Enter the discount percentage: "))
        
        final_price = calculate_discount(original_price, discount_percentage)
        
        if discount_percentage >= 20:
            savings = original_price - final_price
            print(f"\nDiscount applied!")
            print(f"Original price: ${original_price:.2f}")
            print(f"Discount: {discount_percentage}%")
            print(f"You save: ${savings:.2f}")
            print(f"Final price: ${final_price:.2f}")
        else:
            print(f"\nNo discount applied (discount must be 20% or higher)")
            print(f"Price remains: ${final_price:.2f}")
    
    except ValueError:
        print("Please enter valid numeric values for price and discount percentage.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()