const forwardToBlanks = () => {
    const teamName = document.getElementById("team_name").value;
    window.location.href = `/mixquiz/7x7/${teamName}`;
}
