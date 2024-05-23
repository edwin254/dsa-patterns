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

    function diagonoalSum() {
        $sum = 0;

        for ($i = 0; $i < $size; $i++) {
            $sum += $arr[$i][$i];
        }
        return $sum;
    } //    end diagonalSum

    function rowCount() {
        /** return number of rows with duplicated elements in a matrix */
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
        /** return number of COLUMNS with duplicated elements in a matrix */

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

        $diagnaolSum = diagonoalSum(); 
        $rowCount = rowCount(); 
        $columnCount = columnCount();

        $data = array($diagnaolSum, $rowCount, $columnCount);

        $json_data = json_encode($data);
        
        return $json_data;
    }

    $matrix = array(
        0 => array(1, 2, 3, 4),
        1 => array(2, 1, 4, 3),
        2 => array(3, 4, 1, 2),
        3 => array(4, 3, 2, 1)
        );


    echo $json_data;
 
?>