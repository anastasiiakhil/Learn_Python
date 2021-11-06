import sys

a1 = sys.argv[1]
a2 = sys.argv[2]


def lucky_tickets(tickets_list):
    res = []
    for t in tickets_list:
        s1 = [int(i) for i in list(t[:3])]
        s2 = [int(i) for i in list(t[3:])]
        if sum(s1) is sum(s2):
            res.append(t)
    return res


def tickets(int_ticket):
    return [str(t).rjust(6, '0') for t in int_ticket]


def create_range(a1, a2):
    int_a1, int_a2 = int(a1), int(a2)
    if int_a1 >= 0 and int_a2 > int_a1 and int_a2 <= 999999:
        int_ticket = [i for i in range(int_a1, int_a2 + 1)]
        tickets_list = tickets(int_ticket)
        lucky = lucky_tickets(tickets_list)
        return len(lucky)


print(create_range(a1, a2))
