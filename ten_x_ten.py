def write_to_file(puzzle):
    with open('ten_by_ten.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([puzzle[1,1],puzzle[1,2],puzzle[1,3],puzzle[1,4],puzzle[1,5],puzzle[1,6],puzzle[1,7],puzzle[1,8],puzzle[1,9],puzzle[1,10]])
        writer.writerow([puzzle[2,1],puzzle[2,2],puzzle[2,3],puzzle[2,4],puzzle[2,5],puzzle[2,6],puzzle[2,7],puzzle[2,8],puzzle[2,9],puzzle[2,10]])
        writer.writerow([puzzle[3,1],puzzle[3,2],puzzle[3,3],puzzle[3,4],puzzle[3,5],puzzle[3,6],puzzle[3,7],puzzle[3,8],puzzle[3,9],puzzle[3,10]])
        writer.writerow([puzzle[4,1],puzzle[4,2],puzzle[4,3],puzzle[4,4],puzzle[4,5],puzzle[4,6],puzzle[4,7],puzzle[4,8],puzzle[4,9],puzzle[4,10]])
        writer.writerow([puzzle[5,1],puzzle[5,2],puzzle[5,3],puzzle[5,4],puzzle[5,5],puzzle[5,6],puzzle[5,7],puzzle[5,8],puzzle[5,9],puzzle[5,10]])
        writer.writerow([puzzle[6,1],puzzle[6,2],puzzle[6,3],puzzle[6,4],puzzle[6,5],puzzle[6,6],puzzle[6,7],puzzle[6,8],puzzle[6,9],puzzle[6,10]])
        writer.writerow([puzzle[7,1],puzzle[7,2],puzzle[7,3],puzzle[7,4],puzzle[7,5],puzzle[7,6],puzzle[7,7],puzzle[7,8],puzzle[7,9],puzzle[7,10]])
        writer.writerow([puzzle[8,1],puzzle[8,2],puzzle[8,3],puzzle[8,4],puzzle[8,5],puzzle[8,6],puzzle[8,7],puzzle[8,8],puzzle[8,9],puzzle[8,10]])
        writer.writerow([puzzle[9,1],puzzle[9,2],puzzle[9,3],puzzle[9,4],puzzle[9,5],puzzle[9,6],puzzle[9,7],puzzle[9,8],puzzle[9,9],puzzle[9,10]])
        writer.writerow([puzzle[10,1],puzzle[10,2],puzzle[10,3],puzzle[10,4],puzzle[10,5],puzzle[10,6],puzzle[10,7],puzzle[10,8],puzzle[10,9],puzzle[10,10]])




import csv
done = False
xc = 0
yc = 1
num_dead_ends = 0
highest_number = 0

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
    #print(moves_list)
    return moves_list



def do_next_move_recur(puzzle, next_number, position):
    global done
    global xc
    global yc
    global num_dead_ends
    global highest_number

    write_to_file(puzzle)

    if((next_number - 1) > highest_number):
        highest_number = next_number - 1
    if done == True:
        return
    if (next_number == 100):
        done = True
        return

    # we are not done :/
    # a move is a tuple with coordinates (x,y) (same with position)
    possible_moves = list_possible_moves(puzzle, position[xc], position[yc])
    if len(possible_moves) == 0:
        num_dead_ends += 1
    for move in possible_moves:
        print("Highest number reached: {} Current number: {} Number of dead ends reached: {}\r".format(highest_number, next_number - 1, num_dead_ends), end='\r')
        puzzle[(move[xc], move[yc])] = next_number
        do_next_move_recur(dict(puzzle), next_number + 1, move)




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

if __name__ == '__main__':
    main()
