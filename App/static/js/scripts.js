const fileInput = document.querySelector('#file-upload input[type=file]');

//console.log(fileInput)
fileInput.onchange = () => {
    if(fileInput.files.length > 0){
        const fileName = document.querySelector('#file-upload .file-name');
        fileName.textContent = fileInput.files[0].name;
        console.log(fileInput.files[0].name)
    };
};
