class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        while students:
            if sandwiches[0] not in students:
                break
            if sandwiches[0] == students[0]:
                sandwiches.popleft()
                students.popleft()
            else:
                students.append(students[0])
                students.popleft()
        
        return len(students)
