# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.

from typing import List, Dict

def calculate_average_order_value(orders: List[Dict]) -> float:
    """
    Calculate the average order value (AOV) for non-cancelled orders.

    Args:
        orders (List[Dict]): A list of orders, each with keys:
            - "status" (str): e.g., "completed", "cancelled"
            - "amount" (float or int): monetary value of the order

    Returns:
        float: Average order value of non-cancelled orders.
               Returns 0.0 if no valid orders exist.
    """
    total = 0.0
    valid_count = 0

    for order in orders:
        # Defensive programming: ensure keys exist and amount is numeric
        if order.get("status") != "cancelled" and isinstance(order.get("amount"), (int, float)):
            total += order["amount"]
            valid_count += 1

    return total / valid_count if valid_count > 0 else 0.0

