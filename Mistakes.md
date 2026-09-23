# Mistakes Made

### Where my caffeine-fueled hubris collided violently with reality.

##### Mistake One
The fatal Hubris & Issue: When I had finished doing the math derivations and had built out the initial dataframe, I felt like nothing could stop me. of course, when my gyro_z calculations had ballooned to 5.000000e-01, NaN, NaN -7.205759e+15, and then NaN forevermore, I was proven that it would not be an easy ride.

The Punishment: I spent 15 minutes afterwards researching np.wrap, how np.gradient calculates the actual result, and then realized that the issue was the dt- which was identical at every value except for the first due to the very humble prepend=0 I added on to it to keep track of the timestep. the whole (np.gradient(heading,dt)) function caused a division by zero error that caused it to go to nowhere and below.

Lesson learned: np.gradient can calculate the difference on its own, just use your time array directly. Remember KISS: Keep it simply, stupid, no need to already do the difference when np.gradient can calculate the difference.


##### Mistake Two

The fatal Hubris & Issue: when I derived the kinematics equation and the equation for the tilt of each of the sensors, I foolishly presumed that, I could do the same for the yaw (Z-accel drift) by using the same formula (arctan2), which caused it to start at -.06, and then diverge all the way to -1.89. I presumed that negative radians were not exactly the outcome I wanted, and I went to work.

The Punishment: I had to spend a bit of time researching about 2d circular motions, and I learned that, since it was a 2D circular motion, and it was trying to measure against noise rather then the earth (which is what the pitch and roll were measuring against, as both contained accel_z) it was just measuring against its own noise, which caused it to break.

Lesson learned: Yaw, in a 2d circular motion, doesn't derive against anything- you simply add the previous to the gyro_z times the timestep, as the gyro_z is flat (9.81) and it accumulates over the timesteps.
