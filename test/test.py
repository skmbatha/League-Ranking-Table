import os

# Get project directory
baseDir=os.getcwd().split('/')
baseDir.pop()
baseDir='/'.join(baseDir)

if __name__ == "__main__":
    
    # Test 1 - 1st test as provided in documentation (test 1.txt)
    print("Test 1 output:")
    os.system("python3 \'{}/rankGames.py\' \'test 1.txt\'".format(baseDir))
    print()
    
    # Test 2 - Test using a constum random generated test file (test 2.txt)
    print("Test 2 output:")
    os.system("python3 \'{}/rankGames.py\' \'test 2.txt\'".format(baseDir))
    print()
    
    # Test 3 - Test with longer names and entry repetitions (test 3.txt)
    print("Test 3 output:")
    os.system("python3 \'{}/rankGames.py\' \'test 3.txt\'".format(baseDir))
    print()
    
    # Test 4 - Test if the program can take multiple test file names as an input
    print("Test 4 output:")
    os.system("python3 \'{}/rankGames.py\' \'test 1.txt\' 'test 2.txt\' ".format(baseDir))
    print() 
    