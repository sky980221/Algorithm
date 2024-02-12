def solution(phone_book):
    answer = True
    # 접두어인 경우 false 아니면 true
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        # if phone_book[i] in phone_book[i+1]:

        # slice하는데 길이는 이전 원소 길이만큼.
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True