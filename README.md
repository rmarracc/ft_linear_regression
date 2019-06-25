# ft_linear_regression
Simple linear regression machine learning algorithm in Python

## Installation

### Clone

- Clone this repo using `git clone https://github.com/rmarracc/ft_linear_regression`

### Build

- Python is interpreted, so there is no need to build the application

## Usage

- Execute the estimate script with `python estimate.py`
- Execute the learning script with `python train.py`
- You can replace the `data.csv` file by another with a similar formatage (skipped first line, two collumns)

### Estimate

- Give the mileage (or first parameter with another csv file) when it's asked for
- The estimate script requieres a `output.csv` file containing the theta values, given by the learning script

### Train

- Give the desired precision (0.01 gives a 1% error limit) and the learning rate when it's asked for
- The learning script displays the error rate at each iteration, and the number of iterations at the end of the gradiant descent algorithm
- The learning script create then a `output.csv` file containing theta0 and theta1

## How it works ?

### Estimate

- The estimate script just gives you the result of the function f(x) = a + bx (Affine function)

### Train

- The learning script first scale the data (scaling all the values between 0 and 1), to avoid overflows
- Then, the learning script execute the gradiant descend algorithm, processing processively the theta values depending on the learning rates, with the following formulas :
- `temp_theta0 = learning rate + 1 / m * sum(hypothesis(x[i]) - y[i])`
- `temp_theta1 = learning rate + 1 / m * sum(hypothesis(x[i]) - y[i]) * x[i]`
- The hypothesis function here is the estimate function, m represents the number of elements on the `data.csv` file
- The cost (error value) is also calculated with the following formula :
- `cost = 1 / 2m * sum(hypothesis(x[i]) - y[i])`
- When the cost reach the defined precision value, the script reverses the normalization process and create a new tab with the processed theta values
- Finally, the script retrieve the affine function values with the newly processed data and build the `output.csv` file containing the two values

## Notes

- The script handles divergent learning rates, but you can remove this line in the learning script
- The script doesn't contain a matplotlib visualizer for the moment, I will add one soon... maybe