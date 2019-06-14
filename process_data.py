import pandas as pd 
import logging

logging.basicConfig(filename="log/process_data.log", filemode="w", level= logging.DEBUG, format="%(levelname)s\t%(message)s")


def encode_dataset(dataframe):
    dataframe["workclass"] = dataframe["workclass"].map({'Private': 0.5, 'Self-emp-not-inc': 0.5,'Local-gov': 0.5, '?':0.5,'State-gov': 0.7, 'Self-emp-inc': 1, 'Federal-gov': 0.85, 'Without-pay': 0.2,'Never-worked':0.1})
    dataframe["education"] = dataframe["education"].map({'HS-grad': 0.4, 'Some-college': 0.4,'Bachelors': 0.75,'Masters': 0.75, 'Assoc-voc': 0.5, '11th': 0.3, 'Assoc-acdm': 0.5,'10th':0.3, '7th-8th': 0.3,'Prof-school':0.95, '9th': 0.3, '12th': 0.3,'Doctorate': 0.95,'5th-6th': 0.3, '1st-4th': 0.1,'Preschool': 0.1})
    dataframe["marital-status"] = dataframe["marital-status"].map({'Married-civ-spouse': 0.7, 'Never-married': 0.2, 'Divorced': 0.2,'Widowed': 0.2, 'Separated': 0.2, 'Married-spouse-absent': 0.5,'Married-AF-spouse': 0.5})
    dataframe["occupation"] = dataframe["occupation"].map({'Prof-specialty': 0.8, 'Craft-repair': 0.5, 'Exec-managerial': 0.8,'Adm-clerical': 0.4, 'Sales': 0.5, 'Other-service': 0.3,'Machine-op-inspct': 0.3, '?': 0.5,'Transport-moving': 0.5, 'Handlers-cleaners': 0.3,'Farming-fishing': 0.4,'Tech-support': 0.45,'Protective-serv': 0.45,'Priv-house-serv': 0.1, 'Armed-Forces': 0.4})
    dataframe["relationship"] = dataframe["relationship"].map({'Husband': 0.9, 'Not-in-family': 0.3,'Own-child': 0.1, 'Wife':0.9,'Other-relative': 0.3, 'Unmarried': 0.3})
    dataframe["race"] = dataframe["race"].map({'White': 0.5, 'Black': 0.3,'Asian-Pac-Islander': 0.5, 'Amer-Indian-Eskimo':0.3,'Other': 0.3})
    dataframe["gender"] = dataframe["gender"].map({'Male': 0.7, 'Female': 0.3})
    dataframe["native-country"] = dataframe["native-country"].map({'Mexico':0.3 ,'Puerto-Rico':0.3 ,'El-Salvador':0.3 ,'Dominican-Republic':0.3 ,'Columbia':0.3, 'United-States' :0.5 , '?' :0.5 , 'Philippines' :0.5 , 'Germany' :0.5 , 'China' :0.5 , 'India' :0.5 , 'England' :0.5 , 'Jamaica' :0.5 , 'South' :0.5 , 'Guatemala' :0.5 , 'Vietnam' :0.5 , 'Poland' :0.5 , 'Italy' :0.5 , 'Haiti' :0.5 , 'Portugal' :0.5 , 'Japan' :0.5 , 'Peru' :0.5 , 'Taiwan' :0.5 , 'Nicaragua' :0.5 , 'Ecuador' :0.5 , 'Iran' :0.5 , 'Greece' :0.5 , 'Thailand' :0.5 , 'Trinadad&Tobago' :0.5 , 'Outlying-US(Guam-USVI-etc)' :0.5 , 'Cambodia' :0.5 , 'Ireland' :0.5 , 'Laos' :0.5 , 'France' :0.5 , 'Hong' :0.5 , 'Honduras' :0.5 , 'Scotland' :0.5 , 'Yugoslavia' :0.5 , 'Hungary' :0.5 , 'Holand-Netherlands':0.5, 'Canada':0.7})
    dataframe["income"] = dataframe["income"].map({'<=50K':0, '>50K':1})
    return dataframe


if __name__ == "__main__":
    dataset = pd.read_csv("data/trainset.csv")

    
