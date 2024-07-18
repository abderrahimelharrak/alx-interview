#!/usr/bin/python3

"""
Log parsing
"""

import sys

if __name__ == '__main__':

    filesize, c_ount = 0, 0
    co_des = ["200", "301", "400", "401", "403", "404", "405", "500"]
    st_ats = {k_: 0 for k_ in co_des}

    def print_stats(st_ats: dict, file_size: int) -> None:
        print("File size: {:d}".format(filesize))
        for k_, v_ in sorted(st_ats.items()):
            if v_:
                print("{}: {}".format(k_, v_))

    try:
        for l_ine in sys.stdin:
            c_ount += 1
            da_ta = l_ine.split()
            try:
                status_code = da_ta[-2]
                if status_code in st_ats:
                    st_ats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(da_ta[-1])
            except BaseException:
                pass
            if c_ount % 10 == 0:
                print_stats(st_ats, filesize)
        print_stats(st_ats, filesize)
    except KeyboardInterrupt:
        print_stats(st_ats, filesize)
        raise
