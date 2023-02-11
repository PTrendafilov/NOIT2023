const homeLinkElement = document.getElementById('home-link');
const jobsLinkElement= document.getElementById('projects-link');
const projectsCreateLink= document.getElementById('projects-create-link');
const scoreboardLink= document.getElementById('scoreboard-link');
const teamsLink= document.getElementById('teams-link');
const profileLink= document.getElementById('profile-link');
const loginLink= document.getElementById('login-link');
const registerLink= document.getElementById('register-link');
const myJobLink = document.getElementById('my-job-link');
const teamCreateLink = document.getElementById('team-create-link');
if(document.URL==='http://127.0.0.1:8000/projects/'){
	jobsLinkElement.classList.add('active');
	homeLinkElement.classList.remove('active');
}
if(document.URL==='http://127.0.0.1:8000/projects/create_job_page/'){
	projectsCreateLink.classList.add('active');
	homeLinkElement.classList.remove('active');
}
if(document.URL==='http://127.0.0.1:8000/scoreboard/'){
	scoreboardLink.classList.add('active');
	homeLinkElement.classList.remove('active');
}
if(document.URL==='http://127.0.0.1:8000/teams/'){
	teamsLink.classList.add('active');
	homeLinkElement.classList.remove('active');
}
if(document.URL==='http://127.0.0.1:8000/profile/'){
	profileLink.classList.add('active');
	homeLinkElement.classList.remove('active');
}
if(document.URL==='http://127.0.0.1:8000/accounts/'){
	loginLink.classList.add('active');
	homeLinkElement.classList.remove('active');
}
if(document.URL==='http://127.0.0.1:8000/accounts/registration_page' || document.URL==='http://127.0.0.1:8000/accounts/choose_role'){
	registerLink.classList.add('active');
	homeLinkElement.classList.remove('active');
}
if(document.URL==='http://127.0.0.1:8000/projects/jobs_created_by_user/'){
	myJobLink.classList.add('active');
	homeLinkElement.classList.remove('active');
}
if(document.URL==='http://127.0.0.1:8000/teams/create_team'){
	teamCreateLink.classList.add('active');
	homeLinkElement.classList.remove('active');
}