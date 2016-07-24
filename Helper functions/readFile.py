

def readFile():

    fname = "promotorRegionsSample.txt"

    content = []

    DNA = []

    with open(fname) as f:

            content = [x.strip('\r\n') for x in f.readlines()]

            print content

            counter = 1

            while len(content) != 0 :
                #outputFile = open(content[0], 'w')
                #for line in content[:21]:
                    #outputFile.write(line + '\n')
                DNA.append(content[:21])
                del content[:21]



    print content

    print DNA

    #print content.pop(0)
    #print content



if __name__ == "__main__":

    readFile()