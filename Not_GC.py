class MyClass:
    def __init__(self):
        self.data = [1] * 1000000

def create_objects():
    # 객체 생성 후 리스트에 추가
    objs = []
    for _ in range(100):
        obj = MyClass()
        objs.append(obj)

# create_objects 함수를 반복 호출
while True:
    create_objects()
