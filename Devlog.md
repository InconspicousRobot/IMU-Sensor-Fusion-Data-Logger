## Day 1

Derived the base mathematics for the accelerometer, gyroscope, and true position, as well as the heading. Completed 90% of Data Generation module, forgot to commit it. Didn't forget to commit the two mistakes I made on it.

## Day 2

Committed it after finishing it off, beginning complementary filter layer. Began the recursive math for the angle calculator based off of linear interpolation, and finished it.

## Day 3
Finished Complimentary filter layer, added a lesson learned in the mistakes #2 due to an error with the yaw. In addition, not a mistake, but I realized I needed to use a for loop as this is iterative and can't be done otherwise- however, I learned about the @njit (and the @jit, but I used the @njit specifically so I didn't have to worry about it jumping to python if there was an error, and I needed to debug a compilation issue- which happened.) decorator specifically to bypass the limitations of slow native python code. it still would've processed quickly, however, when scaled up to millions of iterations, without the @njit converting it to C, it would've taken several seconds- when it could run far quicker using the decorator. Getting started on the third layer, the trajectory reconstruction.
