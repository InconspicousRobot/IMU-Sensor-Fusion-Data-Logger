# IMU-GPS-Fusion-Data-Logger

(In progress, need to improve technical writing skills.)

Hello! To those reading, this is one of my first projects- I chose this because I plan on building either a EKF or a UKF in the near future, and this contains a good portion of the ideas needed to build it. There are three main components to it, the data generation filter, which generated body-frame accelerometer data, the gyroscope, and the magnetometer to ground it. Further, afterwards, noise/bias is injected at each layer of the data to simulate real world noisy sensors.

The next layer, filters, used a recursive equation in @njit- I wanted it to be scalable, in case I needed to have several million inputs in the future then 10k. 
