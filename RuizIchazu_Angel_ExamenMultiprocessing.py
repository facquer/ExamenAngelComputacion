import random

import time

import multiprocessing , ctypes





def how_many_max_values_sequential(ar):

    #find max value of the list
    maxValue = 0

    for i in range(len(ar)):

        if i == 0:

            maxValue = ar[i]

        else:

            if ar[i] > maxValue:

                maxValue = ar[i]
    print("PRUEBA SECUENCIAL MAX VALUE")
    print(maxValue)
    #find how many max values are in the list

    contValue = 0

    for i in range(len(ar)):

        if ar[i] == maxValue:

            contValue += 1

 

    return contValue

 

# Complete the how_many_max_values_parallel function below.



def parallel(ar, send_end):
    maxValue = 0
    for i in range(len(ar)):
        if i == 0:
            maxValue = ar[i]
        else:
            if ar[i] > maxValue:
                maxValue = ar[i]
                
    contValue = 0

    for i in range(len(ar)):

        if ar[i] == maxValue:

            contValue += 1
    send_end.send(contValue)



def parallel2(ar, send_end, maxValue):
    contValue = 0
    for i in range(len(ar)):
        if ar[i] == maxValue:
            contValue += 1
    send_end.send(contValue)

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def how_many_max_values_parallel(ar):
    
    
    
    B, C = split_list(ar)
    
    pipe_list = []
    pipe_list2 = []
    recv_end, send_end = multiprocessing.Pipe(False)
    recv_end2, send_end2 = multiprocessing.Pipe(False)

    
    
    process1 = multiprocessing.Process(target=parallel, args=(B, send_end))
    process2 = multiprocessing.Process(target=parallel, args=(C, send_end2))
    
    pipe_list.append(recv_end)
    pipe_list2.append(recv_end2)
    
    process1.start()
    process2.start()
    process1.join() 
    process2.join()
    print("PRUEBAAAAAAAAAAAAAA PIPE 1")
    result_list = [x.recv() for x in pipe_list]
    print (result_list)
    print("PRUEBAAAAAAAAAAAAAA PIPE 2")
    result_list2 = [x.recv() for x in pipe_list2]
    print (result_list2)
    
    maxValue = 0
    #if result_list[0] > result_list2[0]:
     #   maxValue = result_list[0]
    #else :
     #   maxValue = result_list2[0]
        
    #print("PRUEBAAAAAAAAAAAAAA MaxValue")
    #print(maxValue)
    
    
    conteito = result_list[0] + result_list2[0]
    
    #pool = multiprocessing.Pool(processes=4)
    #pool.map(parallel, ar)
    #pool.close()
    #pool.join()
    #print("PRUEBAAAAAAAAAAAAAA")
    #print (prueba.value)
    #for i in range(len(ar)):
     #   if ar[i] == pruebita:
      #      conteito += 1

    return conteito

 

if __name__ == '__main__':

   

   

    ar_count = 40000000

   

    #Generate ar_count random numbers between 1 and 30

    ar = [random.randrange(1,30) for i in range(ar_count)]

    inicioSec = time.time()

    resultSec = how_many_max_values_sequential(ar)

    finSec =  time.time()

   

    inicioPar = time.time()   

    resultPar = how_many_max_values_parallel(ar)

    finPar = time.time()   

    print(resultSec)
    print(resultPar)

    print('Results are correct!\n' if resultSec == resultPar else 'Results are incorrect!\n')

    print('Sequential Process took %.3f ms with %d items\n' % ((finSec - inicioSec)*1000, ar_count))

    print('Parallel Process took %.3f ms with %d items\n' % ((finPar - inicioPar)*1000, ar_count))