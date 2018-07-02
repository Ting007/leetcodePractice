class ExamRoom:

    def __init__(self, N):
        """
        :type N: int
        """
        # self.seats = [0 for _ in range(N)]
        self.seated =[0, N-1]
        self.seats = N
        self.best = 0
        

    def seat(self):
        """
        :rtype: int
        """
        dist = 0
        if len(self.seated) == 2:
            self.best = 0
        if len(self.seated) > 2:
            for i in range(len(self.seated)-1):
                current = 0
                if i == 0 or i == len(self.seated)-2:
                    current = self.seated[i+1]-self.seated[i]
                else:
                    current = int((self.seated[i+1]-self.seated[i])/2)
                if current > dist:
                    dist =current
                    if i ==0:
                        self.best = 0
                    elif i == len(self.seated)-2:
                        self.best = self.seats-1
                    else:
                        self.best = int((self.seated[i]+self.seated[i+1])/2)
        # self.seats[best] = 1
        self.seated.append(self.best)
        self.seated.sort()
        # print(self.seats)
        return self.best

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        # self.seats[p] = 0
        self.seated.remove(p)