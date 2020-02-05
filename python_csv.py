import csv

def transform_user_details(csv_file_name):
    new_user_data = []

    with open("user_details.csv", newline='') as csvfile:
        user_details = csv.reader(csvfile, delimiter=",")

        for user in user_details:
            new_user_data.append(user)
    return new_user_data

def create_new_user_data_csv(old_user_data_file,new_file_name):
    new_user_data = transform_user_details(old_user_data_file)
    new_file = open(new_file_name, "w")

    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerpws(new_user_data)

test_csv = transform_user_details("user_details.csv")
print(test_csv)

# create_new_user_data_csv("")