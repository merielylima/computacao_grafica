// ----------- CABO ------------- //
color([0.1,0.1,0.1])
translate([0,0,30])
    cylinder(r =4, h = 55,$fn = 100);
color([0.1,0.1,0.1])
rotate([-45,0,0])
translate([0,-60,60])
    cylinder(r =4, h = 55, $fn = 100);
color([0.1,0.1,0.1])
translate([0,0,85])    
sphere(r =4, h = 55,$fn = 100);
color([0.1,0.1,0.1])
translate([0,39.15,124])    
sphere(r =4, h = 55,$fn = 100);
color([0.1,0.1,0.1])
translate([0,39.15,124])
    cylinder(r =4, h = 30,$fn = 100);
// ----- CONTORNO SETAS ESQUERDA-----//
// botão down
intersection(){
color("#0f2936")
rotate([0, 90, 0])
translate([30, -92, 25])
    cylinder (r = 10,h = 10, $fn = 100,center = true);
color("#0f2936")
rotate([0, 90, 0])
translate([30, -92, 25])
    cylinder (r = 12,h = 10, $fn = 3,center = true);
}
// botão up
intersection(){
color("#0f2936")
rotate([90, -90, 90])
translate([10, 92, 25])
    cylinder (r = 10,h = 10, $fn = 100,center = true);
color("#0f2936")
rotate([90, -90, 90])
translate([10, 92, 25])
    cylinder (r = 12,h = 10, $fn = 3,center = true);
}
// botão right
intersection(){
color("#0f2936")
rotate([90, 0, 90])
translate([-70, -10, 25])
    cylinder (r = 10,h = 10, $fn = 100,center = true);
color("#0f2936")
rotate([90, 0,90])
translate([-70, -10, 25])
    cylinder (r = 12,h = 10, $fn = 3,center = true);
}
// botão left
intersection(){
color("#0f2936")
rotate([-90, 0, -90])
translate([112, 10, 25])
    cylinder (r = 10,h = 10, $fn = 100,center = true);
color("#0f2936")
rotate([-90, 0,-90])
translate([112, 10, 25])
    cylinder (r = 12,h = 10, $fn = 3,center = true);
}
//  CRUZ CENTRAL
color("#0f2936")
rotate([90,0,90])
translate([-92,-10,25])
intersection(){
    union() {
        cube([20, 8, 2], center = true);
        cube([8, 20, 2], center = true);
    }
    cylinder(r = 9.5, h = 10, $fn = 100);
}
// Contorno BRANDO 
color([255,255,255])
rotate([90,0,90])
translate([-92,-10,25])
cylinder(r = 1.5, h = 2, $fn = 100);

// Contorno VERMELHO 
color([255,0,0])
rotate([90,0,90])
translate([-92,-10,25])
cylinder(r = 4, h = 1.5, $fn = 100);

// ----- NINTENDO -----//
// TEXTO ATRÁS
rotate([90, 360, -90])
color([255,255,255])
translate([-27,20.5,26])
text("Nintendo");

// TEXTO FRENTE
rotate([90, 0, 90])
color([255,255,255])
translate([-27,20.5,26])
text("Nintendo");

// primeiro cilindro
difference(){
    union(){
        color([255,255,255])
        rotate([90,90,90])
        translate([-25, -30, 25])
        cylinder (r = 10,h = 0.1, $fn = 100,center = true);
        // retangulo
        color([255,255,255])
        translate([0, 0, 25])
        cube(size = [50.1,60,20], center = true);
        // segundo cilindro
        color([255,255,255])
        rotate([90,90,90])
        translate([-25, 30, 25])
        cylinder(r = 10,h = 0.1, $fn = 100,center = true);
    }
    // ----- diferença nintendo -----//
    // primeiro cilindro
    union(){
        resize(newsize=[51.1,75,16.5])
        translate([0, 0, 5.5])
        union(){
        rotate([90,90,90])
        translate([-25, -30, 25])
        cylinder (r = 10,h = 1, $fn = 100,center = true);
        // retangulo
        translate([0, 0, 25])
        cube(size = [51,60,20], center = true);
        // segundo cilindro
        rotate([90,90,90])
        translate([-25, 30, 25])
        cylinder(r = 10,h = 1, $fn = 100,center = true);
        }
    }
}
// -----LED -----//
//Ponto Branco
color([255,255,255]) 
rotate([90,90,90])
translate([25, 0, 29])
cylinder(r = 1.5, h = 1.1, $fn = 1000);
//Parte Vermelha
color([255,0,0])
rotate([90,90,90])
translate([25, 0, 25])
intersection(){
    cube(size = [8,10,10], center = true);
    cylinder(r = 6, h = 70, $fn = 1000);
}
// ----- CONTORNO BOTÕES START/SELECT -----//
// -----start -----//
color("#0f2936")
rotate([90,90,90])
translate([10, 25, 25])
intersection(){
    cube(size = [15,20,1], center = true);
    cylinder(r = 10, h = 10, $fn = 1000);
}
// -----select -----//
color("#0f2936")
rotate([90,90,90])
translate([10, -25, 25])
intersection(){
    cube(size = [15,20,1], center = true);
    cylinder(r = 10, h = 10, $fn = 1000);
}
// ----- Botões START/SELECT -----//
// -----start -----//
color("#a3bfcb")
rotate([90,90,90])
translate([10, 25, 25])
intersection(){
    cube(size = [10,15,10], center = true);
    cylinder(r = 8, h = 10, $fn = 1000);
}
// -----select -----//
color("#a3bfcb")
rotate([90,90,90])
translate([10, -25, 25])
intersection(){
    cube(size = [10,15,10], center = true);
    cylinder(r = 8, h = 10, $fn = 1000);
}
// --------- CONTORNO BOTÕES DIREITA ---------//
// primeiro
color("#0f2936")
rotate([0, 90, 0])
translate(v = [-2, 78, 21.01])
cylinder (r = 12,h = 10, $fn = 100,center = true);
// segundo
color("#0f2936")
rotate([0, 90, 0])
translate(v = [-2, 105, 21.01])
cylinder (r = 12,h = 10, $fn = 100,center = true);
// terceiro
color("#0f2936")
rotate(a = [0, 90, 0])
translate(v = [25, 78, 21.01])
cylinder (r = 12,h = 10, $fn = 100,center = true);
// quarto
color("#0f2936")
rotate(a = [0, 90, 0])
translate(v = [25, 105, 21.01])
cylinder (r = 12,h = 10, $fn = 100,center = true);

// --------- BOTÕES DIREITA ---------/
// primeiro
color([255,0,0])
rotate([0, 90, 0])
translate(v = [-2, 78, 25])
cylinder (r = 10,h = 10, $fn = 100,center = true);
// segundo
color("#0f2936")
rotate([0, 90, 0])
translate(v = [-2, 105, 25])
cylinder (r = 10,h = 10, $fn = 100,center = true);
// terceiro
color("#0f2936")
rotate(a = [0, 90, 0])
translate(v = [25, 78, 25])
cylinder (r = 10,h = 10, $fn = 100,center = true);
// quarto
color([255,0,0])
rotate(a = [0, 90, 0])
translate(v = [25, 105, 25])
cylinder (r = 10,h = 10, $fn = 100,center = true);

// -------- CONTORNO CRUZ ---------//
// CONTORNO CRUZ DIREITA
color("#0f2936")
rotate([90,45,90])
translate([72,56,25])
intersection(){
    union() {
        cube([72, 32, 1], center = true);
        cube([32, 72, 1], center = true);
    }
    cylinder(r = 37, h = 10, $fn = 100);
}
// CONTORNO CRUZ ESQUERDA
color("#0f2936")
rotate([90,0,90])
translate([-92,-10,25])
intersection(){
    union() {
        cube([72, 32, 1], center = true);
        cube([32, 72, 1], center = true);
    }
    cylinder(r = 37, h = 10, $fn = 100);
}
// ----- CRUZ -----//
// CRUZ DIREITA
color("#a3bfcb")
rotate([90,45,90])
translate([72,56,25])
intersection(){
    union() {
        cube([68, 28, 1.02], center = true);
        cube([28, 68, 1.02], center = true);
    }
    cylinder(r = 35, h = 10, $fn = 100);
}
// CRUZ ESQUERDA
color("#a3bfcb")
rotate([90,0,90])
translate([-92,-10,25])
intersection(){
    union() {
        cube([68, 28, 1.02], center = true);
        cube([28, 68, 1.02], center = true);
    }
    cylinder(r = 35, h = 10, $fn = 100);
}
// ----- DEFESAS -----//
// Defesa L
intersection(){
color("#596673")
translate([0, -72.762, 53.9])
    cube(size = [30,55,10], center = true);
color("#596673")
translate(v = [0, -82, 54])
    cylinder(r = 27, h = 7, $fn = 1000);
}
intersection(){
color("#596673")
rotate([21.5,0,0])
translate([0, -86.7,84])
    cube(size = [30,30,15.09], center = true);
color("#596673")
rotate([21.5,0,0])
translate([0, -82.7,84])
    cylinder(r = 19.5, h = 11.4, $fn = 100);
}
// Defesa R
intersection(){
color("#596673")
translate(v = [0, 72.75, 53.858])
    cube(size = [30,55,10], center = true);
color("#596673")
translate(v = [0, 82, 54])
    cylinder(r = 27, h = 7, $fn = 1000);
}
intersection(){
color("#596673")
rotate([-21.5,0,0])
translate([0, 86.7,84])
    cube(size = [30,30,15], center = true);
color("#596673")
rotate([-21.5,0,0])
translate([0, 82.7,84])
    cylinder(r = 19.5, h = 11.4, $fn = 100);
}

// ----- CONTORNO CONTROLE -----//
color("#0f2936")
rotate([0, 90, 0]) 
translate([10, 90, 0])
cylinder (r = 65,h = 49.9, $fn = 100,center = true);
// retangulo
color("#0f2936")
cube(size = [49.9,180,110], center = true);
// segundo cilindro
color("#0f2936")
rotate(a = [0, 90, 0])
translate(v = [10, -90, 0])
cylinder (r = 65,h = 49.9, $fn = 100,center = true);

// ----- CONTROLE -----//
// primeiro cilindro
color("#596673")
rotate(a = [0, 90, 0]) 
translate(v = [10, 90, 0])
cylinder (r = 60,h = 50, $fn = 100,center = true);
// retangulo
color("#596673")
cube(size = [50,180,100], center = true);
// segundo cilindro
color("#596673")
rotate(a = [0, 90, 0])
translate(v = [10, -90, 0])
cylinder(r = 60,h = 50, $fn = 100,center = true);