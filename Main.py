#create = make 
#calulate = compute


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


def mutate_instruction(string &program, unsigned index):
 	#replaces the present instruction at the given location by a random instruction
 	# The writer has written it in a wrong way. What if the get_random function returns the same instruction 
 	#program[index] = get_random_instruction();

def make_random_program() :
	# This function outputs a string of varibale length. 
    # Creates a random program by first randomly determining its size and then adding that many instructions randomly.

def initialize_population(string programs[]) :
    # Returns nothing. 
    # Creates the first generation's population by randomly creating programs.
    # Intialize Global Array of Strings()

def compute_fitness(string &program, Interpreter &bf) :
	#The Fitness Function. Determines how 'fit' a program is using a few different criteria.
	# Returns a Double 

def score_population(string programs[], double scores[], int &worst_index, Interpreter &bf) :
	#Generates a fitness score for each program in the population.
    #This is done by running the program through the brainfuck interpreter and scoring its output.
    #Also returns the best program produced. 

def compute_total_score(const double scores[]) :
    #returns a double
    # Adds every program's fitness score together.

def select_parent(const std::string programs[], const double scores[], const std::string &other_parent = "") :
    # returns a string(a parent for mating)
    # Selects a parent to mate using fitness proportionate selection.
    #Basically, the more fit a program is, the more likely it is to be selected.
    # We have to implement roulette wheel in this function, the writer has not implemented it.
 
def mutate(std::string child):
    # return a string (a child which has been mutated)
    # We have to write our own code for mutaion. Because we want it to be simple
    # But we can have a look at the writers code. 

def crossover(const std::string &parent1, const std::string &parent2, std::string children[]) :
    # returns nothing
    #Performs crossover between two parents to produce two children.

def genome_exists(const std::string &program, const std::string programs[]) :
	#returns a bool. Tells whether or not the Genome exists in the pool or not 

def load_new_generation() :
	# loads new genration into the pool from the child array. 

def main() :
	# main program responsible for running the GA
    
	#Initialize the brainfuck interpreter and seed random.
    Interpreter brainfuck
    srand(time(0))
    # Array of strings
    string programs[POP_SIZE]
    #Array of strings
    string children[POP_SIZE]
    # Array of double
    double fitness_scores[POP_SIZE]
    # Funtion call to initialize the population
    initialize_population(programs)
    # string which stores the best program
    std::string best_program
    #Just used to have the program keep searching after a match is found.
    bool keep_going = false  

    unsigned long generations = 0;
    
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
		
