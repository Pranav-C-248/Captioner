function uploadImage() {
    let input = document.getElementById("imageInput");
    let file = input.files[0];

    if (!file) {
        alert("Please select an image.");
        return;
    }

    let reader = new FileReader();
    reader.onload = function (e) {
        let preview = document.getElementById("preview");
        preview.src = e.target.result;
        preview.style.display = "block";
    };
    reader.readAsDataURL(file);

    let formData = new FormData();
    formData.append("image", file);

    fetch("/generate_caption", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("caption").textContent = data.caption;
    })
    .catch(error => console.error("Error:", error));
}
