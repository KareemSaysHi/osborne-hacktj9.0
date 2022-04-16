include <puzzlecad.scad>
$burr_scale = 12.75;
$burr_inset = .15;
$burr_bevel = 1;
unit_beveled = false;
burr_plate([["xxx|...|...", ".x.|.x.|.x.", "...|xxx|..."], ["xxx|xx.", "xx.|..."]]);