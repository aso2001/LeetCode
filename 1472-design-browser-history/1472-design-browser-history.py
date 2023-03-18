class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0
        self.len = 1
        self.history = [homepage]
        

    def visit(self, url: str) -> None:
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        self.i += 1
        self.len = self.i + 1
        

    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        return self.history[self.i]


    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.len - 1)
        return self.history[self.i]
        

class BrowserHistory2:

    def __init__(self, homepage: str):
        self.hback = [homepage]
        self.hforward = []
        

    def visit(self, url: str) -> None:
        self.hforward = []
        self.hback.append(url)
        print(self.hback)
        

    def back(self, steps: int) -> str:
        if len(self.hback) < steps:
            steps = len(self.hback)
        cnt = 0
        tmp = ''
        while cnt < steps:
            tmp = self.hback.pop()
            self.hforward.append(tmp)
            cnt += 1
        return tmp


    def forward(self, steps: int) -> str:
        if len(self.hforward) < steps:
            steps = len(self.hforward)
        cnt = 0
        tmp = ''
        while cnt < steps:
            tmp = self.hforward.pop()
            self.hback.append(tmp)
            cnt += 1
        return tmp


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)