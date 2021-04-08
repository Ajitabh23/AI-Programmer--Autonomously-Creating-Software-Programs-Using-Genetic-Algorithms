import brainfuck
def main():
  sourcecode = """++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."""
	
	
  ans=brainfuck.evaluate(sourcecode)
  print(ans)
if __name__ == "__main__": main()