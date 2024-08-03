'''etching drawer'''
import shutil, sys
UP_DOWN_CHAR         = chr(9474) 
LEFT_RIGHT_CHAR      = chr(9472) 
DOWN_RIGHT_CHAR      = chr(9484)  
DOWN_LEFT_CHAR       = chr(9488) 
UP_RIGHT_CHAR        = chr(9492)  
UP_LEFT_CHAR         = chr(9496)
UP_DOWN_RIGHT_CHAR   = chr(9500)  
UP_DOWN_LEFT_CHAR    = chr(9508)  
DOWN_LEFT_RIGHT_CHAR = chr(9516)  
UP_LEFT_RIGHT_CHAR   = chr(9524)  
CROSS_CHAR           = chr(9532)
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
CANVAS_WIDTH -=1
CANVAS_HEIGHT -= 5

canvas = {}
cursor_x = 0
cursor_y = 0

def getCanvasString(canvasData, cx, cy):
    canvasStr = ''

    for rowNum in range(CANVAS_HEIGHT):
        for columnNum in range(CANVAS_HEIGHT):
            if columnNum == cx and rowNum == cy:
                canvasStr += '#'
                continue

            cell = canvasData.get((columnNum, rowNum))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvasStr += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                canvasStr += DOWN_RIGHT_CHAR
            elif cell == set(['A', 'S']):
                canvasStr += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                canvasStr += UP_RIGHT_CHAR
            elif cell == set(['W', 'A']):
                canvasStr += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'D']):
                canvasStr += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                canvasStr += UP_DOWN_LEFT_CHAR
            elif cell == set(['A', 'S', 'D']):
                canvasStr += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'D']):
                canvasStr += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'S', 'D']):
                canvasStr += CROSS_CHAR
            elif cell == None:
                canvasStr += ' '
        canvasStr += '\n' 
    return canvasStr
moves = []
while True:
    print(getCanvasString(canvas, cursor_x, cursor_y))

    print('WASD keys to move, H for help, C to clear, '
          + 'F to save, or QUIT.')
    response = input('> ').upper()

    if response == 'QUIT': 
        print('Thanks for playing!')
        sys.exit()
    elif response == 'H':
        print('Enter W, A, S, and D characters to move the cursor and')
        print('draw a line behind it as it moves. For example, ddd')
        print('draws a line going right and sssdddwwwaaa draws a box.')
        print()
        print('You can save your drawing to a text file by entering F.')
        input('Press Enter to return to the program...')
        continue
    elif response == 'C':
        canvas = {}
        moves.append('C')
    elif response == 'F':
        try:
            print('Enter filename to save to:')
            filename = input('> ')
            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding = 'utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(getCanvasString(canvas, None,  None))
        except:
            print('ERROR: could not save file.')
    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue
        moves.append(command)
        if canvas == {}:
            if command in ('W', 'S'):
                canvas[(cursor_x, cursor_y)] = set(['W', 'S'])
            elif command in ('A', 'D'):
                canvas[(cursor_x, cursor_y)] = set(['A','D'])
        if command == 'W' and cursor_y > 0:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_y = cursor_y - 1
        elif command == 'S' and cursor_y < CANVAS_HEIGHT - 1:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_y = cursor_y + 1
        elif command == 'A' and cursor_x > 0:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_x = cursor_x - 1
        elif command == 'D' and cursor_x < CANVAS_WIDTH - 1:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_x = cursor_x + 1
        else:
            continue

        if (cursor_x, cursor_y) not in canvas:
            canvas[(cursor_x, cursor_y)] = set()
        if command == 'W':
            canvas[(cursor_x, cursor_y)].add('S')
        elif command == 'S':
            canvas[(cursor_x, cursor_y)].add('W')
        elif command == 'A':
            canvas[(cursor_x, cursor_y)].add('D')
        elif command == 'D':
            canvas[(cursor_x, cursor_y)].add('A')