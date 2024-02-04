/*function changes() {
    document.getElementById("cheese").style.display = "none";
    document.getElementById("tomato").style.display = "block";
    document.getElementById("bread").style.display = "block";
    document.getElementById("ps5").style.display = "none";
}

function changes2() {
    document.getElementById("tomato").style.display = "block";
    document.getElementById("ps5").style.display = "none";
    document.getElementById("bread").style.display = "none";
}
*/
const buttons = ["cheese","bread","tomato","ps5"];
let visibleButton = [0];
let hiddenButtons = [1,2,3];
function changes(buttID) {
    document.getElementById(buttID).style.display = "none";
}