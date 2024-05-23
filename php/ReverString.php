<?php
echo "Hello World";
    /**
     * Trim spaces at start and end of sentence
     * Split the sentence into array of words separated
     */
class ReversString {
    // @param string $sentence
    //  return string

    function reverseString($sentence) {
        
        $sentence = trim($sentence);

        $words = preg_split('/\s+/', $sentence);
        
        // Reverse the words
        $reversedWords = array_reverse($words);
        
        return implode(' ', $reversedWords);

    }
}

$reverseInstance = new ReversString();
$answer = $reverseInstance->reverseString(" no changes added to commit");
echo $answer;
?>