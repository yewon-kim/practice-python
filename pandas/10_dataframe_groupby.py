import pandas as pd

years = pd.Series([1990, 1990, 1990, 1991, 1991, 1991, 1992, 1992, 1992])
names = pd.Series(['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'])
departments = pd.Series(['HR', 'RD', 'Admin', 'HR', 'RD', 'Admin', 'HR', 'RD', 'Admin'])
ages = pd.Series([25, 30, 45, 26, 31, 46, 27, 32, 47])
salaries = pd.Series([500000, 480000, 550000, 520000, 500000, 600000, 600000, 520000, 620000])

dat = {
    'Year': years, 
    'Name': names, 
    'Department': departments, 
    'Age': ages, 
    'Salary': salaries
}
data = pd.DataFrame(dat)
print(data)

# groupby()
year_salary_sum = data.groupby(['Year'])['Salary'].sum()
print(year_salary_sum)

year_salary_mean = data.groupby(['Year'])['Salary'].mean()
print(year_salary_mean)

print(data.groupby(['Year', 'Department'])['Salary'].sum())