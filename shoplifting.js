const buttons = ["cheese","bread","tomato","ps5","milk"];
const ptsd = [1, 10, 7, 300, 20];
let hiddenButtons = ["bread","tomato","ps5"];
let visibleButton = ["cheese","milk"];
let score = 0;
for(i = 0; i < hiddenButtons.length; i++) {
    document.getElementById(hiddenButtons[i]).style.display = "none";
    visibleButton.push(hiddenButtons[i]);
    hiddenButtons.splice(i,1);
}

console.log(visibleButton);
console.log(hiddenButtons);

function changes(buttID) {
    let rand = Math.floor(Math.random() * visibleButton.length);
    document.getElementById(buttID).style.display = "none";
    document.getElementById(visibleButton[rand]).style.display = "block";
    /*let objap = hiddenButtons[rand];

    visibleButton.splice(objdis, 1);

    hiddenButtons.splice(obj);*/
}