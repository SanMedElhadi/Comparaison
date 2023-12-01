import csv
import random
import time
from datetime import datetime
import os
import pandas as pd

# Generer un tableau aleatoire de taille j
def generer_tab(j):
    tab = []
    for i in range(j):
        tab.append(random.randint(0,12000))
    return tab


def tri_selection(tab):
    for i in range(0, len(tab) - 1):
        min = tab[i]
        indice = i
        for j in range(i + 1, len(tab)):
            if tab[j] < min:
                min = tab[j]
                indice = j
        tmp = tab[i]
        tab[i] = tab[indice]
        tab[indice] = tmp
    return tab


# TRI_INSERTION
def tri_insertion(tab):
    for i in range(1, len(tab)):
        j = i
        while j > 0 and tab[j] < tab[j - 1]:
            tab[j], tab[j - 1] = tab[j - 1], tab[j]
            j = j - 1


# tri par fision
def fusion(l):
    if len(l)> 1:
        m = len(l) // 2

        g = l[:m]
        d = l[m:]

        fusion(g)
        fusion(d)
        i, j, k = 0, 0, 0
        while i < len(g) and j <len(d):
            if g[i] < d[j]:
                l[k] = g[i]
                i += 1
                k +=1
            else:
                l[k] = d[j]
                j += 1
                k +=1
        while i < len(g) :
            l[k] = g[i]
            i += 1
            k += 1
        while j < len(d) :
            l[k] = d[j]
            j += 1
            k += 1

# tri rapide
def quicksort(liste):
    if len(liste) <= 1:
        return  liste

    pivot = liste.pop()

    petit = []
    grand = []

    for nombre in liste:
        if nombre < pivot:
            petit.append(nombre)
        else:
            grand.append(nombre)

    return quicksort(petit) + [pivot] + quicksort(grand)
#tri par tas
# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, N, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < N and arr[largest] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < N and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap

		# Heapify the root.
		heapify(arr, N, largest)

# The main function to sort an array of given size
def heapSort(arr):
	N = len(arr)

	# Build a maxheap.
	for i in range(N//2 - 1, -1, -1):
		heapify(arr, N, i)

	# One by one extract elements
	for i in range(N-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)


def generate_comparaison_random_sets(size, name):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open('./results_files/CSVs/' + name + size + dt_string + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Taille", "Tri Par Selection", "Tri par Insertion", "Tri par fusion", "Tri rapide", "Tri par tas"])
        for j in range(1, size): #10000
            tab = generer_tab(j)
            lrow = [j]
            start_time = time.time()
            tri_selection(tab)
            end_time = time.time()
            lrow.append(end_time - start_time)

            start_time = time.time()
            tri_insertion(tab)
            end_time = time.time()
            lrow.append(end_time - start_time)

            start_time = time.time()
            fusion(tab)
            end_time = time.time()
            lrow.append(end_time - start_time)
            if(j < 1038):
                start_time = time.time()
                quicksort(tab)
                end_time = time.time()
                lrow.append(end_time - start_time)
            else:
                lrow.append('MAX DEPTH')

            start_time = time.time()
            heapSort(tab)
            end_time = time.time()
            lrow.append(end_time - start_time)

            writer.writerow(lrow)
        file.close()

def generate_comparaison_tailerd_dataset():
     return

def generate_comparaison_pd_dataset(name, dataset, column):
    lrow = [name, column]
    start_time = time.time()
    tri_selection(dataset[column])
    end_time = time.time()
    lrow.append(end_time - start_time)

    start_time = time.time()
    tri_insertion(dataset[column])
    end_time = time.time()
    lrow.append(end_time - start_time)

    start_time = time.time()
    fusion(dataset[column])
    end_time = time.time()
    lrow.append(end_time - start_time)
    if(j < 1038):
        start_time = time.time()
        quicksort(dataset[column])
        end_time = time.time()
        lrow.append(end_time - start_time)
    else:
        lrow.append('MAX DEPTH')

    start_time = time.time()
    heapSort(dataset[column])
    end_time = time.time()
    lrow.append(end_time - start_time)
    return lrow

# Generate CSV File containing comparison of sorting different datasets
def generate_comparaison_datasets():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dset_path = './datasets/CSVs/'
    dcol_path = './datasets/Columns/'
    with open('./results_files/CSVs/' + 'datasets' + dt_string + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["DataSet", "Column", "Tri Par Selection", "Tri par Insertion", "Tri par fusion", "Tri rapide", "Tri par tas"])
        for path in os.listdir(dset_path):
            if os.path.isfile(os.path.join(dset_path, path)):
                dataset = pd.read_csv(os.path.join(dset_path, path), header=0)
                for path in os.listdir(dcol_path):
                    if os.path.isfile(os.path.join(dset_path, path)):
                        with open(os.path.join(dset_path, path)) as f:
                            lines = f.readlines()
                            for line in f.readlines():
                                row = generate_comparaison_pd_dataset(path, dataset, line)
                                writer.writerow(row)
        file.close()      
                