Point(1) = { 12500 , 12500 , 0 , 1.0 };
Point(2) = { -12500 , 12500 , 0 , 1.0 };
Point(3) = { -12500 , -12500 , 0 , 1.0 };
Point(4) = { 12500 , -12500 , 0 , 1.0 };
Point( 5 ) = { 885.692236 , -217.473376 , 0 , 1.0 };
Point( 39 ) = { 885.692236 , 12500 , 0 , 1.0 };
Point( 40 ) = { 885.692236 , -12500 , 0 , 1.0 };
Point( 41 ) = { 12500 , -217.473376 , 0 , 1.0 };
Point( 6 ) = { 844.351402 , -194.677688 , 0 , 1.0 };
Point( 7 ) = { 802.791943 , -172.767408 , 0 , 1.0 };
Point( 8 ) = { 719.017153 , -131.603073 , 0 , 1.0 };
Point( 9 ) = { 634.411590 , -93.803288 , 0 , 1.0 };
Point( 10 ) = { 549.040841 , -59.102431 , 0 , 1.0 };
Point( 11 ) = { 462.795595 , -27.943206 , 0 , 1.0 };
Point( 12 ) = { 375.588401 , -0.679776 , 0 , 1.0 };
Point( 13 ) = { 286.960149 , 20.828501 , 0 , 1.0 };
Point( 14 ) = { 241.924563 , 28.660794 , 0 , 1.0 };
Point( 15 ) = { 196.320553 , 34.191025 , 0 , 1.0 };
Point( 16 ) = { 150.060669 , 37.065032 , 0 , 1.0 };
Point( 17 ) = { 102.948151 , 36.485948 , 0 , 1.0 };
Point( 18 ) = { 78.998368 , 34.602672 , 0 , 1.0 };
Point( 19 ) = { 54.611336 , 30.948579 , 0 , 1.0 };
Point( 20 ) = { 29.546568 , 24.549722 , 0 , 1.0 };
Point( 21 ) = { 16.402036 , 18.871151 , 0 , 1.0 };
Point( 22 ) = { 0.000000 , 0.000000 , 0 , 1.0 };
Point( 23 ) = { 7.941271 , -15.394140 , 0 , 1.0 };
Point( 24 ) = { 17.872025 , -22.731067 , 0 , 1.0 };
Point( 25 ) = { 38.826653 , -32.977880 , 0 , 1.0 };
Point( 26 ) = { 60.415293 , -40.657010 , 0 , 1.0 };
Point( 27 ) = { 82.288144 , -47.185110 , 0 , 1.0 };
Point( 28 ) = { 126.514821 , -58.293412 , 0 , 1.0 };
Point( 29 ) = { 171.091296 , -67.985061 , 0 , 1.0 };
Point( 30 ) = { 215.886396 , -76.791302 , 0 , 1.0 };
Point( 31 ) = { 260.681496 , -85.597543 , 0 , 1.0 };
Point( 32 ) = { 350.227970 , -103.387107 , 0 , 1.0 };
Point( 33 ) = { 439.643270 , -121.707915 , 0 , 1.0 };
Point( 34 ) = { 529.058570 , -140.028724 , 0 , 1.0 };
Point( 35 ) = { 618.364558 , -158.792236 , 0 , 1.0 };
Point( 36 ) = { 707.473784 , -178.352616 , 0 , 1.0 };
Point( 37 ) = { 796.386248 , -198.709863 , 0 , 1.0 };
Point( 38 ) = { 840.787824 , -209.109839 , 0 , 1.0 };
Line(1) = {5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,5};
Line(2) = {1,  39 };
Line(3) = { 39 ,2};
Line(4) = {2,3};
Line(5) = {3,  40 };
Line(6) = { 40 , 4};
Line(7) = {4,  41 };
Line(8) = { 41 , 1};
Line(9) = {5,  39 };
Line(10) = {5,  40 };
Line(11) = {5,  41 };
//The end//
//+
Line(12) = {19, 2};
//+
Line(13) = {25, 3};
//+
Split Curve(1) {19, 25, 5};
//+
n_inlet=70;
n_vertical=50;
r_vertical=1.3;
n_airfoil=50;

n_wake=100;
r_wake=1;
Transfinite Curve {14, 4} = n_inlet Using Progression 1; //inlet and curve of airfoil

//+

Transfinite Curve {8, 9, 12, 13, 10, -7} = n_vertical Using Progression r_vertical;  //inflation layers
//+
Transfinite Curve {3, 5} = n_airfoil Using Bump 0.1; //airfoil
//+
Transfinite Curve {16, 15} = n_airfoil Using Bump 0.2; //airfoil
//+
Transfinite Curve {11} = n_wake Using Progression r_wake; //wake
//+
Transfinite Curve {2, 6} = n_wake Using Bump 0.2; //wake
//+
Curve Loop(1) = {14, 13, -4, -12};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {16, 12, -3, -9};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {11, 8, 2, -9};
//+
Plane Surface(3) = {3};
//+
Curve Loop(4) = {6, 7, -11, 10};
//+
Plane Surface(4) = {4};
//+
Curve Loop(5) = {10, -5, -13, 15};
//+
Plane Surface(5) = {5};
//+
Transfinite Surface {1};
//+
Transfinite Surface {2};
//+
Transfinite Surface {3};
//+
Transfinite Surface {4};
//+
Transfinite Surface {5};
//+
Recombine Surface {1, 2, 3, 4, 5};
//+

//+
Field[1] = BoundaryLayer;
//+
Field[1].EdgesList = {8, 9, 12, 13, 10, -7};
//+
Field[1].ratio = 1.3;
//+
Field[1].AnisoMax = 0;
//+
Field[1].hwall_n = 0.0115;
//+
Field[1].hfar = 0.05;
//+
Extrude {0, 0, 1000} {
  Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Layers{1}; Recombine;
}
//+
Physical Volume("Fluid") = {1, 2, 3, 4, 5};
//+
Physical Surface("inlet") = {33};
//+
Physical Surface("airfoil") = {47, 125, 25};
//+
Physical Surface("outlet") = {95, 73};
//+
Physical Surface("ulw") = {77, 55, 117, 91};
//+
Physical Surface("sides") = {82, 3, 38, 1, 60, 2, 126, 5, 104, 4};
