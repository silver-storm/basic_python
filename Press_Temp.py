# CODE TO TAKE IN PRESSURE AND TEMPERATURE VARATION AS A FUNCTION OF TIME
# AND VISUALIZE THE RESULTS

import numpy as np
from datetime import datetime as dt
import time
import matplotlib.pyplot as plt

# To generate voltage signals for P and T in range 0-100mV
def PT_generator(ext_Input = False):
	if ext_Input:
		P = float(input("Pressure Value : "))
		T = float(input("Temperature Value : "))
	else:
		P = np.random.uniform(0,0.1,1)[0]
		T = np.random.uniform(0,0.1,1)[0]
	return P,T

def main(ext_Input = False):
	P_scaled = []; T_scaled = []
	timestamps = []	

	plt.style.use('ggplot')
	plt.ion()

	print("How many iterations?")
	while True:
	    try:
	        N = int(input())
	    except ValueError:
	        print("Invalid Input")
	        continue
	    break
	    
	plt.figure(1)
	plt.title('Pressure and Temperature Variation with time')

	start = dt.now()
	for i in range(N):
	    cur_time = dt.now()
	    P,T = PT_generator(ext_Input)
	    P_scaled.append(P*1000)
	    T_scaled.append(T*1000)
	    
	    timestamps.append((cur_time-start).total_seconds())
	    
	    time_array = np.array(timestamps,np.float32)
	    
	    plt.subplot(2,1,1)
	    if not ext_Input:
	        plt.xlim(-0.5,N*0.5),plt.ylim(-1,105)
	    plt.scatter(x=time_array[i],y=P_scaled[i],c='k')
	    plt.ylabel(r"Pressure$\rightarrow$")
	    plt.subplot(2,1,2)
	    if not ext_Input:
	        plt.xlim(-0.5,N*0.5),plt.ylim(-1,105)
	    plt.scatter(x=time_array[i],y=T_scaled[i],c='r')
	    plt.ylabel(r"Temperature$\rightarrow$")
	    plt.xlabel(r"Time$\rightarrow$")
	    plt.show(),plt.pause(0.4675)

	plt.figure(2)
	if not ext_Input:
	    plt.xlim(-0.5,N*0.5),plt.ylim(-1,105)
	plt.title('Overall Variation')
	plt.ylabel(r"Pressure$\rightarrow$")
	plt.xlabel(r"Time$\rightarrow$")
	plt.plot(time_array,P_scaled,'co-',label='Pressure')
	plt.ylabel(r"Temperature$\rightarrow$")
	plt.xlabel(r"Time$\rightarrow$")
	plt.plot(time_array,T_scaled,'ro-',label='Temperature')
	plt.legend()
	plt.show()
	
	print('Simulate Again with the same settings?')
	plt.pause(0.0001)
	s1 = input().lower()
	plt.close(1)
	plt.close(2)
	if s1 == 'y':
		main(ext_Input)
	elif s1 != 'n':
		raise ValueError(f"The choice should be either Y or N, not {s1}")

if __name__ == "__main__":
	print("PRESSURE-TEMPERATURE VISUALIZATION\n")
	choice = input("Enter Y to provide user input, or N to generate uniform random values : \n").lower()
	if choice == 'n':
		main()
	elif choice == 'y':
		main(True)
	else:
		raise ValueError(f"ERROR! Your choice hould be Y or N, not {choice}")


