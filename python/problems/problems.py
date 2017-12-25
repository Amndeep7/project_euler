from importlib import import_module
from timeit import default_timer as timer
import sys

def get_attempt(problem, attempt_ver):
    return getattr(problem, "attempt%s" % attempt_ver)

def get_args(problem):
    return getattr(problem, "ARGS")

def format_time(start, end):
    delta = end-start
    if delta < (1/1000)/100:
        return str(delta*10**9) + "ns"
    elif delta < 1:
        return str(delta*1000) + "ms"
    elif delta < 60*60:
        return str(round(delta//60)) + "m" + str(delta - delta//60*60) + "s"
    else:
        return str(delta) + "s"

# python3 problems.py num_problem num_attempt_version
def main():
    problem = import_module(sys.argv[1], "problems")
    start = timer()
    solution = get_attempt(problem, sys.argv[2])(get_args(problem))
    end = timer()
    print(solution)
    print(format_time(start, end))

if __name__ == "__main__":
    main()
