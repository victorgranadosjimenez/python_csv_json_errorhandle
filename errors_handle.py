# def test_without_error_handling():
#     #this code is without error handling
#     connect_to_db()
#
# def test_with_error_handling():
#     try:
#         connect_to_db()
#         #this line will not run if error occurs
#     except:
#         print("an error has occured please fix it")
#
#     finally:
#         print("help me close my open resources or handles")
#
# test_with_error_handling()

def file_read_operation():
    try:
        file = open("order.txt", "r")
        file_line_list = file.readlines()
        for line in file_line_list:
            print(line.strip('\n'))
        print(file_line_list)
        print(file_line_list[0][0]) #instead using list
    except FileExistsError as msg:
        print("I think something had has just happen")
        print("please correct it: {}".format(msg))

    finally:
        file.close()


def file_write_operation(file,order_item):
    try:
        with open(file, "w") as file:
            file.write(order_item + '\n')

    except FileNotFoundError as msg:
        print("I think something had has just happen")
        print("please correct it: {}".format(msg))

    finally:
        file.close()

file_write_operation("order.txt", "KFC")
file_read_operation("order.txt")
