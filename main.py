from tkinter import *
from tkinter import ttk

extremos = ['[', ']']


def f_intersecao():
    a = interA1.get()
    b = interA2.get()
    c = interB1.get()
    d = interB2.get()
    ea = extA1.get()
    eb = extA2.get()
    ec = extB1.get()
    ed = extB2.get()

    if (a != "-∞"):
        a = float(a)
    else:
        ea = "]"
    if (b != "+∞"):
        b = float(b)
    else:
        eb = "["
    if (c != "-∞"):
        c = float(c)
    else:
        ec = "]"
    if (d != "+∞"):
        d = float(d)
    else:
        ed = "["

    if isinstance(a, float) and isinstance(b, float) and isinstance(c, float) and isinstance(d, float):

        if (a >= b or c >= d):
            resposta["text"] = "DIGITE UM INTERVALO VÁLIDO:"

        elif (a < c and a < d and b > c and b > d):  # caso 1
            resposta["text"] = "A ∩ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a > c and a < d and b > c and b < d):  # caso 2
            resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a < c and a < d and b > c and b < d):  # caso 3
            resposta["text"] = "A ∩ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a > c and a < d and b > c and b > d):  # caso 4
            resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a < c and a < d and b < c and b < d):  # caso 5
            resposta["text"] = "A ∩ B = Ø"

        elif (a > c and a > d and b > c and b > d):  # caso 6
            resposta["text"] = "A ∩ B = Ø"

        elif (a == c and a < d and b > c and b < d):  # caso 7
            if (ea == ec and ea == "["):
                r1 = "["
            else:
                r1 = "]"
            resposta["text"] = "A ∩ B = " + str(r1) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a == c and a < d and b > c and b > d):  # caso 8
            if (ea == ec and ea == "["):
                r1 = "["
            else:
                r1 = "]"
            resposta["text"] = "A ∩ B = " + str(r1) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a < c and a < d and b > c and b == d):  # caso 9
            if (eb == ed and eb == "]"):
                r1 = "]"
            else:
                r1 = "["
            resposta["text"] = "A ∩ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(r1)

        elif (a > c and a < d and b > c and b == d):  # caso 10
            if (eb == ed and eb == "]"):
                r1 = "]"
            else:
                r1 = "["
            resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(r1)

        elif (a < c and a < d and b == c and b < d):  # caso 11
            if (eb == "]" and ec == "["):
                resposta["text"] = "A ∩ B = " + "{" + " " + str(b) + " " + "}"
            else:
                resposta["text"] = "A ∩ B = Ø"

        elif (a > c and a == d and b > c and b > d):  # caso 12
            if (ea == "[" and ed == "]"):
                resposta["text"] = "A ∩ B = " + "{" + " " + str(a) + " " + "}"
            else:
                resposta["text"] = "A ∩ B = Ø"

        elif (a == c and a < d and b > c and b == d):  # caso 13
            if (ea == "[" and ec == "["):
                r1 = "["
            else:
                r1 = "]"
            if (eb == "]" and ed == "]"):
                r2 = "]"
            else:
                r2 = "["
            resposta["text"] = "A ∩ B = " + str(r1) + " " + str(a) + " " + "," + " " + str(b) + " " + str(r2)

    elif (isinstance(a, float) and b == "+∞" and c == "-∞" and d == "+∞"):  # caso 14
        resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + "+∞" + " " + str(eb)

    elif (isinstance(a, float) and isinstance(b, float) and c == "-∞" and d == "+∞" and a < b):  # caso 15
        resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (isinstance(a, float) and isinstance(b, float) and isinstance(c, float) and d == "+∞" and a < b):  # caso 16
        if c < a:
            resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if c > a and c < b:
            resposta["text"] = "A ∩ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)
        if c > b:
            resposta["text"] = "A ∩ B = Ø"
        if c == a:
            if (ea == ec and ea == "["):
                r1 = "["
            else:
                r1 = "]"
            resposta["text"] = "A ∩ B = " + str(r1) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if c == b:
            if (eb == "]" and ec == "["):
                resposta["text"] = "A ∩ B = " + "{" + " " + str(b) + " " + "}"
            else:
                resposta["text"] = "A ∩ B = Ø"

    elif (a == "-∞" and isinstance(b, float) and c == "-∞" and d == "+∞"):  # caso 17
        resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (a == "-∞" and isinstance(b, float) and isinstance(c, float) and d == "+∞"):  # caso 18
        if b == c:
            if (eb == "]" and ec == "["):
                resposta["text"] = "A ∩ B = " + "{" + " " + str(b) + " " + "}"
            else:
                resposta["text"] = "A ∩ B = Ø"
        if b > c:
            resposta["text"] = "A ∩ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)
        if b < c:
            resposta["text"] = "A ∩ B = Ø"

    elif (a == "-∞" and isinstance(b, float) and isinstance(c, float) and isinstance(d, float) and c < d):  # caso 19
        if b > c and b < d:
            resposta["text"] = "A ∩ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)
        if b == d:
            if (eb == ed and eb == "]"):
                r1 = "]"
            else:
                r1 = "["
            resposta["text"] = "A ∩ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(r1)
        if b == c:
            if (eb == "]" and ec == "["):
                resposta["text"] = "A ∩ B = " + "{" + " " + str(b) + " " + "}"
            else:
                resposta["text"] = "A ∩ B = Ø"
        if b > d:
            resposta["text"] = "A ∩ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)
        if b < c:
            resposta["text"] = "A ∩ B = Ø"

    elif (a == "-∞" and b == "+∞" and isinstance(c, float) and d == "+∞"):  # caso 20
        resposta["text"] = "A ∩ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)

    elif (a == "-∞" and b == "+∞" and isinstance(c, float) and isinstance(d, float) and c < d):  # caso 21
        resposta["text"] = "A ∩ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

    elif (a == "-∞" and b == "+∞" and c == "-∞" and isinstance(d, float)):  # caso 22
        resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)

    elif (isinstance(a, float) and b == "+∞" and c == "-∞" and isinstance(d, float)):  # caso 23
        if a < d:
            resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)
        if a == d:
            if (ea == "[" and ed == "]"):
                resposta["text"] = "A ∩ B = " + "{" + " " + str(a) + " " + "}"
            else:
                resposta["text"] = "A ∩ B = Ø"
        if a > d:
            resposta["text"] = "A ∩ B = Ø"

    elif (isinstance(a, float) and isinstance(b, float) and c == "-∞" and isinstance(d, float) and a < b):  # caso 24
        if a < d and b > d:
            resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)
        if a == d:
            if (ea == "[" and ed == "]"):
                resposta["text"] = "A ∩ B = " + "{" + " " + str(a) + " " + "}"
            else:
                resposta["text"] = "A ∩ B = Ø"
        if b == d:
            if (eb == ed and eb == "]"):
                r1 = "]"
            else:
                r1 = "["
            resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(r1)
        if d < a:
            resposta["text"] = "A ∩ B = Ø"

    elif (a == "-∞" and isinstance(b, float) and c == "-∞" and isinstance(d, float)):  # caso 25
        if b > d:
            resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)
        if b < d:
            resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if b == d:
            if (eb == "]" and ed == "]"):
                r2 = "]"
            else:
                r2 = "["
            resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(r2)

    elif (isinstance(a, float) and b == "+∞" and isinstance(c, float) and d == "+∞"):  # caso 26
        if a < c:
            resposta["text"] = "A ∩ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)
        if a > c:
            resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if a == c:
            if (ea == "[" and ec == "["):
                r1 = "["
            else:
                r1 = "]"
            resposta["text"] = "A ∩ B = " + str(r1) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (isinstance(a, float) and b == "+∞" and isinstance(c, float) and isinstance(d, float) and c < d):  # caso 27
        if a < c and a < d:
            resposta["text"] = "A ∩ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)
        if a > c and a < d:
            resposta["text"] = "A ∩ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)
        if a == c:
            if (ea == ec and ea == "["):
                r1 = "["
            else:
                r1 = "]"
            resposta["text"] = "A ∩ B = " + str(r1) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)
        if a == d:
            if (ea == "[" and ed == "]"):
                resposta["text"] = "A ∩ B = " + "{" + " " + str(a) + " " + "}"
            else:
                resposta["text"] = "A ∩ B = Ø"
        if a > d:
            resposta["text"] = "A ∩ B = Ø"

    elif (a == "-∞" and b == "+∞" and c == "-∞" and d == "+∞"):  # caso 28
        resposta["text"] = "A ∩ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

    else:
        resposta["text"] = "Falta esse caso"


def f_uniao():
    a = interA1.get()
    b = interA2.get()
    c = interB1.get()
    d = interB2.get()
    ea = extA1.get()
    eb = extA2.get()
    ec = extB1.get()
    ed = extB2.get()

    if (a != "-∞"):
        a = float(a)
    else:
        ea = "]"
    if (b != "+∞"):
        b = float(b)
    else:
        eb = "["
    if (c != "-∞"):
        c = float(c)
    else:
        ec = "]"
    if (d != "+∞"):
        d = float(d)
    else:
        ed = "["

    if isinstance(a, float) and isinstance(b, float) and isinstance(c, float) and isinstance(d, float):

        if (a >= b or c >= d):
            resposta["text"] = "DIGITE UM INTERVALO VÁLIDO:"

        elif (a < c and a < d and b > c and b > d):  # caso 1
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a > c and a < d and b > c and b < d):  # caso 2
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a < c and a < d and b > c and b < d):  # caso 3
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a > c and a < d and b > c and b > d):  # caso 4
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a < c and a < d and b < c and b < d):  # caso 5
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(
                eb) + " " + "∪" + " " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a > c and a > d and b > c and b > d):  # caso 6
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(
                ed) + " " + "∪" + " " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a == c and a < d and b > c and b < d):  # caso 7
            if (ea == "[" or ec == "["):
                r1 = "["
            else:
                r1 = "]"
            resposta["text"] = "A ∪ B = " + str(r1) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a == c and a < d and b > c and b > d):  # caso 8
            if (ea == "[" or ec == "["):
                r1 = "["
            else:
                r1 = "]"
            resposta["text"] = "A ∪ B = " + str(r1) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a < c and a < d and b > c and b == d):  # caso 9
            if (eb == "]" or ed == "]"):
                r1 = "]"
            else:
                r1 = "["
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(r1)

        elif (a > c and a < d and b > c and b == d):  # caso 10
            if (eb == "]" or ed == "]"):
                r1 = "]"
            else:
                r1 = "["
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(r1)

        elif (a < c and a < d and b == c and b < d):  # caso 11
            if (eb == "[" and ec == "]"):
                resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(
                    eb) + " " + "∪" + " " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)
            else:
                resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a > c and a == d and b > c and b > d):  # caso 12
            if (ea == "]" and ed == "["):
                resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(
                    ed) + " " + "∪" + " " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
            else:
                resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a == c and a < d and b > c and b == d):  # caso 13
            if (ea == "[" or ec == "["):
                r1 = "["
            else:
                r1 = "]"
            if (eb == "]" or ed == "]"):
                r2 = "]"
            else:
                r2 = "["
            resposta["text"] = "A ∪ B = " + str(r1) + " " + str(a) + " " + "," + " " + str(b) + " " + str(r2)

    elif (isinstance(a, float) and b == "+∞" and c == "-∞" and d == "+∞"):  # caso 14
        resposta["text"] = "A ∪ B = ] -∞ , +∞ [ "

    elif (isinstance(a, float) and isinstance(b, float) and c == "-∞" and d == "+∞" and a < b):  # caso 15
        resposta["text"] = "A ∪ B = ] -∞ , +∞ [ "

    elif (isinstance(a, float) and isinstance(b, float) and isinstance(c, float) and d == "+∞" and a < b):  # caso 16
        if c < a:
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)
        if c > a and c < b:
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)
        if c > b:
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(
                eb) + " " + "∪" + " " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)
        if c == a:
            if (ea == "[" or ec == "["):
                r1 = "["
            else:
                r1 = "]"
            resposta["text"] = "A ∪ B = " + str(r1) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)
        if c == b:
            if (eb == "[" and ec == "]"):
                resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(
                    eb) + " " + "∪" + " " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)
            else:
                resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)

    elif (a == "-∞" and isinstance(b, float) and c == "-∞" and d == "+∞"):  # caso 17
        resposta["text"] = "A ∪ B = ] -∞ , +∞ [ "

    elif (a == "-∞" and isinstance(b, float) and isinstance(c, float) and d == "+∞"):  # caso 18
        if b == c:
            if (eb == "[" and ec == "]"):
                resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(
                    eb) + " " + "∪" + " " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)
            else:
                resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)
        if b > c:
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)
        if b < c:
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(
                ed) + " " + "∪" + " " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (a == "-∞" and isinstance(b, float) and isinstance(c, float) and isinstance(d, float) and c < d):  # caso 19
        if b > c and b < d:
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)
        if b == c:
            if (eb == "[" and ec == "]"):
                resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(
                    eb) + " " + "∪" + " " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)
            else:
                resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)
        if b == d:
            if (eb == "]" or ed == "]"):
                r1 = "]"
            else:
                r1 = "["
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(r1)
        if b > d:
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if b < c:
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(
                ed) + " " + "∪" + " " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (a == "-∞" and b == "+∞" and isinstance(c, float) and d == "+∞"):  # caso 20
        resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (a == "-∞" and b == "+∞" and isinstance(c, float) and isinstance(d, float) and c < d):  # caso 21
        resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (a == "-∞" and b == "+∞" and c == "-∞" and isinstance(d, float)):  # caso 22
        resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (isinstance(a, float) and b == "+∞" and c == "-∞" and isinstance(d, float)):  # caso 23
        if a < d:
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)
        if a == d:
            if (ea == "]" and ed == "["):
                resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(
                    ed) + " " + "∪" + " " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
            else:
                resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)
        if a > d:
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(
                ed) + " " + "∪" + " " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (isinstance(a, float) and isinstance(b, float) and c == "-∞" and isinstance(d, float) and a < b):  # caso 24
        if a < d and b > d:
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)
        if a == d:
            if (ea == "]" and ed == "["):
                resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(
                    ed) + " " + "∪" + " " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
            else:
                resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)
        if b == d:
            if (eb == "]" or ed == "]"):
                r1 = "]"
            else:
                r1 = "["
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(r1)
        if d < a:
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(
                ed) + " " + "∪" + " " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (a == "-∞" and isinstance(b, float) and c == "-∞" and isinstance(d, float)):  # caso 25
        if b > d:
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if b < d:
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(d) + " " + str(ed)
        if b == d:
            if (eb == "]" or ed == "]"):
                r2 = "]"
            else:
                r2 = "["
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(r2)

    elif (isinstance(a, float) and b == "+∞" and isinstance(c, float) and d == "+∞"):  # caso 26
        if a < c:
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if a > c:
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)
        if a == c:
            if (ea == "[" or ec == "["):
                r1 = "["
            else:
                r1 = "]"
            resposta["text"] = "A ∪ B = " + str(r1) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (isinstance(a, float) and b == "+∞" and isinstance(c, float) and isinstance(d, float) and c < d):  # caso 27
        if a < c and a < d:
            resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if a > c and a < d:
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)
        if a == c:
            if (ea == "[" or ec == "["):
                r1 = "["
            else:
                r1 = "]"
            resposta["text"] = "A ∪ B = " + str(r1) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if a == d:
            if (ea == "]" and ed == "["):
                resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(
                    ed) + " " + "∪" + " " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
            else:
                resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(b) + " " + str(eb)
        if a > d:
            resposta["text"] = "A ∪ B = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(
                ed) + " " + "∪" + " " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (a == "-∞" and b == "+∞" and c == "-∞" and d == "+∞"):  # caso 28
        resposta["text"] = "A ∪ B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    else:
        resposta["text"] = "Falta esse caso"


def f_AB():
    a = interA1.get()
    b = interA2.get()
    c = interB1.get()
    d = interB2.get()
    ea = extA1.get()
    eb = extA2.get()
    ec = extB1.get()
    ed = extB2.get()

    if (a != "-∞"):
        a = float(a)
    else:
        ea = "]"
    if (b != "+∞"):
        b = float(b)
    else:
        eb = "["
    if (c != "-∞"):
        c = float(c)
    else:
        ec = "]"
    if (d != "+∞"):
        d = float(d)
    else:
        ed = "["

    if isinstance(a, float) and isinstance(b, float) and isinstance(c, float) and isinstance(d, float):

        if (a >= b or c >= d):
            resposta["text"] = "DIGITE UM INTERVALO VÁLIDO:"

        elif (a < c and a < d and b > c and b > d):  # caso 1
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(
                ec) + " " + "∪" + " " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a > c and a < d and b > c and b < d):  # caso 2
            resposta["text"] = "A - B = Ø"

        elif (a < c and a < d and b > c and b < d):  # caso 3
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(ec)

        elif (a > c and a < d and b > c and b > d):  # caso 4
            resposta["text"] = "A - B = " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a < c and a < d and b < c and b < d):  # caso 5
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a > c and a > d and b > c and b > d):  # caso 6
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a == c and a < d and b > c and b < d):  # caso 7
            if (ea == "[" and ec == "]"):
                resposta["text"] = "A - B = " + "{" + " " + str(a) + " " + "}"
            else:
                resposta["text"] = "A - B = Ø"

        elif (a == c and a < d and b > c and b > d):  # caso 8
            if (ea == "[" and ec == "]"):
                resposta["text"] = "A - B = " + "{" + " " + str(a) + " " + "}" + " " + "∪" + " " + str(ed) + " " + str(
                    d) + " " + "," + " " + str(b) + " " + str(eb)
            else:
                resposta["text"] = "A - B = " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a < c and a < d and b > c and b == d):  # caso 9
            if (eb == "]" and ed == "["):
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(
                    ec) + " " + "∪" + " " + "{" + " " + str(b) + " " + "}"
            else:
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(ec)

        elif (a > c and a < d and b > c and b == d):  # caso 10
            if (eb == "]" and ed == "["):
                resposta["text"] = "A - B = " + "{" + " " + str(b) + " " + "}"
            else:
                resposta["text"] = "A - B = Ø"

        elif (a < c and a < d and b == c and b < d):  # caso 11
            if (eb == "]" and ec == "["):
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(ec)
            else:
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a > c and a == d and b > c and b > d):  # caso 12
            if (ea == "[" and ed == "]"):
                resposta["text"] = "A - B = " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)
            else:
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

        elif (a == c and a < d and b > c and b == d):  # caso 13
            if (ea == "[" and eb == "]"):
                if (ec == "]" and ed == "["):
                    resposta["text"] = "A - B = " "{" + " " + str(a) + " " + "," + " " + str(b) + " " + "}"
                if (ec == "[" and ed == "["):
                    resposta["text"] = "A - B = " "{" + " " + str(b) + "}"
                if (ec == "]" and ed == "]"):
                    resposta["text"] = "A - B = " "{" + " " + str(a) + "}"
                if (ec == "[" and ed == "]"):
                    resposta["text"] = "A - B = Ø"
            elif (ea == "[" and eb == "["):
                if (ec == "]"):
                    resposta["text"] = "A - B = " "{" + " " + str(a) + "}"
                else:
                    resposta["text"] = "A - B = Ø"
            elif (ea == "]" and eb == "]"):
                if (ed == "["):
                    resposta["text"] = "A - B = " "{" + " " + str(b) + "}"
                else:
                    resposta["text"] = "A - B = Ø"
            else:
                resposta["text"] = "A - B = Ø"

    elif (isinstance(a, float) and b == "+∞" and c == "-∞" and d == "+∞"):  # caso 14
        resposta["text"] = "A - B = Ø "

    elif (isinstance(a, float) and isinstance(b, float) and c == "-∞" and d == "+∞" and a < b):  # caso 15
        resposta["text"] = "A - B = Ø "

    elif (isinstance(a, float) and isinstance(b, float) and isinstance(c, float) and d == "+∞" and a < b):  # caso 16
        if c < a:
            resposta["text"] = "A - B = Ø "
        if c > a and c < b:
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(ec)
        if c > b:
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if c == a:
            if (ea == "[" and ec == "]"):
                resposta["text"] = "A - B = " + "{" + " " + str(a) + " " + "}"
            else:
                resposta["text"] = "A - B = Ø"
        if c == b:
            if (eb == "]" and ec == "["):
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(ec)
            else:
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (a == "-∞" and isinstance(b, float) and c == "-∞" and d == "+∞"):  # caso 17
        resposta["text"] = "A - B = Ø "

    elif (a == "-∞" and isinstance(b, float) and isinstance(c, float) and d == "+∞"):  # caso 18
        if b == c:
            if (eb == "]" and ec == "["):
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(ec)
            else:
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if b > c:
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(ec)
        if b < c:
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (a == "-∞" and isinstance(b, float) and isinstance(c, float) and isinstance(d, float) and c < d):  # caso 19
        if b > c and b < d:
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(ec)
        if b == c:
            if (eb == "]" and ec == "["):
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(ec)
            else:
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if b == d:
            if (eb == "]" and ed == "["):
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(
                    ec) + " " + "∪" + " " + "{" + " " + str(b) + " " + "}"
            else:
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(ec)
        if b > d:
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(
                ec) + " " + "∪" + " " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)
        if b < c:
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (a == "-∞" and b == "+∞" and isinstance(c, float) and d == "+∞"):  # caso 20
        resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(ec)

    elif (a == "-∞" and b == "+∞" and isinstance(c, float) and isinstance(d, float) and c < d):  # caso 21
        resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(
            ec) + " " + "∪" + " " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)

    elif (a == "-∞" and b == "+∞" and c == "-∞" and isinstance(d, float)):  # caso 22
        resposta["text"] = "A - B = " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)

    elif (isinstance(a, float) and b == "+∞" and c == "-∞" and isinstance(d, float)):  # caso 23
        if a < d:
            resposta["text"] = "A - B = " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)
        if a == d:
            if (ea == "[" and ed == "]"):
                resposta["text"] = "A - B = " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)
            else:
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if a > d:
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (isinstance(a, float) and isinstance(b, float) and c == "-∞" and isinstance(d, float) and a < b):  # caso 24
        if a < d and b > d:
            resposta["text"] = "A - B = " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)
        if a == d:
            if (ea == "[" and ed == "]"):
                resposta["text"] = "A - B = " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)
            else:
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if b == d:
            if (eb == "]" and ed == "["):
                resposta["text"] = "A - B = " + "{" + " " + str(b) + " " + "}"
            else:
                resposta["text"] = "A - B = Ø"
        if d < a:
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (a == "-∞" and isinstance(b, float) and c == "-∞" and isinstance(d, float)):  # caso 25
        if b > d:
            resposta["text"] = "A - B = " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)
        if b < d:
            resposta["text"] = "A - B = Ø"
        if b == d:
            if (eb == "]" and ed == "["):
                resposta["text"] = "A - B = " + "{" + " " + str(b) + " " + "}"
            else:
                resposta["text"] = "A - B = Ø"

    elif (isinstance(a, float) and b == "+∞" and isinstance(c, float) and d == "+∞"):  # caso 26
        if a < c:
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(ec)
        if a > c:
            resposta["text"] = "A - B = Ø"
        if a == c:
            if (ea == "[" and ec == "]"):
                resposta["text"] = "A - B = " + "{" + " " + str(a) + " " + "}"
            else:
                resposta["text"] = "A - B = Ø"

    elif (isinstance(a, float) and b == "+∞" and isinstance(c, float) and isinstance(d, float) and c < d):  # caso 27
        if a < c and a < d:
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(c) + " " + str(
                ec) + " " + "∪" + " " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)
        if a > c and a < d:
            resposta["text"] = "A - B = " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)
        if a == c:
            if (ea == "[" and ec == "]"):
                resposta["text"] = "A - B = " + "{" + " " + str(a) + " " + "}" + " " + "∪" + " " + str(ed) + " " + str(
                    d) + " " + "," + " " + str(b) + " " + str(eb)
            else:
                resposta["text"] = "A - B = " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)
        if a == d:
            if (ea == "[" and ed == "]"):
                resposta["text"] = "A - B = " + str(ed) + " " + str(d) + " " + "," + " " + str(b) + " " + str(eb)
            else:
                resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)
        if a > d:
            resposta["text"] = "A - B = " + str(ea) + " " + str(a) + " " + "," + " " + str(b) + " " + str(eb)

    elif (a == "-∞" and b == "+∞" and c == "-∞" and d == "+∞"):  # caso 28
        resposta["text"] = "A - B = Ø"

    else:
        resposta["text"] = "Falta esse caso"


def f_BA():
    a = interA1.get()
    b = interA2.get()
    c = interB1.get()
    d = interB2.get()
    ea = extA1.get()
    eb = extA2.get()
    ec = extB1.get()
    ed = extB2.get()

    if (a != "-∞"):
        a = float(a)
    else:
        ea = "]"
    if (b != "+∞"):
        b = float(b)
    else:
        eb = "["
    if (c != "-∞"):
        c = float(c)
    else:
        ec = "]"
    if (d != "+∞"):
        d = float(d)
    else:
        ed = "["

    if isinstance(a, float) and isinstance(b, float) and isinstance(c, float) and isinstance(d, float):

        if (a >= b or c >= d):
            resposta["text"] = "DIGITE UM INTERVALO VÁLIDO:"

        elif (a < c and a < d and b > c and b > d):  # caso 1
            resposta["text"] = "B - A = Ø "

        elif (a > c and a < d and b > c and b < d):  # caso 2
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(
                ea) + " " + "∪" + " " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a < c and a < d and b > c and b < d):  # caso 3
            resposta["text"] = "B - A = " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a > c and a < d and b > c and b > d):  # caso 4
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(ea)

        elif (a < c and a < d and b < c and b < d):  # caso 5
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a > c and a > d and b > c and b > d):  # caso 6
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a == c and a < d and b > c and b < d):  # caso 7
            if (ec == "[" and ea == "]"):
                resposta["text"] = "B - A = " + "{" + " " + str(c) + " " + "}" + " " + "∪" + " " + str(eb) + " " + str(
                    b) + " " + "," + " " + str(d) + " " + str(ed)
            else:
                resposta["text"] = "B - A = " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a == c and a < d and b > c and b > d):  # caso 8
            if (ec == "[" and ea == "]"):
                resposta["text"] = "B - A = " + "{" + " " + str(c) + " " + "}"
            else:
                resposta["text"] = "B - A = Ø"

        elif (a < c and a < d and b > c and b == d):  # caso 9
            if (ed == "]" and eb == "["):
                resposta["text"] = "B - A = " + "{" + " " + str(d) + " " + "}"
            else:
                resposta["text"] = "B - A = Ø"

        elif (a > c and a < d and b > c and b == d):  # caso 10
            if (ed == "]" and eb == "["):
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(
                    ea) + " " + "∪" + " " + "{" + " " + str(d) + " " + "}"
            else:
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(ea)

        elif (a < c and a < d and b == c and b < d):  # caso 11
            if (ec == "[" and eb == "]"):
                resposta["text"] = "B - A = " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)
            else:
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a > c and a == d and b > c and b > d):  # caso 12
            if (ea == "[" and ed == "]"):
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(ea)
            else:
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

        elif (a == c and a < d and b > c and b == d):  # caso 13
            if (ec == "[" and ed == "]"):
                if (ea == "]" and eb == "["):
                    resposta["text"] = "B - A = " "{" + " " + str(c) + " " + "," + " " + str(d) + " " + "}"
                if (ea == "[" and eb == "["):
                    resposta["text"] = "B - A = " "{" + " " + str(d) + "}"
                if (ea == "]" and eb == "]"):
                    resposta["text"] = "B - A = " "{" + " " + str(c) + "}"
                if (ea == "[" and eb == "]"):
                    resposta["text"] = "B - A = Ø"
            elif (ec == "[" and ed == "["):
                if (ea == "]"):
                    resposta["text"] = "B - A = " "{" + " " + str(c) + "}"
                else:
                    resposta["text"] = "B - A = Ø"
            elif (ec == "]" and ed == "]"):
                if (eb == "["):
                    resposta["text"] = "B - A = " "{" + " " + str(d) + "}"
                else:
                    resposta["text"] = "B - A = Ø"
            else:
                resposta["text"] = "B - A = Ø"

    elif (isinstance(a, float) and b == "+∞" and c == "-∞" and d == "+∞"):  # caso 14
        resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(ea)

    elif (isinstance(a, float) and isinstance(b, float) and c == "-∞" and d == "+∞" and a < b):  # caso 15
        resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(
            ea) + " " + "∪" + " " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)

    elif (isinstance(a, float) and isinstance(b, float) and isinstance(c, float) and d == "+∞" and a < b):  # caso 16
        if c < a:
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(
                ea) + " " + "∪" + " " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)
        if c > a and c < b:
            resposta["text"] = "B - A = " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)
        if c > b:
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)
        if c == a:
            if (ec == "[" and ea == "]"):
                resposta["text"] = "B - A = " + "{" + " " + str(c) + " " + "}" + " " + "∪" + " " + str(eb) + " " + str(
                    b) + " " + "," + " " + str(d) + " " + str(ed)
            else:
                resposta["text"] = "B - A = " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)
        if c == b:
            if (ec == "[" and eb == "]"):
                resposta["text"] = "B - A = " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)
            else:
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

    elif (a == "-∞" and isinstance(b, float) and c == "-∞" and d == "+∞"):  # caso 17
        resposta["text"] = "B - A = " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)

    elif (a == "-∞" and isinstance(b, float) and isinstance(c, float) and d == "+∞"):  # caso 18
        if b == c:
            if (ec == "[" and eb == "]"):
                resposta["text"] = "B - A = " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)
            else:
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)
        if b > c:
            resposta["text"] = "B - A = " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)
        if b < c:
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

    elif (a == "-∞" and isinstance(b, float) and isinstance(c, float) and isinstance(d, float) and c < d):  # caso 19
        if b > c and b < d:
            resposta["text"] = "B - A = " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)
        if b == c:
            if (ec == "[" and eb == "]"):
                resposta["text"] = "B - A = " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)
            else:
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)
        if b == d:
            if (ed == "]" and eb == "["):
                resposta["text"] = "B - A = " + "{" + " " + str(d) + " " + "}"
            else:
                resposta["text"] = "B - A = Ø"
        if b > d:
            resposta["text"] = "B - A = Ø "
        if b < c:
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

    elif (a == "-∞" and b == "+∞" and isinstance(c, float) and d == "+∞"):  # caso 20
        resposta["text"] = "B - A = Ø"

    elif (a == "-∞" and b == "+∞" and isinstance(c, float) and isinstance(d, float) and c < d):  # caso 21
        resposta["text"] = "B - A = Ø "

    elif (a == "-∞" and b == "+∞" and c == "-∞" and isinstance(d, float)):  # caso 22
        resposta["text"] = "B - A = Ø"

    elif (isinstance(a, float) and b == "+∞" and c == "-∞" and isinstance(d, float)):  # caso 23
        if a < d:
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(ea)
        if a == d:
            if (ea == "[" and ed == "]"):
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(ea)
            else:
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)
        if a > d:
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

    elif (isinstance(a, float) and isinstance(b, float) and c == "-∞" and isinstance(d, float) and a < b):  # caso 24
        if a < d and b > d:
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(ea)
        if a == d:
            if (ea == "[" and ed == "]"):
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(ea)
            else:
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)
        if b == d:
            if (ed == "]" and eb == "["):
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(
                    ea) + " " + "∪" + " " + "{" + " " + str(d) + " " + "}"
            else:
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(ea)
        if d < a:
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

    elif (a == "-∞" and isinstance(b, float) and c == "-∞" and isinstance(d, float)):  # caso 25
        if b > d:
            resposta["text"] = "B - A = Ø"
        if b < d:
            resposta["text"] = "B - A = " + str(eb) + " " + str(b) + " " + "," + " " + str(d) + " " + str(ed)
        if b == d:
            if (ed == "]" and eb == "["):
                resposta["text"] = "A - B = " + "{" + " " + str(b) + " " + "}"
            else:
                resposta["text"] = "A - B = Ø"

    elif (isinstance(a, float) and b == "+∞" and isinstance(c, float) and d == "+∞"):  # caso 26
        if a < c:
            resposta["text"] = "B - A = Ø"
        if a > c:
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(ea)
        if a == c:
            if (ec == "[" and ea == "]"):
                resposta["text"] = "A - B = " + "{" + " " + str(c) + " " + "}"
            else:
                resposta["text"] = "A - B = Ø"

    elif (isinstance(a, float) and b == "+∞" and isinstance(c, float) and isinstance(d, float) and c < d):  # caso 27
        if a < c and a < d:
            resposta["text"] = "B - A = Ø "
        if a > c and a < d:
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(ea)
        if a == c:
            if (ec == "[" and ea == "]"):
                resposta["text"] = "B - A = " + "{" + " " + str(c) + " " + "}"
            else:
                resposta["text"] = "B - A = Ø"
        if a == d:
            if (ea == "[" and ed == "]"):
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(a) + " " + str(ea)
            else:
                resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)
        if a > d:
            resposta["text"] = "B - A = " + str(ec) + " " + str(c) + " " + "," + " " + str(d) + " " + str(ed)

    elif (a == "-∞" and b == "+∞" and c == "-∞" and d == "+∞"):  # caso 28
        resposta["text"] = "B - A = Ø"

    else:
        resposta["text"] = "Falta esse caso"


def resetar():
    A1.set("-∞")
    A2.set("+∞")
    B1.set("-∞")
    B2.set("+∞")

    if A1.get() == "-∞":
        eA1.set("]")
    if A2.get() == "+∞":
        eA2.set("[")
    if B1.get() == "-∞":
        eB1.set("]")
    if B2.get() == "+∞":
        eB2.set("[")


janela = Tk()

janela.title("Intervalos")
janela.geometry("230x300")

A1 = StringVar()
A1.set("-∞")

A2 = StringVar()
A2.set("+∞")

B1 = StringVar()
B1.set("-∞")

B2 = StringVar()
B2.set("+∞")

eA1 = StringVar()
eA2 = StringVar()
eB1 = StringVar()
eB2 = StringVar()

if A1.get() == "-∞":
    eA1.set("]")
if A2.get() == "+∞":
    eA2.set("[")
if B1.get() == "-∞":
    eB1.set("]")
if B2.get() == "+∞":
    eB2.set("[")

txt1 = Label(janela, text="Informe o primeiro intervalo")
txt1.place(x=10, y=10)

txt2 = Label(janela, text="A =")
txt2.place(x=10, y=30)

extA1 = ttk.Combobox(janela, values=extremos, textvariable=eA1)
extA1.place(x=35, y=30, width=30)

interA1 = Entry(janela, textvariable=A1)
interA1.place(x=70, y=30, width=40)

txt3 = Label(janela, text=",")
txt3.place(x=115, y=30)

interA2 = Entry(janela, textvariable=A2)
interA2.place(x=127, y=30, width=40)

extA2 = ttk.Combobox(janela, values=extremos, textvariable=eA2)
extA2.place(x=170, y=30, width=30)

txt4 = Label(janela, text="Informe o segundo intervalo intervalo ")
txt4.place(x=10, y=55)

txt5 = Label(janela, text="B =")
txt5.place(x=10, y=75)

extB1 = ttk.Combobox(janela, values=extremos, textvariable=eB1)
extB1.place(x=35, y=75, width=30)

interB1 = Entry(janela, textvariable=B1)
interB1.place(x=70, y=75, width=40)

txt3 = Label(janela, text=",")
txt3.place(x=115, y=75)

interB2 = Entry(janela, textvariable=B2)
interB2.place(x=127, y=75, width=40)

extB2 = ttk.Combobox(janela, values=extremos, textvariable=eB2)
extB2.place(x=170, y=75, width=30)

intersecao = Button(janela, text="A ∩ B", command=f_intersecao)
intersecao.place(x=20, y=120)

uniao = Button(janela, text="A ∪ B", command=f_uniao)
uniao.place(x=70, y=120)

AB = Button(janela, text="A - B", command=f_AB)
AB.place(x=120, y=120)

BA = Button(janela, text="B - A", command=f_BA)
BA.place(x=170, y=120)

resposta = Label(janela, text="", bg="#000", fg="#fff")
resposta.place(x=20, y=180, height=50, width=190)

reset_btn = Button(janela, text="Resetar Valores", command=resetar)
reset_btn.place(x=70, y=250)

janela.mainloop()