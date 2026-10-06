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

##### Mistake Three, Part 1
The fatal Hubris & Issue: At first, I didn't think I did anything wrong- I finished up the trajectory reconstruction layer, thought I did everything right, until it appeared like a cycloid. I then knew that one of two things was wrong: I had made an error in my reconstruction, or I had made an error in data generation. So, I dove into the first, as that'd be the simplest fix: I double-checked my recursive calculations, fixed a few numbers, and than ran it, only for it to now wander in a line downwards, like a flatter cycloid rolling down a hill

The Punishment: I dug through the data generation layer, trying to find what my issue was, and I found multiple things, when I walked through the entire layer. Number one, I was writing the true, world equations, not the actual equations for the body frame- and passing the world equations through the filter that was meant to filter them into the world frame, so I had to work through how I needed to change it- changing the accel_x to 0 as you're moving at a constant forward speed, so there's no acceleration. In addition, I made a minor error on the y-accel, and fixed it.

##### Mistake Three, Part 2
Thinking everything was fine, I ran it again. And it didn't go in an odd cycloid or bump! instead, it starts to go around, then it wanders down a dark forest in which it doesn't return. Now comes my punishment, finding what I missed when building it and trying to add it to every layer instead of building it right the first time, which I try to do.

The Punishment: I looked through the reason why it was wandering off, and then I realized something: I had merely been adding the previous gyroscope equation to itself, and that did nothing to stop the drift, which caused itself to wander down a dark forest in which it did not return from. Therefore, the main punishment was building a magnetometer to have something to anchor the drift to, adjusting the filter so it'd work, and than adding it to both the filter layer and the trajectory reconstruction layer. Furthermore, I also needed to anchor the magnometer and alter several of the equations to get a more accurate circle.

