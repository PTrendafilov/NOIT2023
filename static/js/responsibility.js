const addResponsibility = document.querySelector('#add-responsibility');
const responsibilityValues = document.querySelector('#responsibility-values');
let arrResponsibilities = [];
addResponsibility.addEventListener('click', function (ev) {
    ev.preventDefault();
    const newResponsibilityInput = document.querySelector('#responsibility-textarea');
    if (newResponsibilityInput.value.length === 0) {
        alert("Kindly Enter Responsibility!!!!");
    } else {
        const responsibitiesContainer = addResponsibility.parentElement;
        const newResponsibility = document.createElement("div");
        newResponsibility.classList.add("responsibility");
        newResponsibility.innerHTML =`<span class="responsibility-text">${newResponsibilityInput.value}</span><button class="delete"> <i class="far fa-trash-alt"></i> </button>`;
        const currentIndex = arrResponsibilities.length;
        arrResponsibilities.push(newResponsibilityInput.value);
        newResponsibility.querySelector(".delete").addEventListener("click", function () {
            newResponsibility.remove();
            arrResponsibilities.splice(currentIndex, 1);
            responsibilityValues.value = arrResponsibilities.join('(*)');
        });
        responsibitiesContainer.appendChild(newResponsibility);
        responsibilityValues.value = arrResponsibilities.join('(*)');
        newResponsibilityInput.value = "";
    }
});

