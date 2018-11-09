class WinLoseCondition:
    def __init__(self, limit):
        self.limit = limit
        self.status = "ongoing"

    def track_biggest(self, num):
        if num >= self.limit:
            self.status = "win"
