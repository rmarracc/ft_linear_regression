import numpy
import sys
import matplotlib.pyplot as plt

input_file = "data.csv"
output_file = "output.csv"

def estimate(t, mileage):
	return (t[0] + (t[1] * mileage))

def normalize(d):
	e = (d - min(d)) / (max(d) - min(d))
	return (e)
	
def unnormalize(d, o):
	e = d * (max(o) - min(o)) + min(o)
	return (e)
	
def	load_file(n):
	try:
		d = numpy.loadtxt(n, delimiter = ',', skiprows = 1)
	except:
		print ("data.csv file missing")
		sys.exit()
	return (d)	

def save_file(n, t):
	try:
		numpy.savetxt(n, t, delimiter = ',')
	except:
		print ("file save failed")
		sys.exit()

def enter_learning_rate():
	try:
		learning_rate = float(input("Learning rate : "))
	except:
		print ("type error")
		sys.exit()
	return (learning_rate)

def enter_precision():
	try:
		precision = float(input("Desired precision : "))
	except:
		print ("type error")
		sys.exit()
	return (precision)

def get_cost(m, sum):
	return ((1 / (2 * m)) * sum)

def process_gradiant_algorith(d, n, learning_rate, precision):
	plt.ion()
	fig = plt.figure()
	ax = fig.add_subplot(111)
	line1, = ax.plot(d[:, 0], d[:, 1], 'x')	
	mileage = normalize(d[:, 0])
	price = normalize(d[:, 1])
	t = [0, 0]
	line2, = ax.plot(d[:, 0], unnormalize(estimate(t, mileage), d[:, 1]))
	cost = 1
	prev = 0
	i = 0
	while (abs(cost) > precision):
		i = i + 1
		tmp_0 = 0
		tmp_1 = 0
		sum = 0
		for j in range(n):
			tmp_0 = tmp_0 + (estimate(t, mileage[j]) - price[j])
			tmp_1 = tmp_1 + (estimate(t, mileage[j]) - price[j]) * mileage[j]
			sum = sum + ((estimate(t, mileage[j]) - price[j]) * (estimate(t, mileage[j]) - price[j]))
		cost = float(get_cost(n, sum))
		print("Current error :", abs(cost))
		if (abs(prev - cost) < 0.00000000000001):
			print("Notice : The result seems to converge, the learning process is stopped")
			break
		prev = cost
		if (abs(cost) > 1000000):
			print("Error : The result seems to diverge, please decrease the learning rate")
			sys.exit()
		t[0] = t[0] - learning_rate * (1 / n) * tmp_0
		t[1] = t[1] - learning_rate * (1 / n) * tmp_1
		line2.set_ydata(unnormalize(estimate(t, mileage), d[:, 1]))
		fig.canvas.draw()
		plt.pause(0.01)
	print("Done in", i, "iterations")
	input("Press Enter to continue")
	plt.close()
	return (unnormalize(estimate(t, mileage), d[:, 1]))

def get_bridge(g, d):
	v = 0
	w = 0
	for i in range (len(g) - 1):
		v = v + g[i] - g[i + 1]
		w = w + d[i, 0] - d[(i + 1), 0]
	return (v / w)

def get_function_parameters(g, d):
	t = [0, 0]
	t[1] = get_bridge(g, d)
	t[0] = -t[1] * d[0, 0] + g[0]
	return (t)

def main():
	d = load_file(input_file)
	n = len(d)
	if (n < 2):
		print ("not enough data")
		sys.exit()
	precision = enter_precision()
	learning_rate = enter_learning_rate()
	t = get_function_parameters(process_gradiant_algorith(d, n, learning_rate, precision), d)
	save_file(output_file, t)
	print("file saved :", output_file)

if (__name__ == "__main__"):
	main()