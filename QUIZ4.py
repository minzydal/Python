class MyDeque:
    def __init__(self):
        self.mydeque = []

    def __str__(self):
        return "mydeque([{}])".format(",".join(self.mydeque))

    def __repr__(self):
        return "mydeque([{}])".format(",".join(self.mydeque))

    #함수 지정
    def func(self, _input):
        _input = _input.split(' ')
        if _input[0] == 'push_front':
            return self.push_front(_input[1])
        elif _input[0] == 'push_back':
            return self.push_back(_input[1])
        elif _input[0] == 'pop_front':
            return self.pop_front()
        elif _input[0] == 'pop_back':
            return self.pop_back()
        elif _input[0] == 'size':
            return self.size()
        elif _input[0] == 'empty':
            return self.empty()
        elif _input[0] == 'front':
            return self.front()
        elif _input[0] == 'back':
            return self.back()
        else:
            raise Exception('No Attribution')

    #앞에 넣기
    def push_front(self, _input):
        self.mydeque.insert(0, _input)

    #뒤에 넣기
    def push_back(self, _input):
        self.mydeque.append(_input)

    #앞에 빼기, 없을 경우 -1 출력
    def pop_front(self):
        try:
            return self.mydeque.pop(0)
        except IndexError:
            return -1

    #뒤에 빼기, 없을 경우 -1 출력
    def pop_back(self):
        try:
            return self.mydeque.pop(-1)
        except IndexError:
            return -1

    #리스트 length출력
    def size(self):
        return len(self.mydeque)

    #비어있으면 1 출력 아니면 0 출력
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    #제일 앞에 있는 원소 출력, 없으면 -1 출력
    def front(self):
        try:
            return self.mydeque[0]
        except IndexError:
            return -1

    #제일 뒤에 있는 원소 출력, 없으면 -1 출력
    def back(self):
        try:
            return self.mydeque[-1]
        except IndexError:
            return -1

#deque생성
mydeque = MyDeque()

mydeque.func('push_front 4') #4 덱의 앞에 넣는다
mydeque.func("push_back 1") #1을 덱의 뒤에 넣는다
mydeque.func("push_back 2") #2을 덱의 뒤에 넣는다
mydeque.func("push_back 3") #3을 덱의 뒤에 넣는다
mydeque.func("push_back 4") #3을 덱의 뒤에 넣는다
print('현재 덱 :', mydeque) #[를4, 1, 2, 3]
print('덱의 사이즈 :', mydeque.func("size")) #덱에 들어있는 정수의 개수를 출력
mydeque.func("pop_front") #덱에 가장 앞에 있는 수 즉, 4를 빼고 그 수를 출력한다. 덱이 들어있지 않을 경우 -1 출력.
mydeque.func("pop_back") #덱에 가장 뒤에 있는 수(=4)를 빼고, 그 수 출력.
print('덱이 비어있으면 1 아니면 0 출력 :', mydeque.func("empty")) #덱이 비어있으면 1 아니면 0 출력
print('덱의 가장 앞에 있는 정수 출력 :', mydeque.func("front")) #덱의 가장 앞에 있는 정수 출력(=1), 만약 덱이 들어있지 않을 경우 -1 출력.
print('덱의 가장 뒤에 있는 정수 출력 :',mydeque.func("back")) #덱의 가장 뒤에 있는 정수(3) 출력. 만약 들어있지 않을 경우 01 출력.
print('현재 덱 :', mydeque) #현재 덱 출력.
