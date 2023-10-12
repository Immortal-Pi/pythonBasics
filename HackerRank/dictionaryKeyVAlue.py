def dictionary():
    # https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for key, value in student_marks.items():
        average=0.00
        if key==query_name:

            for i in value:
                average=average+i
            average=float(average)/float(len(value))
            print(f'{average:.2f}')
    return