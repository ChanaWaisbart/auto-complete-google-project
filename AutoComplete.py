from data_manager.manager_program import ManagerProgram
import sys

if __name__ == '__main__':
    # path is the path to the main directory
    path = r"2021-archive"

    if len(sys.argv) != 1:
        sys.exit("Usage: AutoComplete.py")
    else:
        manager_program = ManagerProgram(path)
        manager_program.initialization()
        manager_program.run()
