import matplotlib.pyplot as plt
import pandas as pd

# Read in the file
dpb_file = pd.read_csv('degrees-that-pay-back.csv')
dpb_file = dpb_file.sort_values('Starting Median Salary')

# Grab the majors
majors = dpb_file.get('Undergraduate Major')
majors = [d for d in majors]

# Grab the Salaries - Starting Median, Mid-Career Median, 10th, 25th, 75th, 90th Percentile Mid-Career Salaries
start_sal_50 = dpb_file.get('Starting Median Salary')
mid_sal_10 = dpb_file.get('Mid-Career 10th Percentile Salary')
mid_sal_25 = dpb_file.get('Mid-Career 25th Percentile Salary')
mid_sal_50 = dpb_file.get('Mid-Career Median Salary')
mid_sal_75 = dpb_file.get('Mid-Career 75th Percentile Salary')
mid_sal_90 = dpb_file.get('Mid-Career 90th Percentile Salary')

# Clean the salary data (remove '$' and ',' and convert to an integer)
salary_data = [start_sal_50, mid_sal_10, mid_sal_25, mid_sal_50, mid_sal_75, mid_sal_90]
for i in range(len(salary_data)):
	salary_data[i] = salary_data[i].map(lambda x: x.replace("$", ""))
	salary_data[i] = salary_data[i].map(lambda x: x.replace(",", ""))
	salary_data[i] = salary_data[i].map(lambda x: int(float(x)) / 1000)
	salary_data[i] = list(salary_data[i])
majors = list(majors)

# Setup Configurations
plt.figure(figsize=(10, 8))
plt.title("Salary by Undergraduate Degree", fontsize=24, fontname='Times New Roman')
plt.xlabel("Annual Salary ($10k)", fontname='Times New Roman', fontsize=16)
plt.xticks(fontsize=12, fontname='Times New Roman')
plt.yticks(range(len(majors)), majors, fontsize=10, fontname='Times New Roman')
plt.grid(linewidth=0.1, linestyle='-')

# Data Plotting
colors = ['green', 'pink', 'purple', 'red', 'orange', 'black']
markers = ['^', 'p', 's', '*', 'D', None]
labels = ['Starting Median Salary', 'Mid-Career 10th Percentile Salary', 'Mid-Career 25th Percentile Salary',
          'Mid-Career Median Salary', 'Mid-Career 75th Percentile Salary', 'Mid-Career 90th Percentile Salary']
for i in range(len(salary_data)):
	plt.scatter(salary_data[i], [i for i in range(len(salary_data[i]))], c=colors[i], marker=markers[i],
	            label=labels[i])

# Final Adjustments & Display
plt.margins(0.01)
plt.legend(loc=4, prop={'size': 7})
plt.tight_layout()
plt.show()
