import sys

#Question 1 answer
numbers = [3,7,3,9,3,1]
n = len(numbers)
target=int(input('what is your target value: '))
def count_occurrences(numbers, target):
    count=0
    for i in range(0,n):
        if target == numbers[i]:
            count += 1
    return count
count = count_occurrences(numbers, target)
print('count is' ,count)


#Question 2 answer

data = [10,20,30,40,50]
n=len(data)
target=int(input('whats your target: '))
def search_with_count(data,target):
    index =0
    comparison=0
    for i in range(0,n):
        comparison +=1
        if target == data[i]:
            print('target found')
            break
        else:
            index+=1

    return index, comparison
index, comps = search_with_count(data, target)
print(f'Found at {index}, took {comps} comparisons')


# Question 3 answer
letters =['a','b','a','c','a','d']
target = input('whats your target: ')
n=len(letters)
def find_all_indices(letters, target):
    index=0
    found_indexes=[]
    for i in range(0,n):
        if target == letters[i]:
            found_indexes.append(index)
        index +=1
    return found_indexes

indexes = find_all_indices(letters, target)
print(indexes)




def main():
    print('done')
    return 0


if __name__ == "__main__":
    sys.exit(main())
