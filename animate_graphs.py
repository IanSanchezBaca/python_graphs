#!/usr/bin/env python3
# LIBRARIES
import os
import math
from fractions import Fraction
# from secrets import choice
import warnings
import pygraphviz as pgv

# INITIALIZING RANDOM CRAP
warnings.simplefilter("ignore", RuntimeWarning)
mygraph = pgv.AGraph()
myfile = open("input.txt", "r")
temparr = [1, 2, 3]
print("im too lazy to implement both at the same time.\nCHOOSE (1)LINEAR (2)LOG (3)INFLATION")
rito = input()

if not os.path.exists("uwu"):
    os.makedirs("uwu")
    print("new directory \"uwu\" created")
### READING FILE #############
filearray = []  # saves all of the lines of the input file
filearray = myfile.readlines()
numofnodes = int(filearray[0])
##############################
mygraph.graph_attr['overlap'] = "scale"
mygraph.graph_attr['outputorder'] = "edgesfirst"
mygraph.node_attr['style'] = "filled"
mygraph.node_attr['shape'] = "circle"
mygraph.node_attr['fixedsize'] = "true"
##############################

### PART ONE #################
mydict = {}
# print("createing invis original ", numofnodes)
# percent = float(numofnodes/10)
for x in range(numofnodes):
    # print((percent * x)*10,"%", end = '\r')
    temparr = []
    for y in range(numofnodes):
        if not (x+1 == y+1):
            temparr.append(y+1)
    mydict[x+1] = {"color": filearray[x+1].replace('\n', '')}
# print("done", end = "\r")

# FIRST: THE ONES THAT START IT OFF
for i in range(numofnodes):
    mygraph.add_node("copy{}".format(
        i+1), color=filearray[i+1].replace('\n', ''))
    mygraph.get_node("copy{}".format(i+1)).attr['style'] = "invis"

for x in range(numofnodes):
    for y in range(numofnodes):
        if not (x == y):
            mygraph.add_edge("copy{}".format(x+1), "copy{}".format(y+1))
            mygraph.get_edge("copy{}".format(x+1), "copy{}".format(y+1)).attr['style'] = "invis"

for row in range(numofnodes+1, len(filearray)):
    isclone = bool(0)
    bcopycolor = bool(0)
    copycolor = ""
    bcopy = bool(0)
    copy = ""
    bmove = bool(0)
    move = ""
    mainnode = ""
    copyedgearr = []
    copyedge = ""
    moveedgearr = []
    moveedge = ""
    test = filearray[row]
    temp = ""

    for i in range(len(test)):
        if (test[i].isnumeric()):
            if not isclone and not bcopy and not bmove:
                temp += test[i]
            elif not bcopy and not bmove:
                copycolor += test[i]
                # print("copied color from", copycolor)
            if bcopy and not bmove:
                copyedge += test[i]
            if bmove and not bcopy:
                # this is a string
                moveedge += test[i]

        if (test[i].isalpha()):
            if (test[i] == "c"):
                bcopy = bool(1)
            if (test[i] == "m"):
                bmove = bool(1)

        if (test[i] == " "):
            if not isclone:
                isclone = bool(1)
                mainnode = int(temp)
            if bcopy:
                copyedgearr.append(int(copyedge))
                copyedge = ""
                bcopy = bool(0)
            if bmove:
                moveedgearr.append(int(moveedge))
                moveedge = ""
                bmove = bool(0)

        if i+1 == len(test):
            if bcopy:
                copyedgearr.append(int(copyedge))
                copyedge = ""
                bcopy = bool(0)

            if bmove:
                moveedge += test[i]
                moveedgearr.append(int(moveedge))
                moveedge = ""
                bmove = bool(0)
    mygraph.add_node("copy{}".format(mainnode), color="{}".format(mydict[int(copycolor)]["color"]))
    mygraph.get_node("copy{}".format(mainnode)).attr['style'] = "invis"
    if len(copyedgearr) > 0:
        for i in range(len(copyedgearr)):
            # donothing=""
            mygraph.add_edge("copy{}".format(mainnode), "copy{}".format(copyedgearr[i]))
            mygraph.get_edge("copy{}".format(mainnode), "copy{}".format(
                copyedgearr[i])).attr['style'] = "invis"

    if len(moveedgearr) > 0:
        for i in range(len(moveedgearr)):
            mygraph.remove_edge("copy{}".format(copycolor), "copy{}".format(moveedgearr[i]))
            mygraph.add_edge("copy{}".format(mainnode), "copy{}".format(moveedgearr[i]))
            mygraph.get_edge("copy{}".format(mainnode), "copy{}".format(moveedgearr[i])).attr['style'] = "invis"

    mygraph.get_node("copy{}".format(mainnode)).attr['style'] = "invis"
mygraph.layout(prog="neato")
### END PART ONE ################################################################################################

### PART TWO ####################################################################################################
# FIRST: THE ONES THAT START IT OFF
if int(rito) == 1: # linear
    # REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

    # the original colors first
    for i in range(numofnodes):
        uwu = mygraph.get_node("copy{}".format(i+1)).attr['pos']
        ccc = mygraph.get_node("copy{}".format(i+1)).attr['color']
        xyz = uwu.split(",")
        x = xyz[0]
        y = xyz[1]
        mygraph.add_node(i+1, color=ccc, pos="{},{}!".format(x, y))
    for x in range(numofnodes):
        for y in range(numofnodes):
            if not (x == y):
                mygraph.add_edge(x+1, y+1)
    mygraph.draw("uwu/file000.gif")
    # end of original colors

    ones = 1
    tens = 0
    eh = (1/len(filearray))
    for row in range(numofnodes+1, len(filearray)):
        print(eh*100, "%", end='\r')
        eh += (1/len(filearray))
        isclone = bool(0)
        bcopycolor = bool(0)
        copycolor = ""
        bcopy = bool(0)
        copy = ""
        bmove = bool(0)
        move = ""
        mainnode = ""
        copyedgearr = []
        copyedge = ""
        moveedgearr = []
        moveedge = ""
        test = filearray[row]
        temp = ""

        for i in range(len(test)):
            if (test[i].isnumeric()):
                if not isclone and not bcopy and not bmove:
                    temp += test[i]
                elif not bcopy and not bmove:
                    copycolor += test[i]
                    # print("copied color from", copycolor)
                if bcopy and not bmove:
                    copyedge += test[i]
                if bmove and not bcopy:
                    moveedge += test[i]

            if (test[i].isalpha()):
                if (test[i] == "c"):
                    bcopy = bool(1)
                if (test[i] == "m"):
                    bmove = bool(1)

            if (test[i] == " "):
                if not isclone:
                    isclone = bool(1)
                    mainnode = int(temp)
                if bcopy:
                    copyedgearr.append(int(copyedge))
                    copyedge = ""
                    bcopy = bool(0)
                if bmove:
                    moveedgearr.append(int(moveedge))
                    moveedge = ""
                    bmove = bool(0)

            if i+1 == len(test):
                if bcopy:
                    copyedgearr.append(int(copyedge))
                    copyedge = ""
                    bcopy = bool(0)

                if bmove:
                    moveedge += test[i]
                    moveedgearr.append(int(moveedge))
                    moveedge = ""
                    bmove = bool(0)

    ######################################### LINEAR DISTANCE JUNK ######################################################################
        initialpos = mygraph.get_node("copy{}".format(copycolor)).attr['pos']
        finalpos = mygraph.get_node("copy{}".format(mainnode)).attr['pos']
        xyzi = initialpos.split(",")
        xi = float(xyzi[0])
        yi = float(xyzi[1])
        xyzf = finalpos.split(",")
        xf = float(xyzf[0])
        yf = float(xyzf[1])
        plusx = float((xf - xi)/10)
        plusy = float((yf - yi)/10)
        # print(plusx, plusy)
    ######################################### END LINEAR DISTANCE JUNK #####################################################################

        mygraph.add_node(mainnode, color="{}".format(
            mydict[int(copycolor)]["color"]), pos="{},{}!".format(xi, yi))
        if len(copyedgearr) > 0:
            for i in range(len(copyedgearr)):
                # donothing = ""
                mygraph.add_edge(mainnode, copyedgearr[i])
                # mygraph.get_edge("copy{}".format(mainnode), "copy{}".format(copyedgearr[i])).attr['style']="invis"

        if len(moveedgearr) > 0:
            for i in range(len(moveedgearr)):
                # donothing = ""
                mygraph.remove_edge(copycolor, moveedgearr[i])
                mygraph.add_edge(mainnode, moveedgearr[i])
                # mygraph.get_edge("copy{}".format(mainnode), "copy{}".format(moveedgearr[i])).attr['style']="invis"
        nextx = xi
        nexty = yi
        for i in range(1, 11):
            # donothing=""

            mygraph.get_node(
                mainnode).attr['pos'] = "{}, {}".format(nextx, nexty)
            nextx = nextx + plusx
            nexty = nexty + plusy

            if tens <= 9:
                filename = "uwu/file0{}{}.gif".format(tens, ones)
            else:
                filename = "uwu/file{}{}.gif".format(tens, ones)

            if ones == 9:
                ones = 0
                tens += 1
            else:
                ones += 1
            mygraph.draw(filename)

        if tens <= 9:
            filename = "uwu/file0{}{}.gif".format(tens, ones)
        else:
            filename = "uwu/file{}{}.gif".format(tens, ones)

        mygraph.draw(filename)
    os.system("gifsicle --colors 256 --delay=10 --optimize=3 %s/* > %s" %("uwu", "linear.gif"))
    for f in os.listdir("uwu"):
        os.remove(os.path.join("uwu", f))
    os.rmdir("uwu")
    print("new directory \"uwu\" removed")
    # REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

if int(rito) == 2: # log
    # the original colors first
    for i in range(numofnodes):

        uwu = mygraph.get_node("copy{}".format(i+1)).attr['pos']
        ccc = mygraph.get_node("copy{}".format(i+1)).attr['color']
        xyz = uwu.split(",")
        x = xyz[0]
        y = xyz[1]
        mygraph.add_node(i+1, color=ccc, pos="{},{}!".format(x, y))
    for x in range(numofnodes):
        for y in range(numofnodes):
            if not (x == y):
                mygraph.add_edge(x+1, y+1)
    mygraph.draw("uwu/file000.gif")
    # end of original colors

    ones = 1
    tens = 0
    eh = (1/len(filearray))
    for row in range(numofnodes+1, len(filearray)):
        print(eh*100, "%", end='\r')
        eh += (1/len(filearray))
        print((row-5)*10, "%", end='\r')
        isclone = bool(0)
        bcopycolor = bool(0)
        copycolor = ""
        bcopy = bool(0)
        copy = ""
        bmove = bool(0)
        move = ""
        mainnode = ""
        copyedgearr = []
        copyedge = ""
        moveedgearr = []
        moveedge = ""
        test = filearray[row]
        temp = ""

        for i in range(len(test)):
            if (test[i].isnumeric()):
                if not isclone and not bcopy and not bmove:
                    temp += test[i]
                elif not bcopy and not bmove:
                    copycolor += test[i]
                    # print("copied color from", copycolor)
                if bcopy and not bmove:
                    copyedge += test[i]
                if bmove and not bcopy:
                    moveedge += test[i]

            if (test[i].isalpha()):
                if (test[i] == "c"):
                    bcopy = bool(1)
                if (test[i] == "m"):
                    bmove = bool(1)

            if (test[i] == " "):
                if not isclone:
                    isclone = bool(1)
                    mainnode = int(temp)
                if bcopy:
                    copyedgearr.append(int(copyedge))
                    copyedge = ""
                    bcopy = bool(0)
                if bmove:
                    moveedgearr.append(int(moveedge))
                    moveedge = ""
                    bmove = bool(0)

            if i+1 == len(test):
                if bcopy:
                    copyedgearr.append(int(copyedge))
                    copyedge = ""
                    bcopy = bool(0)

                if bmove:
                    moveedge += test[i]
                    moveedgearr.append(int(moveedge))
                    moveedge = ""
                    bmove = bool(0)

    ######################################### LOG DISTANCE JUNK ######################################################################
        initialpos = mygraph.get_node("copy{}".format(copycolor)).attr['pos']
        finalpos = mygraph.get_node("copy{}".format(mainnode)).attr['pos']
        xyzi = initialpos.split(",")
        xi = float(xyzi[0])
        yi = float(xyzi[1])
        xyzf = finalpos.split(",")
        xf = float(xyzf[0])
        yf = float(xyzf[1])
        # plusx = float((xf - xi)* (1 - math.log10(11-i)) + xi) 
        # plusy = float((yf - yi))
        # print(plusx, plusy)
    ######################################### END LOG DISTANCE JUNK #####################################################################

        mygraph.add_node(mainnode, color="{}".format(mydict[int(copycolor)]["color"]), pos="{},{}!".format(xi, yi))
        if len(copyedgearr) > 0:
            for i in range(len(copyedgearr)):
                # donothing = ""
                mygraph.add_edge(mainnode, copyedgearr[i])
                # mygraph.get_edge("copy{}".format(mainnode), "copy{}".format(copyedgearr[i])).attr['style']="invis"

        if len(moveedgearr) > 0:
            for i in range(len(moveedgearr)):
                # donothing = ""
                mygraph.remove_edge(copycolor, moveedgearr[i])
                mygraph.add_edge(mainnode, moveedgearr[i])
                # mygraph.get_edge("copy{}".format(mainnode), "copy{}".format(moveedgearr[i])).attr['style']="invis"
        nextx = xi
        nexty = yi
        for i in range(1, 11):
            mygraph.get_node(mainnode).attr['pos'] = "{}, {}".format(nextx, nexty)
            
            plusx = float((xf - xi) * (1 - math.log10(11-i)) + xi)
            plusy = float((yf - yi)* (1 - math.log10(11-i)) + yi)
            nextx = plusx
            nexty = plusy

            if tens <= 9:
                filename = "uwu/file0{}{}.gif".format(tens, ones)
            else:
                filename = "uwu/file{}{}.gif".format(tens, ones)

            if ones == 9:
                ones = 0
                tens += 1
            else:
                ones += 1
            mygraph.draw(filename)

        if tens <= 9:
            filename = "uwu/file0{}{}.gif".format(tens, ones)
        else:
            filename = "uwu/file{}{}.gif".format(tens, ones)

        mygraph.draw(filename)
    os.system("gifsicle --colors 256 --delay=10 --optimize=3 %s/* > %s" %("uwu", "log.gif"))
    for f in os.listdir("uwu"):
        os.remove(os.path.join("uwu", f))
    os.rmdir("uwu")
    print("new directory \"uwu\" removed")
### END OF PART TWO #################

### PART THREE
if int(rito) == 3:
    # 5 frames to inflate
    # 10 frames to deflate and move
    # REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

    # the original colors first
    for i in range(numofnodes):

        uwu = mygraph.get_node("copy{}".format(i+1)).attr['pos']
        ccc = mygraph.get_node("copy{}".format(i+1)).attr['color']
        xyz = uwu.split(",")
        x = xyz[0]
        y = xyz[1]
        mygraph.add_node(i+1, color=ccc, pos="{},{}!".format(x, y))
    for x in range(numofnodes):
        for y in range(numofnodes):
            if not (x == y):
                mygraph.add_edge(x+1, y+1)
    mygraph.draw("uwu/file000.gif")
    # end of original colors

    ones = 1
    tens = 0
    eh = (1/len(filearray))
    for row in range(numofnodes+1, len(filearray)):
        print(eh*100, "%", end='\r')
        eh += (1/len(filearray))
        isclone = bool(0)
        bcopycolor = bool(0)
        copycolor = ""
        bcopy = bool(0)
        copy = ""
        bmove = bool(0)
        move = ""
        mainnode = ""
        copyedgearr = []
        copyedge = ""
        moveedgearr = []
        moveedge = ""
        test = filearray[row]
        temp = ""

        for i in range(len(test)):
            if (test[i].isnumeric()):
                if not isclone and not bcopy and not bmove:
                    temp += test[i]
                elif not bcopy and not bmove:
                    copycolor += test[i]
                    # print("copied color from", copycolor)
                if bcopy and not bmove:
                    copyedge += test[i]
                if bmove and not bcopy:
                    moveedge += test[i]

            if (test[i].isalpha()):
                if (test[i] == "c"):
                    bcopy = bool(1)
                if (test[i] == "m"):
                    bmove = bool(1)

            if (test[i] == " "):
                if not isclone:
                    isclone = bool(1)
                    mainnode = int(temp)
                if bcopy:
                    copyedgearr.append(int(copyedge))
                    copyedge = ""
                    bcopy = bool(0)
                if bmove:
                    moveedgearr.append(int(moveedge))
                    moveedge = ""
                    bmove = bool(0)

            if i+1 == len(test):
                if bcopy:
                    copyedgearr.append(int(copyedge))
                    copyedge = ""
                    bcopy = bool(0)

                if bmove:
                    moveedge += test[i]
                    moveedgearr.append(int(moveedge))
                    moveedge = ""
                    bmove = bool(0)

    ######################################### LINEAR DISTANCE JUNK ######################################################################
        initialpos = mygraph.get_node("copy{}".format(copycolor)).attr['pos']
        finalpos = mygraph.get_node("copy{}".format(mainnode)).attr['pos']
        xyzi = initialpos.split(",")
        xi = float(xyzi[0])
        yi = float(xyzi[1])
        xyzf = finalpos.split(",")
        xf = float(xyzf[0])
        yf = float(xyzf[1])
        plusx = float((xf - xi)/10)
        plusy = float((yf - yi)/10)
        # print(plusx, plusy)
    ######################################### END LINEAR DISTANCE JUNK #####################################################################

        mygraph.add_node(mainnode, color="{}".format(mydict[int(copycolor)]["color"]), pos="{},{}!".format(xi, yi), width = .5)
        if len(copyedgearr) > 0:
            for i in range(len(copyedgearr)):
                # donothing = ""
                mygraph.add_edge(mainnode, copyedgearr[i])
                # mygraph.get_edge("copy{}".format(mainnode), "copy{}".format(copyedgearr[i])).attr['style']="invis"

        if len(moveedgearr) > 0:
            for i in range(len(moveedgearr)):
                # donothing = ""
                mygraph.remove_edge(copycolor, moveedgearr[i])
                mygraph.add_edge(mainnode, moveedgearr[i])
                # mygraph.get_edge("copy{}".format(mainnode), "copy{}".format(moveedgearr[i])).attr['style']="invis"
        nextx = xi
        nexty = yi
        inflate_by = float(.1)#float(.5/5)
        deflate_by = float(.5/10)

        # print("inflateing by,", inflate_by, "each time", "deflating by,", deflate_by, "each time", end="\r")
        for i in range(1, 6):
            # main_node_width = float(mygraph.get_node(mainnode).attr['width'])
            # print("before:", main_node_width)
            mygraph.get_node(mainnode).attr['width'] = float((i+5)/10)
            # main_node_width = float(mygraph.get_node(mainnode).attr['width'])
            # print("after:", main_node_width)
           
            if tens <= 9:
                filename = "uwu/file0{}{}.gif".format(tens, ones)
            else:
                filename = "uwu/file{}{}.gif".format(tens, ones)

            if ones == 9:
                ones = 0
                tens += 1
            else:
                ones += 1
            mygraph.draw(filename)


        for i in range(1, 11):
            # donothing=""

            mygraph.get_node(mainnode).attr['pos'] = "{}, {}".format(nextx, nexty)
            nextx = nextx + plusx
            nexty = nexty + plusy
            main_node_width = float(mygraph.get_node(mainnode).attr['width'])
            mygraph.get_node(mainnode).attr['width'] = (main_node_width - deflate_by)
            # print("width: ", mygraph.get_node(mainnode).attr['width'])

            if tens <= 9:
                filename = "uwu/file0{}{}.gif".format(tens, ones)
            else:
                filename = "uwu/file{}{}.gif".format(tens, ones)

            if ones == 9:
                ones = 0
                tens += 1
            else:
                ones += 1
            mygraph.draw(filename)

        if tens <= 9:
            filename = "uwu/file0{}{}.gif".format(tens, ones)
        else:
            filename = "uwu/file{}{}.gif".format(tens, ones)

        mygraph.draw(filename)
    
    os.system("gifsicle --colors 256 --delay=10 --optimize=3 %s/* > %s" %("uwu", "inflation.gif"))
    for f in os.listdir("uwu"):
        os.remove(os.path.join("uwu", f))
    os.rmdir("uwu")
    print("new directory \"uwu\" removed")
### END PART THREE

### NOTES ####################################

# print('\n', counter)
# print(myfile.readline(2))

# print(mygraph)

# print it this way so that you dont get an endl
# for i in colorarray:
#     print(i)

# num = 1
# bruh = "file"
# mix = "{}{}.png".format(bruh, num)
# mygraph.layout(prog='dot') # use this to sort the layout
# mygraph.draw(mix)

# mygraph.add_edge(1, 1)


# mygraph.write("file.dot")

# mygraph.add_node(1, color="red")
# mygraph.add_node(2, color="dodgerblue")
# mygraph.add_edge(1, 2)


# mydict[1] = "red"
# print(mydict[1])

# mygraph.add_node(1, color="{}".format(mydict[1]))

# colorarray = [] #probably dont need this

# for i in range(numofnodes):
#     mydict[i+1] = {"color":filearray[i+1].replace('\n','')}
# for i in range(numofnodes):
#     print(i+1, mydict[i+1]["color"])
# mygraph = pgv.AGraph(mydict)
# mygraph.add_node(1, color = mydict[1][1])


# DICT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11

# mydict[1] = {"color":"red", "nextto":temparr}


#     # print(copycolor)
#     # thisarray = mydict[int(copycolor))]["edge"]

    # mydict[int(mainnode)] = {"color" : mydict[int(copycolor)]["color"], "edge" : copyedgearr}

# tens = 0
# ones = 1
# for i in range(5, len(filearray)):
#     finalpos = mygraph.get_node("copy{}".format(i)).attr['pos']
#     ccc = mygraph.get_node("copy{}".format(i)).attr['color']
#     xyz = finalpos.split(",")
#     x = xyz[0]
#     y = xyz[1]
#     mygraph.add_node(i, color = ccc, pos="{},{}!".format(x, y))
#     mygraph.draw("uwu/file{}{}.gif".format(tens, ones))
#     if ones == 9:
#         ones = 1
#         tens += 1
#     else:
#         ones += 1
