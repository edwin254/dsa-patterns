<?php
/** input @D array
 *  output json
 * find
 * 1.the sum of the values on the main diagonal (which runs from the upper left to the lower right).
 * 2.the number of rows of the matrix that contain repeated elements
 * 3.the number of columns of the matrix that contain repeated elements.

*/
class ProcessMatrix {
    private $arr;
    private $size;


    public function __construct($arr, $size) {
        $this->arr = $arr;
        $this->size = $size;
    }

    public function diagonoalSum() {
        $sum = 0;

        for ($i = 0; $i < $this->size; $i++) {
            $sum += $this->arr[$i][$i];
        }
        return $sum;
    } //    end diagonalSum

    public function rowCount() {
        /** return number of rows with duplicated elements in a matrix */

        $count = 0;
        $visited = array(); //Associative array to store encountered values 

        // For each element in row checks if it exists in visited associative array
         for ($i = 0; $i < $this->size; $i++) {
            
            $visited = array(); // empty to track next row
           
            for ($j = 0; $j < $this->size; $j++) {

                $value = $this->arr[$i][$j];
                
                if (!isset($visited[$value])) {
                    $visited[$value] = 1;
                  }
                else{
                     $count += 1;
                     break;
                  }
                }
            }

         return $count;
         }
    

    public function columnCount() {
        /** return number of COLUMNS with duplicated elements in a matrix */

        $count = 0;
        $visited = array(); //Associative array to store encountered values

        // For each element in column checks if it exists in visited associative array
         for ($i = 0; $i < $this->size; $i++) {

            $visited = array(); // empty to track next column

            for ($j = 0; $j < $this->size; $j++) {

                $value = $this->arr[$j][$i];

                if (!isset($visited[$value])) {
                    $visited[$value] = 1;
                  }
                else{
                    //  if similar element alread traversed , increment count and break to next column
                    $count += 1;
                    break;
                }
                }
            }

         return $count;
        }
    
        public function jsonData() {
            $diagnaolSum = $this->diagonoalSum(); 
            $rowCount = $this->rowCount(); 
            $columnCount = $this->columnCount();
    
            $data = array($diagnaolSum, $rowCount, $columnCount);
    
            $json_data = json_encode($data);
            
            return $json_data;
        }

        }

    $matrix = array(
        0 => array(1, 2, 3, 4),
        1 => array(2, 1, 4, 3),
        2 => array(3, 4, 1, 2),
        3 => array(4, 3, 2, 1)
        );
    
    $size = count($matrix);

    $processMatrix = new ProcessMatrix($matrix, $size);
    echo $processMatrix->jsonData();

    $matrix = array(
        0 => array(2, 2, 2, 2),
        1 => array(2, 3, 2, 3),
        2 => array(2, 2, 2, 3),
        3 => array(2, 2, 2, 2)
        );
    
    $size = count($matrix);

    $processMatrix = new ProcessMatrix($matrix, $size);
    echo $processMatrix->jsonData();
 
 
?>