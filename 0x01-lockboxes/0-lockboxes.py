#!/usr/bin/python3
"""Lock boxes puzzle """


def next_opened_box(opened_boxes):
    """Looks for the next opened box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        list: List with the keys contained in the opened box
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List  contain all the boxes with the keys
    Returns:
        bool: True or false
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    x = {}
    while True:
        if len(x) == 0:
            x[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = next_opened_box(x)
        if keys:
            for key in keys:
                try:
                    if x.get(key) and x.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    x[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in x.values()]:
            continue
        elif len(x) == len(boxes):
            break
        else:
            return False

    return len(x) == len(boxes)


def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
