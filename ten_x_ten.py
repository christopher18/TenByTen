def write_to_file(puzzle):
    #input()
    with open('ten_by_ten.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for i in range(1,11):
            writer.writerow([puzzle[i,1],puzzle[i,2],puzzle[i,3],puzzle[i,4],puzzle[i,5],puzzle[i,6],puzzle[i,7],puzzle[i,8],puzzle[i,9],puzzle[i,10]])



import csv
done = False
xc = 0
yc = 1
num_dead_ends = 0
highest_number = 0
solution = None

# checks if the move is off of the 10x10 square (not a legal move)
def is_not_off_board(cur_pos):
    global xc
    global yc
    if (cur_pos[xc] < 1 or cur_pos[xc] > 10 or cur_pos[yc] < 1 or cur_pos[yc] > 10):
        return False
    else:
        return True


# lists all possible moves on board
def list_possible_moves(puzzle, x_coor, y_coor):
    moves_list = []

    # add any possible moves if there is not already a number there
    if (is_not_off_board((x_coor + 3,y_coor)) and puzzle[(x_coor + 3,y_coor)] == 0):
        moves_list += [(x_coor + 3, y_coor),]
    if (is_not_off_board((x_coor,y_coor - 3)) and puzzle[(x_coor,y_coor - 3)] == 0):
        moves_list += [(x_coor, y_coor - 3),]
    if (is_not_off_board((x_coor - 3,y_coor)) and puzzle[(x_coor - 3,y_coor)] == 0):
        moves_list += [(x_coor - 3, y_coor),]
    if (is_not_off_board((x_coor,y_coor + 3)) and puzzle[(x_coor,y_coor + 3)] == 0):
        moves_list += [(x_coor, y_coor + 3),]
    if (is_not_off_board((x_coor + 2,y_coor - 2)) and puzzle[(x_coor + 2,y_coor - 2)] == 0):
        moves_list += [(x_coor + 2, y_coor - 2),]
    if (is_not_off_board((x_coor - 2,y_coor - 2)) and puzzle[(x_coor - 2,y_coor - 2)] == 0):
        moves_list += [(x_coor - 2, y_coor - 2),]
    if (is_not_off_board((x_coor - 2,y_coor + 2)) and puzzle[(x_coor - 2,y_coor + 2)] == 0):
        moves_list += [(x_coor - 2, y_coor + 2),]
    if (is_not_off_board((x_coor + 2,y_coor + 2)) and puzzle[(x_coor + 2,y_coor + 2)] == 0):
        moves_list += [(x_coor + 2, y_coor + 2),]
    #print("moves list")
    print(moves_list)
    return moves_list



def do_next_move_recur(puzzle, next_number, position):
    global done
    global xc
    global yc
    global num_dead_ends
    global highest_number
    global solution


    if((next_number) > highest_number):
        highest_number = next_number
    if done == True:
        return
    if (next_number == 101):
        done = True
        solution = dict(puzzle)
        return

    write_to_file(puzzle)

    # we are not done :/
    # a move is a tuple with coordinates (x,y) (same with position)
    possible_moves = list_possible_moves(puzzle, position[xc], position[yc])
    if len(possible_moves) == 0:
        num_dead_ends += 1
    temp_puzzle = dict(puzzle)
    for move in possible_moves:
        if done != True:
            print("Choose", move)
            print("Highest number reached: {} Current number: {} Number of dead ends reached: {}\r".format(highest_number, next_number, num_dead_ends), end='\r')
            print("\n")
            puzzle = dict(temp_puzzle)
            puzzle[(move[xc], move[yc])] = next_number
            do_next_move_recur(puzzle, next_number + 1, move)




def solve_puzzle(puzzle):
    #print("We are starting to solve the puzzle");
    for j in range(1,11):
        for i in range(1,11):
            #print("Starting from position: {}, {}".format(i, j))
            #print("puzzle is: " + str(puzzle[(i,j)]))
            puzzle[(i, j)] = 1
            do_next_move_recur(dict(puzzle), 2, (i, j))
            if (done == True):
                #print("Found a solution.  Game completed.")
                return




def initialize_puzzle():
    puzzle = dict()
    for i in range(1,11):
        for j in range(1,11):
            puzzle[(i, j)] = 0
    #print(puzzle)
    return puzzle



def main():
    puzzle = initialize_puzzle();
    solve_puzzle(puzzle)
    if done == True:
        write_to_file(solution)

if __name__ == '__main__':
    main()
