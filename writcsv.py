from apihit import get_person_data
import unicodecsv as csv

def read_as_list():
    f = open('/home/fullcontact-314/Downloads/test.csv')
    reader = csv.reader(f)
    for count, row in enumerate(reader):
        if count == 0:
            continue
        name = row[1]
        email = row[2]
        print(get_person_data("luN3c4FF1bBKqx7qk7fF2nVGGz8klDzy",email))

def read_as_dict():
    f = open('/home/fullcontact-314/Downloads/test.csv')
    t = open('output.csv', 'w')
    person_data_list = []
    reader = csv.DictReader(f)
    
    for item in reader:
        d = get_person_data("luN3c4FF1bBKqx7qk7fF2nVGGz8klDzy",item["email"])
        for key in d.keys():
            item[key] = d[key]
        person_data_list.append(item)
    writer = csv.DictWriter(t, person_data_list[0].keys())
    writer.writeheader()
    writer.writerows(person_data_list)
    return person_data_list



if __name__ == "__main__":
    person_data_list = read_as_dict()