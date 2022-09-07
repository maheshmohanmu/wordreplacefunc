import functions_framework
from flask import Flask, request, redirect, url_for

@functions_framework.http
def word_replace(request):
   replc_dict = {
    "Oracle" : "Oracle©", 
    "Google" : "Google©", 
    "Microsoft" : "Microsoft©", 
    "Amazon" : "Amazon©", 
    "Deloitte" : "Deloitte©"
   }
   
   textinp = request.args.get('inptext')
   temp = textinp.split()
   replc = []
   for wrd in temp:
    replc.append(replc_dict.get(wrd, wrd))
   replc = ' '.join(replc)
 
   return str(replc)