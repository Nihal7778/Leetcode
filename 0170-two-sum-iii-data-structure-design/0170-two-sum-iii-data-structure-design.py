class TwoSum:

    def __init__(self):
        self.twosum = {}
        

    def add(self, number: int) -> None:

        if number in self.twosum:
            self.twosum[number]+=1
        
        else:
            self.twosum[number]=1


        

    def find(self, value: int) -> bool:


        for number in self.twosum:
            k = value-number

            if k == number:
                if self.twosum[number]>1:
                    return True

            elif k in self.twosum:
                return True

        return False
        
 

        

    
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)