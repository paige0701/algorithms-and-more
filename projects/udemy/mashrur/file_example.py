# file_name = './data.txt'

# not recommended way
# f = open(file_name)
# f_contents = f.read() # read all
# f_contents = f.readline() # just read first line
# for line in f:
    # print(line)
    # print(line.strip()) # remove empty line
# f.close()  # definitely close file when you open a file

# recommended way !!
# with open(file_name) as f: # this is context manager no need to close when using with !!
#     for line in f:
#         # print(line.strip())
#         pass

# record_to_add = 'even,choi:python,javascript,c++'

# w option will overwrite all the contents in file
# r is default option for reading a file
# a+ option appends data
# with open(file_name, "a+") as to_write:
#     to_write.write(record_to_add + "\n")


class Student:
    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else :
            self.courses = courses


    def add_to_file(self, filename):
        if self.find_in_file(filename):
            return 'Record already exists'
        else:
            record_to_add = Student.prep_to_write(self.first_name, self.last_name, self.courses)
            with open(filename, '+a') as to_write:
                to_write.write(record_to_add + '\n')
            return 'Record added'

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already enrolled in the {course} course")

    def remove_course(self, course):

        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not found")

    def find_in_file(self, filename):
        with open(filename) as f:
            for line in f:
                first_name, last_name, course_details = Student.prep_record(line.strip())
                student_read_in = Student(first_name, last_name, course_details)
                if self == student_read_in:
                    return True
            return False

    @staticmethod
    def prep_record(line):
        line = line.split(":")
        first_name, last_name = line[0].split(',')
        courses = line[1].rstrip().split(',')
        return first_name, last_name, courses


    @staticmethod
    def prep_to_write(first_name, last_name, courses):
        full_name = first_name + ',' + last_name
        courses = ','.join(courses)
        return full_name + ':' + courses

    def __eq__(self, other):
        return self.first_name == other.first_name \
        and self.last_name == other.last_name


if __name__ == '__main__':
    file_name = 'data.txt'
    joe = Student('joe','chen', ['python', 'javascript', 'go'])
    print(joe.find_in_file(file_name))
    print(joe.add_to_file(file_name))