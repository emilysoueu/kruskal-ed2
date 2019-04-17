def shellSort(arr, n):
 	h = 1; #our steps for sorting
 	while (h < n/2):
 		h = 2*h+1; #calculate max step needed
 	while (h>=1):
 		for i in range (h,n):
 			temp = arr[i];
 			j = i;
 			while (j >= h and arr[j] < arr[j-h]):
 				arr[j] = arr[j-h];
 				j = j-h;
 			arr[j] = temp;
 		h/= 2;

myL = [3, 1 , 6, 2, 8, 4];

shellSort(myL, 6);
print (myL);