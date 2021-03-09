#tugas struktur data
#membuat projeck for and while

for x in range(1,9):
    		print x

print("\n")

#  list untuk menampung nama-nama teman
my_friends = ["tedi", "rahman", "futri", "gun", "Adam"]
for friend in my_friends:
    print friend

print("\n")

#projeck while 1
#akan ber ulang trus sampe di intruksi stop
while True:
    bales = raw_input('tulis, [tulis "stop" adek sugul] :')
    print bales.lower()
    if bales == 'stop':
        break

print("\n")
#projeck while 2
a = 0	
while a < 10:	
   a = a + 2	
   print a
