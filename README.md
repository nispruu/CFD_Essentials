# CFD_Essentials
CFD Essentials 

The python file which is titled "airfoil.py" is a Pyhton program which takes the coordinates from the .CSV file and generates a .geo file to be used with GMSH.
Here are the instructions to use it properly

Pre-Requisites for airfoil.py: python, GMSH, Pandas, numpy

Step[1]: Download and save the airfoil.py file in any directory on your system 

Step[2]: go to airfoiltools ( http://airfoiltools.com/ ) and download the required airfoil in the .CSV  format in the same directory that holds airfoil.py.

Step[3]: open airfoil.py and in Line 12, copy and paste the .CSV file name (along with the extension) within the inverted commas.

Step[4]: open the .CSV airfoil data and copy the text in the cell B1. Then, open airfoil.py and paste the same within the inverted commas in Line 28 after 'X', .


Then open the directory in the terminal and execute airfoil.py on the Terminal.

Once the airfoil is in place within GMSH, then proceed as per this tutorial = "https://www.youtube.com/watch?v=bekRbU7rtZE&t=369s"
