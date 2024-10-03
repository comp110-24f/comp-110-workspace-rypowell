"Obtaining coordinates."

__author__ = "730484742"


def get_coords(xs: str, ys: str) -> None:
    xs_idx: int = 0
    while xs_idx < len(xs):
        ys_idx: int = 0
        while ys_idx < len(ys):
            print(f"({xs[xs_idx]}, {ys[ys_idx]})")
            ys_idx += 1
        xs_idx += 1
