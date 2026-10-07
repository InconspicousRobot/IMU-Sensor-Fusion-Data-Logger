# %%
import Data_Gen as dg
import numpy as np
import pandas as pd
from numba import njit
np.set_printoptions(suppress=True)

# %%
alpha=.98
@njit
def blending_trajectory(accel_x,accel_y,accel_z,gyro_x,gyro_y,gyro_z,mag_yaw,time,dt,alpha):
    roll=np.zeros(len(time))
    pitch=np.zeros(len(time))
    yaw=np.zeros(len(time))
    yaw_filter=0
    prev_roll=0
    prev_pitch=0
    prev_gyro=mag_yaw[0]
    for i in range(len(time)):
        roll_accel_tilt=np.arctan2(accel_y[i],accel_z[i])
        pitch_accel_tilt=np.arctan2(accel_x[i],accel_z[i])
        
        blend_roll_heading=(alpha*(prev_roll+(gyro_x[i]*dt[i]))+((1-alpha)*roll_accel_tilt))        
        blend_pitch_heading=(alpha*(prev_pitch+(gyro_y[i]*dt[i]))+((1-alpha)*pitch_accel_tilt))
        gyro_heading=prev_gyro+(gyro_z[i]*dt[i])
        yaw_filter=(alpha*gyro_heading)+((1-alpha)*mag_yaw[i])
        prev_roll=blend_roll_heading
        prev_pitch=blend_pitch_heading
        prev_gyro=yaw_filter

        roll[i]=blend_roll_heading
        pitch[i]=blend_pitch_heading
        yaw[i]=yaw_filter

    return roll,pitch,yaw

roll_filtered, pitch_filtered, yaw_filtered = blending_trajectory(
    dg.accel_x,
    dg.accel_y,
    dg.accel_z,
    dg.gyro_x,
    dg.gyro_y,
    dg.gyro_z,
    dg.mag_yaw,
    dg.time,
    dg.dt,
    alpha)

# %%
filtered_data=pd.DataFrame({"time":dg.time,
                            "Filtered_roll":roll_filtered,
                            "Filtered_pitch":pitch_filtered,
                            "Filtered_yaw":yaw_filtered,
                            "accel_x":dg.accel_x,
                            "accel_y":dg.accel_y})

print(filtered_data)

# %%
