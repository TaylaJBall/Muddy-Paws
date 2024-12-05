document.addEventListener('DOMContentLoaded', function() {
    const populateButton = document.getElementById('populate-slots-btn');
    const statusMessage = document.getElementById('status-message');
    const jsonContainer = document.getElementById('json-container');


    populateButton.addEventListener('click', function(){
        // Initial status mesage before starting the request
        statusMessage.textContent = 'populating slots... Please wait.';
        statusMessage.style.color = 'green';
        jsonContainer.innerHTML = ''; // Clear any previous content

        fetch(populateSlotsUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status:
                ${response.status}`);
            }
            return response.json();
        })
            .then(data => {
                if (data.status === 'success') {
                    statusMessage.textContent = data.message;
                    statusMessage.style.color = 'green';

                    // Display JSON data
                    populateButton.innerHTML = '';

                    if (data.slots && data.slots.length > 0) {
                        const slots = JSON.parse(data.slots);

                        slots.forEach(slot => {
                            const slotData = slot.fields;
                            const option = document.createElement('option');
                            option.value = `${slotData.booking_date} ${slotData.booking_time}`;
                            option.textContent = `${slotData.booking_date} ${slotData.booking_time}`;
                            populateButton.appendChild(option);
                        });
                    }else{
                        const option = document.createElement('option');
                        option.value = '';
                        option.textContent = 'No slots available.';
                        slotsSelect.appendChild(option)
                    }
                } else {
                    statusMessage.textContent = `Error: ${data.message}`;
                    statusMessage.style.color = 'red';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                statusMessage.textContent = `An error occurred:
                ${error.message}`;
                statusMessage.style.color = 'red';
            });
    });
});
