// Function to handle video submission
function submitVideo() {
    const videoInput = document.getElementById('videoInput');
    const resultElement = document.getElementById('result');

    // Check if a file is selected
    if (videoInput.files.length === 0) {
        resultElement.innerHTML = 'Please upload a video file.';
        resultElement.style.color = 'red';
        return;
    }

    // Get the uploaded video file
    const videoFile = videoInput.files[0];
    const formData = new FormData();
    formData.append('file', videoFile);

    // Display "processing" message
    resultElement.innerHTML = 'Processing video for fact-checking...';
    resultElement.style.color = '#0077b6'; // Blue during processing

    // Send the video to the back-end API using fetch()
    fetch('http://139.84.132.84:5000/factcheck', {  // Replace with your Flask external IP
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            resultElement.innerHTML = data.result;  // Display the real result from API
            resultElement.style.color = '#333';     // Reset color after processing
        })
        .catch(error => {
            resultElement.innerHTML = 'Error processing the video.';
            resultElement.style.color = 'red';
            console.error('Error:', error);
        });
}

}
