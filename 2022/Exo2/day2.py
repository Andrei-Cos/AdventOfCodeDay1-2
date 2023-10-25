def RPSV1(guide):
    total=0
    for i in range(len(guide)):
        mymove=guide[i][2]
        hismove=guide[i][0]
        if mymove=="X" and hismove=="A": #draw and rock
            total+=4
        if mymove=="X" and hismove=="B": #lose and rock
            total+=1
        if mymove=="X" and hismove=="C": #win and rock
            total+=7
        if mymove=="Y" and hismove=="A": #win and paper
            total+=8
        if mymove=="Y" and hismove=="B": #draw and paper
            total+=5
        if mymove=="Y" and hismove=="C": #loose and paper
            total+=2
        if mymove=="Z" and hismove=="A": #loose and scissors
            total+=3
        if mymove=="Z" and hismove=="B": #win and scissors
            total+=9
        if mymove=="Z" and hismove=="C": #draw and scissors
            total+=6
    return total

def RPSV2(guide):
    total=0
    for i in range(len(guide)):
        endsate=guide[i][2]
        hismove=guide[i][0]
        if hismove=="A" and endsate=="X": #he plays rock and I must lose (scissors)
            total+=3
        if hismove=="A" and endsate=="Y": #he plays rock and I must draw (rock)
            total+=4
        if hismove=="A" and endsate=="Z": #he plays rock and I must win(Z) (paper)
            total+=8
        if hismove=="B" and endsate=="X": #he plays paper and I must lose (rock)
            total+=1
        if hismove=="B" and endsate=="Y": #he plays paper and I must draw (paper)
            total+=5
        if hismove=="B" and endsate=="Z": #he plays paper and I must win(Z) (scissors)
            total+=9
        if hismove=="C" and endsate=="X": #he plays scissors and I must lose (paper)
            total+=2
        if hismove=="C" and endsate=="Y": #he plays scissors and I must draw (scissors)
            total+=6
        if hismove=="C" and endsate=="Z": #he plays scissors and I must win(Z) (rock)
            total+=7
    return total




if __name__=="__main__":
    f=open('day_2_input.txt',"r")
    Guide_Strat=f.readlines()
    for i in range(len(Guide_Strat)):
        Guide_Strat[i]=Guide_Strat[i].rstrip()

    print(RPSV1(Guide_Strat))
    print(RPSV2(Guide_Strat))

