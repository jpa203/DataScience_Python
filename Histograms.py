import pandas as pd
import matplotlib.pyplot as plt

# loading dataset
df = pd.read_csv('/Users/jazzopardi/Desktop/CS 677/Homework_3/World_Population_Analysis/world_population.csv')

# Question 2

today_population = df[['Country', '2022 Population']].xs('2022 Population', axis=1)

old_population = df[['Country', '1970 Population']].xs('1970 Population', axis=1)

percentage = ((old_population - today_population) / old_population) * 100

df2 = df.merge(percentage.to_frame('Percentage_Change'), left_index=True, right_index=True)

pop_percent_change = df2[['Country', 'Percentage_Change']].sort_values('Percentage_Change', ascending=False)

print(round(pop_percent_change.head(5)),2)  # need to express this in 2 decimal places
print(round(pop_percent_change.tail(5)),2) # need to express this in 2 decimal places.

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
print(df['2020 Population'].describe())
print(f'Median Value: {med_value:.2f}')

# Question 7

find_q1 = df['2020 Population'].quantile(0.25)
find_median = df['2020 Population'].quantile(0.50)
find_q3 = df['2020 Population'].quantile(0.75)
find_mean = df['2020 Population'].mean()

df.iloc[(df['2020 Population'] - find_q1).abs().argsort(df['2020 Population'])[0:3]]
# Bahamas, Guadeloupe, Belize

df.iloc[(df['2020 Population'] - find_median).abs().argsort(df['2020 Population'])[0:3]]
# Slovakia, Finland, Norway

df.iloc[(df['2020 Population'] - find_q3).abs().argsort(df['2020 Population'])[0:3]]
# Burkina Faso, Mali, Sri Lanka

df.iloc[(df['2020 Population'] - find_mean).abs().argsort(df['2020 Population'])[0:3]]
# Uzbekistan, Angola, Peru

# Question 8

# 2020 Population

lower_quartile = df['2020 Population'].quantile(0.25)
mid_quartile = df['2020 Population'].quantile(0.5)
upper_quartile = df['2020 Population'].quantile(0.75)

new_data = df.loc[df['2020 Population'] > lower_quartile]

final_2020_range = new_data.loc[df['2020 Population'] < upper_quartile]

hist_2020 = final_2020_range.hist(column = '2020 Population', color = 'green')

plt.savefig('histo.pdf')

# 2010 Population

lower_quartile = df['2010 Population'].quantile(0.25)
mid_quartile = df['2010 Population'].quantile(0.5)
upper_quartile = df['2010 Population'].quantile(0.75)

new_data = df.loc[df['2010 Population'] > lower_quartile] 

final_2010_range = new_data.loc[df['2010 Population'] < upper_quartile]


hist_2010 = final_2010_range.hist(column = '2010 Population', color = 'blue')

plt.savefig('histo1.pdf')

# 2000 Population

lower_quartile = df['2000 Population'].quantile(0.25)
mid_quartile = df['2000 Population'].quantile(0.5)
upper_quartile = df['2000 Population'].quantile(0.75)

new_data = df.loc[df['2000 Population'] > lower_quartile]

final_2000_range = new_data.loc[df['2000 Population'] < upper_quartile]

hist_2000 = final_2000_range.hist(column = '2010 Population', color = 'cyan')

plt.savefig('histo2.pdf')

# 1990 Population

lower_quartile = df['1990 Population'].quantile(0.25)
mid_quartile = df['1990 Population'].quantile(0.5)
upper_quartile = df['1990 Population'].quantile(0.75)

new_data = df.loc[df['1990 Population'] > lower_quartile]

final_1990_range = new_data.loc[df['1990 Population'] < upper_quartile]

hist_1990 = final_1990_range.hist(column = '1990 Population', color = 'black')

plt.savefig('histo3.pdf')

# 1980 Population

lower_quartile = df['1980 Population'].quantile(0.25)
mid_quartile = df['1980 Population'].quantile(0.5)
upper_quartile = df['1980 Population'].quantile(0.75)

new_data = df.loc[df['1980 Population'] > lower_quartile]

final_1980_range = new_data.loc[df['1980 Population'] < upper_quartile]

hist_1980 = final_1990_range.hist(column = '1980 Population', color = 'red')

plt.savefig('histo4.pdf')

# Question 9
"""
All histograms have right-skewed distribution, which means there were only a few countries with a very high population.
It seems however that more countries had a high population as time went on, as indicated by the bars and the extension of
the x-axis
""" 

# Question 10
pop_density_rank = df[['Rank','Country', 'Density (per km²)']].sort_values('Density (per km²)', ascending = False)

# Question 11

new_df = df[['Country','1970 Population', '2020 Population']].sort_values('1970 Population', ascending = False)
ranks = list(range(1,len(df)+1))

new_df['Rank_1970'] = ranks

new_df_two = new_df.sort_values('2020 Population', ascending = False)

new_df_two['Rank_2020'] = ranks

final_df = new_df_two.reset_index()

final_df['Overall Rank'] = final_df.Rank_1970 - final_df.Rank_2020

final_df.sort_values('Overall Rank', ascending = False)

#Top 5 - UAE, Jordan, Qatar, Saudi Arabia, Angola

#Bottom 5 - Belarus, Croatia, Hungary, Bulgaria, Georgia 

first_digit = df['2020 Population']

dct = {}

for n in first_digit:
    n = str(n)
    if n[0] in dct:
        dct[n[0]] += 1
    else:
        dct[(n[0])] = 1
        
        
for k, v in dct.items():
    res = (v / sum(dct.values())) *100
    print(f'{k} appeared this many times as a percentange {res:.2f} %')
    
