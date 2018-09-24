try:
 f = open('vybhav',"a")
 f.write('lion king')
except:
 print "something went wrong when writing to the file"
finally:
 f.close()
