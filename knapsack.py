# Class representing an item with a value and weight
class Item:
    def __init__(self, value, weight):
        self.value = value  # The value of the item
        self.weight = weight  # The weight of the item

# Class to solve the fractional knapsack problem
class Solution:
    def fractionalKnapsack(self, W, arr, n):
        """
        Function to calculate the maximum total value in the knapsack
        for the given capacity W using the fractional knapsack approach.

        Parameters:
        W : int - Capacity of the knapsack
        arr : list - List of Item objects
        n : int - Number of items

        Returns:
        float - The maximum value that can be achieved
        """
        # Sort items based on their value-to-weight ratio in descending order
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)

        curWeight = 0  # Tracks the current weight in the knapsack
        finalvalue = 0.0  # Tracks the total value of items in the knapsack

        # Loop through all items
        for i in range(n):
            # If the current item's weight fits completely in the knapsack
            if curWeight + arr[i].weight <= W:
                curWeight += arr[i].weight  # Add the item's weight to the knapsack
                finalvalue += arr[i].value  # Add the item's full value
            else:
                # If the current item can't fit fully, take the fractional value
                remain = W - curWeight  # Remaining capacity in the knapsack
                finalvalue += (arr[i].value / arr[i].weight) * remain  # Add fraction of the item's value
                break  # No further items can be added once the knapsack is full

        return finalvalue  # Return the maximum total value

# Driver code to test the solution
if __name__ == '__main__':
    n = 3  # Number of items
    W = 50  # Capacity of the knapsack

    # List of items (value, weight)
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]

    # Create an object of the Solution class
    obj = Solution()

    # Call the fractionalKnapsack method
    ans = obj.fractionalKnapsack(W, arr, n)

    # Print the result
    print("The maximum value is", ans)
