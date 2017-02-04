assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

boxes = cross(rows, cols) ## This line is to create all possible boxes
row_units = [cross(r,cols) for r in rows] # This creates a list of the boxes in a row
column_units = [cross(rows,c) for c in cols] ## This creates a list of boxes in a column
square_units = [cross(rs,cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')] # this creates a list of the boxes in a 3x3 square
diagnol_units = [['A1','B2','C3','D4','E5','F6','G7','H8','I9'],['I1','H2','G3','F4','E5','D4','C3','B2','A1']] ### Adding diagnol units in the list
### Addding diagnol units will help because this is the list which decides what units get processed together for numbers 1-9.
unitlist = row_units + square_units + column_units + diagnol_units ### Union of all the lists
units = dict((s, [u for u in unitlist if s in u]) for s in boxes) ### Units is a dictionary with key as box and value as the list of list of 9 boxes which follow the law of 1-9 numbers
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes) ### Peers contains a dictionary of boxes which are part of the same units

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    
    for i in values.keys():   ### For each box in the soduku
        for unit in units[i]: ### Find the unit of the box i
            dict_naked_twins=dict() ### create a naked twins dictionary
            for box in unit:  ### for each box within the unit
                if len(values[box])==2:  ## identify the boxes which have only two values
                    dict_naked_twins[box] = values[box] ### Add it to the dictionary
##### Finding naked twins in the naked_twin dictionary
            for twin1_keys in dict_naked_twins.keys():   ##### For each value of naked twin dictionary
                for twin2_keys in dict_naked_twins.keys(): ####### for each value of naked twin dictionary
                    if dict_naked_twins[twin1_keys]== dict_naked_twins[twin2_keys] and twin1_keys !=twin2_keys: #### identify twins which have same value
                        for box2 in unit:  ##### Now search the entire unit and find the box containing the values of the twins
##### Now the twins are found, remove all the values which have value of the naked twin
                            if box2 != twin1_keys and box2!=twin2_keys and len(values[box2])!=1 and len(values[box2])!=0:
                                values[box2]=values[box2].replace(dict_naked_twins[twin1_keys][0],"")
                                values[box2]=values[box2].replace(dict_naked_twins[twin1_keys][1],"")
    return values                                                    
                                        
def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return
        

def eliminate(values):
    """
    This technique eliminates all the values having common numbers to the boxes which have a single number
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

def only_choice(values): 
    """ This technique helps to find boxes in unit which have a unique number and then it removes all other numbers for that box
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
    """ This function executes the constraint propogation algorithm by trying to optimize the sudoku by repeatedly executing
    the elimination, naked_twins and only_choice till there is no optimization left
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Use the Eliminate Strategy
        values = eliminate(values)
        # Use the Only Choice Strategy
        values = only_choice(values)
        #Naked Twins strategy
        values = naked_twins(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def solve(grid):
     return search(grid_values(grid))

def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Chose one of the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))
    
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
