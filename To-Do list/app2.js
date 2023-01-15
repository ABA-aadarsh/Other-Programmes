const deleteButtons=[...document.querySelectorAll(".delete")]
const editButtons=[...document.querySelectorAll(".edit")]
const querybox=document.getElementById("query")
const confirmationbox=document.querySelector(".confirmation-box")
const email=document.querySelector("#email").value
const password=document.querySelector("#password").value

// console.log(deleteButtons);
deleteButtons.forEach((btn)=>{
    btn.addEventListener("click",()=>{
        const id=btn.getAttribute("id").slice(7)
        const task=document.querySelector(`#task-${id}`).textContent
        const entry=document.querySelector(`#entry-${id}`).textContent
        confirmationbox.innerHTML=`
            <form method="post" action="file.php">
                <h3>Are you sure?</h3>
                <input name="task-delete" value="${task}" class="hidden">
                <input name="entry-delete" value="${entry}" class="hidden">
                <input name="email" value="${email}" class="hidden">
                <input name="password" value="${password}" class="hidden">
                <button type="submit">OK</button>
            </form>
        `
        querybox.classList.remove("hidden")
    })
})
editButtons.forEach((btn)=>{
    btn.addEventListener("click",()=>{
        const id=btn.getAttribute("id").slice(5)
        const task=document.querySelector(`#task-${id}`).textContent
        const entry=document.querySelector(`#entry-${id}`).textContent
        confirmationbox.innerHTML=`
            <form method="post" action="file.php">
                <h3>Are you sure?</h3>
                <input name="change" value="${task}">
                <input name="task-edit" value="${task}" class="hidden">
                <input name="entry-edit" value="${entry}" class="hidden">
                <input name="email" value="${email}" class="hidden">
                <input name="password" value="${password}" class="hidden"><br><br>
                <button type="submit">OK</button>
            </form>
        `
        querybox.classList.remove("hidden")
    })
})

const cancelbutton=document.querySelector(".cancel")
cancelbutton.addEventListener("click",(e)=>{
    if(!querybox.classList.contains("hidden")){
        confirmationbox.innerHTML=``
        querybox.classList.add("hidden")
    }
})
