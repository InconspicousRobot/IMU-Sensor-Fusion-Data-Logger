## Day 1

Derived the base mathematics for the accelerometer, gyroscope, and true position, as well as the heading. Completed 90% of Data Generation module, forgot to commit it. Didn't forget to commit the two mistakes I made on it.

## Day 2

Committed it after finishing it off, beginning complementary filter layer. Began the recursive math for the angle calculator based off of linear interpolation, and finished it.

## Day 3
Finished Complimentary filter layer, added a lesson learned in the mistakes #2 due to an error with the yaw. In addition, not a mistake, but I realized I needed to use a for loop as this is iterative and can't be done otherwise- however, I learned about the @njit decorator specifically to bypass the limitations of slow native python code- as since the state of i directly depended on i-1 for the calculations and filtering, I needed to use for loops and I couldn't vectorize it. 

## Day 4 (late entry)
Finished trajectory reconstruction, realized I had an error (Mistakes 3, part 1 and 2.), and added in the magnetometer, and fixed an error where the actual biased accelerometers weren't working. (It still outputed the same filtered trajectory, however.) Also altered the error in Data_Gen, as I needed to change the accel_x and accel_y, as they were measuring the world acceleration, not the actual frame acceleration.
