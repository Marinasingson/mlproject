// Get the file input element
const fileInput = document.getElementById('id_image');

// Listen for file selection
fileInput.addEventListener('change', () => {
  // Get the selected file
  const file = fileInput.files[0];

  // Create a new FileReader object
  const reader = new FileReader();

  // Listen for when the FileReader has loaded the file
  reader.addEventListener('load', () => {
    // Set the preview image source to the loaded file
    const previewImage = document.getElementById('preview-image');
    previewImage.src = reader.result;
  });

  // Read the selected file as a data URL
  reader.readAsDataURL(file);
});
