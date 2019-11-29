const navbar = document.getElementById("navbar");

const expand = () => {
    if (navbar.classList.contains("expandHeight")){
        navbar.classList.remove("expandHeight");
    }
    else{
        navbar.classList.add("expandHeight");
    }
}
