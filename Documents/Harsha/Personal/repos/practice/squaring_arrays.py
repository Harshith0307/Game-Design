#read a list of nuumbers and then square it 

def square(element):
    return element**2
    

def square_array(elements):

    for item in elements:
        print(square(item))
    

if __name__ == '__main__':

    count = int(input("Please enter the number of numbers dumma "))

    elements = list(map(int, input().strip().split()))

    square_array(elements)

    squared_num = list(map(square, elements))

    print(squared_num)
