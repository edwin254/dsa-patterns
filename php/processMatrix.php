<?php
/** input @D array
 *  output json
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

    function rowCount() {
        $count = 0;
        $visited = array(); //Associative array to store encountered values

        // For each element in row checks if it exists in visited associative array
         for ($i = 0; $i < $size; $i++) {
            for ($j = 0; $j < $size; $j++) {

                $value = $arr[$i][$j];
                if (isset($visited[$value])) {
                    echo "The row contains duplicate values.";
                    $count += 1;
                    continue; // Exit loop after finding a duplicate
                  }
                  $visited[$value] = true;
                }
            }

         return $count;
         }
    

    function columnCount() {
        $count = 0;
        $visited = array(); //Associative array to store encountered values

        // For each element in column checks if it exists in visited associative array
         for ($i = 0; $i < $size; $i++) {
            for ($j = 0; $j < $size; $j++) {

                $value = $arr[$j][$i];
                if (isset($visited[$value])) {

                    echo "The row contains duplicate values.";
                    $count += 1;
                    continue; // Exit loop after finding a duplicate
                  }
                  $visited[$value] = true;
                }
            }

         return $count;
        }
    }
 
?>