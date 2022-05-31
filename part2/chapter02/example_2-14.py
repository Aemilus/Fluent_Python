"""
What happens below? Choose the best answer:
    a. t becomes (1, 2, [30, 40, 50, 60]).
    b. TypeError is raised with the message 'tuple' object does not support item assignment.
    c. Neither.
    d. Both a and b.

Use https://pythontutor.com/ to visualize the result.
"""
if __name__ == '__main__':
    t = (1, 2, [30, 40])
    try:
        t[2] += [50, 60]
    except Exception as e:
        print(e)
        print('t:', t)
    