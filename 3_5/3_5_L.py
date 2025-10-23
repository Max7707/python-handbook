f_in = input()
f_even = input()
f_odd = input()
f_eq = input()

numbers = []
with open(f_in, encoding="UTF-8") as file_in:
    for line in file_in:
        line = line.split()

        ev = []
        odd = []
        eq = []
        for number in line:
            n = int(number)
            c_ev = 0
            c_odd = 0
            while n != 0:
                if (n % 10) % 2 == 0:
                    c_ev += 1
                elif (n % 10) % 2 == 1:
                    c_odd += 1
                n = n // 10
                
            if c_ev > c_odd:
                ev.append(number)
            if c_ev < c_odd:
                odd.append(number)
            if c_ev == c_odd:
                eq.append(number)

        with open(f_even, "a", encoding="UTF-8") as f_ev:
            f_ev.write(" ".join(ev) + "\n")
        with open(f_odd, "a", encoding="UTF-8") as f_od:
            f_od.write(" ".join(odd) + "\n")
        with open(f_eq, "a", encoding="UTF-8") as f_eqq:
            f_eqq.write(" ".join(eq) + "\n")
