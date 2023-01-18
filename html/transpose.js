let trans = 0;

const notes = ["C", "C#","D","D#","E","F", "F#","G","G#","A","B","H"];

function transpose(dir) {
    trans+= dir;
    if(trans==12 || trans ==-12){
        trans=0
    } 
    document.getElementById("trans").innerHTML = trans.toString();
    let tone;
    let type;
    let index;

    let chords = document.getElementsByClassName("chord")
    for (let i = 0; i < chords.length; i++) {
        const chord = chords[i];
        tone = chord.getAttribute("tone");
        type = chord.getAttribute("type"); 
        index = notes.indexOf(tone);
        tone = notes[(index + trans + 12) % 12 ];

        chord.getElementsByClassName("innerchord")[0].innerHTML = tone + type;
    }
}