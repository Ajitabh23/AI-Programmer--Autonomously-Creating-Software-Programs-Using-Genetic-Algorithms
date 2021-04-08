#!/usr/bin/python
#
# Brainfuck Interpreter
# Copyright 2011 Sebastian Kaspari
#
# Usage: ./brainfuck.py [FILE]

import sys
import getch
maxcycle=10000
def find_loop_match(dirc,ind,prog):
  loop_count=1
  tmp_inst=dirc+ind
  while loop_count>0:
    if tmp_inst < 0 or tmp_inst >= len(prog):
      return False
    c = prog[tmp_inst]
    if c == '[':
      if dirc > 0:
        loop_count =loop_count+1
      else:
        loop_count =loop_count-1
    elif c == ']':
      if dirc > 0:
        loop_count =loop_count-1
      else:
        loop_count =loop_count+1


    tmp_inst =tmp_inst+dirc
    

  return True
  

def checksyntax(prog):
  for i in range(len(prog)):
    if prog[i] == '[':
      if find_loop_match(1,i,prog)!=True:
	return False
    elif prog[i] == ']':
      if find_loop_match(-1,i,prog)!=True:
        return False 	
  #print("err")		
  return True

 

def evaluate(code):
  #if checksyntax(code)==False:
  #  return "Error"
  tot_cyc=0
	
  ans=""
  code     = cleanup(list(code))
  bracemap = buildbracemap(code)
  #print(code)
 
  cells, codeptr, cellptr = [0], 0, 0

  while codeptr < len(code):
    if tot_cyc>maxcycle:
      return "Error"
	
    command = code[codeptr]

    if command == ">":
      cellptr += 1
      if cellptr == len(cells): cells.append(0)

    if command == "<":
      cellptr = 0 if cellptr <= 0 else cellptr - 1

    if command == "+":
      cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

    if command == "-":
      cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

    if command == "[" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
    if command == "]" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
    #if command == ".": sys.stdout.write(chr(cells[cellptr]))
    if command == ".": 
	ans=ans+chr(cells[cellptr])
	#sys.stdout.write(chr(cells[cellptr]))
    if command == ",": cells[cellptr] = ord(getch.getch())
      
    codeptr =codeptr+ 1
    tot_cyc=tot_cyc+1
	
  return ans	

  
def cleanup(code):
  return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def buildbracemap(code):
  temp_bracestack, bracemap = [], {}

  for position, command in enumerate(code):
    if command == "[": temp_bracestack.append(position)
    if command == "]":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
  return bracemap

def main():
  #if len(sys.argv) == 2: execute(sys.argv[1])
  #else: print("Usage:", sys.argv[0], "filename")
  prog="+[+++++-+>++>++-++++++<<]>++.[+.]]"
  ans=evaluate(prog)
  print(ans)
  

if __name__ == "__main__": main()
