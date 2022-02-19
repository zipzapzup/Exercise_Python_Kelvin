# Consider input where you have the number of citations
# h index is the productivity of a researcher and is the largest number between their research paper and the number of citations
# Consider: Researcher A
# Publishes: A,B,C,D,E,F,G,H,I paper
# Citations: 1,4,1,4,2,1,3,5,6
# Find the h index where it measures the productivity between the largest of the number of citations and paper
# Answer: 4 

hindex = [1,4,1,4,2,1,3,5,6]
no_of_citations = {}
total_citations  = len(hindex)

# Time BigO(n^2)
# Space BigO(n)
def create_mapping(data):
    for i in range(1, len(data) + 1):
        count = 0
        for k in data:
            if k >= i:
                count += 1
        no_of_citations[i] = count  
    return no_of_citations

def find_largest(hindex_dict):
    largest = None
    for i in hindex_dict.keys():
        if hindex_dict[i] >= i:
            largest = i
    return largest

a = create_mapping(hindex)
print('Mapping', a)
final_hindex = find_largest(a)
print(final_hindex)



def subSTR(Str, Num):
    SubString = []
    NewList = list(Str)
    Ptr = 0
    while Ptr < len(NewList):
        Count = 0
        SmallestSubStr = ''
        for i in range(Ptr, len(NewList)):
            if NewList[i] == '0':
                SmallestSubStr += '0'
            else:
                Count += 1
                SmallestSubStr += '1'
                if Count == Num:
                    SubString.append(SmallestSubStr)
                    break

        Ptr += 1

    return list(set(SubString))

def lexicograph(List):
    newSet = set(List)
    newList = sorted(list(newSet))
    return newList[-1]


Final = subSTR('0101101',3)
print(Final)
print("Smallest Substring :", lexicograph(Final))