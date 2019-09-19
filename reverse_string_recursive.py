def recursive_reverse(string):
    if len(string) == 0:
        return string
    else:
        #suppose input is RATUL
        #for first call
        #result = ATUL + R
        #TUL + AR "2nd call"
        #UL + TAR "3rd call"
        #L + UTAR "4th call"
        #LUTAR
        result = recursive_reverse(string[1:]) + string[0]
        print(recursive_reverse(string[1:]))
        return result

string = input("give input:")
#print(recursive_reverse(string))
    
