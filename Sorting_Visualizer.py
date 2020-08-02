import pygame
from numpy.random import randint

pygame.init()
window = pygame.display.set_mode((600,320))
pygame.display.set_caption('Sorting Visualizer')
arr = randint(50,250,100)
x=5
y=299
width = 4
def draw_bars(sortype = "Select Sortype"):
	window.fill((255,255,255))
	for i,height in enumerate(arr):
		pygame.draw.rect(window,(161,68,83),(x+5*i,height,width,y-height))
	over_font = pygame.font.SysFont("arial",30)
	over = over_font.render(sortype,True,(0,255,0))
	window.blit(over,(120,0)) 
	pygame.display.flip()
	pygame.display.update()

##########################################
######### QUICK SORT #####################
##########################################
def partition(arr,si,ei):
	x = arr[si]
	count = 0
	for i in range(si+1,ei+1):
		if x > arr[i]:
			count += 1
	arr[si],arr[si+count] = arr[si+count],arr[si]
	pivot_index = si + count
	l = arr[pivot_index]
	pygame.draw.rect(window,(16,45,228),(x + 5*pivot_index,l,width,y - l))
	pygame.display.update()
	pygame.time.delay(20)
	left_index,right_index = si,ei
	while (left_index < pivot_index) and (right_index > pivot_index):
		if arr[left_index] < arr[pivot_index]:
			left_index += 1
		elif arr[right_index] >= arr[pivot_index]:
			right_index -= 1
		else:
			arr[left_index],arr[right_index] = arr[right_index],arr[left_index]
			pygame.draw.rect(window,(16,45,228),(x + 5*pivot_index,l,width,y - l))
			pygame.time.delay(20)
			left_index += 1
			right_index -= 1
		draw_bars("QUICK SORT")
		pygame.draw.rect(window,(16,45,228),(x + 5*pivot_index,l,width,y - l))
	return pivot_index

def quickSort(arr, start, end):
	# Please add your code here
	if start >=end:
		return
	index = partition(arr,start,end)
	draw_bars("QUICK SORT")
	quickSort(arr,start,index-1)
	quickSort(arr,index+1,end)

######################################
########## MERGE SORT ################
######################################

def merge(li1,li2,arr):
	i=0
	j=0
	temp = []
	while i<len(li1) and j<len(li2):
		if li1[i]<li2[j]:
			temp.append(li1[i])
			i+=1
		else:
			temp.append(li2[j])
			# draw_bars(temp)
			j+=1
		draw_bars("MERGE SORT")

	while i<len(li1):
		temp.append(li1[i])
		i+=1
	while j<len(li2):
		temp.append(li2[j])
		j+=1
	for i in range(len(arr)):
		arr[i] = temp[i]
		l  = temp[i]
		draw_bars("MERGE SORT")
		pygame.time.delay(5)   #BECAUSE MERGE SORT IS TOO FAST!!!

	return arr
def mergeSort(arr):
	l=len(arr)
	if l==1 :
		return arr
	mid=l//2
	li1=arr[:mid]
	li2=arr[mid:]
	li1 = mergeSort(li1)
	li2 = mergeSort(li2)
	
	return merge(li1,li2,arr)

def start_screen():
	window.fill((255,255,255))
	over_font = pygame.font.SysFont("arial",30)
	sort1 = over_font.render("PRESS Q FOR QUICK-SORT",True,(206,26,26))
	sort2 = over_font.render("PRESS M FOR MERGE-SORT",True,(12,151,114))
	sort3 = over_font.render("PRESS B FOR BUBBLE-SORT",True,(194,239,15))
	sort4 = over_font.render("PRESS S FOR SELECTION-SORT",True,(239,104,15))
	randomize = over_font.render("PRESS R TO GENERATE ARRAY",True,(239,104,15))
	window.blit(sort4,(80,30))
	window.blit(sort3,(80,90))
	window.blit(sort2,(80,150))
	window.blit(sort1,(80,210))
	window.blit(randomize,(80,270))
	pygame.display.flip()
	pygame.display.update()

running=True
flag = 0
while running:
	for events in pygame.event.get():
		if events.type==pygame.QUIT:
			running = False
		if events.type==pygame.KEYDOWN:
			if events.key==pygame.K_s:
				flag = 1
			if events.key==pygame.K_b:
				flag = 2
			if events.key==pygame.K_q:
				flag = 3
			if events.key==pygame.K_m:
				flag = 4
			if events.key==pygame.K_r:
				flag = 5
				arr = randint(50,250,100)
				draw_bars()

		if flag==0:
			arr = randint(50,250,100)
			start_screen()
		if flag==1:
			#SELECTION SORT
			for i in range(len(arr)):
				min_idx = i
				for j in range(i+1,len(arr)):
					pygame.event.pump()
					if arr[min_idx] > arr[j]:
						min_idx = j
					pygame.draw.rect(window,(0,0,155),(x + 5*j,arr[j],width,y - arr[j]))
					pygame.display.update()
					draw_bars("SELECTION SORT")				
				#swap on finding
				arr[i],arr[min_idx] = arr[min_idx],arr[i]
				draw_bars("SELECTION SORT")
			pygame.time.delay(5)
			flag = 0
		if flag==2:
			#BUBBLE SORT
			pygame.event.pump()
			for i in range(len(arr)):
				for j in range(len(arr)-i-1):
					if arr[j]>arr[j+1]:
						arr[j],arr[j+1] = arr[j+1],arr[j]
						pygame.draw.rect(window,(0,0,155),(x + 5*j,arr[j],width,y - arr[j]))
						pygame.display.update()
						# pygame.time.delay(5)

					draw_bars("BUBBLE SORT")
			pygame.time.delay(5)
			flag = 0

		if flag==3:
			quickSort(arr,0,len(arr)-1)
			pygame.time.delay(10)
			flag = 0
		if flag==4:
			_ = mergeSort(arr)
			pygame.time.delay(10)
			flag = 0

pygame.quit()
