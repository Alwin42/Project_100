const notesContainer = document.querySelector(".notes-container");
const createBtn = document.querySelector(".btn");

let notes = document.querySelectorAll(".input-box");

function showNotes()
{
    notesContainer.innerHTML = localStorage.getItem("notes"); 
}

showNotes();

function saveNotes()
{
    localStorage.setItem("notes", notesContainer.innerHTML);
}

createBtn.addEventListener("click", () => {
    let inputBox = document.createElement("p");
    let img = document.createElement("img");
    inputBox.className = "input-box";
    inputBox.setAttribute("contenteditable", "true");
   
    img.src = "../assets/delete.png";
    inputBox.appendChild(img);
    notesContainer.appendChild(inputBox);
    saveNotes();
});

notesContainer.addEventListener("click", function (e) {
    if (e.target.tagName === "IMG") {
        e.target.parentElement.remove();
        saveNotes();
    }
    else if (e.target.tagName === "P")
        {
        notes = document.querySelectorAll(".input-box"); 
        notes.forEach(nt =>{
            nt.onkeyup = function() {
                saveNotes();
            }
        })
    }
});
const clearAllBtn = document.querySelector(".clear-all-btn");

clearAllBtn.addEventListener("click", () => {
    notesContainer.innerHTML = "";
    saveNotes();
});