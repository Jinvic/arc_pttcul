def ptt_cul(cc, score):
    if(score > 10000000):
        return cc+2
    elif(score >= 9800000):
        return cc+1+(score-9800000)/200000
    else:
        return max(cc+(score-9500000)/300000, 0)


def b30_cul():
    return 0


def r10_cul(b30, ptt):
    return (ptt*40-b30*30)/10
