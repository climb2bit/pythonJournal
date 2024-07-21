import random, sys, time
WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Deep cave.')
print('Press Ctrl-C to stop.')
time.sleep(2)

leftWidth = 20
gap_width = 10

while True:
    rightWidth = WIDTH - gap_width - leftWidth
    print(('#' * leftWidth) + (' ' * gap_width) + ('#' * rightWidth))

    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    diceroll = random.randint(1, 6)
    if diceroll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1
    elif diceroll  == 2 and leftWidth + gap_width < WIDTH - 1:
        leftWidth = leftWidth + 1
    else:
        pass
 