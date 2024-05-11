#--------------------------------------------------------------------------#
#									      #
#									      #
#			GMSH Airfoil Generator Tool			      #
#									      #
#                      By Nispruha Geetha Srinivas			      #
#--------------------------------------------------------------------------#
import pandas as pd
import os

#importing and cleaning the dataframe of Coordinates
df = pd.read_csv("p51htip-il.csv")
df.drop([0,1,2,3,4,5,6,7], axis=0, inplace=True) #remain as it is

CamLine=df.where(df=='Camber line').dropna(how='all').dropna(axis=1)
deleterowsfrom = CamLine.index

#print(deleterowsfrom)

 
for index, row in df.iterrows():
	if index<deleterowsfrom-1:
		pass
	else:
		df.drop(index,axis=0, inplace=True)

df.rename(
    columns={"Name": "X", "NACA 66": "Y"},
    inplace=True,
)

df.reset_index(inplace=True)
#print(df)
# End of importing and cleaning the dataframe of Coordinates

z=0; #Z Coordinate
mesh_den=1.0 #Element Size Factor


#printing the .geo file
#-----Checking if an airfoil file exists and deleting it---#
if os.path.isfile("airfoil.geo")==True:
	os.remove("airfoil.geo")
else:
	pass
#-----End of checking if an airfoil file exists and deleting it---#

#writing the GMSH file#
x1max=500
x2max=-200
y1max=150
y2max=-150

f = open("airfoil.geo", "a")
print("Point(1) = {",x1max,",",y1max,",",z,",",mesh_den,"};", file=f)
print("Point(2) = {",x2max,",",y1max,",",z,",",mesh_den,"};", file=f)
print("Point(3) = {",x2max,",",y2max,",",z,",",mesh_den,"};", file=f)
print("Point(4) = {",x1max,",",y2max,",",z,",",mesh_den,"};", file=f)

print("Line(1)={1,2};", file=f)
print("Line(2)={2,3};", file=f)
print("Line(3)={3,4};", file=f)
print("Line(4)={4,1};", file=f)

totalrows = len(df.index)

#print(totalrows)

for index, row in df.iterrows():
	if index<=totalrows-2:
		print("Point(",index+5,") = {",row['X'],",",row['Y'],",",z,",",mesh_den,"};", file=f)
		#f.write("'Point(',index+1,') = {',row['X'],',',row['Y'],',',z,',',mesh_den,'};")
	else:
 		break
 		

for index, row in df.iterrows():
	if index<=totalrows-3:
		print("BSpline(",index+5,") = {",index+5,",",index+6,"};", file=f)
		#f.write("'Point(',index+1,') = {',row['X'],',',row['Y'],',',z,',',mesh_den,'};")
	else:
		print("BSpline(",index+5,") = {",index+5,", 5};", file=f)
		break




#---------------------------END----------------------------------------#

