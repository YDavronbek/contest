def kwargsAcceptFun(**kwargs):
    print("Type:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")