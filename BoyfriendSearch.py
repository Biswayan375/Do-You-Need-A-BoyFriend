import pygame
pygame.init

# Colors
black = (200, 200, 200)
blue = (0, 0, 200)
grey = (160, 160, 160)
green = (0, 200, 0)
red = (200, 0, 0)

# Screen parameters and window
screenWidth = 512
screenHeight = 512
win=pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Boyfriend Search")

dimension = 32

boxWidth = screenWidth//dimension
boxHeight = screenHeight//dimension
a=[[0 for i in range(dimension)] for j in range(dimension)]

# print(a)
adjList = [0 for i in range(9)]
queue = []
print(queue)
# print(adjList)

def searchTheBoyfriend():
    ver = src
    queuePointer = 0
    print(ver[0], ver[1])
    while(1):
        j = 0
        if ver[1] + 1 <= (dimension - 1):
            if a[ver[0]][ver[1] + 1] == 0:
                adjList[j] = [ver[0], ver[1] + 1]
                a[adjList[j][0]][adjList[j][1]] = 1
                j += 1
                queue.append([ver[0], ver[1] + 1])
                queuePointer += 1
            if ver[1] + 1 == dst[1] and ver[0] == dst[0]:
                break
        if ver[0] + 1 <= (dimension - 1):
            if a[ver[0] + 1][ver[1]] == 0:
                adjList[j] = [ver[0] + 1, ver[1]]
                a[adjList[j][0]][adjList[j][1]] = 1
                j += 1
                queue.append([ver[0] + 1, ver[1]])
                queuePointer += 1
            if ver[0] + 1 == dst[0] and ver[1] == dst[1]:
                break
        if ver[0] - 1 >= 0:
            if a[ver[0] - 1][ver[1]] == 0:
                adjList[j] = [ver[0] - 1, ver[1]]
                a[adjList[j][0]][adjList[j][1]] = 1
                j += 1
                queue.append([ver[0] - 1, ver[1]])
                queuePointer += 1
            if ver[0] - 1 == dst[0] and ver[1] == dst[1]:
                break
        if ver[1] - 1 >= 0:
            if a[ver[0]][ver[1] - 1] == 0:
                adjList[j] = [ver[0], ver[1] - 1]
                a[adjList[j][0]][adjList[j][1]] = 1
                j += 1
                queue.append([ver[0], ver[1] - 1])
                queuePointer += 1
            if ver[0] == dst[0] and ver[1] - 1 == dst[1]:
                break
        if queuePointer == 0:
            break
        else:
            ver = queue.pop(0)
            a[ver[0]][ver[1]] = 1
            drawInk(ver[0], ver[1], (173, 3, 253))
            draw()
            queuePointer -= 1
        
        # for i in queue:
        #     print(i)
        # print(queue, queuePointer)

def drawInk(x, y, color):
    size = screenHeight // dimension
    pygame.draw.rect(win, color, (x * size, y * size, size, size))
    pygame.display.update()

def draw():
    x = 0
    y = 0
    for l in range(dimension):
        pygame.draw.line(win, black, (x, 0), (x, screenWidth))
        pygame.draw.line(win, black, (0, y), (screenHeight, y))
        x += screenWidth // dimension
        y += screenHeight // dimension
        pygame.display.update()

def redrawGameWindow():
    win.fill(grey)
    draw()
    pygame.display.update()

def gameLoop():
    redrawGameWindow()
    clock=pygame.time.Clock()

    running = True

    global givingSrc, givingDest, src, dst
    givingSrc = True
    givingDest = False

    while running:
        clock.tick(60)
        pygame.time.delay(50)
        for event in pygame.event.get(): #This loop is used to detect the events and work accordingly

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    searchTheBoyfriend()

            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                # print(pygame.mouse.get_pos())
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    x = pos[0] // (screenWidth / dimension)
                    y = pos[1] // (screenHeight / dimension)
                    if a[int(x)][int(y)] == 0 and givingSrc == False and givingDest == False:
                        a[int(x)][int(y)] = 1
                        drawInk(x, y, blue)
                    elif a[int(x)][int(y)] == 0 and givingSrc == True:
                        a[int(x)][int(y)] = 10
                        src = [int(x), int(y)]  # Saving source index
                        drawInk(x, y, green)
                        givingSrc = False
                        givingDest = True
                    elif a[int(x)][int(y)] == 0 and givingDest == True:
                        a[int(x)][int(y)] = 10
                        dst = [int(x), int(y)]  # Saving destination index
                        drawInk(x, y, red)
                        givingDest = False
                    # print(a)
                    # print(x, y)

gameLoop()
# print(a)
pygame.quit()