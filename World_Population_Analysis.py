import pandas as pd
from matplotlib import pyplot as plt

# loading data set

df = pd.read_csv('/Users/jazzopardi/Desktop/CS 677/Homework_3/World_Population_Analysis/world_population.csv')

# Question 2

today_population = df[['Country', '2022 Population']].xs('2022 Population', axis=1)

old_population = df[['Country', '1970 Population']].xs('1970 Population', axis=1)

percentage = ((old_population - today_population) / old_population) * 100

df2 = df.merge(percentage.to_frame('Percentage_Change'), left_index=True, right_index=True)

pop_percent_change = df2[['Country', 'Percentage_Change']].sort_values('Percentage_Change', ascending=False)

# print(pop_percent_change.head(5))  # need to express this in 2 decimal places
# print(pop_percent_change.tail(5))  # need to express this in 2 decimal places.

# Question 3

twenty_population = df[['Country', '2020 Population']].xs('2020 Population', axis=1)

ten_population = df[['Country', '2010 Population']].xs('2010 Population', axis=1)

percentage = ((ten_population - twenty_population) / ten_population) * 100

df3 = df.merge(percentage.to_frame('Percentage_Change_10_Years'), left_index=True, right_index=True)

percentage_change = df3[['Country', 'Percentage_Change_10_Years']].sort_values('Percentage_Change_10_Years',
                                                                               ascending=False)
#
# print(percentage_change.head(5))
# print(percentage_change.tail(5))

# Question 4

highest_pop_2020 = df[['Country', '2020 Population']].sort_values('2020 Population', ascending=False)
lowest_pop_2020 = df[['Country', '2020 Population']].sort_values('2020 Population', ascending=True)

# print(highest_pop_2020.head(5))
# print(lowest_pop_2020.head(5))

# Question 5

highest_pop_1970 = df[['Country', '1970 Population']].sort_values('1970 Population', ascending=False)
lowest_pop_1970 = df[['Country', '1970 Population']].sort_values('1970 Population', ascending=True)


# print(highest_pop_1970.head(5))  # Pakistan beat Russia for a spot in the top 5
# print(lowest_pop_1970.head(5)) # Motserrat beat Saint Barthelemt for a spot in the top 5

# Question 6

med_value = df['2020 Population'].median()
# print(df['2020 Population'].describe())
# print(f'Median Value: {med_value:.2f}')

# Question 7

# Question 8

# 2020 Population

lower_quartile = df['2020 Population'].quantile(0.25)
mid_quartile = df['2020 Population'].quantile(0.5)
upper_quartile = df['2020 Population'].quantile(0.75)

new_data = df.loc[df['2020 Population'] > lower_quartile]

final_2020_range = new_data.loc[df['2020 Population'] < upper_quartile]

check = final_2020_range.hist(column = '2020 Population')

print(check)
