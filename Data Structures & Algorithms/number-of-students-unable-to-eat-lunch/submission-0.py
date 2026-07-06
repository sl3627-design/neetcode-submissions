class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students:
            if sandwiches[0] not in students:
                break
            if sandwiches[0] == students[0]:
                del sandwiches[0]
                del students[0]
            else:
                students.append(students[0])
                del students[0]
        
        return len(students)
