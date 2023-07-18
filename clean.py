import pandas as pd



def clean_file(file):
    """This Function has been used to remove the null value from the data set"""

    df = pd.read_csv("Output.csv")
    df.columns = ['index', "Actor", "Movie", "Year"]
    data = df.drop(['index'], axis=1)

    # Here I am droping the Nan value in the Actor column:
    data.drop(index=data[pd.isnull(data.Actor) == True].index, inplace=True)

    # reseting the index so that i can drop more data because we only required 1000
    data.reset_index(drop=True)
    data.drop(index=[i for i in range(1000, 1472)], inplace=True)
    data = data.reset_index(drop=True)

    # Saving the updated csv as  """'updated_output_file.csv'"""
    data.to_csv('updated_output_file.csv')
    print("New file has been created:updated_output_file.csv ")

    # return the file name for classification :
    return 'updated_output_file.csv'
