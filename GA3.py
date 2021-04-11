#create = make 
#calulate = compute
#remove = delete

import random
import brainfuck
#Don't modify this group of constants.
#The max value of a 'cell' in the memory tape.
CHAR_SIZE = 255

#The number of types of mutations: (ADD, DELETE, CHANGE).
NUM_MUTATIONS = 3  

#The list of brainfuck instructions.
INSTRUCTIONS = ['+', '-', '>', '<', '[', ']', '.'] 

#Holds the number of instructions allowed.
#(sizeof(INSTRUCTIONS) / sizeof(INSTRUCTIONS[0]))
NUM_INSTRUCTIONS =  7 

#Number of children two parents create upon reproduction.
NUM_CHILDREN = 2 

#Modify any constants below.

#The size of the population. This always remains the same between generations.
POP_SIZE = 10

#The minimum size a possible program can be.
MIN_PROGRAM_SIZE = 10

#The maximum size a possible program can be.
MAX_PROGRAM_SIZE = 500

#The chance of a 'gene' in a child being mutated.
MUTATION_RATE = 0.05

#The score an erroneous program receives.
ERROR_SCORE = 1

#The size of the program is multiplied by this then added to score.
LENGTH_PENALTY = 0.001  

#How often to display the best program so far.
DISPLAY_RATE = 10000

#These aren't constant because they can be changed by the user.
GOAL_OUTPUT = "hi"
GOAL_OUTPUT_SIZE = len(GOAL_OUTPUT)

   #These two functions used to generate either a random double or unsigned int.
   #Why didn't I just overload one function? Slipped my mind at the time. 
def get_random_double(low, high):
    #returns double 
    return low + (high-low)*(random.random())


def get_random_int(low, high):
    #returns unsigned
    return random.randint(low, high)



def get_random_instruction() :
    #returns char
    return INSTRUCTIONS[random.randint(0, NUM_INSTRUCTIONS - 1)];



def add_instruction(program, index) :
    #returns nothing 
    #Need to convert char to string for use by insert.  
    if len(program)+1 <= MAX_PROGRAM_SIZE :
    	program = program[0:index+1] + get_random_instruction() + program[index+1: ]
    return program


"""
def delete_instruction(program, index):
    #returns nothing
    #Subtract 2 instead of 1 to account for the off-by-one difference between a string length and the last element index.
    # I don't understand why are we subtracting 2 and not 1
    if len(program) - 2 >= MIN_PROGRAM_SIZE:
        tmp = index+1
        first_part = program[:index] 
    	#last_part =  program[tmp:]
    	return first_part
    return program
"""
def delete_instruction(program, index):
    if len(program) -2 >= MIN_PROGRAM_SIZE:
        fp = program[:index]
        lp = program[index+1:]
        return fp+lp
    return program
def mutate_instruction(program, index):
 	#replaces the present instruction at the given location by a random instruction
 	# The writer has written it in a wrong way. What if the get_random function returns the same instruction 
 	#program[index] = get_random_instruction();
 	program = program[0:index] + get_random_instruction() + program[index+1: ]
 	return program

def make_random_program() :
	# This function outputs a string of varibale length. 
    # Creates a random program by first randomly determining its size and then adding that many instructions randomly.
    program_size = get_random_int(MIN_PROGRAM_SIZE, MAX_PROGRAM_SIZE)
    program = get_random_instruction()
    for i in range(1, program_size):
    	program += get_random_instruction()

    return program

def initialize_population(programs):
    # Returns nothing. 
    # Creates the first generation's population by randomly creating programs.
    # Intialize Global Array of Strings()
    for i in range(0, POP_SIZE):
    	programs[i] = make_random_program()

def compute_fitness(program) :
	#The Fitness Function. Determines how 'fit' a program is using a few different criteria.
	# Returns a Double 
	#The score of the worst program possible (Besides erroneous program, and not taking into account program length).
    max_score = GOAL_OUTPUT_SIZE * CHAR_SIZE
    score = 0

    output = brainfuck.evaluate(program)

    #Impose a very large penalty for error programs, but still allow them a chance at reproduction for genetic variation.
    if output == "Error" :
        return ERROR_SCORE

    """ We need to know whether the goal output or the program's output is larger
       because that's how many iterations of the next loop need to be done. """
    min_str = output if (len(output) < len(GOAL_OUTPUT)) else GOAL_OUTPUT
    max_str = output if(len(output) >=len(GOAL_OUTPUT)) else GOAL_OUTPUT

    #The more each character of output is similar to its corresponding character in the goal output, the higher the score.
    for i in range(0, len(max_str)) :
        output_char = ord(min_str[i]) if (i < len(min_str)) else ord(max_str[i]) + int(CHAR_SIZE)
        score += abs(output_char - ord(max_str[i]))
    
    #Impose a slight penalty for longer programs.
    score += (len(program)* LENGTH_PENALTY)  

    """The lower the score of a program, the better (think golf).
       However other calculations in the program assume a higher score is better.
       Thus, we subtract the score from max_score to get a final score. */"""
    final_score = max_score - score
    return final_score

def score_population(programs, scores, worst_program_index) :
	#Generates a fitness score for each program in the population.
    #This is done by running the program through the brainfuck interpreter and scoring its output.
    #Also returns the best program produced. (Not in our code)
    best_program = ""
    best_score = 0
    #Arbitrarily high number.
    worst_score = 9999  

    for i in range(0, POP_SIZE):
    
        scores[i] = compute_fitness(programs[i])

        if scores[i] > best_score :
            best_program = programs[i]
            best_score = scores[i]
        
        elif scores[i] < worst_score :
            worst_program_index[0] = i
            worst_score = scores[i]
    
    return best_program
    
def compute_total_score(scores) :
    #returns a double
    # Adds every program's fitness score together.
    total_score = 0.0
    
    for i in range(0, POP_SIZE) :
        total_score += scores[i]

    return total_score

def select_parent(programs, scores, other_parent = "") :
    # returns a string(a parent for mating)
    # Selects a parent to mate using fitness proportionate selection.
    #Basically, the more fit a program is, the more likely it is to be selected.
    # We have to implement roulette wheel in this function, the writer has not implemented it.

    #// Holds each program's chance of being selected (a # between 0 and 1).
    program_chances = [0]*POP_SIZE  
    score_total = compute_total_score(scores)
    random.seed()
    rand_val = random.random()

    for i in range(0, POP_SIZE):
    
        #// Cast i to int so when we go to subtract 1, if i is 0 it doesn't overflow (as an unsigned int can't be negative).
        prev_chance = 0 if (((i) - 1) < 0) else program_chances[i - 1]

        """/* We add the previous program's chance to this program's chance because that is its range of being selected.
           The higher the fitness score, the bigger this program's range is. */"""
        #Why are we adding previous program's chance to this program's chance??
        program_chances[i] = (scores[i] / score_total) + (prev_chance)

        #// Need to subtract a small amount from rand_val due to floating-point precision errors. Without it, equality check could fail.
        if program_chances[i] >= (rand_val - 0.001) and (programs[i] != other_parent) :
        	return programs[i]
    

    """If the other parent was the last program in the list, we might get here.
       In that case, just return the 1st program. */"""
    return programs[0]

 
def mutate(child):
    # return a string (a child which has been mutated). Gets a string child as input
    # We have to write our own code for mutaion. Because we want it to be simple
    # But we can have a look at the writers code. 
    #Loop through each command and randomly decide to mutate it based on the mutation rate.
    for i in range(0, len(child)):
    
        if MUTATION_RATE >= random.random():
        
            mutation_type = get_random_int(1, NUM_MUTATIONS)
           
            if mutation_type ==1:
            	child = mutate_instruction(child, i)
            elif mutation_type ==2:
            	child =add_instruction(child, i)
            elif mutation_type ==3:
            	child = delete_instruction(child, i)


    return child

def crossover(genome1, genome2, children) :
    # returns 2 strings (children)
    #Performs crossover between two parents to produce two children.
    # We need to find which program is longest.
    min_str = genome1 if(len(genome1)< len(genome2)) else genome2
    max_str = genome1 if (len(genome1) >= len(genome2)) else genome2

    #Determine a crossover point at random.
    crosspoint = random.randint(1, len(max_str) - 1)

    #Find the substring of the program after the crossover point
    max_str_contrib = max_str[crosspoint:]

    #Then erase after that point
    max_str = max_str[:crosspoint]

    """/* If the cross-over point is less than the length of the smaller program, then we need to combine part of it with the larger program.
       If not, then we do nothing and just take part of the larger program and add it to it. */"""
    if crosspoint <= len(min_str):
        max_str += min_str[crosspoint:]
        min_str = min_str[:crosspoint]
    

    #Add the 2nd part of the larger program to the smaller program.
    min_str += max_str_contrib

    #Call the mutate function on the children which has a small chance of actually causing a mutation.
    children[0] = mutate(min_str)
    children[1] = mutate(max_str)

def program_exists(genome, genomes) :
    #returns a bool. Tells whether or not the Genome exists in the pool or not 
    for i in range(0, POP_SIZE):
        if genome == genomes[i] :
            return True

    return False


def load_new_generation(programs, children) :
	# loads new genration into the pool from the child array.
    for i in range(0, POP_SIZE) :
        programs[i] = children[i] 
    for i in range(0, POP_SIZE):
    	children[i] = ""
def replace_program(parent, child,programs):
    for i in range(POP_SIZE):
        if parent == programs[i] :
            programs[i] = child
            break
        
    

def main() :
    random.seed()
    programs = ["++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>-----.>-----------------."]*POP_SIZE
    #programs[1] = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>+++++++++++.++++++."
    #programs[2] = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.++." 
    #programs[3] = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++++++++++++.--------."
    fitness_scores = [1.23]*POP_SIZE

    initialize_population(programs)

    best_program = "Not_best"

    keep_going = False

    generations = 0

    #// And now we just repeat the process of selection and reproduction over and over again.
    while 1 :
        worst_program_index = [0]

        best_program = score_population(programs, fitness_scores, worst_program_index)

        #// Select two parents randomly using fitness proportionate selection
        parent1 = select_parent(programs, fitness_scores)
        parent2 = select_parent(programs, fitness_scores, parent1)

        #// Mate them to create children
        children = ["Chote_Prateek"]*NUM_CHILDREN
        crossover(parent1, parent2, children)
        """children[0] = child1
        children[1] = child2"""
        """/* Replace the parent programs with the children. We replace the parents to lessen the chance of premature convergence.
           This works because by replacing the parents, which are most similar to the children, genetic diversity is maintained.
           If the parents were not replaced, the population would quickly fill with similar genetic information. */"""
        replace_program(parent1, children[0], programs)
        replace_program(parent2, children[1], programs)

        """/* Replace the worst program with the best program if it was replaced by its child. (Elitism).
           This is done to ensure the best program is never lost. */"""
        if not program_exists(best_program, programs):
            programs[worst_program_index[0]] = best_program

        #// Report on the current best program every so often.
        if not (generations % DISPLAY_RATE):
        
            #print("Best program evolved so far: ")
            #print(best_program)

            output = brainfuck.evaluate(best_program)
            print(output)

            if output == GOAL_OUTPUT and not keep_going:
            
                print("Program evolved!")
                print("Save source code as a text file? (y/n) ")
                answer = input()
                """
                if answer == 'y':
                {
                    std::ofstream srcfile("bfsrc.txt");
                    srcfile << GOAL_OUTPUT << ":\n\n" << best_program;
                    std::cout << "Source code saved as 'bfsrc.txt'\n" << std::endl;
                }
                """
                print("It took roughly ")
                print(generations)
                print(" generations to evolve this program.") 
                print("Keep evolving for more efficiency? (y/n) ")
                answer = input()

                #Quit the program if the user doesn't want to continue.
                if answer != 'y':
                    return 0

                keep_going = true
            
        ++generations
    

    

if __name__ == "__main__": main()
