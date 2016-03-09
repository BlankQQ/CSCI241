
import time
import random
def Insertion_Sort(array):
    for i in range(len(array)):
        current = array[i]
        j = i
        while j > 0 and array[j-1] > current:
            array[j] = array[j-1]
            j -= 1
        array[j] = current

def Selection_Sort(array):
    for startingindex in range(len(array)):
        minimumposition = startingindex
        for j in range(startingindex, len(array)):
            if array[minimumposition] > array[j]:
                minimumposition = j
        temp = array[startingindex]
        array[startingindex] = array[minimumposition]
        array[minimumposition] = temp

def Get_Time(Sort, array, end_number):
    start = time.clock()
    Sort(array)
    end = time.clock()
    selection_run_time = end - start
    print(end_number, selection_run_time)

if __name__ == '__main__':
    end_number = 1
    for i in range(3):
        sel_rand_list = []
        sel_increase_list = []
        sel_decrease_list = []
        ins_rand_list = []
        ins_increase_list = []
        ins_decrease_list = []
        end_number = end_number * 10

        for j in range(0, end_number):
            sel_rand_list.append(random.randint(0, end_number))
        ins_rand_list = list(sel_rand_list)
        for k in range(0, end_number):
            sel_increase_list.append(k)
            ins_increase_list.append(k)
        for l in range(end_number, 0, -1):
            sel_decrease_list.append(l)
            ins_decrease_list.append(l)

        print("Selection Random")
        Get_Time(Selection_Sort, sel_rand_list, end_number)
        print("Insertion Random")
        Get_Time(Insertion_Sort, ins_rand_list, end_number)
        print("Selection Increase")
        Get_Time(Selection_Sort, sel_increase_list, end_number)
        print("Insertion Increase")
        Get_Time(Insertion_Sort, ins_increase_list, end_number)
        print("Selection Decrease")
        Get_Time(Selection_Sort, sel_decrease_list, end_number)
        print("Insertion Decrease")
        Get_Time(Insertion_Sort, ins_decrease_list, end_number)
