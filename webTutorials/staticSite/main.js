const changeColor = () => {
    const colors = ['blue', 'red', 'yellow', 'green', 'purple'];
    document.getElementById('header').style.backgroundColor = colors[Math.floor(Math.random() * 5)];
}