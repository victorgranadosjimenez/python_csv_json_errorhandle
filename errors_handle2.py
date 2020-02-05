class DrinkListFileManager():
    def __init__(self,file_path_name):
        self.file = open(file_path_name)


    def _open_file(self, file_option):
        #_ makes the function hidden
        try:
            file=open(self.file, file_option)
        except FileNotFoundError as msg:
            print("I think something had has just happen")
            print("please correct it: {}".format(msg))

    def print_file(self):
        print(self._open_file("r").read())


    def line_count(self):
        count=self._open_file("r")
        return len(count.readlines())


    def write_to_file(self,item):
        file=self._open_file("w")
        file.write(item,"\n")
        file.close()

drink_file_manager = DrinkListFileManager("\Users\Victor Jimenez\Engineering47\week4\day2\Hamlet.txt")
drink_file_manager.write_to_file("Who wrote that")
print(drink_file_manager.line_count())