# Annex B: Smart Vending Machine
Section: 9-Arayat
C# and Name: #12 - Leonardo Palma
Date of checking: August 14, 2026

## Step 1: Identify the Main Problem:
Main problem: The vending machine at school is quite inefficient or unreliable in everyday use.

----------------------------------------------------------------------
## Step 2: Identify Sub-Problems.
Sub-Problem 1. Wrong amount of change given - The vending machine usually makes mistakes or wrong calculations in giving the exact amount of change needed for paid amount.

Sub-Problem 2. No tracking of item amount - The vending machine doesn't notify anyone if an item in it has run out which may cause inefficiency in product renewal speed.

Sub-Problem 3. Not accident friendly or straightforward instructions - Since the vending machine drops the immediate item you press which may cause problems because if the student accidentally presses a wrong drink or snack then their money would be wasted.

Sub-Problem 4. Speed of transactions in the vending machine - The vending machine takes very long or it takes a slow time to process the transactions made by students when used consecutively, such as recess breaks where students would want to line up to buy a snack.

----------------------------------------------------------------------
## Step 3: Define Computational Thinking Approaches
### Format Of Boxes:
### | Sub- Problem | CT skill | Solution |
| 1. Wrong amount of change given |  Algorithmic Thinking  | Code an automatic calculator that checks on how much money the student inputted into the vending machine whether if its not enough, exact, or excess, and calculate the exact amount of change by validating the amount of money put in by the student then the cost of the product they would decide to buy and subtract if its excess money. |

| 2. No tracking of item amount |  Pattern Recognition  | Code visual sensors on the position of each of the 1st product that if the visual sensors cant sense anything it will report real time to a small monitoring website/code to see what product needs to be stocked in real time. |

| 3. Not accident-friendly or straightforward instructions |  Abstraction  | We can implement an double check or confirmation feature that could show that this is the item you want to buy and to press again to surely buy it, If said person is in a rush they can just double tap the item to buy 1, it could give them more time to react if they pick the wrong product. |

| 4. Speed of transactions in the vending machine |  Decomposition  | We can implement general faster refresh rate while the product still falls from its place in the vending machine or we can increase money intake to scan and validate money transfer. |

------------------------------------------------------------------------
## Step 4: Draw a flowchart or write a pseudocode for the identified subproblem

### Sub-Problem: Wrong amount of change given. Pseudocode:
START

INPUT money\
INPUT selected_product\
GET product_price

IF money < product_price THEN\
    DISPLAY "Insufficient money"\
ELSE\
    change ← money - product_price\
    DISPENSE selected_product\
    GIVE change\
    DISPLAY "Transaction successful"\
END IF

END
