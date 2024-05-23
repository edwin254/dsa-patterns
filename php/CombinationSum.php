<?php


class Solution {

    /**
     * @param Integer[] $candidates
     * @param Integer $target
     * @return Integer[][]
     */

    function combinationSum($candidates, $target)
    {
        $result = array();
        $current = array();

        $this->traverse($candidates, count($candidates), 0, $target, $current, $result);
        return $result;
    }

    function traverse($candidates, $candidatesLength, $start, $target, $current, &$result)
    {
        if ($target == 0) { 
            array_push($result, $current); 
            return $result;
        }
        for ($i = $start; $i < $candidatesLength; $i++) {
            $remaining = $target - $candidates[$i];
            if ($remaining >= 0) {
                array_push($current, $candidates[$i]); 
                $this->traverse($candidates, $candidatesLength, $i, $remaining, $current, $result);
                array_pop($current); 
            }
        }
    }
}

$candidates = [2,3,6,7];
$target = 7;
// $expectedResult = [[2,2,3],[7]];

$candidates = [2,3,5]; 
$target = 8;

$result = new Solution();
$combination = $result->combinationSum($candidates, $target);

print_r($combination);

?>