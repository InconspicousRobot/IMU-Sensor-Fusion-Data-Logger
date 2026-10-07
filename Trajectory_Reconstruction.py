# %%
import importlib
import numpy as np
import Data_Gen as dg
import filters as ft
import matplotlib.pyplot as plt
import pandas as pd
from numba import njit
importlib.reload(dg)
importlib.reload(ft)

print(ft.yaw_filtered[0])

# %%
@njit
def world_acceleration(accel_x,accel_y,yaw,dt,time,alpha,gyro_z):
    pos_out_x=np.zeros(len(time))
    pos_out_y=np.zeros(len(time))
    world_velocity_x=0
    world_velocity_y=0
    world_acceleration_x=0
    world_acceleration_y=0
    prev_world_acceleration_x=0
    prev_world_acceleration_y=0
    prev_vel_x=0
    prev_vel_y=1
    prev_pos_x=2    
    prev_pos_y=0
    tau=(alpha*dt[0])/(1-alpha)
    for i in range(len(time)):
        yaw_compensated=yaw[i]+(.44555*gyro_z[i]*tau)
        
        world_acceleration_x=(accel_x[i] * np.cos(yaw_compensated))-(accel_y[i]*np.sin(yaw_compensated))
        world_acceleration_y=(accel_x[i] * np.sin(yaw_compensated))+(accel_y[i]*np.cos(yaw_compensated))
        if i == 0:
            prev_world_acceleration_x=world_acceleration_x
            prev_world_acceleration_y=world_acceleration_y
        world_velocity_x =prev_vel_x+ (.5*(world_acceleration_x+prev_world_acceleration_x)*dt[i])
    
        world_velocity_y =prev_vel_y+ (.5*(world_acceleration_y+prev_world_acceleration_y)*dt[i])
        
        pos_out_x[i]=prev_pos_x+(.5*(prev_vel_x+world_velocity_x)*dt[i])
        prev_pos_x=pos_out_x[i]
        
        pos_out_y[i]=prev_pos_y+(.5*(prev_vel_y+world_velocity_y)*dt[i])

        prev_pos_y=pos_out_y[i]
        prev_vel_x=world_velocity_x
        prev_vel_y=world_velocity_y
        prev_world_acceleration_x=world_acceleration_x
        prev_world_acceleration_y=world_acceleration_y
        
    return pos_out_x,pos_out_y
final_x,final_y = world_acceleration(dg.accel_x,dg.accel_y, ft.yaw_filtered,dg.dt,dg.time,ft.alpha,dg.gyro_z)

# %%
plt.axis('equal')
plt.plot(final_x,final_y)
plt.show()

# %%
export_data= {
    'timestamp': dg.time,
    'dt': dg.dt,
    "True Position X": dg.position_x,
    'True Position Y': dg.position_y,
    'accel_x':dg.accel_x,
    'accel_y':dg.accel_y,
    'accel_z':dg.accel_z,
    'Heading':dg.heading,
    'gyro_x':dg.gyro_x,
    'gyro_y':dg.gyro_y,
    'gyro_z':dg.gyro_z,
    'biased_gyro_z':dg.biased_gyro_z,
    'mag_yaw':dg.mag_yaw,
    'yaw_filtered':ft.yaw_filtered,
    'pos_x_reconstructed': final_x,
    "pos_y_reconstructed": final_y
}

df_export=pd.DataFrame(export_data)
csv_filename="imu_dead_reckoning_trajectory.csv"
df_export.to_csv(csv_filename,index=False)
print(df_export.head())


