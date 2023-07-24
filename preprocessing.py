import csv

department = {'Human Resources':0, 'Research & Development':1, 'Sales':2}
education = {"Other":0, "Technical Degree":1, "Human Resources":2, "Marketing":3, "Life Sciences": 4, "Medical": 5}
martial_status = {"Single":0, "Married":1, "Divorced":2}

age_min = 18
age_max = 60

dist_min = 1
dist_max = 29

income_min = 1009
income_max = 20000

company_min = 0
company_max = 9

years_at_company_min = 0
years_at_company_max = 40

def bound(min, max, val):
    if val < min:
        return min
    if val > max:
        return max
    return val

def preprocess(data_file):
    ret = []
    with open(data_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        for row in spamreader:
            processedRow = []
            for i in row:
                if i.isdigit():
                    processedRow.append(int(i))
                else:
                    processedRow.append(i)

            processedRow[0] = bound(age_min, age_max, processedRow[0])
            if processedRow[1] == 'No':
                processedRow[1] = 0
            else:
                processedRow[1] = 1
            processedRow[2] = department.get(processedRow[2])
            processedRow[3] = bound(dist_min, dist_max, processedRow[3])
            processedRow[5] = education.get(processedRow[5])
            processedRow[8] = martial_status.get(processedRow[8])
            processedRow[9] = bound(income_min, income_max, processedRow[9])
            processedRow[10] = bound(company_min, company_max, processedRow[10])
            processedRow[12] = bound(years_at_company_min, years_at_company_max, processedRow[12])
            ret.append(processedRow)
    return ret

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(preprocess("Attrition Data.csv"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
