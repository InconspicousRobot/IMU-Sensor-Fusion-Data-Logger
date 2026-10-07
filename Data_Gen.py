# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
rng=np.random.default_rng()

# %%
time=np.arange(0,15.0,0.01)
radius=2
angular_velocity=.5
dt=np.diff(time,prepend=0)

# %%
position_x=radius*np.cos(angular_velocity*time)
position_y=radius*np.sin(angular_velocity*time)
vel_x=(-1)*radius*(angular_velocity)*np.sin(angular_velocity*time)
vel_y=radius*(angular_velocity)*np.cos(angular_velocity*time)
#For the world, not the body frame, accel_x=(-1)*radius*(angular_velocity**2)*np.cos(angular_velocity*time)
accel_x=np.zeros(len(time))
#acceleration is constant, not jittering
accel_y=np.full(len(time),radius*(angular_velocity**2))
accel_z=np.full(len(time),9.81)

#Angle of the robot
heading=np.unwrap(np.arctan2(vel_y,vel_x))

#Gyroscopes measure the rate of change of the angle the robot is pointing at over time.
#gyro_x is "Roll", gyro_y is "Pitch", and gyro_z is "Yaw"
gyro_x=np.zeros(len(time))
gyro_y=np.zeros(len(time))
#Note- This is where mistake one was made. If you use the dt here, it will start spouting NaN figures and completely disrupt the gyro_z
gyro_z=np.gradient(heading,time)

#Gyro bias
gyro_bias= np.cumsum(np.random.normal(loc=0.0, scale=0.0001, size=len(time)))
biased_gyro_z=gyro_z+gyro_bias

#accelerometer bias. No Z-bias because it's not moving
accel_bias_x= np.random.normal(loc=0.0, scale=0.05, size=len(time))
accel_bias_y= np.random.normal(loc=0.0, scale=0.05, size=len(time))
accel_x=accel_bias_x+accel_x
accel_y=accel_bias_y+accel_y

mag=np.full(len(time),heading)
noise_std=0.05
mag_bias=np.random.normal(loc=0.0,scale=noise_std,size=len(time))
mag_yaw=mag+mag_bias
# %%
df=pd.DataFrame({'timestamp': time,
                 'dt': dt,
                 "True Position X": position_x,
                 'True Position Y': position_y,
                 'accel_x':accel_x,
                 'accel_y':accel_y,
                 'accel_z':accel_z,
                 'Heading':heading,
                 'gyro_x':gyro_x,
                 'gyro_y':gyro_y,
                 'gyro_z':gyro_z,
                 'biased_gyro_z':biased_gyro_z,
                 'mag_yaw':mag_yaw})


# %%
#def get_accelx():
#    plt.plot(time,biased_accel_x,label="Biased Accel X",color='red')
#    plt.plot(time,accel_x, label='Accel X', color='blue')
#    plt.legend()
#    plt.show()

# %%
#def get_accely():
#    plt.plot(time,biased_accel_y,label='Biased Accel Y',color='red')
#    plt.plot(time,accel_y,label="Accel Y",color='blue')
#    plt.legend()
#    plt.show()

# %%

def get_gyro():
    plt.plot(time,biased_gyro_z, label='Gyroscope Z with drift',color='red')
    plt.plot(time,gyro_z, label='Gyroscope Z',color='blue')
    plt.legend()
    plt.show()


