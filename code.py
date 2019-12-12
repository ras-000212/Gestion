import pandas as pd
import os
import datetime
os.getcwd()

file_produits = pd.read_csv('FichierProduits.csv',encoding="ISO-8859-1",sep=';')
file_panier=pd.read_csv('FichierPanier.csv',encoding="ISO-8859-1",sep=';',parse_dates=['DateAchat']) 
res_produits = file_produits[['Code Article','PrixUnitaire']]
res_panier=file_panier[['Qté','DateAchat','Code Article']]

res = pd.merge(res_produits,res_panier,on='Code Article')
res['rev']= (res['Qté'] * res['PrixUnitaire'])
print(res)

 