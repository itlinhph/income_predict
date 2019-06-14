import csv
from sklearn.model_selection import train_test_split

def divide_train_test(file_dataset):
    with open(file_dataset, 'r') as f:
        rows = csv.reader(f)
        list_data = list(rows)
    label = list_data.pop(0)
    train_set, test_set = train_test_split(list_data, test_size = 0.2, random_state=40)
    train_set.insert(0,label)
    test_set.insert(0,label)
    
    with open("data/trainset.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(train_set)

    with open("data/testset.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(test_set)

divide_train_test("data/dataset_train.csv")