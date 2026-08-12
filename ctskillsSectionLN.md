## **Main problem** - Vending machine is unreliable and inconsistent.

**Sub Problem 1** - Sometimes the machine does not give the correct change when it is given newer currency.

-*The CT skill we can use in this Sub Problem is Pattern Recognition, for example, the machine does not give correct change only when its given new currency, so we can make sure to register new currency immediately after it is changed.*

**Sub Problem 2** - Items run out, but the machine doesn’t notify anyone.

-*The CT skill we can use in this Sub Problem is Abstraction. For example, we ignore the big problem and only focus on the fact that the machine has trouble with notifying about its inventory.*

**Sub Problem 3** - Students press the wrong buttons and get the wrong item.

-*The CT skill we can use in this Sub Problem is Algorithm Design. We can improve the design used to select different items and add a confirmation step.*

**Sub Problem 4** - The machine is slow when multiple students use it in succession.

-*The CT skill we can use in this Sub Problem is Decomposition. We can decompose the problem into little parts and optimize each part to make the whole thing faster.*

## **Pseudocode**
**Sub Problem 3

START

Display options(numbers)

User selects a number

Display: You selected Item [number]. Confirm? Y/N

If answer = Y, give item.

Else
Return to Display options

END

