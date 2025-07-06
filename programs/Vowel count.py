# Functions - Count no.of vowels 
	def vow(s):
	    count=0
	    for chaar in s:
	        if(chaar=='a' or chaar=='e' or chaar=='i' or chaar=='o' or chaar=='u' 
	        or chaar=='A' or chaar=='E' or chaar=='I' or chaar=='O' or chaar=='U'):
	            count=count+1
	    return count
	    
print(vow("aeiAAaaou"))
