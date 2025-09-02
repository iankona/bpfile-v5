


class 类:
    def __init__(self):
        self.start = 0 
        self.index = 0 
        self.final = 0



    def __calc__(self, size):
        if size < 1: raise ValueError(f"出错")
        i = self.index
        j = self.index + size
        if j > self.final: raise ValueError(f"出错")
        self.index = j
        return i, j

    def __calcseek0__(self, size):
        if size < 1: raise ValueError(f"出错")
        i = self.index
        j = self.index + size
        if j > self.final: raise ValueError(f"出错")
        return i, j

    def __calcinvert__(self, size):
        if size < 1: raise ValueError(f"出错")
        i = self.index - size
        j = self.index
        if j > self.final: raise ValueError(f"出错")
        self.index = i
        return i, j

    def __calcinvertseek0__(self, size):
        if size < 1: raise ValueError(f"出错")
        i = self.index - size
        j = self.index
        if j > self.final: raise ValueError(f"出错")
        return i, j


    def size(self):
        return self.final - self.start

    def seek(self, size):
        j = self.index + size
        if j < self.start: raise ValueError(f"stacke::seek::回跳的索引值超出slice范围...")
        if j > self.final: raise ValueError(f"stacke::seek::往前的索引值超出slice范围...")
        self.index = j

    def tell(self):
        return self.index

    def slicetell(self):
        return self.index - self.start


    def remainsize(self):
        return self.final - self.index



    def remainsizeinvert(self):
        return self.index - self.start

    



    





