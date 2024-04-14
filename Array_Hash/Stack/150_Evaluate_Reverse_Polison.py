
from typing import List 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize an empty stack
        stack = []

        # Now loop through the tokens
        for token in tokens:
            # Check if the token is a digit
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.append(int(token))
            else:
                # Pop the last two operands from the stack
                operand2 = stack.pop()
                operand1 = stack.pop()

                # Perform the operation
                result = self.doMath(token, operand1, operand2)

                # Push the result back to the stack
                stack.append(result)

        # Finally, return the result popped from the stack if the stack is not empty
        return stack.pop() if stack else 0

    # Helper function for the math calculations
    def doMath(self, operator, operand1, operand2):
        # Check the operator and perform the corresponding operation
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            # Division rounding towards zero
            return int(operand1 / operand2)
        
        
# Example RPN expression: ["2", "1", "+", "3", "*"]
example_tokens = ["2", "1", "+", "3", "*"]

# Create an instance of the Solution class
solution = Solution()

# Call the evalRPN method with the example tokens
result = solution.evalRPN(example_tokens)

# Print the result
print("Result:", result)
