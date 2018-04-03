class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *nums):
        for num in nums:
            if isinstance(num, list) or isinstance(num, tuple):
                for item in num:
                    self.result += item
            else:
                self.result += num
        return self
    def subtract(self, *nums): 
        for num in nums:
            count = 0
            if isinstance(num, list) or isinstance(num, tuple):
                for item in num:
                    count += item
                self.result -= count
            else:
                self.result -= num
        return self
    
        


md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result