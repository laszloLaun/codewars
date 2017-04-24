function pig_it(text) {
    text = text.split(" ");
    console.log(text);
    punctuation = "!?";
    pigged_text = [];
    for (var i = 0; i < text.length; i++) {
        if (text[i].includes("?")) {
            pigged_text.push(text[i]);
        }
        else {
            pigged_text.push(text[i].slice(1, text[i].length) + text[i].slice(0, 1) + "ay");
        }
    }
    pigged_text = pigged_text.join(" ");
    console.log(pigged_text);
    return pigged_text;
}