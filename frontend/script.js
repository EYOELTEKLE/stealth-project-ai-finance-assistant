document
  .getElementById("fileInput")
  .addEventListener("change", function (event) {
    const file = event.target.files[0];
    const imagePreview = document.getElementById("imagePreview");

    if (file) {
      // Display the selected image
      const reader = new FileReader();
      reader.onload = function (e) {
        imagePreview.innerHTML = `<img src="${e.target.result}" alt="Preview">`;
      };
      reader.readAsDataURL(file);
    } else {
      imagePreview.innerHTML = "";
    }
  });

document.getElementById("uploadButton").addEventListener("click", function () {
  const fileInput = document.getElementById("fileInput");
  const resultDiv = document.getElementById("result");

  // Check if a file is selected
  if (fileInput.files.length === 0) {
    resultDiv.textContent = "Please select an image to upload.";
    return;
  }

  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append("file", file);

  // Replace with your API endpoint
  const apiUrl = "http://localhost:3000/api/files/upload-invoice";

  // Send the image to the server
  fetch(apiUrl, {
    method: "POST",
    body: formData,
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      // Display the result from the server
      resultDiv.textContent =
        "Success! Response: " + JSON.stringify(data, null, 2);
    })
    .catch((error) => {
      // Handle errors
      resultDiv.textContent = "Error: " + error.message;
    });
});
