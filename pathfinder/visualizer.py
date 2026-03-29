

import pygame, sys, math
from graph import build_city
from astar import astar

# colours
WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
GREY   = (200, 200, 200)
GREEN  = (0,   200, 100)  
RED    = (220, 50,  50)   
YELLOW = (220, 200, 0)    
PURPLE = (180, 50,  230)  

# window
W, H = 900, 620

# setup
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("A* Pathfinder")
clock  = pygame.time.Clock()
font   = pygame.font.SysFont("Arial", 10)
font2  = pygame.font.SysFont("Arial", 13, bold=True)

# load city
positions, adjacency = build_city()

# state
start = None   # start place name
end   = None   # end place name
visited_log = []   # nodes A* explored
path        = []   # final shortest path
step        = 0    # animation step
done        = False
msg = "Click a place to set START"


def pos(name):
    # convert graph (x,y) to screen pixel
    gx, gy = positions[name]
    return int(gx * W / 720) + 10, int(gy * H / 580) + 10


def draw_circle(name, color):
    x, y = pos(name)
    pygame.draw.circle(screen, color, (x, y), 10)
    pygame.draw.circle(screen, BLACK, (x, y), 10, 2)
    lbl = font.render(name, True, BLACK)
    screen.blit(lbl, (x - lbl.get_width() // 2, y + 12))


def clicked_node(mx, my):
    for name in positions:
        x, y = pos(name)
        if math.hypot(mx - x, my - y) < 18:
            return name
    return None


# main loop
while True:

    # --- events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit(); sys.exit()

            if event.key == pygame.K_r:   # reset
                start = end = None
                visited_log = []; path = []
                step = 0; done = False
                msg = "Click a place to set START"

            if event.key == pygame.K_s:   # solve
                if start and end:
                    path, cost, visited_log, _ = astar(positions, adjacency, start, end)
                    step = 0; done = False
                    msg = "Running A*... yellow = visited, purple = path"

        if event.type == pygame.MOUSEBUTTONDOWN:
            node = clicked_node(*event.pos)
            if node:
                if start is None:
                    start = node
                    msg = f"Start = {node}. Now click END."
                elif end is None and node != start:
                    end = node
                    msg = f"{start} -> {node}. Press S to solve!"

    # --- animate ---
    if not done and step < len(visited_log):
        step += 2
    if not done and step >= len(visited_log) and visited_log:
        done = True
        msg = f"Done! Path = {len(path)} stops. Press R to reset."

    # --- draw ---
    screen.fill(WHITE)

    # draw roads
    seen = set()
    for place, nb_list in adjacency.items():
        for nb, _ in nb_list:
            key = tuple(sorted([place, nb]))
            if key not in seen:
                x1, y1 = pos(place)
                x2, y2 = pos(nb)
                pygame.draw.line(screen, GREY, (x1, y1), (x2, y2), 2)
                seen.add(key)

    # draw final path (thick purple)
    if done and path:
        for i in range(len(path) - 1):
            x1, y1 = pos(path[i])
            x2, y2 = pos(path[i + 1])
            pygame.draw.line(screen, PURPLE, (x1, y1), (x2, y2), 5)

    # draw all nodes grey
    for name in positions:
        draw_circle(name, GREY)

    # draw visited nodes yellow
    for i in range(min(step, len(visited_log))):
        name, _ = visited_log[i]
        if name not in (start, end):
            draw_circle(name, YELLOW)

    # draw path nodes purple
    if done:
        for name in path:
            if name not in (start, end):
                draw_circle(name, PURPLE)

    # draw start and end on top
    if start: draw_circle(start, GREEN)
    if end:   draw_circle(end,   RED)

    # show message
    screen.blit(font2.render(msg, True, BLACK), (10, H - 25))
    screen.blit(font2.render("S=Solve  R=Reset  Q=Quit", True, GREY), (W - 220, H - 25))

    pygame.display.flip()
    clock.tick(60)
