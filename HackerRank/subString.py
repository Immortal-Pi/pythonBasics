def count_substring(string, sub_string):
    # https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
    count = 0
    for i in range(0, len(string)):

        lencount = 0
        for j in range(0, len(sub_string)):

            if ((i+j)<len(string)):
                # print(sub_string[j], j, string[i + j], i + j, '-')
                if sub_string[j] == string[i + j]:
                    # print(sub_string[j],j,string[i+j],i+j)
                    lencount += 1
                else:
                    break;
            if lencount == len(sub_string):
                # print('yes')
                count += 1
                i = len(sub_string) - 1

    print(count)
    return