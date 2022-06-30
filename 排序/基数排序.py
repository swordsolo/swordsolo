def bucket_sort(list):
    max_num = max(list)
    max_len = len(str(max_num))
    for i in range(max_len):
        bucket = [[] for _ in range(10)]
        for num in list:
            mod = num // (10 ** i) % 10
            bucket[mod].append(num)
        list = []
        for l in bucket:
            list.extend(l)
    return list


if __name__ == "__main__":
    list = [999, 23, 45, 65, 777, 1234, 4, 9]
    print(bucket_sort(list))
