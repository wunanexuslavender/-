#lst=[88,89,90,98,00,99,1,3]
# for index in range(len(lst)):
#     if str(lst[index])!=0:
#         lst[index]='19'+str(lst[index])
#     else:
#         lst[index]='200'+str(lst[index])
def convert_year(year):
    if year >= 0 and year <= 99:
        return 1900 + year
    elif year >= 00 and year <= 3:
        return 2000 + year
    else:
        return year

years = [88, 89, 90, 98, 0, 99, 1, 3]
converted_years = []

for year in years:
    converted_years.append(convert_year(year))

print(converted_years)



