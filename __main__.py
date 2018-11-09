from game import WinLoseCondition, Board

if __name__ == "__main__":
    limit = int(input("Masukkan limit angka: "))
    dimension = int(input("masukkan besar board: "))

    win_lose_condition = WinLoseCondition(limit)
    board = Board(dimension, win_lose_condition)

    while(win_lose_condition.status == "ongoing"):
        direction = input("masukkan arah (asdw): ")
        if(direction in "asdw" and len(direction) == 1):
            board.move(direction)
            board.show()
        else:
            print("Input salah, ulangi")

    status_mapper = {
        "lose": "kalah",
        "win": "menang",
    }
    print("Anda {}".format(status_mapper[win_lose_condition.status]))
    print("Skor anda: {}".format(board.get_score()))
