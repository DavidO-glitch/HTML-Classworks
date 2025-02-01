document.getElementById('userform').addEventListener('submit', function(event) {
    event.preventDefault(); // prevent the form from submitting the traditional way 

    //Get from values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const dob = document.getElementById('dob').value;
    const contact = document.getElementById('contact').value;
    const password = document.getElementById('password').value; // Get password
    const address = document.getElementById('address').value;
    const gender = document.getElementById('gender').value;

    //Display the result 
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `
        <h2>Submitted Information</h2>
        <p><strong>Name:</strong> ${name}</p>
        <p><strong>Email:</strong> ${email}</p>
        <p><strong>Date of Birth:</strong> ${dob}</p>
        <p><strong>Contact Number:</strong> ${contact}</p>
        <p><strong>Password:</strong> ${password}</p> <!-- Display password -->
        <p><strong>Address:</strong> ${address}</p>
        <p><strong>Gender:</strong> ${gender}</p>
    `;
});
