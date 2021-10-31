#loadBar from Tyler Luedtke https://www.youtube.com/watch?v=MtYOrIwW1FQ
def loadBar(iteration, total, prefix='', suffix='', decimals=1,length=100, fill='>'):
    #this lihne might be wront
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end= '\r')
    if iteration == total:
        print()
