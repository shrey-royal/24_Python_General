"""
# raise Exception
def calculateTotal(*prices: int):
    # print(prices, type(prices))
    for price in prices:
        if price < 1:
            raise ValueError("Price can't be negative.")
        
    return sum(prices)


if __name__ == "__main__":
    totalPrice = 0
    try:
        totalPrice = calculateTotal(1, 23, 12, 2134, 234, 23, 1, 1)
    except ValueError as e:
        print(e)

    print(f"Calculate Total: {totalPrice if totalPrice != 0 else "Error"}")
"""

# Custom Exception
class OverheatWarningException(Exception):
    def __init__(self, temperature, threshold) -> None:
        self.temperature = temperature
        self.threshold = threshold
        super().__init__(f"Warning: Temperature {self.temperature}°C exceeds the safe threshold of {self.threshold}°C.")

class TemperatureMonitor:
    def __init__(self, threshold=75) -> None:
        self.threshold = threshold

    def check_temperature(self, temperature):
        if temperature > self.threshold:
            raise OverheatWarningException(temperature, self.threshold)
        else:
            print(f"Temperature {temperature}°C is within the safe limit.")

if __name__ == "__main__":
    monitor = TemperatureMonitor(threshold=50)

    temps = [40, 42, 56, 20, 58]

    for temp in temps:
        try:
            monitor.check_temperature(temp)
        except OverheatWarningException as e:
            print(e)