from collections import deque
import numpy as np

with open('1a_data.txt') as f:

    window = deque(maxlen=3)
    previous = 1E10
    count = 0

    for i, line in enumerate(f):
        window.append(line)

        if len(window) == 3:

            current = np.array([int(element) for element in window]).sum()

            if current > previous:
                count += 1

            previous = current

    print(count)