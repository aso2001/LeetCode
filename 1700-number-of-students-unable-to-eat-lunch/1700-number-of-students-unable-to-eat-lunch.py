class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while True:
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
            else:
                tmp = students[0]
                students = students[1:]
                students.append(tmp)
            if not len(students):
                return 0
            if (sum(students) == 0 and sandwiches[0]) or (sum(students) == len(students) and not sandwiches[0]):
                return len(students)