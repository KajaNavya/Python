if __name__ == '__main__':
    N = int(input())
    List=[];
    for i in range(N):
        command=input().split();
        if command[0] == "insert":
            List.insert(int(command[1]),int(command[2]))
        elif command[0] == "append":
            List.append(int(command[1]))
        elif command[0] == "pop":
            List.pop();
        elif command[0] == "print":
            print(List)
        elif command[0] == "remove":
            List.remove(int(command[1]))
        elif command[0] == "sort":
            List.sort();
        else:
            List.reverse();
