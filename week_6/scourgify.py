import sys 
import pandas as pd 


def main():
    if len(sys.argv) == 2:
        data = pd.read_csv(sys.argv[1])
        data = modify(data)
        out = pd.DataFrame({'first name':data['first name'],'last name':data['last name'],'house':data['house']})
        out.to_csv('after.csv',index=False)

    else:
        sys.exit()

def modify(data):
    length = len(data.values)
    data['first name'] = ['' for _ in range(length)]
    data['last name'] = ['' for _ in range(length)]
    for i in data.columns.values:
        if i == 'name':
            for j in range(len(data.values)):
                first_name,last_name = data[i][j].split(',')
                last_name = last_name.strip()
                data['first name'][j] = first_name
                data['last name'][j] = last_name
    return data

if __name__ == '__main__':
    main()