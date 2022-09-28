import pandas as pd

# question 1

df = pd.read_csv('/Users/jazzopardi/Desktop/ds_salaries.csv')

# question 2

average_year = df.groupby(['work_year'])['salary_in_usd'].mean()  # average salaries by year # question

# question 3

max_year = max(average_year)
min_year = min(average_year)

# question 4

average_exp_job_title_year = df.groupby(['work_year', 'experience_level', 'job_title', 'salary_in_usd']) \
    ['salary_in_usd'].mean()

# Question 5

filter_data = df.groupby(['job_title', 'salary_in_usd']).mean()

new_df = filter_data.reset_index()

highest_paying_job = new_df['job_title'].max()
lowest_paying_job = new_df['job_title'].min()

# Question 6

average_job_title_year = df.groupby(['work_year', 'job_title'])['salary_in_usd'].mean()


# Question 7

def first_to_last_year_diff(df):
    diff = (df[df.work_year == df.work_year.max()].salary_in_usd
            - df[df.work_year == df.work_year.max()].salary_in_usd)

    return diff


min_max = df.groupby(["job_title", "salary_in_usd"]).apply(first_to_last_year_diff)

# Question 8

remote_ratio = df.groupby(['work_year', 'remote_ratio', 'salary_in_usd'])[
    'salary_in_usd'].mean()  # remote ratio

remote_ratio_zero = len(df.loc[df['remote_ratio'] == 0])
remote_ratio_fifty = len(df.loc[df['remote_ratio'] == 50])
remote_ratio_hundred = len(df.loc[df['remote_ratio'] == 100])

# question 9

company_location_high = df.groupby(['company_location', 'salary_in_usd']).mean().sort_values('salary_in_usd',
                                                                                             ascending=False)
company_location_low = df.groupby(['company_location', 'salary_in_usd']).mean().sort_values('salary_in_usd',
                                                                                            ascending=True)
print(average_year)
print(f'Max year: {max_year}')
print(f'Min year: {min_year}')
print(average_exp_job_title_year)
print(highest_paying_job)
print(lowest_paying_job)
print(average_job_title_year)
print(min_max)
print(remote_ratio)
print(f'Entries for zero remote ratio: {remote_ratio_zero}')
print(f'Entries for fifty remote ratio: {remote_ratio_fifty}')
print(f'Entries for hundred remote ratio: {remote_ratio_hundred}')
for n in company_location_high.index[0:10]:
    print(n[0], end = ', ') # highest paying locations
print()
for n in company_location_low.index[0:10]:
    print(n[0], end = ', ') # lowest paying locations
