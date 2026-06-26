class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_queue = deque(students)

        while len(student_queue):
            flag = False
            for _ in range(len(student_queue)):
                student = student_queue.popleft()
                if student == sandwiches[0]:
                    sandwiches.pop(0)
                    flag = True
                    break
                else:
                    student_queue.append(student)

            if not flag:
                return len(student_queue)

        return 0