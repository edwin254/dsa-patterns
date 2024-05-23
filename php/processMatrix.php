<?php
/**
 * find
 * 1.the sum of the values on the main diagonal (which runs from the upper left to the lower right).
 * 2.the number of rows of the matrix that contain repeated elements
 * 3.the number of columns of the matrix that contain repeated elements.

*/
function processMatrix($arr) {

        $size = count($arr[$i]);

        function diagonoalSum($size) {
            $sum = 0;

            for ($i = 0; $i < $size; $i++) {
                $sum += $arr[$i][$i];
            }
            return $sum;
        } //    end diagonalSum

    function rowCount($arr) {
        $count = 0;
        $visited = array(); //Associative array to store encountered values

        // For each element checks if it exists in visited associative array
         for ($i = 0; $i < $arr; $i++) {
            for ($j = 0; $j < count($arr[$i]); $j++) {

                if (isset($seen[$value])) {
                    echo "The row contains duplicate values.";
                    break; // Exit loop after finding a duplicate
                  }
                  $seen[$value] = true;
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