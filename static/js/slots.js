document.addEventListener('DOMContentLoaded', function() {
    const populateButton = document.getElementById('populate-slots-btn');
    const statusMessage = document.getElementById('status-message');

    populateButton.addEventListener('click', function(){
        statusMessage.textContent = 'populating slots... Please wait.';
        statusMessage.style.color = 'var(--yellow)';

        fetch('{% url "populate_slots" %}')
            .then(response => reponse.json())
            .then(data => {
                if (data.status === 'success') {
                    statusMessage.textContent = data.message;
                    statusMessage.style.color = 'var(--yellow)';
                } else {
                    statusMessage.textContent = `Error: ${data.message}`;
                    statusMessage.style.color = 'red';
                }
            })
            .catch(error => {
                statusMessage.textContent = 'An error occurred while populating the slots.';
                statusMessage.style.color = 'red';
            });
    });
});