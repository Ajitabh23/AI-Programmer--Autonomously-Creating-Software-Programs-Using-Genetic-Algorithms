#create = make 
#calulate = compute
#remove = delete

import random
#Don't modify this group of constants.
#The max value of a 'cell' in the memory tape.
CHAR_SIZE = 255

#The number of types of mutations: (ADD, DELETE, CHANGE).
NUM_MUTATIONS = 3  

#The list of brainfuck instructions.
INSTRUCTIONS[] = {'+', '-', '>', '<', '[', ']', '.'} 

#Holds the number of instructions allowed.
NUM_INSTRUCTIONS = (sizeof(INSTRUCTIONS) / sizeof(INSTRUCTIONS[0]))  

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
MUTATION_RATE = 0.01  

#The score an erroneous program receives.
ERROR_SCORE = 1.0  

#The size of the program is multiplied by this then added to score.
LENGTH_PENALTY = 0.001  

#How often to display the best program so far.
DISPLAY_RATE = 10000  

#These aren't constant because they can be changed by the user.
GOAL_OUTPUT = "Computerphile"
GOAL_OUTPUT_SIZE = GOAL_OUTPUT.length()

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



def add_instruction(program) :
    #returns nothing 
    #Need to convert char to string for use by insert.  
    if(program.length()+1 <= MAX_PROGRAM_SIZE)
    	program = program + get_random_instruction()
    return program



def delete_instruction(program, index) :
    #returns nothing
    #Subtract 2 instead of 1 to account for the off-by-one difference between a string length and the last element index.
    # I don't understand why are we subtracting 2 and not 1
    if(len(program) - 2) >= MIN_PROGRAM_SIZE)
        first_part = program[:index] 
    	last_part = program[index+1:]
    	return first_part + last_part
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
    	programs.append(make_random_program())

def compute_fitness(program, Interpreter &bf) :
	#The Fitness Function. Determines how 'fit' a program is using a few different criteria.
	# Returns a Double 
	#The score of the worst program possible (Besides erroneous program, and not taking into account program length).
    max_score = GOAL_OUTPUT_SIZE * CHAR_SIZE
    score = 0
    final_score

    output = bf.run(program)

    #Impose a very large penalty for error programs, but still allow them a chance at reproduction for genetic variation.
    if output == Interpreter::ERROR :
        return ERROR_SCORE

    """ We need to know whether the goal output or the program's output is larger
       because that's how many iterations of the next loop need to be done. """
    min_str = (len(output) < len(GOAL_OUTPUT)) ? output : GOAL_OUTPUT
    max_str = (len(output) >=len(GOAL_OUTPUT)) ? output : GOAL_OUTPUT

    #The more each character of output is similar to its corresponding character in the goal output, the higher the score.
    for i in range(0, len(max_str)) :
        output_char = (i < len(min_str)) ? min_str[i] : max_str[i] + CHAR_SIZE
        score += abs(output_char - max_str[i])
    
    #Impose a slight penalty for longer programs.
    score += (len(program)* LENGTH_PENALTY)  

    """The lower the score of a program, the better (think golf).
       However other calculations in the program assume a higher score is better.
       Thus, we subtract the score from max_score to get a final score. */"""
    final_score = max_score - score
    return final_score

def score_population(programs, scores, Interpreter &bf) :
	#Generates a fitness score for each program in the population.
    #This is done by running the program through the brainfuck interpreter and scoring its output.
    #Also returns the best program produced. (Not in our code)
    best_program = ""
    best_score = 0
    #Arbitrarily high number.
    worst_score = 9999  

    for i in range(0, POP_SIZE):
    
        scores[i] = calculate_fitness(programs[i], bf);

        if scores[i] > best_score :
            best_program = programs[i]
            best_score = scores[i]
        
        elif scores[i] < worst_score :
            worst_index = i
            worst_score = scores[i]
    
    return best_program;
    
def compute_total_score(scores) :
    #returns a double
    # Adds every program's fitness score together.
    total_score = 0
    
    for i in range(0, POP_SIZE) :
        total_score += scores[i]

    return total_score

def select_parent(programs, scores, other_parent = "") :
    # returns a string(a parent for mating)
    # Selects a parent to mate using fitness proportionate selection.
    #Basically, the more fit a program is, the more likely it is to be selected.
    # We have to implement roulette wheel in this function, the writer has not implemented it.
 
def mutate(child):
    # return a string (a child which has been mutated). Gets a string child as input
    # We have to write our own code for mutaion. Because we want it to be simple
    # But we can have a look at the writers code. 

def crossover(genome1, genome2, children) :
    # returns nothing
    #Performs crossover between two parents to produce two children.

def genome_exists(genome, genomes) :
	#returns a bool. Tells whether or not the Genome exists in the pool or not 
    for i in range(0, POP_SIZE):
    	if genome == genomes[i] :
        	return true

    return false


def load_new_generation(programs, children) :
	# loads new genration into the pool from the child array.
    for i in range(0, POP_SIZE) :
		programs[i] = children[i] 
    for i in range(0, POP_SIZE):
    	children[i] = ""

def main() :
	# main program responsible for running the GA
    
	#Initialize the brainfuck interpreter and seed random.
    Interpreter brainfuck
    srand(time(0))
    # List of strings
    programs = ["Prateek"]*POP_SIZE
    #List of strings
    children = ["Chota_Prateek"]*POP_SIZE
    #List of double
    fitness_scores = [0.01]*POP_SIZE
    # Funtion call to initialize the population
    initialize_population(programs)
    # string which stores the best program
    best_program = "Not_the_best_program"
    #Just used to have the program keep searching after a match is found.
    keep_going = false  
    #to keep track of number of generations 
    generations = 0;
    
	while(1) :
		# steps of GA
        #process of one generation
        #calcutlates the score of the new generation
        if(generations>=MAX_GEN_COUNT)
        	break
        score_population(programs, fitness_scores, worst_program_index, brainfuck);
        for i in range(0, POP_SIZE/2):
        	# select parents
        	parent1 = select_parent()
        	parent2 = select_parent()
            # crossover
        	child1, child2 = crossover(parent1, parent2)
        	children[i*2] = child1
        	children[i*2+1] = child2
        
        load_new_generation()
        generations++
