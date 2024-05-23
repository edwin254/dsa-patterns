<?php
/**
 * find
 * 1.the sum of the values on the main diagonal (which runs from the upper left to the lower right).
 * 2.the number of rows of the matrix that contain repeated elements
 * 3.the number of columns of the matrix that contain repeated elements.

*/
function processMatrix($arr)
    {
        function diagonoalSum($size) {
            $sum = 0;

            for ($i = 0; $i < $size; $i++) {
                $sum += $arr[$i][$i];
            }
            return $sum;
        } //    end diagonalSum

    function rowCount($arr) {
        $count = 0;
         for ($i = 1; $i < $arr; $i++) {
            for ($j = 0; $j < count($arr[$i]); $j++) {
                //  compare current row element with previous element

                if ($arr[$i][$j] == $arr[$i - 1][$j]) {
                    $count += 1;
                    continue;
                }
            }
         }
         return $count;
    }

    function columnCount($arr) {
        $count = 0;

         for ($i = 0; $i < $arr; $i++) {
            for ($j = 1; $j < count($arr[$i]); $j++) {

                //  compare current column  element with previous element
                if ($arr[$j][$i] == $arr[$j - 1][$i]) {
                    $count += 1;
                    continue;
                }
            }
         }
         return $count;
    }
    }
 
?>