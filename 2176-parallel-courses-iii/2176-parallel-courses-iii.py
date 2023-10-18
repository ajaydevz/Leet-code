class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Build a graph representing prerequisites
        graph = defaultdict(list)
        for pre, course in relations:
            graph[course].append(pre)

        # Array to store the calculated time for each course
        course_times = [0] * (n + 1)

        def calculate_course_time(course):
            # If the course time is already calculated, return it
            if course_times[course] > 0:
                return course_times[course]

            pre_max_time = 0
            # Calculate the maximum time from prerequisites
            for pre in graph[course]:
                pre_max_time = max(pre_max_time, calculate_course_time(pre))

            # Total time for the current course is its time plus the maximum time from      prerequisites
            course_total_time = time[course - 1] + pre_max_time

            # Store the calculated course time in the array
            course_times[course] = course_total_time

            return course_total_time

        # Calculate the maximum time required to complete any course
        max_time = max(calculate_course_time(course) for course in range(1, n + 1))
        return max_time