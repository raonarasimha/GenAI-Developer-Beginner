class MathDemo:
    def instance_method(self, x):
        print(f"Instance method called with self={self} and x={x}")

    @staticmethod
    def static_method(x):
        print(f"Static method called with x={x}")

    @classmethod
    def class_method(cls, x):
        print(f"Class method called with cls={cls} and x={x}")

if __name__ == "__main__":
    obj = MathDemo()
    obj.instance_method(10)  # Instance method
    MathDemo.static_method(20)  # Static method
    MathDemo.class_method(30)   # Class method 