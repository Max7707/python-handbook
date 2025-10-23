from module_5_1.task_A import Point

class PatchedPoint(Point):

    def __init__(self, *args):
        if args and isinstance(args[0], tuple):
            super().__init__(args[0][0], args[0][1])
        else:
            super().__init__(*args)


point = PatchedPoint()
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)
