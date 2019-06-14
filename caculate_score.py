from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import sys

RESULT_FILE = "data/result_prv.csv"

def read_data(filename):
    data = [line.rstrip('\n') for line in open(filename)]
    data = [1 if item == ">50K" else 0 for item in data]
    return data

if __name__ == "__main__":
    user_file = sys.argv[1]
    result = read_data(RESULT_FILE)
    user_result = read_data(user_file)
    accuracy = accuracy_score(result, user_result)
    f1 = f1_score(result, user_result, average="weighted")
    f1_micro = f1_score(result, user_result, average="micro")

    print("accuracy:", round(accuracy, 3))
    print("f1_weighted:", round(f1, 3))
    print("f1_micro:", round(f1_micro, 3))