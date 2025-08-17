const s = "    fly me    to   the moon  ";

function lengthOfLastWord(s) {
    const stripped = s.trimEnd();
    const lastWord = stripped.split(" ").at(-1);
    return lastWord.length
}

console.log(lengthOfLastWord(s));
