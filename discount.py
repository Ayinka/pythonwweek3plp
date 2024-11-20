def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
        price (float): The original price.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount, or the original price if the discount is less than 12%.
    """
    # Check if the discount is 12% or higher
    if discount >= 12:
        # Apply the discount
        discount = original_price * (discount / 100)
        final_price = original_price - discount
        return final_price
    else:
        # Return the original price if the discount is less than 12%
        return price

# Example usage
original_price = float(input("Price of Goods: "))  # Convert input to float
discount = float(input("Discount Allowed: "))     # Convert input to float
final_price = calculate_discount(original_price, discount)

# Print results using f-strings
print(f"Original Price: ${original_price:.2f}")
print(f"Discount: {discount:.2f}%")
print(f"Final Price: ${final_price:.2f}")
