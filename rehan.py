import pandas as pd
df = pd.DataFrame({'TITLE': [],'DESCRIPTION': [],'DATE': [],'TIME': []})
writer = pd.ExcelWriter('Report1.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()

nor = int(input(" Enter the number of reminders you want to enter: "))
while nor > 0:
    title1 = input("Enter the Title: ")
    Description1 = input("Enter the Description: ")
    Date1 = input("Enter the date (YYYY-MM-DD): ")
    Time1 = input("Enter the time: ")

    reader = pd.read_excel(r'Report1.xlsx')
    df2 = pd.DataFrame({'TITLE': [title1],'DESCRIPTION': [Description1],'DATE': [Date1],'TIME': [Time1]})
    df3 = reader.append(df2)
    writer2 = pd.ExcelWriter('Report1.xlsx', engine='xlsxwriter')
    df3.to_excel(writer2, sheet_name='Sheet1', index=False)
    writer2.save()
    nor = nor - 1