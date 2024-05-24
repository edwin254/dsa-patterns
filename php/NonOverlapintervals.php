<?php
class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    
function eraseOverlapIntervals($intervals) 
{
    $overlaps = 0;

    //  sort our interval with timestamp
    usort($intervals, fn($a, $b) => $a[1] < $b[1] ? -1 : 1);
    $intEnd = PHP_INT_MIN;

    //  check if current interval start < intEnd it means that current interval is overlapping t
    // and increment overlaps go to next element
    foreach ($intervals as $interval) {
        if ($interval[0] >= $intEnd) {
            $intEnd = $interval[1];
            continue;
        }
        $overlaps++;
    }

    return $overlaps;
}
}

$intervals = [[1,2],[2,3],[3,4],[1,3]];
$result = new Solution();
echo $result->eraseOverlapIntervals($intervals);
?>