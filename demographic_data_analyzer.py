import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read data from file
    df = pd.read_csv('adult.data.csv') 

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts() 

    # What is the average age of men?
    sex_filt = df['sex'] == 'Male'
    average_age_men = round(df.loc[sex_filt,'age'].mean(),1) 

    # What is the percentage of people who have a Bachelor's degree? 
    percentage_bachelors = round((df['education'].value_counts()['Bachelors']) / (len(df['education'])) *100 , 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    hi_filt = df['education'].isin(['Bachelors','Masters','Doctorate']) 
    lo_filt = ~(df['education'].isin(['Bachelors','Masters','Doctorate']))

    higher_education = df.loc[hi_filt,['education','salary']] 
    lower_education = df.loc[lo_filt,['education','salary']]

    # percentage with salary >50K
    higher_education_rich =  round(( len(higher_education.loc[higher_education['salary'] == '>50K']) / len(higher_education) ) *100 ,1)
    lower_education_rich = round((len(lower_education.loc[lower_education['salary'] == '>50K']) / len(lower_education) ) *100 , 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    sal_filt = (df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')
    num_min_workers = df['hours-per-week'] == min_work_hours

    rich_percentage = round((len(df.loc[sal_filt]) / len(df.loc[num_min_workers])) *100 , 1)

    # What country has the highest percentage of people that earn >50K?
    high_sal = df['salary'] == '>50K' #A filter to choose rows where sal >50k 
    high_sal_num = df.loc[high_sal,'native-country'].value_counts() #The number of people earning a salary >50k per country (The countries here are all countries that have at least 1 person earning >50k)

    hi_cntry = df['native-country'].isin(high_sal_num.index) #A filter to choose the countries having at least 1 person with sal >50k
    high_cnt_ppl_num = df.loc[hi_cntry,'native-country'].value_counts() #The num of people per each country

    hi_sal_ratio = (high_sal_num / high_cnt_ppl_num).idxmax()

    highest_earning_country = hi_sal_ratio
    highest_earning_country_percentage = round((high_sal_num / high_cnt_ppl_num).max() *100 ,1 )

    # Identify the most popular occupation for those who earn >50K in India.
    india_filt = (df['native-country'] == 'India') & (df['salary'] == '>50K')
    max_occp = df.loc[india_filt,'occupation'].value_counts().idxmax()
    top_IN_occupation = max_occp

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
