class MyClass:
    def __init__(self):
        self.data = [1] * 1000000

def create_objects():
    objs = []
    for _ in range(100):
        obj = MyClass()
        objs.append(obj)

    # 객체 사용 후 참조 해제
    objs.clear()

while True:
    create_objects()
