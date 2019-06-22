from collections import deque

if __name__ == "__main__":
    que = deque([])
    que.append(1)
    que.append(2)
    que.append(3)
    print(que)
    que.popleft()
    print(que)
    que.popleft()
    print(que)
    que.popleft()
    print(que)