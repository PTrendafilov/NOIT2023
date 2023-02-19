const addSkill = document.querySelector('#add-skill');
const skillValues = document.querySelector('#skill-values');
const optionsAutocomplete = document.querySelector('#options-skills-autocomplete');
let arrSkills = [];
addSkill.addEventListener('click', function (event) {
    event.preventDefault();
    const newSkillInput = addSkill.previousElementSibling.querySelector('input');

    if (newSkillInput.value.length === 0) {
        alert("Kindly Enter Skill Name!!!!");
    } else {
        const SkillsContainer = addSkill.parentElement;
        const newSkill = document.createElement("div");
        newSkill.classList.add("skill");
        newSkill.innerHTML = `<span class="skill-text">${newSkillInput.value}</span><button class="delete"> <i class="far fa-trash-alt"></i> </button>`;
        newSkill.querySelector(".delete").addEventListener("click", function(skillValue) {
            newSkill.remove();
            const index = arrSkills.indexOf(skillValue);
            arrSkills.splice(index, 1);
            skillValues.value = arrSkills.join('(*)');
        });
        SkillsContainer.appendChild(newSkill);
        arrSkills.push(newSkillInput.value);
        skillValues.value = arrSkills.join('(*)');
        newSkillInput.value = "";
        optionsAutocomplete.style.display = 'none';
    }
});
