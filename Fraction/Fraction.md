# Rational number 

  A rational number is a number of the fraction form a/b where a and b are both integers and b is different from zero.


# Fraction class 
  
  Class constructor which creates a rational fraction type object, being initialized with two integer variables.
  
### Initialization <h3>
  
  The object is initialized with two integer variables, which will represent the value of the numerator and denominator of the fraction, respectively.
  During the initialization of the object, two of the class methods are applied: verifyType(), which verifies if both values are integer type; and
  verifyNullDen(), which verifies if the denominator is equal to zero or null. In both cases, if the conjecture is true, the program will raise an
  exception.
  
## Methods <h2>
  
  * add(*object*)
  > Addition method. It adds up the object with the parameter object. It executes the lcm method to equal the denominators, then adds up the numerators,
  > and then simplifies using the simplify method.
  
  * divide(*object*)
  > Division method. It divides the object by the parameter object. When you divide fractions, you cross multiply the terms: the numerator of the object 
  > is multiplied by the denominator of the parameter object and the denominator of the object is multiplied by the numerator of the parameter object. 
  > And then the result is simplified using the simplify method.
  
  * equality(*object*)
  > Comparison method between the object and the parameter object. It uses the lcm method to equal the denominators so the numerators are comparable. If
  > the numerators are equal then the method returns True. If they're different, it returns False.
  
  * increase()
  > Increment method. It adds up 1 to the object. By adding 1, it adds up to the object a fraction which both numerator and denominator are equal to the       > its denominator. Then it is used the simplify method.
  
  * lcm(*object*)
  > Method used to equal the object's denominator to the parameter object's denominator, so the fractions will become comparable.
  
  * multiply(*object*)
  > Multiplication method between the object and the parameter object. Numerators are multiplied one by the other and denominators are multiplied one
  > by the other. Then it is used the simplify method.
  
  * printFraction()
  > Print method. Prints on the screen the fraction that represents the object.
  
  * simplify()
  > Simplify fraction method. Calculates the divisors list of both numerator and denominator and compares them until it finds the highest value in common.
  > Then it divides both numerator and denominator by this number.
  
  * subtract(*object*)
  > Subtraction method. Subtracts the parameter object from the object. It uses the lcm method to equal the denominators and then subtracts from the
  > numerator the value of the parameter object's numerator. Then it uses the simplify method.
  
  * verifyNullDen()
  > Method to verify if the denominator of the object is zero or null. Raises an exception if the conjecture is true.
  
  *verifyType()
  > Method to verify if the numerator and the denominator are integer values. Raises an exception if at least one of them is not.
