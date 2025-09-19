import math
from log import log_info, log_warning, log_error

def calculate_square_root(numbers: list) -> None:
    for number in numbers:
        try:
            if number < 0:
                log_warning(f"Negative number found: {number}. We're skipping it.")
                continue
            
            root = math.sqrt(number)
            log_info(f"Square root of {number} - {root:.2f}")

        except Exception as e:
            log_error(f"Error calculating the root for {number}: {e}")

if __name__ == "__main__":
    numbers = [22, 15, -43, 5, 72, 2234, 0, -57, "22"]
    calculate_square_root(numbers)
