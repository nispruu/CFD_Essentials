#--------------------------------------------------------------------------#
#									      #
#									      #
#			GMSH Airfoil Generator Tool			      #
#									      #
#                      By Nispruha Geetha Srinivas			      #
#--------------------------------------------------------------------------#


#--------------------------------------------------------------------------#

#     Acceptable domain size for airfoil : x * y :: 25*25 m^2	      # 
#									      #
#		Methodology to Compute grid spacing delta_s for given y+    #
#									      #
#	Step[1]: Value of Wall friction coeff : Cf = 0.026/(Re)^(1/7)
#	Step[2]: Wall shear stress: Tau_wall=(Cf*density*U_freestream)^2)/2
#	Step[3]: Friction velocity: U_fric= sqrt(Tau_wall/density)
#	Step[4]: wall spacing: delta_s = (y+)*(kinematic viscosity)/(U_fric * density)
#									      #
#--------------------------------------------------------------------------#



import pandas as pd
import os

#importing and cleaning the dataframe of Coordinates
df = pd.read_csv("naca4412-il.csv")
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
    columns={"Name": "X", "NACA 4412": "Y"},
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
x1max=12500
x2max=-12500
y1max=12500
y2max=-12500

f = open("airfoil.geo", "a")

print("Point(1) = {",x1max,",",y1max,",",z,",",mesh_den,"};", file=f)
print("Point(2) = {",x2max,",",y1max,",",z,",",mesh_den,"};", file=f)
print("Point(3) = {",x2max,",",y2max,",",z,",",mesh_den,"};", file=f)
print("Point(4) = {",x1max,",",y2max,",",z,",",mesh_den,"};", file=f)




totalrows = len(df.index)

#print(totalrows)

for index, row in df.iterrows():
	if index<=totalrows-2 and (index+5)!=5:
		print("Point(",index+5,") = {",row['X'],",",row['Y'],",",z,",",mesh_den,"};", file=f)
		#f.write("'Point(',index+1,') = {',row['X'],',',row['Y'],',',z,',',mesh_den,'};")
	elif index<=totalrows-2 and (index+5)==5:
		print("Point(",index+5,") = {",row['X'],",",row['Y'],",",z,",",mesh_den,"};", file=f)
		print("Point(",totalrows+4,") = {",row['X'],",",y1max,",",z,",",mesh_den,"};", file=f)
		print("Point(",totalrows+5,") = {",row['X'],",",y2max,",",z,",",mesh_den,"};", file=f)
		print("Point(",totalrows+6,") = {",x1max,",",row['Y'],",",z,",",mesh_den,"};", file=f)
	else:
 		break
 		
linestr="Line(1) = {";
for index, row in df.iterrows():
	if index<=totalrows-3:
		n=str(index+5)
		linestr=linestr+n+","
		#print("Spline(",index+5,") = {",index+5,",",index+6,"};", file=f)
		#f.write("'Point(',index+1,') = {',row['X'],',',row['Y'],',',z,',',mesh_den,'};")
	else:
		n=str(index+5)
		linestr=linestr+n+",5};"
		#print("Spline(",index+5,") = {",index+5,", 5};", file=f)
		break
print(linestr,file=f)

print("Line(2) = {1, ",totalrows+4,"};", file=f)
print("Line(3) = {",totalrows+4,",2};", file=f)
#Line(3) = {39, 2};
print("Line(4) = {2,3};", file=f)
#Line(4) = {2, 3};
print("Line(5) = {3, ",totalrows+5,"};", file=f)
#Line(5) = {3, 40};
print("Line(6) = {",totalrows+5,", 4};", file=f)
#Line(6) = {40, 4};
print("Line(7) = {4, ",totalrows+6,"};", file=f)
#Line(7) = {4, 41};
print("Line(8) = {",totalrows+6,", 1};", file=f)
#Line(8) = {41, 1};
print("Line(9) = {5, ",totalrows+4,"};", file=f)
#Line(9) = {5, 39};
print("Line(10) = {5, ",totalrows+5,"};", file=f)
#Line(10) = {5, 41};
print("Line(11) = {5, ",totalrows+6,"};", file=f)
#Line(11) = {5, 40};

print("//The end//", file=f)






#---------------------------END----------------------------------------#
