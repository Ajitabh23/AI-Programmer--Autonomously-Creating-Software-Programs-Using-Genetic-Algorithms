#jastabh
#malteek
#create = make 
#calulate = compute

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

def main() :
	# main program responsible for running the GA

	while(1) :
		# steps of GA
		
